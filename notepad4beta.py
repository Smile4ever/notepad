#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  notepad3.txt
#  
#  Copyright 2014 Paul Sutton <psutton@ER1401>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#http://effbot.org/zone/vroom.htm  
#http://knowpapa.com/text-editor/
#
import Tkinter # note use of caps
from Tkinter import *



#set up
window = Tk()
window.title('Notepad 3.0')
window.geometry("420x220")
window.resizable(1,1)




#define text entry box
notetext = Text(window, height=400, width=210)
#display text entry box
notetext.pack()
notetext.grid(row = 1, column = 3,)

txt = Text(notetext, height=15, width=55)
scr = Scrollbar(notetext)
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)
txt.pack(side=LEFT)

scr.pack(side="right", fill="y", expand=False)
notetext.pack(side="left", fill="both", expand=True)

def newfile():
	notetext.delete(1.0, END)
	
def openfile():
	text = open("document.txt").read()
	notetext.delete(1.0, END)
	notetext.insert(END, text)
	notetext.mark_set(INSERT, 1.0)
		
	
def savefile():
	f = open("document.txt", "w")
	text = notetext.get(1.0, END)
	try:
		# normalize trailing whitespace
		f.write(text.rstrip())
		f.write("\n")
	finally:
		f.close()

#create menu bar and menu	
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile ) 
filemenu.add_command(label="Open", command=openfile )
filemenu.add_command(label="Save", command=savefile )
filemenu.add_command(label="Exit", command=exit )
	
#filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)


#display window
window.config(menu=menubar)
window.mainloop()


#define text entry box
notetext = Text(window, height=290, width=150)
#display text entry box
notetext.grid(row = 1, column = 3,)


#display window

window.mainloop()
