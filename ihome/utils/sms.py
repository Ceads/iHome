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


class CCP(object):
    def __init__(self):
        # 初始化REST SDK
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    # 发送模板短信
    # @param to 手机号码
    # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
    # @param $tempId 模板Id
    def send_template_sms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)

        if result.get("statusCode") == "000000":
            # 发送成功
            return 1
        else:
            # 发送失败
            return 0

# sendTemplateSMS(手机号码,内容数据,模板Id)

if __name__ == '__main__':
    # sendTemplateSMS("15351545159", ["123456", 5], 1)
    CCP().send_template_sms("15351545159", ["123456", 5], 1)