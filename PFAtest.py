#!/usr/bin/env python 

'''PFAtest
    create a billboard
'''
from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'warn'
CRITI = 'criti'
REGU = 'regu'

SIGNS = {
    'do not enter': CRITI,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRITI,
    'merging traffic': WARN,
    'one way': REGU,
}

critiCB = lambda: showerror('Error', 'Error Button Pressed')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit,
       bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritiButton = pto(MyButton, command=critiCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachsign in SIGNS:
    signType = SIGNS[eachsign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=1)' % (
        signType.title(), eachsign,
        '.upper()' if signType == CRITI else '.title()'
    )
    eval(cmd)
top.mainloop()
