# /usr/bin/env python
# _*_ coding:utf8 _*_
# 本程序旨在练习easygui和文件操作的一些简单函数
# 本程序是用python来实现账号登录及注册界面，实现的基本功能如下：
#   1.如不登录与注册，则直接进入游客界面
#   2.如选择登录，会自动核对用户名与密码是否正确，如用户名不存在，则选择进入注册界面
#   3.在注册界面，会自动检查用户名是否已经存在

import sys

import easygui as g


# 登录函数,用户名已注册为实现
def DengLu():
    fields = ('用户名：', '密码：')
    msg = '请输入用户名和密码：'
    title = '登录'
    yonghu = g.multpasswordbox(msg, title, fields)

    if yonghu == None or yonghu == ['', '']:
        g.msgbox('游客你好，欢迎来到我们的python学习园地!', ok_button='确定 ')
        return 2
    else:
        # 将用户名读取在list1中
        list1 = []
        ZhangHao = open('zhanghao.txt')
        for each_line in ZhangHao:
            (zhanghao_, huiche_) = each_line.split('\n')
            list1.append(zhanghao_)
        ZhangHao.close()

        # 将密码读取在list2中
        list2 = []
        MiMa = open('mima.txt')
        for each_line in MiMa:
            (mima_, huiche_) = each_line.split('\n')
            list2.append(mima_)
        MiMa.close()

        # 确认用户名和密码是否存在并且匹配
        for X in list1:
            if X == str(yonghu[0]) and list2[list1.index(X)] != str(yonghu[1]):
                g.msgbox('密码错误，请重新输入!', ok_button='确定 ')
                return 0
                break
            elif X == str(yonghu[0]) and list2[list1.index(X)] == str(yonghu[1]):
                g.msgbox(str(yonghu[0]) + '你好，欢迎来到我们的python学习园地!', ok_button='确定 ')
                return 2
                break
        if str(yonghu[0]) not in list1:
            g.msgbox('账号不存在，请注册：', ok_button='确定 ')
            return 1


# 注册函数
def ZhuCe():
    values = []

    def zhuce():
        msg = '*为必填项'
        title = '账号中心'
        fields = ['*用户名', '*密码', 'QQ']
        return g.multenterbox(msg, title, fields, values)

    YongHuZhuCe = zhuce()
    if YongHuZhuCe == None:
        g.msgbox('游客你好，欢迎来到我们的python学习园地!', ok_button='确定 ')
        return 2
    else:
        while YongHuZhuCe[0] == '' or YongHuZhuCe[1] == '':
            g.msgbox('用户名或密码不能为空！', ok_button='继续填写 ')
            values = [YongHuZhuCe[0], YongHuZhuCe[1], YongHuZhuCe[2]]
            YongHuZhuCe = zhuce()

        # 检验用户名是否被占用
        list3 = []
        ZhangHao = open('zhanghao.txt')
        for each_line in ZhangHao:
            (zhanghao_, huiche_) = each_line.split('\n')
            list3.append(zhanghao_)
        ZhangHao.close()
        while str(YongHuZhuCe[0]) in list3:
            g.msgbox('该用户名已被占用！', ok_button='重新输入 ')
            YongHuZhuCe = zhuce()

        # 将账号密码分别存储在两个txt文件内
        ZhangHao = open('zhanghao.txt', 'a')
        ZhangHao.write(YongHuZhuCe[0] + '\n')
        ZhangHao.close()
        MiMa = open('mima.txt', 'a')
        MiMa.write(YongHuZhuCe[1] + '\n')
        MiMa.close()
        return 0


def main():
    # 创建两个txt临时文件，分别用于存放用户名和密码
    ZhangHao = open('zhanghao.txt', 'w')
    MiMa = open('mima.txt', 'w')
    ZhangHao.close()
    MiMa.close()

    # 输入邀请码
    password = '111111'
    while password != '000000':
        password = g.passwordbox('请输入邀请码(默认“000000”)：', '即将开始easygui简单练习！')
        if password == None:
            sys.exit(0)  # user chose to cancel，退出程序

    while 1:
        # 请选择登录或者注册
        choices = ['已有账号，直接登录', '开始注册']
        choice = 0
        choice = g.indexbox('登录/注册：', '请选择：', choices=choices)

        # 登录
        while choice == 0:
            choice = DengLu()

        # 注册
        while choice == 1:
            choice = ZhuCe()
            if choice == 0:
                # 注册成功重新切入登录页面
                g.msgbox('注册成功，即将进入登录页面！', ok_button='确定 ')
                choice = DengLu()
        if choice == 2:
            g.msgbox('已完成登录或以游客身份进入，这部分可以随意发挥了', ok_button='确定 ')

        msg = "是否要重新开始？"
        title = "请选择"
        if g.ccbox(msg, title, choices=('再来一次', '退出程序')):
            pass  # user chose to continue
        else:
            sys.exit(0)  # user chose to cancel，退出程序


if __name__ == '__main__':
    main()
