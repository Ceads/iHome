# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from ihome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8a216da8635e621f01637173b9260a8b'

# ���ʺ�Token
accountToken = '7fcf2c8d871940f7a4c4756a6303ab88'

# Ӧ��Id
appId = '8a216da8635e621f01637173b9830a92'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

def sendTemplateSMS(to, datas, tempId):
    # ��ʼ��REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    print result


    # sendTemplateSMS(�ֻ�����,��������,ģ��Id)

if __name__ == '__main__':
    sendTemplateSMS("15351545159", ["123456", 5], 1)