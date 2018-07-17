#!/usr/bin/env python
'''listdir
    list dir and sub files
'''
import os
from time import sleep
from Tkinter import *


class Dirlist(object):
    def __init__(self, initlist=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory lister v1.1')
        self.label.pack()
        self.cwd = StringVar(self.top)
        self.dir1 = Label(self.top, fg='blue',
                          font=('Helvetica', 12, 'bold'))
        self.dir1.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15,
                            width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') \
                    and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config( \
                selectbackground='LightSkyBlue')
            self.top.update()
            return


if __name__ == '__main__':
    pass
