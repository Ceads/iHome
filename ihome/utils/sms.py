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


class CCP(object):
    # cls.instance
    def __new__(cls, *args, **kwargs):
        # �ж�cls�Ƿ�ӵ������_instance����������������������Ψһ���󣨵�������
        if not hasattr(cls,"_instance"):
            # ����һ����������
            obj = super(CCP, cls).__new__(cls, *args, **kwargs)
            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls._instance = obj
        # ֱ�ӷ���
        return cls._instance

    # def __init__(self):


    # ����ģ�����
    # @param to �ֻ�����
    # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
    # @param $tempId ģ��Id
    def send_template_sms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)

        if result.get("statusCode") == "000000":
            # ���ͳɹ�
            return 1
        else:
            # ����ʧ��
            return 0

# sendTemplateSMS(�ֻ�����,��������,ģ��Id)

if __name__ == '__main__':
    # sendTemplateSMS("15351545159", ["123456", 5], 1)
    # CCP().send_template_sms("15351545159", ["123456", 5], 1)
    obj1 = CCP()
    obj2 = CCP()

    print id(obj1)
    print id(obj2)