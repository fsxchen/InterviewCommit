#!/usr/bin/env python3
# coding:utf-8

"""
编写程序，要求能够正确解析redis协议的字符串，
并自证其正确性。比如，当输入是"+OK\r\n"时，
应该解析成正确结果"OK"; 当输入是":1000\r\n"，
应该解析成正确结果1000。
"""


def get_redis_protocal_string(strings):
    avaliable_char_list = []
    for s in strings.strip(r"\r\n"):
        if s.isdigit() or s.isalpha():
            avaliable_char_list.append(s)
    return "".join(avaliable_char_list)


if __name__ == "__main__":
    test1 = r"+OK\r\n"
    test2 = r":1000\r\n" 
    print(get_redis_protocal_string(test1))
    print(get_redis_protocal_string(test2))