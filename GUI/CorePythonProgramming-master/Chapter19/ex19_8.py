#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例19.8（P547）


# 程序目的：
#  
#
# 程序功能：
# 
# 
#
# 
# 编程要点
# 1. 
# 2. 
# 
#
# 最后编辑：2014_07_09

from Tkinter import Button, END, Label, W
from Pmw import initialise, ComboBox, Counter

top = initialise()
lb = Label(top, text = 'Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Counter(top, labelpos = W, label_text = 'Number:', 
	datatype = 'integer', entryfield_value = 2,
	increment = 2, entryfield_validate = {'validator':
	'integer', 'min': 2, 'max': 12})
ct.pack()

cb = ComboBox(top, labelpos = W, label_text = 'Type:')
for animal in ('dog', 'cat', 'hamster', 'python'):
	cb.insert(END, animal)
cb.pack()

qb = Button(top, text = 'QUIT', command = top.quit, bg = 'red', fg = 'white')
qb.pack()

top.mainloop()
