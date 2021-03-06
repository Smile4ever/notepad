#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  notepad4.txt
#	added a scroll bar using info from
#  http://stackoverflow.com/questions/16577718/fit-tkinter-scrollbar-to-text-widget?rq=1
#   notepad 5 added a 2nd menu and also added an exit dialogue box
# notepad 6, added open and save dialogues (they seem to work) 
# note pad 6 = legacy code is still in source incase of issues
# notepad 7 = added menu insert
# added insert date time to insert menu


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
import tkFileDialog
import tkMessageBox
import sys
import time

#window = Tkinter.Tk(className=" Just another Text Editor")

#set up
window = Tk()
window.title('Notepad 7.0')
window.geometry("420x220") #set window size
window.resizable(1,1)

#define text entry box
notetext = Text(window, height=420, width=210)  #set text box size
#display text entry box
notetext.pack()
notetext.grid(row = 1, column = 3,)

#code for scroll bars

txt = Text(notetext, height=15, width=55)
scr = Scrollbar(notetext)	
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)
txt.pack(side=LEFT)

#place scroll bar in application

scr.pack(side="right", fill="y", expand=False)
notetext.pack(side="left", fill="both", expand=True)

#define menu option calls

def newfile():
	txt.delete(1.0, END)
	
# legacy open file 	
def openfile():
	text = open("document.txt").read()
	txt.delete(1.0, END)
	txt.insert(END, text)
	txt.mark_set(INSERT, 1.0)
	
def open_command():
        file = tkFileDialog.askopenfile(parent=window,mode='rb',title='Select a file')
        if file != None:
            text = file.read()
            txt.insert(END, text)
            file.close()	

#def save_command(self):
def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = txt.get('1.0', END+'-1c')
        file.write(data)
        file.close()

#legacy save file
def savefile():
	f = open("document.txt", "w")
	text = txt.get(1.0, END)
	try:
		# normalize trailing whitespace
		f.write(text.rstrip())
		f.write("\n")
	finally:
		f.close()
	
		
	
def about_cmd():
    label = tkMessageBox.showinfo("About", "Notepad by Paul Sutton")		

def exit_cmd():
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		sys.exit()
		
		
def insert_date_time():
	dati = time.ctime() # set variable to grab the current date and time
	txt.insert(END, dati) #insert date and time in to document
	print dati	# legacy test	
	
	
# create a menu
def dummy():
    print ("I am a Dummy Command, I will be removed in the next step")
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_cmd)

insertmenu = Menu(menu)
menu.add_cascade( label="Insert", menu=insertmenu)
insertmenu.add_command(label="Date/time", command=insert_date_time)		

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_cmd)


#display window
#window.config(menu=menubar)
window.config(menu=menu)

window.mainloop()

#define text entry box
notetext = Text(window, height=290, width=150)
#display text entry box
notetext.grid(row = 1, column = 3,)



