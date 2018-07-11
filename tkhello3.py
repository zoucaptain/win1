#! /usr/bin/env python
# _*_ coding:utf8 _*_
'''tkhello
    with label and button
'''
import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text='hello world')
label.pack()

quit = Tkinter.Button(top, text='quit', command=top.quit,bg='red',fg='white')
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()
