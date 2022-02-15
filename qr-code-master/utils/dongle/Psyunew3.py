# -- coding: utf-8 --
import platform
from datetime import datetime
import random
import sys
from ctypes import *

path = "./lib/"
if 'Windows' in platform.system():
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary(path+'Syunew3D.dll')
    else:
        Psyuunew=windll.LoadLibrary(path+'Syunew3D_x64.dll')
else:
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary(path+'libPsyunew3.so')
    else:
       Psyuunew=cdll.LoadLibrary(path+'libPsyunew3_64.so')

##获到锁的版本
NT_GetIDVersion=Psyuunew.NT_GetIDVersion
NT_GetIDVersion.argtypes=(c_void_p,c_char_p)
NT_GetIDVersion.restypes=(c_int)


##获取锁的扩展版本
NT_GetVersionEx=Psyuunew.NT_GetVersionEx
NT_GetVersionEx.argtypes=(c_void_p,c_char_p)
NT_GetVersionEx.restypes=(c_int)


##算法函数
sWrite_2Ex=Psyuunew.sWrite_2Ex  
sWrite_2Ex.argtypes=(c_ulong ,c_void_p,c_char_p)
sWrite_2Ex.restypes=(c_int)

sWriteEx=Psyuunew.sWriteEx  
sWriteEx.argtypes=(c_ulong ,c_void_p,c_char_p)
sWriteEx.restypes=(c_int)

sRead=Psyuunew.sRead  
sRead.argtypes=(c_void_p,c_char_p)
sRead.restypes=(c_int)

sWrite_2=Psyuunew.sWrite  
sWrite_2.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)

sWrite_2=Psyuunew.sWrite_2  
Psyuunew.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)
##算法函数

##写一个字节到加密锁中
YWrite=Psyuunew.YWrite
YWrite.argtypes=(c_byte ,c_short,c_char_p ,c_char_p,c_char_p )
YWrite.restypes=(c_int)

##从加密锁中读取一个字??
YRead=Psyuunew.YRead
YRead.argtypes=(c_void_p,c_short,c_char_p ,c_char_p,c_char_p )
YRead.restypes=(c_int)

##写一个字节到加密锁中
YWriteEx=Psyuunew.YWriteEx
YWriteEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YWriteEx.restypes=(c_int)

##从加密锁中读取一批字??
YReadEx=Psyuunew.YReadEx
YReadEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YReadEx.restypes=(c_int)

##查找指定的加密锁（使得普通算法一??
FindPort_2=Psyuunew.FindPort_2  
FindPort_2.argtypes=(c_int ,c_ulong ,c_ulong ,c_char_p)
FindPort_2.restypes=(c_int)

##查找加密??
FindPort=Psyuunew.FindPort  
FindPort.argtypes=(c_int ,c_char_p)
FindPort.restypes=(c_int)

##获取锁的ID
GetID=Psyuunew.GetID  
GetID.argtypes=(c_void_p,c_void_p,c_char_p)
GetID.restypes=(c_int)

##从加密锁中读字符??
YReadString=Psyuunew.YReadString 
YReadString.argtypes=(c_char_p ,c_short,c_int ,c_char_p ,c_char_p,c_char_p)
YReadString.restypes=(c_int)

##写字符串到加密锁??
YWriteString=Psyuunew.YWriteString
YWriteString.argtypes=(c_char_p,c_short,c_char_p ,c_char_p,c_char_p )
YWriteString.restypes=(c_int)

##设置写密??
SetWritePassword=Psyuunew.SetWritePassword
SetWritePassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetWritePassword.restypes=(c_int)

##设置读密??
SetReadPassword=Psyuunew.SetReadPassword
SetReadPassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetReadPassword.restypes=(c_int)

##设置增强算法密钥一
SetCal_2=Psyuunew.SetCal_2
SetCal_2.argtypes=(c_char_p,c_char_p)
SetCal_2.restypes=(c_int)

##使用增强算法一对字符串进行加密
EncString=Psyuunew.EncString  
EncString.argtypes=(c_char_p,c_char_p,c_char_p)
EncString.restypes=(c_int)

##使用增强算法一对二进制数据进行加密
Cal=Psyuunew.Cal  
Cal.argtypes=(c_void_p,c_void_p,c_char_p)
Cal.restypes=(c_int)

##设置增强算法密钥??
SetCal_New=Psyuunew.SetCal_New
SetCal_New.argtypes=(c_char_p,c_char_p)
SetCal_New.restypes=(c_int)

##使用增强算法二对字符串进行加??
Cal_New=Psyuunew.Cal_New  
Cal_New.argtypes=(c_void_p,c_void_p,c_char_p)
Cal_New.restypes=(c_int)

##使用增强算法二对字符串进行加??
EncString_New=Psyuunew.EncString_New  
EncString_New.argtypes=(c_char_p,c_char_p,c_char_p)
EncString_New.restypes=(c_int)

