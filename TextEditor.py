# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:45:15 2018

@author: bhanu
"""
import tkinter #Python with tkinter outputs the fastest and easiest way to create the GUI applications
import tkinter.scrolledtext as ScrolledText



import tkinter.filedialog
#import tkinter.Menu
'''
root is the name of the main window object
classNmae is used to change the name of the window
default name of the window will be Tk
'''
root = tkinter.Tk(className = "TextEditor")

# defining txext area
textArea = ScrolledText.ScrolledText(root, width=100, height=80)


# FUNCTIONS
# open a file from menu


def openFile():
    file = tkinter.filedialog.askopenfile(mode='r', title='Select a file')
    if file != None:
        contents = file.read()
        #textArea.delete(1.0, END)
      #  textArea.destroy()
        textArea.insert(1.0, contents)
        file.close()
     
    


# MenuOption

menu = tkinter.Menu(root)
root.config(menu=menu)
fileMenu = tkinter.Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")


helpMenu = tkinter.Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="About")


textArea.pack()# allow to write on the defined text area
root.mainloop()# it open the window untill we close it




'''
mainloop() is an infinite loop used to run the application,
wait for an event to occur and process the event till the window is not closed.
'''
root.mainloop()