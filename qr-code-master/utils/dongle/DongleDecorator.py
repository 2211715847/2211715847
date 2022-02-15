
from utils.dongle import Psyunew3
from ctypes import *
import platform
DevicePath=create_string_buffer(260)
ret=c_int()

class DongleDecorator():
    def __init__(self, callable=None):
        self.callable = callable
        pass

    def __call__(self, func):
        def _call(*args, **kwargs):
            if not self.findPort():
                if (self.callable): self.callable()
                return
            if not self.checkKeyByFindort_2():
                if (self.callable): self.callable()
                return
            if not self.checkKeyByEncstring():
                if (self.callable): self.callable()
                return
            if not self.CheckKeyByEncstring_New():
                if (self.callable): self.callable()
                return
            if not self.CheckKeyByReadEprom():
                if (self.callable): self.callable()
                return
            self.isLinux()
            return func(*args, **kwargs)
        return _call

    def findPort(self):
        ##这个用于判断系统中是否存在着加密锁。不需要是指定的加密锁,
        ret = Psyunew3.FindPort(0, DevicePath)
        if (ret != 0):
            # print('未找到加密锁,请插入加密锁后，再进行操作。')
            return False
        else:
            # print('找到加密锁。')
            return True

    def checkKeyByFindort_2(self):
        ##使用普通算法一来检查是否存在指定的加密锁
        if (Psyunew3.CheckKeyByFindort_2() == 0):
            # print('使用普通算法一来检查:找到指定的加密锁')
            return True
        else:
            # print('使用普通算法一来检查:未能找到指定的加密锁')
            return False

    def checkKeyByEncstring(self):
        ##使用增强算法一来检查是否存在指定的加密锁
        ret = Psyunew3.CheckKeyByEncstring()
        if (ret == 1):
            # print('你生成加密代码时没有设置该函数')
            return True
        else:
            if (ret == 0):
                # print('使用增强算法一来检查:找到指定的加密锁')
                return True
            else:
                # print('使用增强算法一来检查:未能找到指定的加密锁')
                return False

    def CheckKeyByEncstring_New(self):
        ##使用增强算法二来检查是否存在指定的加密锁
        ret = Psyunew3.CheckKeyByEncstring_New()
        if (ret == 0):
            # print('使用增强算法二来检查:找到指定的加密锁')
            return True
        else:
            if (ret < 0):
                # print('使用增强算法二来检查:未能找到指定的加密锁')
                return False
            else:
                if (ret == 2):
                    # print('当前锁不支持这个功能。')
                    return False

    def CheckKeyByReadEprom(self):
        ##使用读写储存器来检查是否存在指定的加密锁
        ret = Psyunew3.CheckKeyByReadEprom()
        if (ret == 1):
            # print('你生成加密代码时没有设置该函数')
            return True
        else:
            if (ret == 0):
                # print('使用读写储存器来检查:找到指定的加密锁')
                return True
            else:
                # print('使用读写储存器来检查:未能找到指定的加密锁')
                return False

    def isLinux(self):
        if 'Linux' in platform.system():
            Psyunew3.CloseUsbHandle(DevicePath)  # 关闭USB设备


if __name__ == '__main__':
    def callable():
        print("您没有插入对应的加密狗")


    @DongleDecorator(callable=callable)
    class test:
        def __init__(self):
            pass

        # @DongleCallable(callable=callable)
        def tes(self, t):
            print(t)

    t = test()
    t.tes("test")