##返回锁的出厂编码
GetProduceDate=Psyuunew.GetProduceDate  
GetProduceDate.argtypes=(c_char_p,c_char_p)
GetProduceDate.restypes=(c_int)

##设置ID种子
SetID=Psyuunew.SetID
SetID.argtypes=(c_char_p ,c_char_p)
SetID.restypes=(c_int)

##设置普通算??
SetCal=Psyuunew.SetCal
SetCal.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetCal.restypes=(c_int)

##生产日期转换函数
##SnToProduceDate=Psyuunew.SnToProduceDate
##SnToProduceDate.argtypes=(c_char_p ,c_char_p )
##SnToProduceDate.restypes=(c_void)

##使用增强算法对字符串进行解密使用软件
##StrDec=Psyuunew.StrDec
##StrDec.argtypes=(c_char_p,c_char_p,c_char_p)
##StrDec.restypes=(c_void )
##
##StrEnc=Psyuunew.StrEnc  
##StrEnc.argtypes=(c_char_p,c_char_p,c_char_p)
##StrEnc.restypes=(c_void)
##
##EnCode=Psyuunew.EnCode    
##EnCode.argtypes=(c_void_p ,c_void_p ,  c_char_p )
##EnCode.restypes=(c_void)
##
##DeCode=Psyuunew.DeCode   
##DeCode.argtypes=(c_void_p , c_void_p , c_char_p  )
##DeCode.restypes=(c_void)
##使用增强算法对字符串进行解密使用软件)


##使用增强算法对二进制数据进行加密使用软件)
##DecBySoft=Psyuunew.DecBySoft         
##DecBySoft.argtypes=(c_void_p, c_void_p )

##EncBySoft=Psyuunew.EncBySoft         
##EncBySoft.argtypes=(c_void_p   ,  c_void_p   )
##使用增强算法对二进制数据进行加密使用软件)

##字符串及二进制数据的转换
##HexStringToc_byteArray=Psyuunew.HexStringToc_byteArray
##HexStringToc_byteArray.argtypes=(c_char_p ,c_void_p)
##HexStringToc_byteArray.restypes=(c_void)
##
##ByteArrayToHexString=Psyuunew.ByteArrayToHexString
##ByteArrayToHexString.argtypes=(c_void_p,c_char_p ,c_int )
##ByteArrayToHexString.restypes=(c_void)
##字符串及二进制数据的转换

 ##初始化锁函数,注意，初始化锁后，所有的数据??，读写密码也??0000000-00000000，增强算法不会被初始??
ReSet=Psyuunew.ReSet
ReSet.argtypes=[c_char_p]
ReSet.restypes=(c_int)

##以下函数只限于带U盘的??
##设置是否显示U盘部分盘符，真为显示，否为不显示
SetHidOnly=Psyuunew.SetHidOnly 
SetHidOnly.argtypes=( c_bool,c_char_p)
SetHidOnly.restypes=(c_int)

##设置U盘部分为只读状态，
SetUReadOnly=Psyuunew.SetUReadOnly 
SetUReadOnly.argtypes=[c_char_p]
SetUReadOnly.restypes=(c_int)
##以上函数只限于带U盘的??

##以下函数只支持智能芯片的??
##生成SM2密钥??
YT_GenKeyPair=Psyuunew.YT_GenKeyPair
YT_GenKeyPair.argtypes=(c_char_p ,c_char_p,c_char_p,c_char_p)
YT_GenKeyPair.restypes=(c_int)

##设置Pin??
YtSetPin=Psyuunew.YtSetPin
YtSetPin.argtypes=(c_char_p,c_char_p,c_char_p )
YtSetPin.restypes=(c_int)

##设置SM2密钥对及身份
Set_SM2_KeyPair=Psyuunew.Set_SM2_KeyPair
Set_SM2_KeyPair.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p )
Set_SM2_KeyPair.restypes=(c_int)

##返回加密锁的公钥
Get_SM2_PubKey=Psyuunew.Get_SM2_PubKey
Get_SM2_PubKey.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p)
Get_SM2_PubKey.restypes=(c_int)

##对二进制数据进行SM2加密
SM2_EncBuf=Psyuunew.SM2_EncBuf
SM2_EncBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p)
SM2_EncBuf.restypes=(c_int)

##对二进制数据进行SM2解密
SM2_DecBuf=Psyuunew.SM2_DecBuf
SM2_DecBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p ,c_char_p)
SM2_DecBuf.restypes=(c_int)

##对字符串进行SM2加密
SM2_EncString=Psyuunew. SM2_EncString
SM2_EncString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2_EncString.restypes=(c_int)

##对字符串进行SM2解密
SM2_DecString=Psyuunew.SM2_DecString
SM2_DecString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2_DecString.restypes=(c_int)

##对消息进行SM2签名
YtSign=Psyuunew.YtSign
YtSign.argtypes=(c_char_p , c_char_p  ,c_char_p ,c_char_p)
YtSign.restypes=(c_int)

