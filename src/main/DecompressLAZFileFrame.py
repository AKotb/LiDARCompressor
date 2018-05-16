import os
import tkFileDialog
from Tkinter import *

from src.main import LASHandler


class DecompressLAZFileFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        parentlastoolsdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\LAStools")
        self.CONST_LASTOOLS_PATH = os.path.join(parentlastoolsdir, "bin")
        self.init_window()

    def init_window(self):
        self.master.title("Decompress LAZ File-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputlazlbl = Label(self.master, text="LAZ File")
        inputlazlbl.place(x=20, y=50)
        self.inputlaztxtfield = Text(self.master, height=1, width=50)
        self.inputlaztxtfield.place(x=100, y=50)
        inputlazbtn = Button(self.master, text="Browse", command=self.selectlaz)
        inputlazbtn.place(x=520, y=50)

        outputlaslbl = Label(self.master, text="LAS File")
        outputlaslbl.place(x=20, y=100)
        self.outputlastxtfield = Text(self.master, height=1, width=50)
        self.outputlastxtfield.place(x=100, y=100)
        outputlasbtn = Button(self.master, text="Browse", command=self.selectlas)
        outputlasbtn.place(x=520, y=100)

        self.startdecompressbtn = Button(self.master, text="Start", command=self.decompresslaz)
        self.startdecompressbtn.place(x=480, y=200)
        self.canceldecompressbtn = Button(self.master, text="Cancel", command=self.exit)
        self.canceldecompressbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def selectlaz(self):
        inputlazfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAZ File",
                                                        filetypes=(("LAZ Files", "*.laz"), ("All Files", "*.*")))
        self.inputlaztxtfield.delete(1.0, END)
        self.inputlaztxtfield.insert(END, inputlazfilepath)

    def selectlas(self):
        outputlasfilepath = tkFileDialog.askdirectory(initialdir="/", title="Select LAS File Directory")
        self.outputlastxtfield.delete(1.0, END)
        self.outputlastxtfield.insert(END, outputlasfilepath)

    def decompresslaz(self):
        self.canceldecompressbtn.place_forget()
        self.startdecompressbtn.place_forget()
        inputlazfilepath = self.inputlaztxtfield.get("1.0", 'end-1c')
        outputlasfilepath = self.outputlastxtfield.get("1.0", 'end-1c')
        lashandler = LASHandler.LASHandler()
        returneddata = lashandler.decompresslazfile(self.CONST_LASTOOLS_PATH, inputlazfilepath, outputlasfilepath)
        self.okbtn = Button(self.master, text="OK", command=self.exit)
        self.okbtn.place(x=480, y=200)
        self.compressiontimelbl = Label(self.master, text="Decompression Time: %s Sec" % returneddata[0])
        self.compressiontimelbl.place(x=20, y=150)
