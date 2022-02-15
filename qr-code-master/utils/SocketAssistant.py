import _thread
import socket  # socket模块


class SocketAssistant():
    port = 3100
    Socket_Assistant_PRINT = None

    def __init__(self, PRINT_IP):
        super(SocketAssistant, self).__init__()
        '''
        网口助手
        :param PRINT_IP: 喷码机IP
        :param PRINT_PORT: 喷码机端口 发送数据端口3100
        '''
        # 定义socket类型，发送消息到喷码机
        self.Socket_Assistant_PRINT = socket.socket()
        self.Socket_Assistant_PrintAKC = socket.socket()
        self.Socket_Assistant_PRINT.settimeout(10)
        self.Socket_Assistant_PrintAKC.settimeout(1)
        self.Socket_Assistant_PRINT.connect((PRINT_IP, 3100))
        self.Socket_Assistant_PrintAKC.connect((PRINT_IP, 3101))

        _thread.start_new_thread(self.getPrintMessage, ())

    def sendMsg(self, msg):
        if type(msg) != bytearray:
            self.Socket_Assistant_PRINT.send(str(msg).encode())
            return
        self.Socket_Assistant_PRINT.send(msg)

    def receiveMsg(self):
        return self.Socket_Assistant_PRINT.recv(1024).decode()

    def receiveMsgAKC(self):
        return self.Socket_Assistant_PrintAKC.recv(1024).decode()

    def disconnect_socket(self):
        try:
            self.Socket_Assistant_PRINT.shutdown(socket.SHUT_RDWR)
        except:
            self.Socket_Assistant_PRINT.close()
        try:
            self.Socket_Assistant_PrintAKC.shutdown(socket.SHUT_RDWR)
        except:
            self.Socket_Assistant_PrintAKC.close()

    def CheckAck(self, strReturn):
        '''
        喷印成功确认码
        :param strReturn:
        :return:
        '''
        result = False
        strReturn = str(strReturn).strip()
        if strReturn != None and strReturn != "" and len(strReturn) > 0 and chr(6) in strReturn:
            return True
        return result

    def getPrintMessage(self):
        while True:
            try:
                self.receiveMsg()
                self.receiveMsgAKC()
            except:
                pass
