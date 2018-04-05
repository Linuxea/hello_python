# Base64是一种用64个字符来表示任意二进制数据的方法
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
import base64

if __name__ == '__main__':
    after = base64.b64encode(b"i love you")
    print(after)
    before = base64.b64decode(after)
    print(before)
