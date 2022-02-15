import json
import os

from utils.BaseConver import alphabet2digit, digit2alphabet, digit2base32, base322digit

common_json = {
    "print_ip": "",  # 喷码机IP地址
    "template_name": "",  # 模板名称
    "logo_name": "",  # 图片模板名称
    "fixed_content1": "",  # 固定字符1
    "fixed_content2": "",  # 固定字符2
    "error_correction": 0,  # 矫正等级
    "step_num": 0,  # 步长
    "direction": 0,  # 方向
    "repeat_num": 0,  # 重复次数
    "guide_num": 0,  # 引导字符
    "repeat_select": 0,  # 是否重复喷印（整个计划）
    "product_num_select": 0,  # 是否需要产品号
    "start_num": 0,  # 开始位置
    "end_num": 0,  # 结束位置
    "baseN": 10,  # 进制转换
    "current_num": 0  # 当前喷印值
}


def readCommonConfig():
    with open(f"{os.path.abspath(os.path.dirname(__file__))}/../config/common_config.json", "r+") as f:
        common_json = json.loads(f.read())
    return common_json


def resizeBaseNtoTen(common_json):
    '''
    修改进制
    :param common_json:
    :return:
    '''
    common_json["current_num"] = str(common_json["current_num"]).lstrip("0")
    if common_json["current_num"] == "":
        common_json["current_num"] = "0"
    if common_json["baseN"] == 16:
        common_json["start_num"] = "0x" + str(common_json["start_num"])
        common_json["start_num"] = int(common_json["start_num"], 16)
        common_json["end_num"] = "0x" + str(common_json["end_num"])
        common_json["end_num"] = int(common_json["end_num"], 16)
        common_json["current_num"] = int(common_json["current_num"], 16)
    elif common_json["baseN"] == 26:
        common_json["start_num"] = int(alphabet2digit(common_json["start_num"]))
        common_json["end_num"] = int(alphabet2digit(common_json["end_num"]))
        common_json["current_num"] = int(alphabet2digit(common_json["current_num"]))
    elif common_json["baseN"] == 32:
        common_json["start_num"] = int(base322digit(common_json["start_num"]))
        common_json["end_num"] = int(base322digit(common_json["end_num"]))
        common_json["current_num"] = int(base322digit(common_json["current_num"]))
    elif common_json["baseN"] == 10:
        common_json["start_num"] = int(common_json["start_num"])
        common_json["end_num"] = int(common_json["end_num"])
        common_json["current_num"] = int(common_json["current_num"])

    return common_json


def resizeTentoBaseN(common_json):
    if common_json["baseN"] == 16:
        common_json["start_num"] = str(hex(common_json["start_num"]))[2:].upper()
        common_json["end_num"] = str(hex(common_json["end_num"]))[2:].upper()
        common_json["current_num"] = str(hex(common_json["current_num"]))[2:].upper()
    elif common_json["baseN"] == 26:
        common_json["start_num"] = str(digit2alphabet(int(common_json["start_num"]))).upper()
        common_json["end_num"] = str(digit2alphabet(int(common_json["end_num"]))).upper()
        common_json["current_num"] = str(digit2alphabet(int(common_json["current_num"]))).upper()
    elif common_json["baseN"] == 32:
        common_json["start_num"] = str(digit2base32(int(common_json["start_num"])).upper())
        common_json["end_num"] = str(digit2base32(int(common_json["end_num"])).upper())
        common_json["current_num"] = str(digit2base32(int(common_json["current_num"])).upper())
    return common_json


def saveCommonConfig(common_json):
    '''
    保存当前产品生产的流水码
    :param product_num: 产品流水号
    :return:
    '''
    with open(f"{os.path.abspath(os.path.dirname(__file__))}/../config/common_config.json", "w") as f:
        json.dump(common_json, f)
