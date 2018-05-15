# coding=utf-8
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

from config import DevelopmentConfig

# 创建Flask应用程序实例
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

# 创建SQLAlchemy对象
db = SQLAlchemy(app)

# 创建redis数据库链接对象
redis_store = redis.StrictRedis(host=DevelopmentConfig.REDIS_HOST, port=DevelopmentConfig.REDIS_PORT)

# 开启CSRF保护
# 只做保护校验：至于生成csrf_token cookie 还有请求时携带csrf_token 需要自己来完成
CSRFProtect(app)

# session信息存储
Session(app)
