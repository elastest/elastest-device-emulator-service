import gevent.socket
from gevent import queue
from gevent.threadpool import ThreadPool

# avoid socket monkey patching
import imp
from futile.logging import LoggerMixin

fp, pathname, description = imp.find_module('socket')
try:
    socket_ = imp.load_module('socket_', fp, pathname, description)
finally:
    if fp:
        fp.close()

# from socket import socketpair

_exceptions = ("Warning", "Error", "InterfaceError", "DatabaseError",
               "DataError", "OperationalError", "IntegrityError",
               "InternalError", "ProgrammingError", "NotSupportedError")


class DBPool(LoggerMixin):
    def __init__(self, connectionstring, poolsize, modulename='pyodbc'):
        conns = self.conns = [DBConnection_(socket_.socketpair())
                              for _ in xrange(poolsize)]
        tp = self.threadpool = ThreadPool(poolsize)

        q = self.queue = queue.Queue(poolsize)

        # check if the module imports submodules, e.g. mysql-connector-python needs "mysql.connector"
        modulename_parts = modulename.split(".")

        # the normal pyodbc, sqlite modules will have normally have 1 part
        if (len(modulename_parts) == 1):
            module = __import__(modulename)
        # the mysql-connector-python uses mysql.connector as imported module
        elif (len(modulename_parts) == 2):
            fromlist = [str(modulename_parts[1])]
            module = __import__(modulename, fromlist=fromlist)

        for conn in conns:
            tp.spawn(self.worker, conn)
            conn.connect(connectionstring, module)
            q.put(conn)

        class Exc(object):
            pass

        self.exc = Exc

        for e in _exceptions:
            setattr(Exc, e, getattr(module, e))

        # special treatment for the mysql-connector-python
        if modulename == "mysql.connector":
            # instead of using the modules paramstyle "pyformat" -> use quote paramstyle
            # as it seems to be compatible without extending the db_adapter
            self.paramstyle = "quote"
        else:
            self.paramstyle = module.paramstyle

    def worker(self, conn):
        while True:
            conn.pipe[1].recv(1)
            try:
                function = conn.state.function
                conn.state.ret = function(*conn.state.args,
                                          **conn.state.kwargs)
                conn.state.status = 0
            except Exception as inst:
                conn.state.error = inst
                conn.state.status = -1
            finally:
                conn.pipe[1].send('\0')

    def get(self):
        return DBConnection(self, self.queue.get())

    @property
    def size(self):
        return self.queue.qsize()

    @property
    def ready(self):
        return not self.queue.empty()


class DBConnection_(LoggerMixin):
    class State(object):
        pass

    def __init__(self, pipe):
        self.pipe = pipe
        self.state = self.State()

    def connect(self, connectionstring, module):
        if isinstance(connectionstring, dict):
            self.conn = self.apply(module.connect, kwargs=connectionstring)
        else:
            self.conn = self.apply(module.connect, (connectionstring, ))

    def __del__(self):
        try:
            self.conn.close()
        except AttributeError:
            pass

    def apply(self, function, args=(), kwargs={}):
        if function.__name__ == "execute":
            self.logger.debug("%s%s", function.__name__, args)

        self.state.function = function
        self.state.args = args
        self.state.kwargs = kwargs
        gevent.socket.wait_write(self.pipe[0].fileno())
        self.pipe[0].send('\0')
        gevent.socket.wait_read(self.pipe[0].fileno())
        self.pipe[0].recv(1)
        if self.state.status != 0:
            raise self.state.error
        return self.state.ret


class DBConnection(LoggerMixin):
    def __init__(self, pool, conn_):
        self.pool = pool
        self.conn_ = conn_
        self.__finalized = False

    def apply(self, function, *args, **kw):
        return self.conn_.apply(function, args, kw)

    def release(self):
        if self.conn_ is not None:
            if not self.__finalized:
                self.logger.warning("DBConnection has not been finalized"
                                    " before releasing it. "
                                    "Commencing roll-back.")
                self.rollback()
            self.pool.queue.put(self.conn_)
            self.conn_ = None
    __del__ = release

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self.__finalized:
            if exc_type is None:
                self.commit()
            else:
                self.rollback()
        self.release()

    def cursor(self):
        return DBCursor(self, self.conn_.apply(self.conn_.conn.cursor))

    def commit(self):
        self.__finalized = True
        self.conn_.apply(self.conn_.conn.commit)

    def rollback(self):
        self.__finalized = True
        self.conn_.apply(self.conn_.conn.rollback)


class DBCursor(object):
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def execute(self, *args):
        return self.conn.apply(self.cursor.execute, *args)

    def executemany(self, *args):
        return self.conn.apply(self.cursor.executemany, *args)

    def fetchone(self, *args):
        return self.conn.apply(self.cursor.fetchone, *args)

    def fetchall(self, *args):
        return self.conn.apply(self.cursor.fetchall, *args)

    def fetchmany(self, *args):
        return self.conn.apply(self.cursor.fetchmany, *args)

    @property
    def description(self):
        return self.cursor.description

    @property
    def rowcount(self):
        return self.cursor.rowcount

import unittest
import time


class TestDBPool(unittest.TestCase):
    def percentile(self, timings, percent):
        idx = int((len(timings)-1) * percent)
        return timings[idx]

    def test_benchmark(self):
        requests = 1000
        concurrency = 10
        sql = 'SELECT 1'

        timings = []

        def timer(pool, sql):
            conn = pool.get()
            t0 = time.time()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            timings.append(time.time()-t0)
            print result
        pool = DBPool(':memory:', concurrency, 'sqlite3')

        greenlets = []
        for _ in xrange(requests):
            greenlets.append(gevent.spawn(timer, pool, sql))

        for g in greenlets:
            g.join()

        print '66%% %f' % self.percentile(timings, 0.66)
        print '90%% %f' % self.percentile(timings, 0.90)
        print '99%% %f' % self.percentile(timings, 0.99)
        print '99.9%% %f' % self.percentile(timings, 0.999)
        print '100%% %f' % self.percentile(timings, 1.00)

if __name__ == '__main__':
    unittest.main()
