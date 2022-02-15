import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from pages.BailaimaRegisterPageUI import Ui_Dialog
import wmi


class BailaimaRegister(QDialog, Ui_Dialog):

    def __init__(self):
        super(BailaimaRegister, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        self.s = wmi.WMI()

        self.save_btn.clicked.connect(self.registerMachine)
        self.register_input.setText(self.getRegisterText())

    def get_CPU_info(self):
        cpu = []
        cp = self.s.Win32_Processor()
        for u in cp:
            cpu.append(
                {
                    "Name": u.Name,
                    "Serial Number": u.ProcessorId,
                    "CoreNum": u.NumberOfCores
                }
            )
        #   print(":::CPU info:", json.dumps(cpu))
        return cpu

        # 硬盘序列号

    def get_disk_info(self):
        disk = []
        for pd in self.s.Win32_DiskDrive():
            disk.append(
                {
                    "Serial": self.s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(),  # 获取硬盘序列号，调用另外一个win32 API
                    "ID": pd.deviceid,
                    "Caption": pd.Caption,
                    "size": str(int(float(pd.Size) / 1024 / 1024 / 1024)) + "G"
                }
            )
        #   print(":::Disk info:", json.dumps(disk))
        return disk

        # mac 地址（包括虚拟机的）

    def get_network_info(self):
        network = []
        for nw in self.s.Win32_NetworkAdapterConfiguration():  # IPEnabled=0
            if nw.MACAddress != None:
                network.append(
                    {
                        "MAC": nw.MACAddress,  # 无线局域网适配器 WLAN 物理地址
                        "ip": nw.IPAddress
                    }
                )
        #    print(":::Network info:", json.dumps(network))
        return network

    # 主板序列号
    def get_mainboard_info(self):
        mainboard = []
        for board_id in self.s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard

    def getRegisterText(self):
        '''
        返回注册文本信息
        :return:
        '''
        a = self.get_network_info()
        b = self.get_CPU_info()
        c = self.get_disk_info()
        d = self.get_mainboard_info()
        machinecode_str = ""
        machinecode_str = machinecode_str + a[0]['MAC'] + b[0]['Serial Number'] + c[0]['Serial'] + d[0]
        return str(machinecode_str)

    def getCombinNumber(self):
        machinecode_str = self.getRegisterText()
        selectindex = [15, 30, 32, 38, 43, 46]
        macode = ""
        for i in selectindex:
            macode = macode + machinecode_str[i]
        return macode

    def registerMachine(self):
        macode = self.getCombinNumber()
        text = str(self.activation_input.text()).strip()
        if macode == text:
            with open("activation_code.txt", "w") as f:
                f.write(text)
            QMessageBox.information(self, '消息', '激活成功！', QMessageBox.Retry, QMessageBox.Retry)
            self.close()
        else:
            QMessageBox.information(self, '消息', '激活码错误！', QMessageBox.Retry, QMessageBox.Retry)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BailaimaRegister()
    window.show()
    sys.exit(app.exec_())
