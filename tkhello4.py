#!/usr/bin/env python
#  _*_ coding:utf8 _*_
'''tkhello4
    label button add scrollbar
'''
from Tkinter import *


def resize(ev=None):
    label.config(font='Helvectica -%d bold' %
                 scale.get())

#top
top = Tk()
top.geometry('250x150')
#label
label = Label(top, text='Hello world', font='Helvectica -12 bold')
label.pack(fill=Y, expand=1)
#scale
scale = Scale(top, from_=10, to=40,
              orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
#Button
quit = Button(top, text='QUIT',
              command=top.quit, activeforeground='white',
              activebackground='red')
quit.pack()

#mainloop
mainloop()
