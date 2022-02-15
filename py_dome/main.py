import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import pyperclip
import base64
from Crypto.Cipher import AES
time=""

class DateTimeEditDemo(QWidget):
    #密钥
    key = '0D1A9A7CB27972878BAD8EFACDC7C46D'
    # 偏移量
    vi = '0000000000015304'
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        #设置窗口的标题与初始大小
        self.setWindowTitle('设置过期时间')
        self.resize(300, 90)
        #垂直布局
        vlayout = QVBoxLayout()
        #指定当前地日期为控件的日期，注意没有指定时间
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), self)
        # 设置日期时间格式，可以选择/ . : -等符号自定义数据连接符
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        # time=dateEdit.date()
        # time=time.toString("yyyyMMdd")
        # print(time)
        btn = QPushButton()
        btn.setText("获取密钥")
        btn.clicked.connect(self.my_click)
        btn2 = QPushButton()
        btn2.setText("设置软件到期时间")
        btn2.clicked.connect(self.set_key)
        #布局控件添加，设置主窗口的布局
        vlayout.addWidget(self.dateEdit)
        vlayout.addWidget(btn)
        vlayout.addWidget(btn2)
        self.setLayout(vlayout)
    def my_click(self):
        time = self.dateEdit.date()
        time = time.toString("yyyyMMdd")
        print(time)
        #加密
        data = time.encode('utf8')
        data = (lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode('utf-8'))(data)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.vi.encode('utf8'))
        encryptedbytes = cipher.encrypt(data)
        encodestrs = base64.b64encode(encryptedbytes)
        enctext = encodestrs.decode('utf8')
        print(enctext)
        pyperclip.copy(enctext)
        QMessageBox.about(self, "key", f"密钥{enctext}已复制到剪切板")
    def set_key(self):
        try:
            time = self.dateEdit.date()
            time = time.toString("yyyyMMdd")
            print(time)
            # 加密
            data = time.encode('utf8')
            data = (lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode('utf-8'))(data)
            cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.vi.encode('utf8'))
            encryptedbytes = cipher.encrypt(data)
            encodestrs = base64.b64encode(encryptedbytes)
            enctext = encodestrs.decode('utf8')
            print(enctext)
            f = open("lib/libkey.txt", "w")
            f.write(enctext)
            f.close()
            QMessageBox.information(self, "消息", "修改成功")
        except:
            QMessageBox.warning(self, "警告", "设置失败\n请在软件文件夹下设置")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DateTimeEditDemo()
    demo.show()
    sys.exit(app.exec_())
