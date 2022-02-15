
import os
import socket
import sys
import time


from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, QThread, QMutex, pyqtSignal
from PyQt5.QtGui import QPixmap

import TinkTime
from BailaimaRegister import BailaimaRegister
from BailaimaSetting import BailaimaSetting
from TinkTime import Jtime
from utils.PrinterHandler import Printer
from utils.SysConfig import readCommonConfig
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QLabel, \
    QFileDialog, QMessageBox, QInputDialog
from pages.BailaimaPageUI import Ui_MainWindow
from utils.dongle.DongleDecorator import DongleDecorator as dongleDecorator
from utils.dongle.Dongle import Dongle
# from utils.thread.threadUtil import ThreadUtil
# thread = ThreadUtil()

qmut_1 = QMutex()
text=""
enableStr = "/*按钮普通态*/\n" \
            "QPushButton {\n" \
            "    color: #000000;\n" \
            "    /*背景颜色*/\n" \
            "    background-color: #ffffff;\n" \
            "    outline: none;\n" \
            "    border-radius: 5px;\n" \
            "    border: 1px solid #dddddd;\n" \
            "}\n" \
            "QPushButton:hover {\n" \
            "    border: 1px solid #7084D4;\n" \
            "}\n" \
            "QPushButton:pressed {\n" \
            "    padding-left: 3px;\n" \
            "    padding-top: 3px;\n" \
            "}"

disableStr = "/*按钮普通态*/\n" \
             "QPushButton {\n" \
             "    /*字体颜色为白色*/\n" \
             "    color: #000000;\n" \
             "    /*背景颜色*/\n" \
             "    background-color: #DDDDDD;\n" \
             "    outline: none;\n" \
             "    border-radius: 5px;\n" \
             "    border: 1px solid #dddddd;\n" \
             "}\n" \
             "QPushButton:hover {\n" \
             "    border: 1px solid #7084D4;\n" \
             "}\n" \
             "QPushButton:pressed {\n" \
             "    padding-left: 3px;\n" \
             "    padding-top: 3px;\n" \
             "}"


