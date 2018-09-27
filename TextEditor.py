# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:45:15 2018

@author: bhanu
"""
import tkinter #Python with tkinter outputs the fastest and easiest way to create the GUI applications

'''
root is the name of the main window object
classNmae is used to change the name of the window
default name of the window will be Tk
'''
root = tkinter.Tk(className = "MyTextEditor")

textArea = tkinter.scrolledtext.ScrolledText(root, width = 100, height = 50)
textArea.pack()

#menuOption
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)

menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

helpMenu = Menu(menu)

menu.add_cascade(label="help",menu=helpMenu)
helpMenu.add_command(label="About Us")



'''
mainloop() is an infinite loop used to run the application,
wait for an event to occur and process the event till the window is not closed.
'''
root.mainloop()