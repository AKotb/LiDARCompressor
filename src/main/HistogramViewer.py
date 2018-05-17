import os
import tkFileDialog
from Tkinter import *

from src.main import LASHandler


class HistogramViewer(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Histogram-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputlaslbl = Label(self.master, text="LAS File")
        inputlaslbl.place(x=20, y=50)
        self.inputlastxtfield = Text(self.master, height=1, width=50)
        self.inputlastxtfield.place(x=100, y=50)
        inputlasbtn = Button(self.master, text="Browse", command=self.selectlas)
        inputlasbtn.place(x=520, y=50)

        self.generatehistogrambtn = Button(self.master, text="Generate Histogram", command=self.generatehistogram)
        self.generatehistogrambtn.place(x=400, y=100)
        self.cancelbtn = Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=520, y=100)

    def exit(self):
        self.master.destroy()

    def selectlas(self):
        inputlasfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAS File",
                                                          filetypes=(("LAS Files", "*.las"), ("All Files", "*.*")))
        self.inputlastxtfield.delete(1.0, END)
        self.inputlastxtfield.insert(END, inputlasfilepath)

    def generatehistogram(self):
        inputlasfilepath = self.inputlastxtfield.get("1.0", 'end-1c')
        lashandler = LASHandler.LASHandler()
        loadedLASFile = lashandler.loadLASFile(inputlasfilepath)
        lashandler.generateLASFileHistogram(loadedLASFile)