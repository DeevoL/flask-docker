class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfing(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    pass