# coding = utf-8


""" python3 默认将输入的东东看作是字符串
    python2 需要使用 raw_input() 将输入的东东转化为字符串，默认保留输入东东的原本数据类型
"""
something = input("请输入一些东东:\t")

print("something you input is: %s" % something)
