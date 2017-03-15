#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: entry_validate.py
# Created Time: Fri Mar  3 23:21:10 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import Tkinter as tk

class Example(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        
        vcmd = (self.register(self.onValidate),'%d',"%i",'%P','%s','%S','%v','%V','%W')
        self.entry = tk.Entry(self,validate='key',validatecommand=vcmd)
        self.text = tk.Text(self,height=10,width=40)
        self.entry.pack(side='top',fill='x')
        self.text.pack(side='bottom',fill='both',expand=True)

    def onValidate(self,d,i,P,s,S,v,V,W):
        self.text.delete('1.0','end')
        self.text.insert('end','OnValidate:\n')
        self.text.insert('end',"d='%s'\n"%d)
        self.text.insert('end',"i='%s'\n"%i)
        self.text.insert('end',"P='%s'\n"%P)
        self.text.insert('end',"s='%s'\n"%s)
        self.text.insert('end',"S='%s'\n"%S)
        self.text.insert('end',"v='%s'\n"%v)
        self.text.insert('end',"V='%s'\n"%V)
        self.text.insert('end',"W='%s'\n"%W)

        if S == S.lower():
            return True
        else:
            self.bell()
            return False

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill='both',expand=True)
    root.mainloop()