##对SM2签名进行验签
YtVerfiy=Psyuunew.YtVerfiy
YtVerfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_void_p,c_char_p)
YtVerfiy.restypes=(c_int)

##SM2算法初始化(使用软件)
IniSM2=Psyuunew.IniSM2
IniSM2.restypes=(c_int)

##对字符串进行SM2解密(使用软件)
SM2EncString=Psyuunew.SM2EncString
SM2EncString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2EncString.restypes=(c_int)


##对字符串进行SM2加密（使用软件）
SM2DecString=Psyuunew.SM2DecString
SM2DecString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2DecString.restypes=(c_int)

##对消息进行SM2签名（使用软件）
SM2Sign=Psyuunew.SM2Sign
SM2Sign.argtypes=(c_char_p , c_char_p ,c_int ,c_char_p ,c_char_p)
SM2Sign.restypes=(c_int)

##对SM2签名进行验签（使用软件）
SM2Verfiy=Psyuunew.SM2Verfiy
SM2Verfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p)
SM2Verfiy.restypes=(c_int)

##释放SM2算法(使用软件)
ReleaseSM2=Psyuunew.ReleaseSM2

##返回锁的硬件芯片唯一ID
GetChipID=Psyuunew.GetChipID 
GetChipID.argtypes=(c_char_p,c_char_p)
GetChipID.restypes=(c_int)
##以上函数只支持智能芯片的锁

##以下函数只支持D8
CheckDate=Psyuunew.CheckDate
CheckDate.argtypes=(c_char_p,c_char_p)
CheckDate.restypes=(c_int)
##以上函数只支持D8


if 'Linux' in platform.system():
	CloseUsbHandle=Psyuunew.CloseUsbHandle
	CloseUsbHandle.argtype=c_char_p
	CloseUsbHandle.restypes=(c_void_p)

def CheckDateEx(Path):
    dt=datetime.now()
    nowDate=dt.strftime( '%Y/%m/%d/%H/%M/%S' )
    ret=CheckDate(nowDate.encode('utf-8'),Path)
    return ret

