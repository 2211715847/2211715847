import json
import os

from PyQt5 import QtGui
from PyQt5.QtCore import QRegExp, Qt, QSize, pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QMessageBox

from utils.SysConfig import readCommonConfig
from pages.BailaimaSettingPageUI import Ui_Dialog


class BailaimaSetting(QDialog, Ui_Dialog):
    save_common_json_signal = pyqtSignal(str)

    common_json = {}

    def __init__(self):
        super(BailaimaSetting, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        self.save_icon = QtGui.QIcon()
        self.save_icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "/icon/save.png"))
        self.save_btn.setIconSize(QSize(60, 60))
        self.save_btn.setIcon(self.save_icon)

        self.common_json = readCommonConfig()
        self.initInputText()
        self.save_btn.clicked.connect(self.saveCommonConfigJson)

        self.basen_select.currentIndexChanged.connect(self.changeBaseN)

    #TODO 选择切换输入内容
    def changeBaseN(self):
        validator = QRegExpValidator(self)
        if int(self.basen_select.currentText()) == 10:
            reg = QRegExp('[0-9]+$')
            validator.setRegExp(reg)
        elif int(self.basen_select.currentText()) == 16:
            reg = QRegExp('[A-F0-9]+$')
            validator.setRegExp(reg)
        elif int(self.basen_select.currentText()) == 26:
            reg = QRegExp('[A-Z]+$')
            validator.setRegExp(reg)
        elif int(self.basen_select.currentText()) == 32:
            reg = QRegExp('[0123456789ABCDEFGHJKLMNPRSTVWXYZ]+$')
            validator.setRegExp(reg)
        self.start_num_input.setValidator(validator)
        self.end_num_input.setValidator(validator)

    def saveCommonConfigJson(self):
        self.common_json["print_ip"] = self.print_ip_input.text()
        self.common_json["fixed_content1"] = self.fixed_input1.text()
        self.common_json["fixed_content2"] = self.fixed_input2.text()

        self.common_json["start_num"] = self.start_num_input.text().upper()
        self.common_json["end_num"] = self.end_num_input.text().upper()

        self.common_json["error_correction"] = self.error_correction_select.currentIndex()
        self.common_json["direction"] = self.direction_select.currentIndex()
        self.common_json["repeat_select"] = self.repeat_num_select.currentIndex()
        self.common_json["product_num_select"] = self.product_num_select.currentIndex()

        self.common_json["step_num"] = int(self.step_num_input.text())
        self.common_json["repeat_num"] = int(self.repeat_num_input.text())
        self.common_json["guide_num"] = self.guide_num_input.text()
        self.common_json["baseN"] = int(self.basen_select.currentText())

        self.common_json["current_num"] = self.end_num_input.text().upper()

        self.writeCommonConfig()
        QMessageBox.information(self, '消息', '成功保存！', QMessageBox.Retry, QMessageBox.Retry)
        self.save_common_json_signal.emit("OK")

    def initInputText(self):
        self.print_ip_input.setText(self.common_json["print_ip"])
        self.fixed_input1.setText(self.common_json["fixed_content1"])
        self.fixed_input2.setText(self.common_json["fixed_content2"])
        self.start_num_input.setText(str(self.common_json["start_num"]).upper())
        self.end_num_input.setText(str(self.common_json["end_num"]).upper())
        self.step_num_input.setText(str(self.common_json["step_num"]))
        self.repeat_num_input.setText(str(self.common_json["repeat_num"]))
        self.guide_num_input.setText(str(self.common_json["guide_num"]))

        self.error_correction_select.setCurrentIndex(int(self.common_json["error_correction"]))
        self.direction_select.setCurrentIndex(int(self.common_json["direction"]))
        self.repeat_num_select.setCurrentIndex(int(self.common_json["repeat_select"]))
        self.product_num_select.setCurrentIndex(int(self.common_json["product_num_select"]))
        self.basen_select.setCurrentText(str(self.common_json["baseN"]))

    def writeCommonConfig(self):
        with open(f"{os.path.abspath(os.path.dirname(__file__))}/config/common_config.json", "w+") as f:
            jsonstr = json.dumps(self.common_json)
            f.write(jsonstr)