class BailaiMa(QMainWindow, Ui_MainWindow):
    printer = None

    def __init__(self,parent=None):
        super(BailaiMa, self).__init__(parent)
        # TODO 暂时不需要
        # if not self.isRegister():
        #     sys.exit(0)
        self.setupUi(self)
        ''''''
        setup()
        self. Thread_1 = Thread_1(self)
        self.Thread_1.start()
        self.Thread_1.signal.connect(self.messageDialog)
        ''''''
        self.start_btn.clicked.connect(self.start)
        self.exit_btn.clicked.connect(self.finish)
        self.setting_btn.clicked.connect(self.setting)

        self.start_icon = QtGui.QIcon()
        self.start_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "/icon/start.png"))

        self.stop_icon = QtGui.QIcon()
        self.stop_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "/icon/stop.png"))

        self.setting_icon = QtGui.QIcon()
        self.setting_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "/icon/setting.png"))

        self.exit_icon = QtGui.QIcon()
        self.exit_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "/icon/exit.png"))

        self.start_btn.setIconSize(QSize(60, 60))
        self.setting_btn.setIconSize(QSize(60, 60))
        self.exit_btn.setIconSize(QSize(60, 60))

        self.start_btn.setIcon(self.start_icon)
        self.exit_btn.setIcon(self.exit_icon)
        self.setting_btn.setIcon(self.setting_icon)



        self.initUI(None)

    def initUI(self, msg):
        commonConfig = readCommonConfig()
        self.init_num_text.setText(str(commonConfig["start_num"]))
        self.stop_num_text.setText(str(commonConfig["end_num"]))
        self.initTable()

    def isRegister(self):
        bailaimaregister = BailaimaRegister()
        if os.path.isfile("activation_code.txt"):
            with open("activation_code.txt", "r") as f:
                if f.read() == bailaimaregister.getCombinNumber():
                    return True
                else:
                    bailaimaregister.show()
                    bailaimaregister.exec_()
                    return False
        else:
            bailaimaregister.show()
            bailaimaregister.exec_()
            return False

    def start(self):
        '''
        开始功能
        :return:
        '''
        if self.start_btn.text() == "开始":
            self.stopBtnUi()
            # 开始喷印
            self.startPrint()
        else:
            self.stopPrint()

    def stopPrint(self):
        '''
        停止打印
        :return:
        '''
        self.start_btn.setDisabled(True)
        self.printer.stop()
        self.startBtnUi()
        self.status_num_text.setText("已停止")
        self.status_num_text.setStyleSheet("color:black")

    def stopBtnUi(self):
        '''
        用户点击开始后按钮的UI
        :return:
        '''
        self.start_btn.setText("停止")
        self.start_btn.setIcon(self.stop_icon)
        self.setting_btn.setDisabled(True)
        self.setting_btn.setStyleSheet(disableStr)
        self.exit_btn.setDisabled(True)
        self.exit_btn.setStyleSheet(disableStr)

    def startBtnUi(self):
        '''
         用户点击停止后按钮的UI
         :return:
         '''
        self.start_btn.setText("开始")
        self.start_btn.setDisabled(False)
        self.start_btn.setIcon(self.start_icon)
        self.setting_btn.setDisabled(False)
        self.setting_btn.setStyleSheet(enableStr)
        self.exit_btn.setDisabled(False)
        self.exit_btn.setStyleSheet(enableStr)

    def startPrint(self):
        '''
        开始打印 初始化打印机
        :return:
        '''
        if self.printer == None:
            self.printer = Printer()
            self.printer.print_image_bytes_signal.connect(self.addPrintMsg)
            self.printer.print_stop_signal.connect(self.startBtnUi)
            self.printer.print_error_signal.connect(self.printErrorHandle)
            self.printer.print_signal.connect(self.printStatus)
        self.printer.start()

    def printStatus(self, msg):
        '''
        打印机状态回调
        :param msg: 返回信息
        :return:
        '''
        if msg == "连接中":
            self.status_num_text.setText(msg)
            self.status_num_text.setStyleSheet("color:#0C7884")
        if msg == "已停止":
            self.status_num_text.setText(msg)
            self.status_num_text.setStyleSheet("color:#0C7884")
        if msg == "连接成功":
            self.status_num_text.setText(msg)
            self.status_num_text.setStyleSheet("color:green")
        if msg == "开始打印失败,请重新打印":
            self.status_num_text.setText(msg)
            self.status_num_text.setStyleSheet("color:red")
        if msg == "停止失败，请手动关闭":
            self.status_num_text.setText(msg)
            self.status_num_text.setStyleSheet("color:red")

    def printErrorHandle(self, msg):
        '''
        喷印过程中的错误回调
        :param msg:
        :return:
        '''
        if socket.timeout == type(msg["ERROR"]):
            QMessageBox.information(self, '消息', f'{msg["ERROR"]}{msg["MESSAGE"]}！', QMessageBox.Retry,
                                    QMessageBox.Retry)
            self.status_num_text.setText(msg["MESSAGE"])
            self.status_num_text.setStyleSheet("color:red")
            self.startBtnUi()
        else:
            QMessageBox.information(self, '消息', f'{msg}', QMessageBox.Retry, QMessageBox.Retry)
            self.stopPrint()

    def addPrintMsg(self, jsonStr):
        '''
        滚动table
        :param jsonStr: 显示数据
        :return:
        '''
        label = self.imageBuilder(jsonStr)
        self.current_num_text.setText(str(jsonStr["current_num"]))
        self.loglist_table.setItem(self.loglist_table.rowCount() - 1, 0, self.tableItem(jsonStr["current_num"]))
        self.loglist_table.setItem(self.loglist_table.rowCount() - 1, 1, self.tableItem(jsonStr["content"]))
        self.loglist_table.setCellWidget(self.loglist_table.rowCount() - 1, 2, label)
        self.loglist_table.setRowHeight(self.loglist_table.rowCount() - 1, 150)

    def imageBuilder(self, jsonStr):
        '''
        字节流转化为图片
        :param jsonStr: 字节流
        :return:
        '''
        label = QLabel("")
        label.setAlignment(Qt.AlignCenter)
        qp = QPixmap()
        qp.loadFromData(bytes(jsonStr["img"]))
        label.setPixmap(qp.scaled(120, 120))
        return label

    def initTable(self):
        self.loglist_table.setRowCount(1)
        self.loglist_table.setColumnCount(3)
        self.loglist_table.setHorizontalHeaderLabels(['计数器', '二维码内容', '二维码'])
        self.loglist_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loglist_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        font = self.loglist_table.horizontalHeader().font()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.loglist_table.horizontalHeader().setFont(font)

    def finish(self):
        if self.printer != None:
            try:
                self.printer.disconnect_print()
            except:
                pass
        self.close()

    def setting(self):
        bailaimasetting = BailaimaSetting()
        bailaimasetting.save_common_json_signal.connect(self.initUI)
        bailaimasetting.exec_()

    def tableItem(self, text):
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def messageDialog(self,text):
        """
        弹窗
        :return:
        """
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', text)
        msg_box.exec_()
        dongle = Dongle()
        self.a=dongle.check()
        if(self.a):
            pass
        else:
            app = QApplication.instance()
            app.quit()
