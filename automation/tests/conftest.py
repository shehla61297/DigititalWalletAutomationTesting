from backports import configparser
import pytest
import logging

logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger("Log")


def get_environment():
    environment_prop = None
    try:
        configs = configparser.ConfigParser()
        configs.read('env_config.properties')
        environment = configs['DEFAULT']['set.environment']
        log.info(" The machine to test is  - ")
        log.info(environment)
        if environment == "local":
            environment_prop = 'config_local.properties'
            log.info(environment_prop)
        elif environment == "dev":
            environment_prop = 'config_dev.properties'
            log.info(environment_prop)
        else:
            environment_prop = None
    except Exception as e:
        log.error(e)
    finally:
        assert environment_prop is not None
    return environment_prop


def get_environment_specific_properties():
    environment_prop = get_environment()
    log.info(environment_prop)
    configs = configparser.ConfigParser()
    configs.read(environment_prop)
    return configs


config = get_environment_specific_properties()


class Config:

    @staticmethod
    def get_base_url():
        return config['DIGITAL-WALLET_API']['api.baseurl']

    @staticmethod
    def get_api_endpoint():
        return config['DIGITAL-WALLET_API']['api.user.endpoint']
