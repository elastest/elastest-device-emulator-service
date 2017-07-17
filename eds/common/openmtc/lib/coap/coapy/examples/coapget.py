import sys
import getopt
import coapy.connection
import coapy.options
import coapy.link

uri_path = '.well-known/r'
host = 'ns.tzi.org'
port = 61616
verbose = False
output_path = None
block_option = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'u:h:p:vo:b:', [ 'uri-path=', 'host=', 'port=', 'verbose', '--output-path=', '--start-block='])
    for (o, a) in opts:
        if o in ('-u', '--uri-path'):
            uri_path = a
        elif o in ('-h', '--host'):
            host = a
        elif o in ('-p', '--port'):
            port = a
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-o', '--output-path'):
            output_path = a
        elif o in ('-b', '--start-block'):
            block_option = coapy.options.Block(block_number=int(a), size_exponent=coapy.options.Block.MAX_SIZE_EXPONENT)
except getopt.GetoptError, e:
    print 'Option error: %s' % (e,)
    sys.exit(1)

remote = (host, port)
req = coapy.connection.Message(code=coapy.GET, uri_path=uri_path)
if block_option is not None:
    req.addOption(block_option)

ep = coapy.connection.EndPoint()
tx_rec = ep.send(req, remote)

outfile = None
if output_path is not None:
    outfile = file(output_path, 'w')

while tx_rec.response is None:
    rv = ep.process(1000)
    if rv is None:
        print 'No message received; waiting'
        continue
    msg = rv.message
    if verbose:
        print msg
        for o in msg.options:
            print ' %s' % (str(o),)
        print ' %s' % (msg.payload,)

    if rv.pertains_to != tx_rec:
        print 'Response not pertinent; waiting'
        continue
    if msg.RST == tx_rec.response_type:
        print 'Server responded with reset'
        break
    if coapy.OK != msg.code:
        print 'Pertinent response code not OK: %d (%s)' % (msg.code, coapy.codes.get(msg.code, 'UNDEFINED'))
        break

    if outfile is not None:
        outfile.write(msg.payload)

    ct = msg.findOption(coapy.options.ContentType)
    if (ct is None) or (ct.value_as_string.startswith('text/')):
        print msg.payload
    elif 'application/link-format' == ct.value_as_string:
        (resources, _) = coapy.link.decode_resource_descriptions(msg.payload)
        print '%d resources available at %s:' % (len(resources), uri_path)
        for link in resources:
            print '  %s' % (link.encode(),)
    else:
        print 'Unhandled content type %s: %s' % (ct.value, binascii.hexlify(msg.payload))

    block_option = msg.findOption(coapy.options.Block)
    if block_option is None:
        break
    if block_option.more:
        nblk = coapy.options.Block(block_number=block_option.block_number+1, size_exponent=block_option.size_exponent)
        req.replaceOption(nblk)
        tx_rec = ep.send(req, remote)

