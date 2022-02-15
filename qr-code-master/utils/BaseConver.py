ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def alphabet2digit(alphabet):
    """26进制 -> 10进制"""
    return sum(ALPHABET.index(a) * (26 ** e) for e, a in enumerate(reversed(alphabet)))


def digit2alphabet(digit):
    """10进制 -> 26进制"""
    mod, remainder = divmod(digit, 26)
    alphabet = ALPHABET[remainder]
    while mod:
        mod, remainder = divmod(mod, 26)
        alphabet = ALPHABET[remainder] + alphabet
    return alphabet


def digit2base32(num, b=32):
    '''
    将数字转化为任意进制
    :param num: 当前数字
    :param b: base322digit
    :return:
    '''
    return ((num == 0) and "0") or \
           (digit2base32(num // b, b).lstrip("0") + "0123456789ABCDEFGHJKLMNPRSTVWXYZ"[num % b])


def base322digit(num):
    baseText = "0123456789ABCDEFGHJKLMNPRSTVWXYZ"
    num = str(num).upper()
    sumValue = 0
    count = 0
    for i in range(len(num) - 1, -1, -1):
        sumValue = sumValue + (baseText.find(num[i]) * (32 ** count))
        count += 1
    return sumValue


def digit2hexadecimal(digit):
    '''
    十进制转十六进制
    :param digit:
    :return:
    '''
    return hex(digit)[2:]
