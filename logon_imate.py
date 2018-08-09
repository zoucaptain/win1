#!/usr/bin/env python 
# _ * _ coding:utf8 _ * _
"""logon_imatate
    build a logon gui by easygui
"""
import sys

import easygui


def denglu():
    field = ('用户名', '密码')
    msg = '请输入用户名密码：'
    title = '登录'
    yonghu = easygui.multpasswordbox(msg, title, field)
    if yonghu == None or yonghu == ['', '']:
        easygui.msgbox('你好，欢迎进入主程序', ok_button='确定')
        return 2
    else:
        # 将用户名读取在list1中
        list1 = []
        zhanghao = open('zhanghao1.txt')
        for each_line in zhanghao:
            (zhanghao_, huanhang) = each_line.split('\n')
            list1.append(zhanghao_)
        zhanghao.close()
        # 将密码读取在list1中
        list2 = []
        mima = open('mima1.txt')
        for each_line in mima:
            (mima_, huiche) = each_line.split('\n')
            list2.append(mima_)
        mima.close()

        # 确认用户名和密码是否存在并且匹配
        for x in list1:
            if x == str(yonghu[0]) and (list2[list1.index(x)] != str(yonghu[1])):
                easygui.msgbox('密码错误，请重新输入', ok_button='确定')
                return 0
                break
            elif x == str(yonghu[0]) and (list2[list1.index(x)] == str(yonghu[1])):
                easygui.msgbox('欢迎进入主程序', ok_button='确定')
                return 2
                break
        if str(yonghu[0]) not in list1:
            easygui.msgbox('用户不存在，请注册', ok_button='确定')
            return 1


def zhuce():
    values = []

    def zhuce1():
        msg = '*为必填项'
        title = '账号中心'
        fields = ['*用户名', '*密码', 'QQ']
        return easygui.multenterbox(msg, title, fields, values)

    yonghuzhuce = zhuce1()
    while yonghuzhuce == None:
        easygui.msgbox('欢迎进入主界面', ok_button='确定')
        return 2
    else:
        while yonghuzhuce[0] == '' or yonghuzhuce[1] == '':
            easygui.msgbox('用户名和密码不能为空，请重新输入', ok_button='继续填写')
            values = [yonghuzhuce[0], yonghuzhuce[1], yonghuzhuce[2]]
            yonghuzhuce = zhuce1()

    # 检验用户名是否被占用
    list3 = []
    zhanghao = open('zhanghao1.txt')
    for each_line in zhanghao:
        (zhanghao_, huiche_) = each_line.split('\n')
        list3.append(zhanghao_)
    zhanghao.close()
    while str(yonghuzhuce[0]) in list3:
        easygui.msgbox('用户已存在', ok_button='重新输入')
        yonghuzhuce = zhuce1()

    # 将账号密码分别存储在两个txt文件内
    zhanghao = open('zhanghao1.txt', 'a')
    zhanghao.write(yonghuzhuce[0] + '\n')
    zhanghao.close()
    mima = open('mima1.txt', 'a')
    mima.write(yonghuzhuce[1] + '\n')
    mima.close()
    return 0


def main():
    # 创建两个txt临时文件，分别用于存放用户名和密码
    zhanghao = open('zhanghao1.txt', 'w')
    mima = open('mima1.txt', 'w')
    zhanghao.close()
    mima.close()

    # 输入邀请码
    password = '111111'
    while password != '000000':
        password = easygui.passwordbox('请输入邀请码（默认‘000000’）', '进入easygui操作界面')
        if password == None:
            sys.exit(0)
    while 1:
        # 请选择登录或者注册
        choices1 = ['已有账号，直接登录', '开始注册']
        choice = 0
        choice = easygui.indexbox('登录/注册：', '请选择：', choices=choices1)

        # 登录
        while choice == 0:
            denglu()

        # 注册
        while choice == 1:
            choice = zhuce()
            if choice == 0:
                easygui.msgbox('注册成功，即将进入登录界面', ok_button='确定!')
                choice = denglu()
        # 工作界面
        if choice == 2:
            easygui.msgbox('已完成登录，以游客身份登录，可以随意发挥了', ok_button='确定')

        # 是否继续
        msg = "是否重新开始？"
        title = '请选择'
        if easygui.ccbox(msg, title, choices=('Continue', 'Cancel')):
            pass
        else:
            sys.exit(0)


if __name__ == '__main__':
    main()