def HexStringToByteArrayEx(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_byte
    temp=''
    for n in range(0,mylen,2):
        temp=InString[n:2+n]
        temp='0x'.encode()+temp
        in_data=int(temp,16)
        array_data[n/2]=(in_data)
    return array_data

def StringToByteArray(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_int
    temp=''
    for n in range(0,mylen):
        temp=InString[n:1+n]
        in_data=ord(temp)
        array_data[n]=(in_data)
    array_data[n+1]=0
    return array_data

def ByteArrayToString(InBuf):
    arrBytes = bytearray()
    for n in range(0,len(InBuf)):
        arrBytes.append(InBuf[n])
    return arrBytes.decode()
    

def ByteArrayToHexString(in_data,inlen):
    OutString=''
    temp=''
    for n in range(0,inlen):
        temp='%02X' % in_data[n]
        OutString=OutString+temp
    return OutString

def EnCode(InData,Key,pos):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=EncBySoft(InData,KeyBuf,pos)	
    return OutData

def DeCode(InData,Key,pos):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=DecBySoft(InData,KeyBuf,pos)
    return OutData


def EncBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray

    temp_string=''
    cnDelta = 2654435769
    _sum = 0
    a = 0
    b = 0
    c = 0
    d = 0
 
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d 
    y = 0
    z = 0

    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = (inb[pos +n + 4])
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        _sum = (cnDelta + _sum) & 0xffffffff
        temp=(z << 4) & 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1= (z + _sum) & 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        y = (y+ temp)& 0xffffffff
        temp=(y << 4)& 0xffffffff
        temp=(temp + c)& 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        z=(z+temp)& 0xffffffff
        n = n - 1

    outb={}
    for n in range(0,4):
        outb [n]= (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def DecBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray
    temp_string=''
    cnDelta = 2654435769
    _sum = 0xC6EF3720
    a = 0
    b = 0
    c = 0
    d = 0
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d
    y = 0
    z = 0
    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = inb[pos +n + 4]
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        temp=(y << 4)
        temp= ( temp+ c) & 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        z=(z-temp) & 0xffffffff
        #z -= ((y << 4) + c) ^ (y + _sum) ^ ((y >> 5) + d)
        temp=(z << 4)& 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1=(z + _sum)& 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        y = (y -temp)& 0xffffffff
        _sum = (_sum -cnDelta)& 0xffffffff
        n = n - 1
    
    outb={}
    for n in range(0,4):
        outb[n] = (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def StrDec(InString,Key):
   OutBuf={}
   mylen=len(InString)/2
   KeyBuf=HexStringToByteArrayEx(Key)
   InBuf=HexStringToByteArrayEx(InString)
   for n in range(0,(mylen-8)+1,8):
        tempBuf=DecBySoft(InBuf,KeyBuf,n)
        for i in range(0,8):
             OutBuf[i+ n] = tempBuf[i]
   if mylen>8:
       for n in range(len(OutBuf),mylen):
            OutBuf[n]=(InBuf[n])
   return ByteArrayToString(OutBuf)


def StrEnc(InString,Key):
    OutBuf={}
    InBuf={}
    temp_Buf=InString.encode('utf-8')
    mylen=len(InString)+1
    for n in range(0,mylen-1):
        InBuf[n]=temp_Buf[n]
    InBuf[n+1]=(0)
    if mylen<8:
            for n in range(mylen,8):
                 InBuf[n]=(0)
            mylen=8
            
    KeyBuf=HexStringToByteArrayEx(Key)
    for n in range(0,(mylen-8)+1,8):
         tempBuf=EncBySoft(InBuf,KeyBuf,n)
 
         for i in range(0,8):
              OutBuf[i+ n] = tempBuf[i]
    if mylen>8:
       for n in range(len(OutBuf),mylen-1):
            OutBuf[n]=(InBuf[n])
       OutBuf[n+1]=0
    OutString=ByteArrayToHexString(OutBuf,mylen)
    return OutString

#使用增强算法二检查是否存在对应的加密锁
def CheckKeyByEncstring_New():
    DevicePath=create_string_buffer(260)
    EncInString=["24447","28250","16120","3477","14430","27688","19542","28963","2746","7676","23587","29156","6142","26519","19225","25002","12980","31068","4115","17383","6279","16973","26120","20396","27711","524","5654","4524","20424","31449",  \
"24948","11832","7723","17304","2942","17219","17810","14796","941","27230","16711","5013","12187","23229","13236","4533","21762","11056","8292","20878","9148","13354","17919","16164","24515","4540","6225","10007","11058","17816",  \
"23106","26794","28737","30993","22494","18366","27468","24345","16462","24278","21708","13890","8157","12564","11099","27325","31218","23609","7603","22621","795","27304","5294","11412","31487","17763","23878","26739","9834","17931",  \
"29333","685","26948","26851","26582","10643","154","7885","29281","9496","23698","16202","5043","22734","6778","6781","25442","26086","7865","11047","31019","27955","20186","26794","30439","28966","27527","14602","12945","22482",  \
"2700","744","66","3306","12495","24452","7219","17341","3165","27842","13504","22847","20063","16165","5218","22017","9503","29644","27570","4151","22023","25211","15212","28080","30625","28564","24169","17889","19352","32281",  \
"13220","25562","14517","428","26677","10318","25825","12429","24919","19342","28456","21921","18021","16269","18867","17000","10968","12765","13260","24836","22602","11695","21469","26168","14453","24022","29041","9063","24371","28355",  \
"20272","30864","13439","4234","9446","26199","15985","6363","14716","16382","2885","17672","7420","32102","15187","7172","656","11539","11031","28768","14978","1573","15658","592","19516","6750","17478","16804","12360","10273",  \
"3397","12238","10833","3184","2338","25057","17183","21739","5877","8847","25246","29143","28153","13354","2519","2069","10121","12963","11508","25382","26909","5516","11583","1837","11858","21016","29474","25323","13023","7450",  \
"10280","8643","31902","19713","4345","7607","1421","23521","1889","29031","1473","2412","5193","10777","23926","7411","10682","6571","7943","18281","31968","18593","14573","9568","5","2077","16321","24841","31888","9184",  \
"22591","29750","19727","13389","16705","2652","14121","4198","32190","649","26026","24523","7893","4465","635","19649","11707","869","28837","22057","13773","7768","9813","16772","28291","9179","9938","11509","1402","29473",  \
"7303","16701","2153","19196","4862","959","28458","11230","20705","18556","17850","23000","20987","17432","30256","32412","24885","15827","13000","27518","21145","24975","32730","31598","23889","12751","24034","5375","5543","6581",  \
"4985","19554","1798","7938","5977","9578","28149","13337","6749","30088","4642","10748","12669","26063","16469","16972","8148","5362","25719","24907","16541","22848","17300","24541","4401","8877","21973","32130","23305","31946",  \
"16516","29276","32192","12491","28683","8495","22802","1920","20981","26971","22230","11099","12010","6371","5384","10863","9398","32359","12224","6254","16450","6957","11066","20649","14231","29971","32206","22547","17377","2206",  \
"14840","24382","7018","23277","22609","25691","2970","11204","8595","30013","13052","18309","14488","4438","23354","31025","17498","11191","29471","7276","14836","19730","10388","20342","18078","21947","8867","17713","22964","24482",  \
"23413","14112","20143","16474","6743","30565","14121","11028","3504","8897","17628","29346","1292","29335","21410","27512","19219","12009","4981","28070","8081","16472","21103","30431","20846","25127","26315","27764","30902","29751",  \
"14562","32088","20626","27915","27949","9245","12620","27589","11848","18676","10831","27174","5869","945","15395","3730","15348","32194","12915","7688","22104","29757","7690","3628","3380","22995","28368","14144","24512","6358",  \
"11729","9766","12120","30007","22326","3679","26996","3721","21577","23565","20912","509","5493","26099","27589","11366","19522","16243","1422","3126"]
    EncOutString=["C26AE3193AE60624","030D7BBEBEB4F03B","2E9CDB758B74BC6F","6E2E34CFDD734B35","CC6E60FB76F5F775","DCBCEAE6DA2F89EC","C29592B8A7E65777","267B449CE1CD261C","33934F70D8554B76","B26D1C99C5C06F15","B8FF820705852584","64B92419C12E30DD","0C9A9E621C1065FB","597A2E67AE8D4C6E","C02E7A5E4ADE1130","2145E76E9C5DF370","B4722E47943EF076","823A5B535564C851","4B9077E5BE6C5004","963FEE2A537F1A37","2ED8A34B4D208284","348757979805FF6B","47382273D6AC599A","D001BCA7089C8388","8069149A75E2E2F5","8A9626CC9A89BFD7","F9EE2FDB0C49EC00","561CA461E548A02A","E0D9A5C613946CF9","35755B734F96A021",  \
"AF3328FCBD59F642","817CF283AB56343E","9A2BDE027588A1CA","70DBB7AA4EFCFF07","96CD5B7B2DDD4CE2","08DE4CC84B3F0988","47819ABDE95D6D8B","FC9F22CBC06F9251","9DD136BCB6F81D63","54C3F027BA2A09AB","71EBEAFF9D7B1831","585FDF67AEED2D9B","F4E825E80516CFC1","9AF6CE6CD2C34F2D","A2BEC1F2C2FF558A","43BF4D7774B4EB9A","AD2EA8CFB089A5C1","23F6D33777375903","106F43B95D4D308E","3CB72D0CF6EADD72","3BE6D0685D88E68E","3B494D18EEF524AF","3C8949C682322D41","F1C1919DE2AF27FD","79C99D3FB93BB14C","7290F71BE78D2E95","292AB685E8084778","867BA978F427228B","985F31FA34FB9C7B","C289E479091D69E7",  \
"34AE94173614EA16","D51FFB6586A993F1","146E7708E4062D1D","A15E22AF4D50331C","C63EB5A810FC815E","B0D7E517A2B58825","32CC9DC7E6EE8625","1D2861E6D86A8E79","F6351D236F8EE444","5C4988C9C43893E8","3A1ED59E1827A771","0BCFA53D53E1A92B","14528568C46A2A02","9E00E63BDC7EDF5F","8135E44B44670B3F","FC8FF204FE1FD42C","EF3262AE9AC9CFCD","1D71B52028E118B5","D47CDB6D11CB1EFB","9E39F67F82F4F4CA","1DAE6B6BD781F9E3","C0DDA77FFB96A0BF","DB750577FD507C85","32FF3F75DA4B477B","61A573CF81B7C897","432E95627614F44D","8E0B121500B84DB1","0392376608BFD5A9","5B1DEC57EA081E1D","C7B435F393A97EBB",  \
"47B38EA44C8C57EE","A70D4578C0D7B3B2","7954313073906CFE","9904D5732D4F9CDB","BFE9BEA856B15E66","E1DC311B6371D537","3A24741DB10ABE74","CEB1597355676F1A","3771716461559DEA","666B528051E67C4B","D38850D64B5E19ED","EC9039D61991E937","A327CC3C212130D2","A9AE576186FDAF83","61F2798C91C41560","77C9991ED5703CAA","414C83A24A16BDC9","2F9690473F6868C0","4363031E9DEAF8C7","FEEF503B81E7FAD2","8EBFE914ED20CC08","F24313DE7EA102F7","159BED47239591CC","D51FFB6586A993F1","E1671631632BFA83","3CD59CD5C415EEB1","34B82B58031D6993","2E320104003E6DDC","8C3B2ABC163EF11F","FD7EB9B0FA375604",  \
"FC4A87D443E928F9","CDAF1ADB30B7F4F4","B9D5B4AA78D8D1DA","BB612119BDBAA289","66B952E1BEACDB77","A3C58F686FA51F51","2EFB85D069064B2E","A3E992EE1EFF6444","FA7269D1C79C451D","21F934667002084E","0A0794A9122353A7","8415893B3FE198FA","4195A5F85EC1F5BD","FBE1A5C0CC0782CF","CFDFC99038A6DAEE","CA4EC158D46079BE","D965D1B03DCB0370","F21110E45CFCFDBD","C101B72E84E049DB","C363B16C53BA16A2","53F88723CDC7C6E0","F92C51B266530256","E0A2ED62E3DBD859","BE40845EDCAA5406","7A4E1EF13161488C","03BAE66420DAFCF0","1E96503A48245757","63CC893E40147FF2","A5B3CD5E8B306B36","6B8C90366DD7F089",  \
"BFBD0E711A2EA249","0EF195EF6958BE55","829C1B4349F128BF","71C5B48484916624","F54A25E90A0712F2","777522561F993EBE","4822732A6A9FCA2A","7461678C884D6853","C9FE2486500709B5","CEC83C91A35C43FE","F4D14316361A57F0","02859FC789C44C8D","3E4DDFF72C2E2D64","D3B20E14E2A24F48","4C72BBC4389CEFF6","70B20FAF1143F16A","7913A20C68FC9544","DDCE06DF83FEC7ED","BD56A7C269BD43D3","582FB5F3599B2091","29F2843DE915E1D6","3DC229C96C5E2D59","DB59FBB56C9AF9F0","7A0AF7581DECD553","0BB1AAB755CD93CF","01FF41F9E4FA8647","4C7BDFE58B233028","ACBF6437618AF43E","AE240978AC8F05E4","B182CA68E91F694F",  \
"EECBF4E5D02E10FC","D027A715198E2BF9","219D60E048897FAC","2398D9C1422581D1","DB33A6FD08FBE6B0","A06EF531F2EF881A","D0EBF12C89D5B743","B62151A7B9CC45D8","251E9190217A9B17","DBF299074DE9713C","5AC44D210C7C999A","769BD18B1D8381B1","29DA8D8A7A377BB0","D518BBD3CC6806ED","CEDF1C1191C868CD","DAA081DCD62F909F","606FE62DF1ED527B","23FC443731DA36B4","5D6B26861C545ADB","52C74D03D3B8E0FF","81920FC93A375FA5","C844DD2B28DEA058","B2BC7286377280EE","CB0380E20DEF2416","20ECA74364D95E68","445081321A97F5D3","80A850ECB63CF376","24AA2D864A955F31","EB51F80520368100","378BE732F564F2A0",  \
"C766D24B4F31D386","0817499BC1754EE1","ACC130C66E04488B","78C4F8BF9225CC50","E5BF723006C11ED1","03DE97D07192CC67","20C864C58B2A5E58","EF541EE2FAD35357","4E4F26C76D817F92","6558B0EE41F0BCB8","37EE1035A79574E9","BD71AFB31AF9A5DF","543A81678878A73A","3B494D18EEF524AF","894318A8144E6752","B1916D92D7A67518","844C6DD1BECFC0B4","C10F72A2888FB716","6D8CB98595650F08","3C12DDB262DCDDEF","06DF9308085EB30C","20D271C6A0E21B3D","0E68B24D909819E4","A05865DA79A5EC48","AA013E3D860F2A8B","AD015D5F7E415334","690AD5A55EB03462","A63584CFB174C9E2","DB00DB5A3DAEB898","71A4B23E67369094",  \
"3EBE942EDED059D0","D4C6C5E0FEB3CF62","0B607D768637525F","51680B8A9163931B","BF3E5F96EB6223C0","2ACE844814DAC651","E2145BEC4740EF53","E215254FE1CAD6DD","34D63C7F5953582C","F6ADED8F05E8881D","6383BFAE97E81AB8","CB0D603D0404CF34","FDA217600C0A5A11","D5586891E59948FD","8EED593E0312F582","32F6CA7D11873F18","20CAED072FEF0DC5","EA76ED19CFCFF4C9","642C213647BF922E","2A2E15A245CD6D84","4CDAF22F28FA4999","9982748AD3DF7348","F2E229C66340FB9C","5C4F7B1CB28F360E","61D01598437FBC53","9EA7357CE68AC5CE","11759BE5C2331B73","3ABDECA2A46E9C2A","84A7F3E85747430E","4C475BE2F3B74D5D",  \
"C4172C0480B9AF08","DBF282AFF088EC1D","13A1825D179CB413","3DA170AF97CF419C","713180C072D8DE99","D969987B06F06767","BC702BCA4F432DA9","345CA7284A5E3BBB","0FF983BA1F98C3F1","A878A3FC67B36801","C2FE192A27A0F433","24964CB889CCE7F3","BF3E683F8389DEC1","FAE4B15E9BFA95DC","9F5746E80B5A35CC","FC6EB0D044A4823D","FA084521F29B7D00","C04FB7C8F78B8BC7","38CA3ADE16003C03","B5655B1FEBDDD7D7","1D7D5430573958EC","853031234B1F7271","104D79E9F7DADC9F","D56A29577C218376","13E33CCFD72AB0DF","FE54219CF2EAB443","0E9E5F2C8825A610","24877CC25758C748","62F8B2CC00434B04","E5EEA6F67AD9581F",  \
"32249DF08707CCC2","92A2AC4175369C5D","CF2B90680F986372","A1A92E1E8EBA1C37","82D0773F68CCA682","0F47AD8239F4792B","FC56B4F059243708","3293CEC5F3C8F905","E850BD00347A158D","CFEE9E8E5484B59E","BB3A80E0411A3D0E","D86AC6F7119F23BB","45B96F001A298D1F","4DB26B8E61656091","83E251524EAECB4B","E8B57B662FCED856","55A195DB5D205BE8","0C9154680D00C3AB","5196694B91E40336","BE65D16A105144A3","CBBD7BA7C39B9B23","6406CD6B24CE4DC4","C3F1D52AB3B7EEC8","39EC53ACE48CA60F","454B2C7C1029DD4F","BA0668860B80249D","6F23217894BF0D8B","D06B8FC51025889D","A556C743D802DA4B","51E72AD89BF198B6",  \
"D0C8599B23548107","1E8A3885AC080FE0","809D528F174D76D6","307539CEB17F4728","9E45995ECDA65A88","2A3AF539C0103FAF","D04C4F182629C3D9","F61CDBEFC901A7CF","97FC55F01168CE38","B1AFD9E418565D57","0C22C3986193E749","9ADBFA6FD56F5480","A52E76968478ECAE","8D3DB5E71A62CDE7","57E8ED02220CBB21","227573644C8B252E","32247942F13D1CCF","861F66650D246D9C","AEBD1C9EBC258A7E","0EAFF13B9E366F4A","0D44354AA464C561","6513F85D9D485FB0","8F1C72EB058F51AD","CB4A915F0847196F","3F129B9911B5965B","E0F310D6C12A641D","AB4A5A2A0891EA4C","A7946158F493B583","64D0DDC9B85DE6DF","FDBB1BF5A45FFA78",  \
"4E555E67F8FE9DEE","739CFFA28136E2A7","EC973ED315C05731","90DF75EDA15B233D","9AE3F3D56E5A112A","D5C32F140761826F","5E739349E63F2938","267FC446C74CED7C","A9902AB835AAE592","DA50B057330DC1AE","BA2E630E34423DC2","8135E44B44670B3F","E43D80FE31F1AB0B","4ABAF3C4E4D98112","6F2E38ED0EAD4868","1BBE348DD3B5D8DD","DA51224A3B41EEA7","312C9F5D4ACE0F3D","A81845374261C3A0","BDF38709A5BE7839","ABFFA8B3A68F7659","E70D6360C18071ED","FEF2003E0F4E5215","77549D867A1568B5","9262CCBB73352AF3","E98A725024EE5ACC","2EB8B4C8336DAD32","D722D8D5001771A1","BBFA5279087CDF05","515C220066455986",  \
"93FEB2CEDAE92CD9","7BB906DDB809FA3F","7CFCD64CEE7610B3","DC9864B0FD021F5A","3C3A375E78C6B4CF","3EA6C2641AF809DA","BA04B1FB004528FC","CDF76686C6926E92","B9489CB011285E96","EAF852BC8A1B0900","216B330CDCD78568","3F69E73C5488C7FA","C95ED11444A90529","90FE0BAFE13128A7","1C6062F2835D8ADE","641D2A44457B5070","E38DC5E5563B1EE6","0771F0B8713F733C","E68E05B0F92648DC","8E5FD8DBE432AC95","00971ABCF9A7A120","7A333DB4C12852D8","306739D063A2E22B","A945067163BEA540","BD863C3D9ADE4D8B","68FD10D8CF6A4A02","B8282BB478A9DA30","EB640F84F10ABDBD","8883026014E4E5C8","97AD6C92897AB4B4",  \
"1E48D764D7B17C33","0FDE495581318079","F1DAB2584F9B164B","5BDCF4FFCBACEFA5","F57942338AE13A31","D068CEF1C9276F15","BC702BCA4F432DA9","7CB6336E0FBBC8CE","219D067326D90CC4","8CFE15B48073B2BC","21925D5D36575D46","4C7554C5F353B343","FEE84C784AD62A6B","4F23D0067A01FBE1","8B68E5B0545FC7B4","1409E19C12B032AF","8220DD6B24660EAB","397F08657B6B55C8","C3CB97CCDDC43AB1","6BD134680C65528C","7BD1EA68C42BE0E3","72FB278B4A8E9112","8CCA3CFE73F8C538","4ED2BEAF2F781CE0","E5640E54125DF4FE","59EED1F6B6B291B0","CBE481C08A108079","AE95310BAD365C62","3E23864747637753","BADE35CADB60448E",  \
"00FF13F1E4AEC1F9","662E3EDA09A59191","E01522658D6AA468","1955BD7DFCF76FAF","8604A8F932ED1A41","D8C57C9D3F05FC87","E84528EB803C1377","A80B1A75BA1F67B4","D3E0E95AF3BFACBF","761E3F1C068E0F55","5A4C2C66887E7D0A","26F86DBA1C72CA6C","E0F146B002390F99","11DF698C1D90643F","F74CFA7A4BD02255","65C5202264313738","2DEDFBC2A3A57E44","C1A9A2949327D510","CB8504EFFFAC0D23","898C3B1AA5D10482","F463CED7813BB412","5690A04448632034","9251CFF6248C5274","46970AE739DD2649","B09270D2B24DC707","EF90FE9C321C6D5A","FCC34167027BDA6A","10D7A651BD25E1C8","22FEB4FBD3C48E31","7A420A4CF928C0EF",  \
"CD606AD63B91F5C6","A3375AF652E21BDC","9D35865D531C69F4","AD2405FDF134E82C","E95F2946B5D018AF","38F78A40F62D82DD","29E138935BFDB6CB","031A7F83661B0858","3716A94F3BCD93E7","866CC7FB5BD6EA44","C4071CB43E816643","B4046DDF087BC02D","18871E92D9C03685","C50376C7B1F99A30","A80B1A75BA1F67B4","A373496B360948A1","D7993830727CB307","60B6ED363F8DCC61","A1AA0434DA0B42E7","57638231FEA7CA08"]
#@NoUseNewKeyEx return 1 #如果没有使用这个功能，直接返回1
#@NoSupNewKeyEx return 2 #果该锁不支持这个功能，直接返回2
    myrnd=random.randint(1, (500 -1 ))
    mylen = len(EncInString[myrnd])+1
    if  mylen < 8 :
        mylen = 8 
    outstring = create_string_buffer((mylen* 2+1))#//注意，这里要??一个长度，用于储存结束学符串
    for n in range(0,255):
         ret=FindPort(n,DevicePath)
         if ret!=0:
             CloseDongle(DevicePath)
             return ret
         ret=EncString_New(EncInString[myrnd].encode('utf-8'), outstring,DevicePath)
         if outstring.value.decode('utf-8').lower()==EncOutString[myrnd].lower():
             CloseDongle(DevicePath)
             return 0
    CloseDongle(DevicePath)
    return -92


#使用增强算法一检查加密锁，这个方法可以有效地防止仿真
def CheckKeyByEncstring():
#推荐加密方案：生成随机数，让锁做加密运算，同时在程序中端使用代码做同样的加密运算，然后进行比较判断。
    DevicePath=create_string_buffer(260)
#@NoUseKeyEx return 1 #如果没有使用这个功能，直接返回1
    InString=('%X%X' % ((int)(random.uniform(0, 24174836)),(int)(random.uniform(0, 24174836))))
    for n in range(0,255):
         ret=FindPort(n,DevicePath)
         if ret!=0 :
            CloseDongle(DevicePath)
            return ret
         if Sub_CheckKeyByEncstring(InString,DevicePath)==0:
            CloseDongle(DevicePath)
            return 0
    return -92

def Sub_CheckKeyByEncstring(InString,DevicePath):
#//'使用增强算法对字符串进行加密
    nlen = len(InString) + 1
    if nlen < 8 :
          nlen = 8
    outstring = create_string_buffer((nlen * 2+1))#//注意，这里要加1一个长度，用于储存结束学符??
    outstring = StrEnc(InString, '0D1A9A7CB27972878BAD8EFACDC7C46D'.encode('utf-8'))
    outstring_2 = create_string_buffer((nlen * 2+1))#//注意，这里要加1一个长度，用于储存结束学符??
    EncString(InString.encode('utf-8'),outstring_2,DevicePath)
    if outstring.lower()==outstring_2.value.decode('utf-8').lower():#//比较结果是否相符
         ret=0
    else:
         ret=-92
    return ret

#//使用带长度的方法从指定的地址读取字符串
def ReadStringEx(addr,DevicePath):
    InArray=c_ubyte*1
    blen = InArray(0)
#//先从地址0读到以前写入的字符串的长??
    ret = YReadEx(blen, addr, 1, '86799CCC'.encode('utf-8'), 'DBC3F2B4'.encode('utf-8'), DevicePath)
    if ret != 0 :
        return ''
    outstring=create_string_buffer(blen[0])		
#再从地址1读取指定长度的字符串
    ret = YReadString(outstring, addr+1, blen[0], '86799CCC'.encode('utf-8'), 'DBC3F2B4'.encode('utf-8'), DevicePath)
    if ret!=0:
        return ''
    return outstring.value


#//使用从储存器读取相应数据的方式检查是否存在指定的加密锁
def CheckKeyByReadEprom():
    DevicePath=create_string_buffer(260)
#@NoUseCode_data return 1 #如果没有使用这个功能，直接返回1
    for n in range(0,255):
        ret=FindPort(n,DevicePath)
        if ret!=0 :
            CloseDongle(DevicePath)
            return ret
        outstring=ReadStringEx(0,DevicePath)
        if(outstring=='15304'.encode('utf-8')):
            CloseDongle(DevicePath)
            return 0
    CloseDongle(DevicePath)
    return -92

#使用普通算法一查找指定的加密锁
def CheckKeyByFindort_2():
    DevicePath=create_string_buffer(260)
    ret=FindPort_2(0, 1, -230755786, DevicePath)
    CloseDongle(DevicePath)
    return ret

def CloseDongle(DevicePath):
    if 'Linux' in platform.system():
        CloseUsbHandle(DevicePath)#关闭USB设备

