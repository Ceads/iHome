# coding=utf-8
# 此文件中定义和用户登陆，注册有关api
from flask import request, jsonify

from ihome.utils.response_code import RET
from . import api


@api.route("/users", methods=["POST"])
def register():
    """
    用户注册功能
    1、接收参数（手机号，短信验证码，密码）并进行参数检验
    2、从redis中获取短信验证码（如果取不到，说明短信已过期）
    3、对比短信验证码，如果一致
    4、创建User对象并保存注册用户的信息
    5、把注册用户的信息添加进数据库
    6、返回应答，注册成功
    # """
    # 1、接收参数（手机号，短信验证码，密码）并进行参数检验
    req_dict = request.json
    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")

    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")

    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")


        # 2、从redis中获取短信验证码（如果取不到，说明短信已过期）
        # 3、对比短信验证码，如果一致
        # 4、创建User对象并保存注册用户的信息
        # 5、把注册用户的信息添加进数据库
        # 6、返回应答，注册成功
