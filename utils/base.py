from abc import abstractmethod
import os
from typing import Any, Dict, Optional

from loguru import logger


class BaseLogger:
    def __init__(self):
        self.logger = logger
        self.dev_period: str = 'dev'
        self.configuration = None
        self.set_configs()

    def set_configs(
        self,
        configs: Optional[Dict] = None
    ) -> None:
        assert 'LOG_ENV' in os.environ.keys() and os.environ.get('LOG_ENV')
        if os.environ.get('LOG_ENV') in ['dev', 'pre', 'prod']:
            self.dev_period = os.environ['LOG_ENV']
        else:
            self.dev_period = 'custom'

        if configs and self.dev_period == 'custom':
            self.configuration = configs
        elif self.dev_period in ['dev', 'pre', 'prod']:
            if self.dev_period == 'dev':
                self.configuration = self.default_dev_config()
            elif self.dev_period == 'pre':
                self.configuration = self.default_pre_config()
            elif self.dev_period == 'prod':
                self.configuration = self.default_prod_config()
            self.logger.configure(**self.configuration)  # pyright: ignore
        else:
            raise NotImplementedError

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    @classmethod
    @abstractmethod
    def default_dev_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you dev your projects """

    @classmethod
    @abstractmethod
    def default_pre_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you run your projects in pre env """

    @classmethod
    @abstractmethod
    def default_prod_config(cls) -> Dict[str, Any]:
        """ Used LogConfigurations when you run your projects in prod env """

    def set_bind_info(
        self,
        **extra_infos
    ):
        """ Set BindInfos """
        input_keys = extra_infos.keys()
        if self.configuration:
            expected_keys = self.configuration['extra'].keys()
            assert all(
                k in expected_keys for k in input_keys), "All input_keys: {input_keys}, should in expected_keys: {expected_keys}"
            self.logger = self.logger.bind(**extra_infos)
        else:
            raise NotImplementedError('Configuration is not properly set')
