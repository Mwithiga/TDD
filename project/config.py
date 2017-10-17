# project/config.py
class BaseConfig:
	"""Base configuration"""
	DEBUG = False
	TESTING = False
class DevelopmentConfig(BaseConfig):
	"""Devepment Configuration"""
	DEBUG = True

class TestingConfig(BaseConfig):
	"""Testing Configuration"""
	DEBUG = True
	TESTING = True

class ProductionConfig(BaseConfig):
	"""docstring for ProductionConfig"""
	DEBUG = False
		