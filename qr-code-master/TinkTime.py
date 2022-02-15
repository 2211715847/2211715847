import base64
from Crypto.Cipher import AES
from PyQt5.QtCore import QDate
import os
"""
获取当前时间
"""
# 密钥
key = '0D1A9A7CB27972878BAD8EFACDC7C46D'
# 偏移量
vi = '0000000000015304'
def atime():
    newtime=QDate.currentDate()#获取当前日期
    newtime=newtime.toString("yyyyMMdd")
    # print(newtime)
    return newtime

def settiem():
    if os.path.isfile("lib/libkey.txt"):
        f = open("lib/libkey.txt", "r")
        key = f.read()
        # print(key)
        return key
    else:
        f = open("lib/libkey.txt", "w")
        f.write("8z1hWaRgNmSPqypMwa4u4w==")
        f.close()
        return "8z1hWaRgNmSPqypMwa4u4w=="


def Jtime():
    """
    判断是否到期
    :type 可以使用
    :false 不可使用
    """
    newtime=atime()
    temp=settiem()
    timeing=decrypt(temp)
    if newtime<timeing:
        return True
    else:
        return False
def decrypt(data):
    try:
        """解密"""
        data = data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC,vi.encode('utf8'))
        text_decrypted = cipher.decrypt(encodebytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        print(text_decrypted)
        return text_decrypted
    except:
        f = open("lib/libkey.txt", "w")
        f.write("8z1hWaRgNmSPqypMwa4u4w==")
        f.close()
        return "20000101"
