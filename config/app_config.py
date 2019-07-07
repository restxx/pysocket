# coding=utf-8
# __author__ = 'doc007'

import sys
from oslo_config import cfg
from oslo_config import types

cli_opts = [
    cfg.IPOpt('host',
              version=4,
              default='119.119.119.119',
              help='IP address to listen on.'),
    cfg.PortOpt('port',
            default=9292,
            help='Port number to listen on.')
]

CONF = cfg.CONF

CONF.register_cli_opts(cli_opts)


if __name__ == '__main__':
    CONF(sys.argv[1:])
    print(CONF.host, CONF.port)
    pass
