# coding=utf-8


import logging

logging.basicConfig(filename="_log.log", level="DEBUG")

logging.info("这是一条 info 级别的日志")
logging.debug("这是一条 debug 级别的日志")
logging.warning("这是一条 warning 级别的日志")
logging.error("这是一条 error 级别的日志")
logging.fatal("这是一条 fatal 级别的日志")