"""
2022.1.24
"""

class Thread_1(QThread):  # 线程1
    signal = pyqtSignal(str)
    k1 = True
    k2 = True
    def __init__(self,BailaiMa):
        super(Thread_1, self).__init__()
        self.BailaiMa= BailaiMa
    def run(self):
        print("启动线程")
        self.dongleThread()


    def dongleThread(self):
        """
        加密狗检查定时器，定时检查加密狗是否存在
        :return:
        """
        dongle = Dongle(callable=self.threadDongleCallable)
        while True:
            self.k2=dongle.check()
            # print(self.k2)
            if(self.k2):
                self.k1=True
            time.sleep(0.5)
    def threadDongleCallable(self):
        """
        定时器中加密狗检查未通过时的回调函数，重新插入加密狗继续运行程序或直接退出程序
        :return:
        """
        if(self.k1!=self.k2):

            text = "加密狗已移除!\n您可以插入加密狗继续操作程序\n或退出该程序，请确保程序已备份。"
            self.signal.emit(text)
            self.k1=self.k2
            # print("2")

    def inputDialog(self):
        text, ok = QInputDialog.getText(self, '输入文本框', '请输入您的文本内容')
        if ok:
            self.text.setText(text)
def setupDongleCallable():
    """
    启动时加密狗检查未通过时的回调函数，抛异常结束程序
    :return:
    """
    text="请插入加密狗后在执行本程序"
    BailaiMa.messageDialog(self=BailaiMa,text=text)
    #raise Exception(text)
    sys.exit(0)





@dongleDecorator(callable=setupDongleCallable)
def setup():
    """
    启动函数，调用时先检查加密狗是否存在
    :return:
    """
    if (Jtime()):
        pass
    else:  # 不可使用，1弹出输入框，修改key，判断后进入QMessageBox(QMessageBox.Warning, '警告', text)
        #加一个自定义报错
        while not Jtime():
            key, ok = QInputDialog.getText(None, "密钥更换", "输入新密钥")
            f = open("lib/libkey.txt", "w")
            f.write(key)
            f.close()
            # print(ok)
            if ok:
                if Jtime():
                    QMessageBox.information(None, "消息", "密钥更换成功")
                else:
                    QMessageBox.critical(None, "错误", "密钥错误，请重新输入")
            else:
                sys.exit(0)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BailaiMa()
    window.showFullScreen()  # 显示窗口
    window.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # window = BailaiMa()
    # window.showFullScreen()
    # sys.exit(app.exec_())
