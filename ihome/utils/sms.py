# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from ihome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

# 主帐号
accountSid = '8a216da8635e621f01637173b9260a8b'

# 主帐号Token
accountToken = '7fcf2c8d871940f7a4c4756a6303ab88'

# 应用Id
appId = '8a216da8635e621f01637173b9830a92'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id

def sendTemplateSMS(to, datas, tempId):
    # 初始化REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    print result


    # sendTemplateSMS(手机号码,内容数据,模板Id)

if __name__ == '__main__':
    sendTemplateSMS("15351545159", ["123456", 5], 1)