# -- coding: utf-8 --
import Psyunew3
import sys
from ctypes import *
import platform
DevicePath=create_string_buffer(260)
ret=c_int()

##这个用于判断系统中是否存在着加密锁。不需要是指定的加密锁,
ret = Psyunew3.FindPort(0,DevicePath)
if(ret!=0):
    print('未找到加密锁,请插入加密锁后，再进行操作。')
    exit()

##使用普通算法一来检查是否存在指定的加密锁
if (Psyunew3.CheckKeyByFindort_2() == 0):
    print('使用普通算法一来检查:找到指定的加密锁')
else:
    print('使用普通算法一来检查:未能找到指定的加密锁')


##使用增强算法一来检查是否存在指定的加密锁
ret = Psyunew3.CheckKeyByEncstring()
if (ret == 1):
    print( '你生成加密代码时没有设置该函数')
else:
    if (ret == 0):
        print('使用增强算法一来检查:找到指定的加密锁')
    else:
        print('使用增强算法一来检查:未能找到指定的加密锁')

##使用增强算法二来检查是否存在指定的加密锁
ret = Psyunew3.CheckKeyByEncstring_New()
if (ret == 0):
    print('使用增强算法二来检查:找到指定的加密锁')
else:
    if (ret < 0):
        print('使用增强算法二来检查:未能找到指定的加密锁')
    else:
        if (ret == 2):
           print('当前锁不支持这个功能。')

##使用读写储存器来检查是否存在指定的加密锁
ret = Psyunew3.CheckKeyByReadEprom()
if (ret == 1):
     print('你生成加密代码时没有设置该函数')
else:
    if (ret == 0):
         print('使用读写储存器来检查:找到指定的加密锁')
    else:
         print('使用读写储存器来检查:未能找到指定的加密锁')


outstring =Psyunew3.StrEnc("20220214", '0D1A9A7CB27972878BAD8EFACDC7C46D'.encode('utf-8'))
print(ret)



if 'Linux' in platform.system():
    Psyunew3.CloseUsbHandle(DevicePath)#关闭USB设备






               
        
		
