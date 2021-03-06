# coding=utf-8
import redis
import logging

class Config(object):
    """配置类"""
    # 设置SECRET_KEY
    SECRET_KEY = "+0rgH2oxng+J1cH5zVt0kLZeMcEiCAA8GJgniP1pVAjxj+GKJpb0qaFfCtcskWFo"

    # mysql数据库相关配置
    # 设置数据库的链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_sz08"
    # 关闭追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session数据库配置
    # 设置session信息存放到redis数据库
    SESSION_TYPE = "redis"
    # 设置session存储到哪个redis数据库中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 设置session过期时间，两天
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopmentConfig(Config):
    """开发环境中配置类"""
    DEBUG = True

    # 开发阶段日志等级
    LOG_LEVEL=logging.DEBUG


class ProductionConfig(Config):
    """生产环境中的配置类"""
    # 设置数据库的链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_sz08"

    # 生产阶段日志等级
    LOG_LEVEL=logging.WARN

class TestingConfig(Config):
    """测试环境中的配置类"""
    # 设置数据库的链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_testcase"
    # 开启测试标志
    TESTING = True


config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
