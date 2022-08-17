__Author__ = "xq"
'''
^, <, > 分别是居中、左对齐、右对齐，后面带宽度，
 : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
b、d、o、x 分别是二进制、十进制、八进制、十六进制。

此外我们可以使用大括号 {} 来转义大括号，如下实例：'''

print ("{} 对应的位置是 {{0}}".format("runoob"))


print("{:.2f}".format(2))
print("{:+.2f}".format(2))
print("{:+.2f}".format(2))
print("{:0>2d}".format(2))
print("{:x<4d}".format(2))
print("{:,}".format(2))
print("{:.2%}".format(2))
print("{:.2e}".format(2))
print("{:>10d}".format(2))
print("{:<10d}".format(2))
print("{:^10d}".format(2))