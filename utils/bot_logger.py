import sys
from typing import Any, Dict

from .base import BaseLogger

SYS_OUT_FORMAT = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '\
    + '<level>{level}</level> | '\
    + '<level>{extra[user_id]}</level> | '\
    + '<level>{extra[session_id]}</level> | '\
    + '<level>{extra[trace_id]}</level> | '\
    + '<level>{extra[info_name]}</level> | '\
    + '<level>{message}</level> | '\
    + '<level>{extra[extra_info]}</level>'

LOG_FORMAT = '{time:YYYY-MM-DD HH:mm:ss.SSS}|'\
    + '{level}|'\
    + '{extra[user_id]}|'\
    + '{extra[session_id]}|'\
    + '{extra[trace_id]}|'\
    + '{extra[info_name]}|'\
    + '{message}|'\
    + '{extra[extra_info]}'


class BotLogger(BaseLogger):

    @classmethod
    def default_dev_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you dev your projects """
        config = {
            'handlers': [
                {'sink': sys.stdout, 'format': SYS_OUT_FORMAT},
                {
                    'sink': 'runtime_info.log', 'mode': 'a',
                    'format': LOG_FORMAT, 'rotation': '1 day'
                },
            ],
            'extra': {
                'user_id': 'default',
                'session_id': 'default',
                'trace_id': 'default',
                'info_name': 'default_info_name',
                'extra_info': '',
            }
        }
        return config

    @classmethod
    def default_pre_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you run your projects in pre env """
        config = {
            'handlers': [
                {'sink': sys.stdout, 'format': SYS_OUT_FORMAT},
                {
                    'sink': 'runtime_info.log', 'mode': 'a',
                    'format': LOG_FORMAT, 'rotation': '1 day'
                },
                {
                    'sink': 'runtime_error.log', 'mode': 'a',
                    'format': LOG_FORMAT, 'level': 'ERROR', 'rotation': '1 day'
                },
            ],
            'extra': {
                'user_id': 'default',
                'session_id': 'default',
                'trace_id': 'default',
                'info_name': 'default_info_name',
                'extra_info': '',
            }
        }
        return config

    @classmethod
    def default_prod_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you run your projects in prod env """
        config = {
            'handlers': [
                {'sink': sys.stdout, 'format': SYS_OUT_FORMAT},
                {
                    'sink': 'runtime_info.log', 'mode': 'a',
                    'format': LOG_FORMAT, 'rotation': '1 day'
                },
                {
                    'sink': 'runtime_error.log', 'mode': 'a',
                    'format': LOG_FORMAT, 'level': 'ERROR', 'rotation': '1 day'
                },
            ],
            'extra': {
                'user_id': 'default',
                'session_id': 'default',
                'trace_id': 'default',
                'info_name': 'default_info_name',
                'extra_info': '',
            }
        }
        return config


def log_test():
    import os
    os.environ['LOG_ENV'] = 'dev'
    logger = BotLogger()
    logger.set_bind_info(
        user_id='123',
        session_id='456',
        trace_id='759',
        info_name='test_info',
        extra_info='extra_info',
    )
    logger.info("你好啊")
    logger.error("错误")
    logger.warning("警告")

    os.environ['LOG_ENV'] = 'pre'
    logger = BotLogger()
    logger.set_bind_info(
        user_id='123',
        session_id='456',
        trace_id='759',
        info_name='test_info',
        extra_info='extra_info',
    )
    logger.info("你好啊")
    logger.error("错误")
    logger.warning("警告")

    os.environ['LOG_ENV'] = 'prod'
    logger = BotLogger()
    logger.set_bind_info(
        user_id='123',
        session_id='456',
        trace_id='759',
        info_name='test_info',
        extra_info='extra_info',
    )
    logger.info("你好啊")
    logger.error("错误")
    logger.warning("警告")

if __name__ == "__main__":
    log_test()
