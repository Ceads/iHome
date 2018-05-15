# coding=utf-8
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

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

    # session数据库配置
    # 设置session信息存放到redis数据库
    SESSION_TYPE = "redis"
    # 设置session存储到哪个redis数据库中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 设置session过期时间，两天
    PERMANENT_SESSION_LIFETIME = 86400*2

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

# session信息存储
Session(app)

@app.route('/', methods=["GET", "POST"])
def index():
    # 测试redis
    redis_store.set("name", "itcast")

    # 测试session存储
    session["name"]="itheima"

    return 'index'


if __name__ == '__main__':
    # 运行开发web服务器
    app.run()
