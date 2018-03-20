# -*- coding: utf8 -*-
import logging

# 创建一个logger
logger = logging.getLogger('practical_logging')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('practical_logging.log')
# fh.setLevel(logging.INFO)

# 再创建一个handler，用于输出到控制台，仅输出错误信息
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
# formatter_f = logging.Formatter('[%(asctime)s][%(process)d:%(thread)d][%(levelname)s] %(message)s')
# fh.setFormatter(formatter_f)
formatter_c = logging.Formatter('[%(asctime)s]-[%(process)d]-[%(thread)d]-[%(name)s]-[%(lineno)s]-[%(levelname)s]: %(message)s')
ch.setFormatter(formatter_c)

# 给logger添加handler
# logger.addHandler(fh)
logger.addHandler(ch)

# 记录日志
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')