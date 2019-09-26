When pip connection is broken and an error like this appears:

    Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', error(104, 'Connection reset by peer'))': /simple/test/

Didable ipv6

    sudo sh -c 'echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6'