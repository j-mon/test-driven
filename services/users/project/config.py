# services/users/project/config.py


class BaseConfig:
    """Base configuration"""
    Testing = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configurstion"""
    pass
