import os
import tkFileDialog
from Tkinter import *

from src.main import LASHandler


class CompressASCIIFileFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        parentlastoolsdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\LAStools")
        self.CONST_LASTOOLS_PATH = os.path.join(parentlastoolsdir, "bin")
        self.init_window()

    def init_window(self):
        self.master.title("Compress ASCII File-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputasciilbl = Label(self.master, text="ASCII File")
        inputasciilbl.place(x=20, y=50)
        self.inputasciitxtfield = Text(self.master, height=1, width=50)
        self.inputasciitxtfield.place(x=100, y=50)
        inputasciibtn = Button(self.master, text="Browse", command=self.selectascii)
        inputasciibtn.place(x=520, y=50)

        outputlazlbl = Label(self.master, text="LAZ File")
        outputlazlbl.place(x=20, y=100)
        self.outputlaztxtfield = Text(self.master, height=1, width=50)
        self.outputlaztxtfield.place(x=100, y=100)
        outputlazbtn = Button(self.master, text="Browse", command=self.selectlaz)
        outputlazbtn.place(x=520, y=100)

        self.startcompressbtn = Button(self.master, text="Start", command=self.compressascii)
        self.startcompressbtn.place(x=480, y=200)
        self.cancelcompressbtn = Button(self.master, text="Cancel", command=self.exit)
        self.cancelcompressbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def selectascii(self):
        inputasciifilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select ASCII File",
                                                          filetypes=(("ASCII Files", "*.txt"), ("All Files", "*.*")))
        self.inputasciitxtfield.delete(1.0, END)
        self.inputasciitxtfield.insert(END, inputasciifilepath)

    def selectlaz(self):
        outputlazfilepath = tkFileDialog.askdirectory(initialdir="/", title="Select LAZ File Directory")
        self.outputlaztxtfield.delete(1.0, END)
        self.outputlaztxtfield.insert(END, outputlazfilepath)

    def compressascii(self):
        self.cancelcompressbtn.place_forget()
        self.startcompressbtn.place_forget()
        inputasciifilepath = self.inputasciitxtfield.get("1.0", 'end-1c')
        outputlazfilepath = self.outputlaztxtfield.get("1.0", 'end-1c')
        lashandler = LASHandler.LASHandler()
        returneddata = lashandler.compressasciifile(self.CONST_LASTOOLS_PATH, inputasciifilepath,
                                                    outputlazfilepath)
        self.okbtn = Button(self.master, text="OK", command=self.exit)
        self.okbtn.place(x=480, y=200)
        self.compressiontimelbl = Label(self.master, text="Compression Time: %s Sec" % returneddata[0])
        self.compressiontimelbl.place(x=20, y=150)
        self.compressionratiolbl = Label(self.master, text="Compression Ratio: %s " % returneddata[1])
        self.compressionratiolbl.place(x=20, y=175)
