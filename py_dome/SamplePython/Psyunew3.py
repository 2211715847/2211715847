# -- coding: utf-8 --
import platform
from datetime import datetime
import random
from ctypes import *

if 'Windows' in platform.system():
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('Syunew3D.dll')
    else:
        Psyuunew=windll.LoadLibrary('Syunew3D_x64.dll')
else:
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('libPsyunew3.so')
    else:
       Psyuunew=cdll.LoadLibrary('libPsyunew3_64.so')         

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
    EncInString=["29256","14753","21060","29777","8775","21518","9158","15731","11755","7176","11040","10639","800","28625","21898","22775","2287","16973","21088","9630","31105","3325","15643","9494","23587","25089","26452","19088","7996","7710",  \
"17096","10463","21079","15027","27469","21620","31","16325","20705","25954","10333","22004","412","6491","23034","30850","5047","5553","27906","18259","12174","18772","23710","30951","14745","28377","16664","27745","7285","11888",  \
"27098","23426","13016","24556","5999","11437","20895","27838","21887","25828","29123","20986","29909","14792","31327","16976","9565","17308","10924","26642","12317","20289","9220","18227","20802","20538","5089","16197","12822","29353",  \
"32220","11641","769","19791","9649","11938","13710","13199","6458","306","22119","10091","23150","1850","1880","27524","10603","26732","6471","13597","28264","21531","17985","32279","17345","25401","2927","30453","8175","6745",  \
"8987","6361","8076","2986","7855","22404","28498","6400","8374","29529","22043","21964","14040","27482","24289","2337","21472","3881","8895","20401","27065","12550","13038","24013","9068","30677","8903","24936","16163","20760",  \
"12742","1044","2088","754","5508","3330","28901","24097","25531","8965","19685","4108","7237","11919","10960","5297","21276","23472","20082","18612","31322","15389","19123","6999","19514","2343","15263","24699","21781","1471",  \
"8288","17060","7525","120","21821","21745","29635","30082","11684","17703","22251","20658","11804","11686","32694","20345","26192","1905","2848","745","27403","15400","17470","29105","28725","22544","3663","23080","731","23561",  \
"28330","5182","25379","12183","14028","4995","32346","13017","20043","2348","2282","28819","7397","9736","14427","28711","5233","31883","7513","10135","23274","712","7597","3461","5227","13423","3648","19249","19756","21714",  \
"27934","3712","905","20708","15216","31729","20986","16694","30592","16553","14619","3068","14008","17513","2470","9990","24482","31633","28274","31174","1002","22822","5757","24399","23125","24776","32478","18515","22738","22714",  \
"23760","32035","28265","7134","10159","32690","23876","2997","17137","3474","13485","8802","18483","16884","27406","9382","28974","22443","6130","29667","8636","2857","19969","30","4568","7295","5383","23028","6042","29023",  \
"1005","25771","4414","22301","31420","10276","28444","25769","31904","17120","23984","31893","10723","31745","3987","28436","23021","30026","10111","15353","21833","32029","16974","29875","12194","125","8443","15958","16832","7433",  \
"29341","29588","17295","21252","15986","26302","1560","22354","28114","17351","19845","1395","30262","4674","19232","29065","9019","22365","14163","6744","152","22510","2985","15168","25640","31333","23754","15939","6117","18646",  \
"21633","19972","9194","4849","19385","1990","14447","12296","1148","19816","14288","24846","1010","14190","24709","21141","3174","9978","5931","16078","14146","30669","20600","12172","12048","21066","6986","24640","2427","7539",  \
"19096","16381","16715","4329","16253","4982","20588","26350","21300","14074","27110","11878","24853","125","21477","15569","28828","16784","25010","16466","32610","26982","3512","29098","27425","18129","13183","26172","31667","27203",  \
"27058","522","3347","10189","31772","2485","22873","14626","1446","21631","25280","32659","10842","7756","32163","26131","29025","31132","31355","25396","16136","24977","28642","6951","28342","27631","9362","8639","3319","6934",  \
"6502","23661","12659","20488","13142","1093","30965","23657","1405","18422","8041","13433","15126","3541","14805","16666","8569","21970","4198","20943","21026","15231","6245","11962","31913","6160","3645","19100","20683","17493",  \
"12150","5336","2144","31424","5308","27503","4449","22884","11223","11525","22505","1011","20914","27353","12338","26046","3161","15056","24727","5049"]
    EncOutString=["0EA7AA3D1F6BC5AB","4439F457755095D4","61D215B95B38288A","2551E01762E927F9","ED4C354E1CC31A62","152AFE391E30364E","D864A054665AD93E","B6D828D9C4FE842E","81789277DE224FF8","0756518C89F92974","CA524CD3C031956B","87406EC62FB0B07F","FA331F9C0D63FB7D","2F6FA1A7FD6A5954","03C49479B55EFAF5","F9307C30D3B34F60","86764DD8387E6435","348757979805FF6B","E4A0857F9E602DA4","E65CF0D9458D2757","B44B8F2E78A25233","90E834AADC9433A3","B80B7F967CA344FA","284DD1DB5B22168C","B8FF820705852584","0E4D8848BF32F501","A55E04168A3F9DD2","336D1D00151DBD32","C06828FA235BED00","9EF12735BB6DFC77",  \
"0444EA8C3BBC5E0E","18E222269E5D5576","A41BA2239BB53633","AFCB72F5E6C50F23","BD7EDC04A7889C74","8E0C1924FF3C0912","C3FCC520586569B8","BD9FC43588A8E3D8","E850BD00347A158D","40D3904766FFC5AB","52C14937BD52DDEC","653F8F942033971D","4879EA8CF082A093","FF1FE04CDEC1720A","A967B15BA113E606","F112CCF8507B8A22","3D3CB1F07964F94C","C49AF195337875ED","F0324609AB340E06","AF77752508B2F9FE","62DE0DEFD790D337","448271EA69337841","943FE7FED317243D","6D6088739266AD76","77D92A6E92F72AF7","3952763624EAA45C","0A545A178DE15070","088CDD9FF2860000","1ACD38A000AE0615","2AFDA22FC7AFFFF8",  \
"907D3792DDDEDD25","39645DD0D4870F3C","6D9FFE445FD4A545","BF54638159BFE512","ED8CE1456D8B4F53","AEDFEE8F391B1284","BA77776EC1E39E10","F8BE8D78AE92A7F2","1BE91615C5688F67","5EC6BE92B3493180","5A133D4EFD2D06F2","ACE8FA03611405C2","0DD311F38D143C38","9227563874A60DD0","7841197B8D006971","35F398825105EFC5","C772F859F43B5763","D2F035D3309AAAC3","9B445F0314EC3C2A","389461B12FBC8A49","18757DB285B70096","F76E744EC82BC50C","0ABE7A008ABA94C5","9FC80BC87E2C00DD","0ED1F4C1C918F253","2A12C2CFE6314483","64F060BE5ECF5F56","F8C45BE3572B581E","6F14561AFB051FC8","D801FC12FB55F25D",  \
"07DD1D6A3CEC53EE","F6A81C408C106D96","25F28BA5BB9B8D12","E6423BE56D7E9613","775194B6DE943429","D87DBF09A5DB17F2","72298F56BE7E0DB8","2839A30101D10253","D9F6D661BFF07A1E","951471234FF237C8","BB6CE33827D8D922","AE0B5872975F4DB3","EF75F2909B5B9254","67098CB56FA52D72","8B004DFE2F476F52","FA8E6C0C38A57FB3","436B66A66C7C4499","2D5F040F064A6795","22112097192CB590","F3420D8B8778A309","276A50D4678171D2","BA37124043613103","76F365016589CAF7","44E4A74F637FF558","9FC415ECD23E1690","D725E0F1F96CCA7E","5BD58E07F9C3C4CA","5DEE4E8D68B13701","CEC4F40D0E0855AB","FB8020E4F0DE7C0E",  \
"187B016F873DFDF7","989D5AB8F5CD6698","2D72B2CCC61AD3A3","42616CACC2659039","33499BEEC4CC07C1","81DDEC6F25487D0A","F81B11CCAB1EB8EA","46D9059EA75215D4","86789BBE353815F9","BB82502C76487D3B","E7DA25E214CBF4BD","C012C72AF64D9AF8","703B49419A91FAB3","5AB0310F89C54243","55A4A05F4A0A912A","CA1EC3D235E7DC22","1B2F98CD3905E58E","A630ECB593189C50","1C2B55F9052FED0C","EB41406F2E88E29C","F82C7BEB3DB6B437","951CDA3F48258B08","8FA7E88B5E0A133F","90B3BA02A0A2C2C2","870CD19C303508B4","B28A3EBE94D77BB7","5FB2D640EEAC754F","266F75D1D45B0385","5BEADEF8F940D278","9714EF74208D1DE8",  \
"092B781ADE34AF18","37F1CF683261CC12","2937E7C779578FC8","70084A34E636E24F","3EF47C1B6BA25903","E60CACA5ABC38642","A0FB0259CB11FEE5","73B0AF0583C4E2E8","06381C12E7E6E98C","2E80DFC7B8874E30","C38DCCD97CC175B7","EBABE09FB8264416","656B04CC80B80E52","0F1A7771DCA5B6AB","A39B7A7769CD2D64","F9C4FC28E093DB19","078DECB1EB86FE54","BE9BADB22809C3D0","8F33B636E2B62886","64FC243431CC1EEE","74B9816639F7ADA4","155DD6683AF1325C","31CDF79589D4C724","017817008B50D626","F1A3A6B7A3D4A5FE","DF37E84AABD9C018","896BEF1407750A4C","9EA1EFF5C0F8B6F6","47097EB6A94608E6","1303495C317DF59D",  \
"7CBC5B0F88F08D43","AE890023CCA47335","01925E2CAA660CDE","7B372E7B61680663","4073BF7F3823B1C8","756F7CC67CA7FE56","C2A1335D9E7CD70D","19F18BA782A0F39F","B65B429172B80F0C","1CB4AD5012C13CE7","B477F3C12B7C3010","97295134D2BE0460","4B0FB7FC76DA95F6","864B57A6BFE056A9","4F3CBB749EF26DFD","09BAD9AFA2EBDB34","04A7DEA8B977BB23","807A440E94F56874","1BEDD2E462B44695","86DBFF0FC99DEC40","A3DDA8ED20452B2B","026E7117AEF3DBF3","025FEEFEE63608CE","E4557B5636E3EC52","7CC32662BD2E79AA","69759BD515AC2DC9","CDB1E958C60F43FB","ED242E2996FF79FB","6E59F8D65DB9693A","DB229E2E7BD931E7",  \
"DE6457481F085C3D","E97BC3075FCBF15E","97994499D59F84E5","ADB3FA75ECC05AE3","78A1A16DCA47005D","BB07D60609597A4D","84E50B20C4CCECA0","064B4640D6DD61C2","4BA7BFC3A2947287","CBC6BAACD167DB40","BBF605508538E48A","DAB6A5B5B50E04C0","F36207AB5FEC5ABD","2390D9D765FA27C6","AFDDF5212E27F4BE","57C77BD14274D814","6739FDF6665D9765","E8C784F34E9495A6","DD3CB80B3EE2721C","C88AB8C1C3BFA8E7","2605E2B3290C85C7","A0B12C48F90FFC76","09CBAC47EDC18C60","1D7B63D5C418C554","3033DD5B8F53A50B","27D647D8373E7692","75C9F87E241CD50E","2CAA001C85802AF7","52EB7F34A2B0A703","958917C19B6A5393",  \
"F373304B1B82A60C","B34E5983B0ABCA12","9C47FDA7EE5EE96C","CFDADA27F441C51D","A7F2EECE444D6EFD","0A48EF1F91EE0AF4","ACE8FA03611405C2","18EF5EC8B390EE5D","DABA031243F33804","74EBB5B4ABA5531D","4560AE743D38E308","B6F30143A3D54F8E","4F28904317293309","3CE2D9575FAB41B8","4F6221FF2AC1B9B8","927B8DF07C3A0B4B","97AD6C92897AB4B4","FE5B2B72E53A6C37","0E7EE578E91811FF","F5ACC8893E5E45C3","584B535727E72501","29E121BD8CF02E4B","7765E6A8F800E011","2F4E9EC7963E29BB","2D29B93CF52C568A","F14BE095690F31F6","0BA65F349D869F48","D6DA771991266A72","AFFD0A365C1BE576","8379839AF6C0959A",  \
"C26119B0E3CBF99D","009170C71C8ABE02","9F9C42E8568A098F","A91E981B19407871","C2429AD336568A1C","D04EE464E586F5C1","DCB7367D42B76AEA","3D880C58E6DFF657","A98E3A4DEAFA1EED","0122DC5EF561A53D","877740EF346EDE62","2422A4451B744F9D","62CEB33B6C5E24FB","7BA3D60ED4B97CD5","CD18E6198D737688","EEC5CF7DE6C674DA","FD1128F6F8A6C9E8","0C79F275BE952EC0","145C134FA6DBF037","C2EC55D9C939E465","543B9EC942E39F94","053275E89A4D30F4","E42F3FA234335EC5","4951982BCC7B3462","D2EC68EE8FB76A32","FAE1B8D020D45935","35EF2FCADF0D6530","EF79872F97DFA277","A29DB3ED9EACF8F5","91C5E7129F7CE57B",  \
"4DFBC1ECA86FD1FD","3EB6C7AB76DC37AE","267B0D04B37AB511","F4733190A411EE89","F37345519C0A7E5C","22BBA7D93E448920","0D74D8290F628586","FDC798F4D2713AB0","022CE1EC57A6C336","1220F7DEA271B97D","D7E512D6DB6811E7","BBAB2F7ED6C4AF52","D7FAAE24DC0606D0","3FBC3585FA120D92","1DC11CA5E7FE385E","847EA16E52EB4198","8FCF3EAB1E263D3B","F0C61B1D9C08B29E","3BD2BEC83A847373","14D35414922759AD","4C250ED76F509064","F6B1DF314753925B","1DA54305612515A7","85823952B35879B9","745AB12845D6654E","0E2729DB33B11E97","465E56F4352F0845","5C144E3529F03C66","A0E0F24E47AA789B","494ED35FA6F28DA3",  \
"8F7780E8A51740E8","9DA37D4AD4F3AED9","EF3FD8E3EE2A6F2E","B74E42BE5E02ECD0","5711D40406D2A688","66C03C44D48979F3","D820271AAE7F7988","0CAFA9AE59BEBBA4","CED7F4E908A1C236","06107F87178F13C9","E2BBC10741A21CD4","1674431D2C5C99AC","66487172BE29C42E","76355AE4FC5BEEF3","30C932542135FC4E","9BAF2D20D761C56D","7980308BE9014D31","34101A356F698DF9","15190F96F593F10C","80355FE3C5FD3728","3200F549F104DDF6","E9C735B5A53E16DA","27D179DD9F55BE98","111ACD34667C2DBD","04FD0EEDF5EBC4F7","34E2DA2448002566","2C74B4AAB63D4110","A09E300B73F260B2","ABB70138847F7F69","9105D88953EB800B",  \
"ACAA55F1245B2807","56A40A514BE4E8B9","943FC9177093BE3F","4B4D9F9D728FB171","8F1B71105BD31D0A","339F93A1A223AC01","6142C43953BB0ADC","2042BC7E78E910E5","CFAB19FC065C1CDB","2A41ADE9207937B5","CBB0BA99F8BEF09D","C545962C3BBB32A6","EE690B4132309FFE","12571E3FCE2E71B5","B21EED539BAE0619","451667B64D643D17","8C621E99ECF2BBA8","5EEBB30502D0C4AC","21987F85341C88EA","5C32B1B639DC84FA","64FF7E7FBD30D4B2","9605EF93476A6EAE","D1D7B55D80BC0E16","D6ED3D356890FB87","8773CE181A17AE85","2D19A102745E3A42","BA8E71C98B7CEA46","5E07A45D3548AF0C","E74F989143C7CD40","B5DCFB69EFBF4EC3",  \
"89F0BA9FB450826B","96102D5C57186A47","843BFEE9D1BF5738","F681BFCCE4CD69AE","41A17211DA9F0BC7","846902C6290D9D19","3B73F55358405D9D","07CC715C4AF98125","CD18495E1F33AF90","05039A5875789B9D","C1240F70CC74D5E3","58F431749B6882BF","20F0DCC40214FFCD","0E2729DB33B11E97","CD81C834D605CE4E","B8CBAAD5E868A1F5","AACB9835E278C934","C9A27E00BC360DF4","558EFA46F9779668","F78774C985D9F0E6","3320A4D8155532EA","9AAECE8D8DDBCF9E","19A8CD9C7DF0130E","5D9CF34EA741EE88","AF2F34C727679D99","1BBE76FFF930EDF1","A38D4003CD3E0F80","B8E01277A4AC3656","FB8CF811783F726F","B2ADA3B891F902B7",  \
"B386F5D0341987FE","7280DF642B1FB6B6","F74C73C55232D341","94AF7979BAEB2E0D","9829105187FCBCCE","585350B4F0CD196E","9AC1F0EF70BD2463","4082814302E94CD3","9035A5163328DED2","53FF7817796D80E2","3053C6F99AA5E9FE","70AF1F6BFA06D21D","6DE89EAC5E02B093","21D26E90B603E77B","CE609F1178C007FB","17961FBC30304650","BFD5606B32D3CE7E","22ED5E70457601F0","C35489DBB2C64682","518B6B6EBA409959","A8C740C19AFD5C26","374E779EA06750F9","07EF6AE7EE98E57D","032AE9456E3FFB4C","101E81869B310AE0","E4CCB198BB204AE1","D262F8BBA0E79055","2FB9FDEC992A7847","DE013A99725A16C4","2E1F24D6A74482FF",  \
"E3DF9871A6F6FD73","9FF0E70295AEB823","544CE796E3A80A69","1F960317252117E4","C4FB327901EA6EA1","396CABB827C5CC5C","951501CDAB0548C3","B5B8E413AFC9C76C","1E1E61A89765CAE2","F854A86061BB8905","B11659E0605422D0","5CDE58ED2E002F52","183B80D5C10E7C8A","759D370CB7F1B4C3","6729F5975BF21C13","BD463DDB038A229B","A62245C263086BD9","80082023BF0E85F8","345CA7284A5E3BBB","FC14400D1720F1E0","461FAC148C225E02","922119CF044C16E2","DA16442B8A4D751F","7AFF14AE79B53FAF","C6D55D141F0A75B6","54AAEB3AEEE6F9E5","8D54DE9D31DEEE2F","9D7F23CC40D22562","6D55C79117D546FB","A8B396B11BAD5C8A",  \
"C210BBC03E6BB697","C76C5E2054FA79F8","160CD757AA42A800","75EB698D16E82082","6B2E74F41AE73A43","4086BA709FB8F2D1","39C24745EFCF3BA2","0103D63E0DDBD2DE","880564AACADCA5B1","9E052C8923E4E492","89377D3D614A631F","CCDB0D03BB9A93FB","674EAE4D81437D59","35892E297336402F","7CDEE82121CDA93B","663177ED538F2675","21DA68A6E6F527F8","56DEA21758022C2C","AE92F03DFA224F20","3CC43EDCD3C78AA1"]
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

