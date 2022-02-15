from io import BytesIO
from utils.SysConfig import readCommonConfig
import qrcode
import numbers
from PIL import Image

ERROR_CORRECT_M = 0
ERROR_CORRECT_L = 1
ERROR_CORRECT_Q = 3
ERROR_CORRECT_H = 2


class QrCodeBuilder():
    '''
    二维码图片生成器
    '''
    # Qrcode 图片大小 2 是 25X25
    Qr_version = 2
    # 默认是ERROR_CORRECT_L
    Qr_error_correction = ERROR_CORRECT_L
    # QtCode对象
    QrCode = None
    common_json = {}

    def __init__(self, Qr_version=2):
        '''
        初始化QrCode
        :param Qr_version: 设置QrCode的生成的二维码大小
        :param Qr_error_correction: 设置QrCode校验码的等级
        '''
        self.common_json = readCommonConfig()
        self.QrCode = qrcode.QRCode(
            version=Qr_version,
            error_correction=int(self.common_json["error_correction"]),
            box_size=1,
            border=0
        )

    def AsciiToHex(self, text):
        _bytes = text.encode()
        text = ""
        for b in _bytes:
            text = text + str(hex(b))[2:]
        return str(text)

    def GenerateQRCode(self, Text):
        '''
        直接发送二维码到喷码机
        已启用
        :param Text: 内容
        :return: 喷印的指令
        '''
        self.QrCode.add_data(Text)
        self.QrCode.make(fit=False)
        img = self.QrCode.make_image()
        # 设置位灰度图
        img = img.convert("1")
        # TODO 开始读取
        imgByteArr = BytesIO()
        # 设置图片格式为位图BMP
        img.save(imgByteArr, format='bmp')
        # 图片的字节流
        imgByteArr = BytesIO(imgByteArr.getvalue())
        # capture_img = Image.open(imgByteArr).convert('RGBA')
        # capture_img.save("Temp.bmp")
        # TODO 暂时不需要保存图片
        # with open(os.path.abspath(os.path.dirname(__file__)) + '/../temp/Temp.bmp', 'wb') as f:  # 写入
        #     f.write(imgByteArr.getvalue())
        # VJ100 = VJ1000ActiveX()
        # print(VJ100.UpdateLogoData("test", os.path.abspath(os.path.dirname(__file__)) + '/../temp/Temp.bmp'))

        # 获取RGBA值
        capture_img = Image.open(imgByteArr).convert('RGBA')
        num = capture_img.size[0]
        num2 = capture_img.size[1]
        text = ""
        num3 = capture_img.size[0] / 8
        if capture_img.size[0] % 8 > 0:
            num3 = num3 + 1
        for i in range(0, capture_img.size[0]):
            text2 = ""
            for j in range(0, int(num3)):
                for k in range(0, 8):
                    num4 = k + j * 8
                    if num4 >= capture_img.size[0]:
                        text2 = text2 + str(0)
                        continue
                    color = capture_img.getpixel((i, num4))
                    colorA = color[3]
                    colorR = color[0]
                    colorG = color[1]
                    colorB = color[2]
                    if colorA != 255 or colorB != 255 or colorG != 255 or colorR != 255:
                        text2 = text2 + "1"
                    else:
                        text2 = text2 + "0"
            text3 = f"{hex(int(text2, 2))}"[2:]
            text3 = text3.zfill(6).upper()
            text = text + text3
        # TODO Logo name用户自定义
        return str(chr(2)) + "L" + f'{self.common_json["logo_name"]}' + str(chr(10)) + str(num).zfill(2) + str(
            num2).zfill(3) + text + str(
            chr(3)), imgByteArr.getvalue()

    def GenerateQRCodeSingleFile(self, template_name, Text):
        self.QrCode.add_data(Text)
        self.QrCode.make(fit=False)
        img = self.QrCode.make_image()
        # 设置位灰度图
        img = img.convert("1")
        imgByteArr = BytesIO()
        # 设置图片格式为位图BMP
        img.save(imgByteArr, format='bmp')
        # 图片的字节流
        imgByteArr = BytesIO(imgByteArr.getvalue())
        capture_img = Image.open(imgByteArr).convert('RGBA')
        # 右边扩充一列 颜色为白色
        capture_img = self.image_border(capture_img, 'r', 1, color=(255, 255, 255))
        imageList = list()
        if capture_img.size[1] != 25:
            return
        if capture_img.size[0] < 4 or capture_img.size[0] * capture_img.size[1] > 31280:
            return
        num = 0
        num2 = 0
        if capture_img.size[1] == 34:
            num3 = 140
        elif capture_img.size[1] != 24:
            num3 = 300
        else:
            num3 = 200
        text = self.AsciiToHex(template_name)
        text2 = self.AsciiToHex(str(capture_img.size[1]))
        text4 = ""
        text6 = ""
        for i in range(0, capture_img.size[0]):
            for j in range(0, capture_img.size[1]):
                if capture_img.getpixel((i, j))[0] != 0:
                    text6 = text6 + "0"
                else:
                    text6 = text6 + "1"
                if ((capture_img.size[1] != 34 or (j != 1 and j != 9 and j != 17 and j != 25 and j != 33)) and (
                        (capture_img.size[1] != 16 and capture_img.size[1] != 24) or (
                        j != 7 and j != 15 and j != 23)) and (
                        capture_img.size[1] != 25 or (j != 0 and j != 8 and j != 16 and j != 24))):
                    continue
                text5 = "0" + f"{hex(int(text6, 2))}"[2:]
                text5 = text5.upper()
                text4 = text4 + text5[len(text5) - 2:]
                if (((i > 0 and i % num3 == 0) or i == capture_img.size[0] - 1) and j == capture_img.size[1] - 1):
                    num = num + 1
                    if i == num3:
                        text3 = self.AsciiToHex(str(num3 + 1))
                    else:
                        text3 = self.AsciiToHex(str(i - num2))
                        if len(text3) == 4:
                            text3 = "30" + text3
                    imageList.append(
                        "024C" + text + self.AsciiToHex(str(num)) + "0A" + text2 + text3 + self.AsciiToHex(
                            text4) + "03")
                    num2 = i
                    text4 = ""
            text6 = ""
        return self.HexStringToByteArray(imageList[0]), imgByteArr.getvalue()

    def HexStringToByteArray(self, text):
        text = str(text).strip()
        buffer = bytearray()
        for i in range(0, len(text), 2):
            buffer.append(int("0x" + text[i: i + 2], 16))
        return buffer

    def image_border(self, img, loc='a', width=3, color=(0, 0, 0)):
        '''
        src: (str) 需要加边框的图片路径
        dst: (str) 加边框的图片保存路径
        loc: (str) 边框添加的位置, 默认是'a'(
            四周: 'a' or 'all'
            上: 't' or 'top'
            右: 'r' or 'rigth'
            下: 'b' or 'bottom'
            左: 'l' or 'left'
        )
        width: (int) 边框宽度 (默认是3)
        color: (int or 3-tuple) 边框颜色 (默认是0, 表示黑色; 也可以设置为三元组表示RGB颜色)
        '''
        # 读取图片
        img_ori = img
        w = img_ori.size[0]
        h = img_ori.size[1]

        # 添加边框
        if loc in ['a', 'all']:
            w += 2 * width
            h += 2 * width
            img_new = Image.new('RGB', (w, h), color)
            img_new.paste(img_ori, (width, width))
        elif loc in ['t', 'top']:
            h += width
            img_new = Image.new('RGB', (w, h), color)
            img_new.paste(img_ori, (0, width, w, h))
        elif loc in ['r', 'right']:
            w += width
            img_new = Image.new('RGB', (w, h), color)
            img_new.paste(img_ori, (0, 0, w - width, h))
        elif loc in ['b', 'bottom']:
            h += width
            img_new = Image.new('RGB', (w, h), color)
            img_new.paste(img_ori, (0, 0, w, h - width))
        elif loc in ['l', 'left']:
            w += width
            img_new = Image.new('RGB', (w, h), color)
            img_new.paste(img_ori, (width, 0, w, h))
        else:
            pass
        return img_new
