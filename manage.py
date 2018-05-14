# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect


class Config(object):
    """配置类"""
    DEBUG = True

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


# 创建Flask应用程序实例
app = Flask(__name__)

app.config.from_object(Config)

# 创建SQLAlchemy对象
db = SQLAlchemy(app)
# 创建redis数据库链接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护
# 只做保护校验：至于生成csrf_token cookie 还有请求时携带csrf_token 需要自己来完成
CSRFProtect(app)


@app.route('/', methods=["GET", "POST"])
def index():
    # 测试redis
    redis_store.set("name", "itcast")
    return 'index'


if __name__ == '__main__':
    # 运行开发web服务器
    app.run()
