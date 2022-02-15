# # coding:utf-8
# # @文件: utils.py
# # @创建者：州的先生
# # #日期：2019/12/8
# # 博客地址：zmister.com
#
# # 加密
# def enctry(s):
#  k = '0D1A9A7CB27972878BAD8EFACDC7C46D'
#  encry_str = ""
#  for i,j in zip(s,k):
#   # i为字符，j为秘钥字符
#   temp = str(ord(i)+ord(j))+'_' # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
#   encry_str = encry_str + temp
#  return encry_str
#
# # 解密
# def dectry(p):
#  k = '0D1A9A7CB27972878BAD8EFACDC7C46D'
#  dec_str = ""
#  for i,j in zip(p.split("_")[:-1],k):
#   # i 为加密字符，j为秘钥字符
#   temp = chr(int(i) - ord(j)) # 解密字符 = (加密Unicode码字符 - 秘钥字符的Unicode码)的单字节字符
#   dec_str = dec_str+temp
#  return dec_str
#
# data = "20220221"
# print("原始数据为：",data)
# enc_str = enctry(data)
# print("加密数据为：",enc_str)
# dec_str = dectry(enc_str)
# print("解密数据为：",dec_str)


import base64
from Crypto.Cipher import AES


class AesEncrypt:
    # 密钥
    key = '0D1A9A7CB27972878BAD8EFACDC7C46D'
    # 偏移量
    vi = '0000000000015304'

    def encrypt(self, data):
        """加密"""
        data = data.encode('utf8')
        data = (lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode('utf-8'))(data)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.vi.encode('utf8'))
        encryptedbytes = cipher.encrypt(data)
        encodestrs = base64.b64encode(encryptedbytes)
        enctext = encodestrs.decode('utf8')
        return enctext

    def decrypt(self, data):
        """解密"""
        data = data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.vi.encode('utf8'))
        text_decrypted = cipher.decrypt(encodebytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted


if __name__ == '__main__':
    # 注意点：加密数据中有中文的时候，会有问题
    data = "20220214"
    aes = AesEncrypt()
    # 加密
    enctext = aes.encrypt(data)
    print(enctext)
    # # 解密
    text_decrypted = aes.decrypt(enctext)
    print(text_decrypted)



