from time import sleep

from PyQt5.QtCore import pyqtSignal, QThread

from utils.BaseConver import digit2alphabet, digit2hexadecimal, digit2base32
from utils.QrCode import QrCodeBuilder
from utils.SysConfig import readCommonConfig, saveCommonConfig, resizeBaseNtoTen, resizeTentoBaseN
from utils.SocketAssistant import SocketAssistant


class Printer(QThread):
    common_json = {}
    assistant = None
    print_image_bytes_signal = pyqtSignal(dict)
    print_stop_signal = pyqtSignal(str)
    print_error_signal = pyqtSignal(dict)
    print_signal = pyqtSignal(str)
    print_select_template = False
    stop_flag = False
    print_flag = False

    def __init__(self):
        super(Printer, self).__init__()
        self.common_json = readCommonConfig()

    def run(self):
        # try:
        self.print_signal.emit("连接中")
        if self.assistant == None:
            self.assistant = SocketAssistant(self.common_json["print_ip"])
        self.print_signal.emit("连接成功")
        self.handlerSendMsg()

    # except Exception as error:
    #     self.print_error_signal.emit({"ERROR": error, "MESSAGE": "网络连接失败"})

    def stop(self):
        if self.assistant != None:
            self.stop_flag = True
            if not self.print_flag:
                self.print_stop_signal.emit("STOP")
            else:
                self.assistant.sendMsg(f"{chr(2)}O0{chr(3)}")

    def handlerSendMsg(self):
        self.common_json = readCommonConfig()
        self.common_json = resizeBaseNtoTen(self.common_json)
        self.print_flag = True
        self.assistant.sendMsg(f"{chr(2) + 'O1' + chr(3)}")
        # 重复打印全部循环
        if self.common_json["repeat_select"] == 0:
            if self.common_json["direction"] == 0:
                end_num = self.common_json["end_num"] + 1
            else:
                end_num = self.common_json["end_num"] - 1
            while True:
                if self.stop_flag:
                    break
                self.sendMessagePrint(end_num)
        else:
            if self.common_json["direction"] == 0:
                end_num = self.common_json["end_num"] + 2
            else:
                end_num = self.common_json["end_num"] - 2
            self.sendMessagePrint(end_num)

        self.assistant.sendMsg(f"{chr(2)}O0{chr(3)}")
        self.print_stop_signal.emit("STOP")
        self.stop_flag = False
        self.print_flag = False

    def sendMessagePrint(self, end_num):
        character_length_template, step_num = self.select_print_config()
        if self.common_json["current_num"] != self.common_json["end_num"]:
            start_num = self.common_json["current_num"]
        else:
            start_num = self.common_json["start_num"]
        for i in range(start_num, end_num, step_num):
            for j in range(0, self.common_json["repeat_num"]):
                if self.stop_flag:
                    break
                sleep(0.01)
                product_text, guide_num = self.select_product_text_config(i, character_length_template)
                try:
                    # 二维码生成器
                    if self.print_select_template == False:
                        builder = QrCodeBuilder()
                        message, imageByte = builder.GenerateQRCodeSingleFile("A", product_text)
                        self.assistant.sendMsg(message)
                        sleep(0.01)
                        self.assistant.sendMsg(
                            f"{chr(2)}UW2{chr(10)}{guide_num}{chr(3)}{chr(2)}MB{chr(3)}")
                        self.print_select_template = True
                    else:
                        builder = QrCodeBuilder()
                        message, imageByte = builder.GenerateQRCodeSingleFile("B", product_text)
                        self.assistant.sendMsg(message)
                        sleep(0.01)
                        self.assistant.sendMsg(
                            f"{chr(2)}UW3{chr(10)}{guide_num}{chr(3)}{chr(2)}MA{chr(3)}")
                        self.print_select_template = False
                except Exception as err:
                    self.print_error_signal.emit({"ERROR": err, "MESSAGE": "二维码生成失败"})
                flag = False
                while not flag:
                    if self.stop_flag:
                        break
                    text = None
                    try:
                        text = self.assistant.receiveMsgAKC()
                    except Exception as error:
                        print(error)
                    flag = self.assistant.CheckAck(text)
                if self.stop_flag:
                    break
                self.print_image_bytes_signal.emit(
                    {"img": imageByte,
                     "current_num": guide_num,
                     "content": product_text})
                self.save_current_product_num(guide_num)

    def select_product_text_config(self, i, character_length_template):
        '''
        文本信息选择
        :param i: 流水号
        :param character_length_template: 字符模板长度
        :return:  产品信息,引导字符
        '''
        guide_num = ""
        if self.common_json["product_num_select"] == 0:
            i = self.select_current_product_num_base(i)
            guide_num = i
            if str(self.common_json['guide_num']).strip() != "":
                guide_num = str(i).rjust(
                    len(str(character_length_template)), str(self.common_json['guide_num']))
            product_text = self.common_json['fixed_content1'] + guide_num + self.common_json[
                'fixed_content2']
        else:
            product_text = self.common_json['fixed_content1'] + self.common_json['fixed_content2']
        return product_text, guide_num

    def save_current_product_num(self, i):
        '''
        保存当前喷印的值
        :param i:
        :return:
        '''

        temp = self.common_json
        temp = resizeTentoBaseN(temp)
        if i.strip() == "":
            i = self.common_json["end_num"]
        temp["current_num"] = i
        saveCommonConfig(temp)
        self.common_json = resizeBaseNtoTen(self.common_json)

    def select_current_product_num_base(self, i):
        '''
        选择当前流水号进制
        :param i: 流水号
        :return:
        '''
        guide_num = str(i)
        if self.common_json["baseN"] == 26:
            guide_num = str(digit2alphabet(i))
        elif self.common_json["baseN"] == 16:
            guide_num = str(digit2hexadecimal(i))
        elif self.common_json["baseN"] == 32:
            guide_num = str(digit2base32(i, 32))
        return str(guide_num).upper()

    def select_print_config(self):
        '''
        选择喷印字符模板长度和步进方向
        :return:
        '''
        self.common_json = resizeTentoBaseN(self.common_json)
        character_length_template = self.common_json['end_num']
        self.common_json = resizeBaseNtoTen(self.common_json)

        if self.common_json["direction"] == 0:
            step_num = abs(int(self.common_json["step_num"]))
        else:
            character_length_template = self.common_json['start_num']
            step_num = -abs(int(self.common_json["step_num"]))
        return character_length_template, step_num

    def disconnect_print(self):
        if self.assistant != None:
            self.assistant.disconnect_socket()
