'''
Created on 10.06.2013

@author: kca
'''

class Session(object):
    '''
    classdocs
    '''

    def __init__(self, *args, **kw):
        '''
        Constructor
        '''
        
        super(Session, self).__init__(*args, **kw)
        
        self._map = {}
        
