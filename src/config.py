import os
import binascii

class Config(object):
    """Base config"""
    self.DEBUG = False
    self.trader = 'cassandra_classic'


class DevelopmentConfig(Config):
    super(DEBUG)
    self.DEBUG = True

class ProductionConfig(Config):
    super(DEBUG)
    pass
