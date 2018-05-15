# coding=utf-8
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import Config


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

# 创建Manager管理对象
manager = Manager(app)
Migrate(app, db)
# 添加迁移命令
manager.add_command("db", MigrateCommand)


@app.route('/', methods=["GET", "POST"])
def index():
    # 测试redis
    redis_store.set("name", "itcast")

    # 测试session存储
    session["name"] = "itheima"

    return 'index'


if __name__ == '__main__':
    # 运行开发web服务器
    # app.run()
    manager.run()
