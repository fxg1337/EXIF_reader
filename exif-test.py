
#======================
# imports
#======================
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import subprocess, sys, os
from os.path import join as pjoin
from subprocess import PIPE, run
from tkinter import messagebox
import exifread




class EXIF(Tk):
    def __init__(self):
        super(EXIF, self).__init__()

        self.title("Exif Reader")
        self.minsize(100, 50)

        self.buttonstart()
        self.buttonquit()


    def  buttonstart(self):

        self.bstart = ttk.Button(width = 16,text = "Start",command = self.run).grid(column = 1, row = 1)
        
        
    def buttonquit(self):
        self.bquit = ttk.Button(width = 16,text = "Quit",command = self.quit).grid(column = 2, row = 1)
        

    def  run(self):

        keep_list={}
        
        pic_selected = filedialog.askopenfilename()
        folder_selected = filedialog.askdirectory()

        
        pic_run = open(pic_selected, 'rb')
        tags = exifread.process_file(pic_run)
        keep_list[pic_selected] = tags

        file_name = ("list.txt")

        fname = os.path.join(folder_selected, file_name)

        with open(fname, 'w') as f:
            for key, value in keep_list.items():
                f.write('%s:%s\n' % (key, value))
        
    def quit(self):
        os._exit(1)
        

        
fxg = EXIF()

fxg.mainloop()

