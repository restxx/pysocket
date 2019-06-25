#!/usr/bin/python
# coding:utf-8
# author dongguanghua
# -*- coding: utf-8 -*-
from oslo_context import context
from oslo_log import log as logging
from oslo_config import cfg
import sys

LOG = logging.getLogger(__name__)


# 在上述在REST的入口处，通过
# context.RequestContext()
# 即生成了这样的request_id，之后每次log都会自动带上它。

def prepare_service(argv=None, config_file=None):
    logging.register_options(cfg.CONF)           # 注册配置项
    log_level = cfg.CONF.default_log_levels  # 设置默认日志级别INFO
    logging.set_defaults(default_log_levels=log_level)
    if argv is None:
        argv = sys.argv
    cfg.CONF(argv[1:], default_config_files=config_file)  # 将进程中配置文件或日志文件注册在配置项中
    logging.setup(cfg.CONF, 'tslog')  #


if __name__ == '__main__':
    prepare_service()
    for i in range(5):
        context.RequestContext()
        LOG.info("Welcome to Oslo Logging")
        LOG.error("Without context")
        LOG.info("With context")

# tslog.py --log-file=/var/log/tslog.log
# tslog.py --log-dir=/usr/local/src/guang/pysocket/ts/tslogs/
