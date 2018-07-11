# /usr/bin/env python
# _*_ coding:utf8 _*_
'''tkhello
    use button
'''
import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello world', command=top.quit)
quit.pack()
Tkinter.mainloop()
