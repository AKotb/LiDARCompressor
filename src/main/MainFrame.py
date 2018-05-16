import os
import tkFileDialog
import tkMessageBox
from Tkinter import *

from src.main import LASHandler
from src.main.CompressASCIIFileFrame import CompressASCIIFileFrame
from src.main.CompressLASFileFrame import CompressLASFileFrame
from src.main.DecompressASCIIFileFrame import DecompressASCIIFileFrame
from src.main.DecompressLAZFileFrame import DecompressLAZFileFrame


class MainFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        parentlastoolsdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\LAStools")
        self.CONST_LASTOOLS_PATH = os.path.join(parentlastoolsdir, "bin")
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Main Window-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load File", command=self.loadfile)
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = Menu(menubar, tearoff=0)

        toolsmenu.add_command(label="View Metadata", command=self.metadata)
        toolsmenu.add_command(label="View Histogram", command=self.histogram)
        toolsmenu.add_separator()
        compressmenu = Menu(self, tearoff=False)
        toolsmenu.add_cascade(label="Compress", menu=compressmenu)
        compressmenu.add_command(label='LAS', command=self.compresslas)
        compressmenu.add_command(label='ASCII', command=self.compressascii)
        decompressmenu = Menu(self, tearoff=False)
        toolsmenu.add_cascade(label="Decompress", menu=decompressmenu)
        decompressmenu.add_command(label='LAZ', command=self.decompresslaz)
        decompressmenu.add_command(label='ASCII', command=self.decompressascii)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        S = Scrollbar(self.master)
        S.pack(side=RIGHT, fill=Y)
        self.T = Text(self.master, height=400, width=380)
        self.T.pack(side=LEFT, fill=Y)
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)

    def exit(self):
        exit()

    def loadfile(self):
        self.inputfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAS File",
                                                          filetypes=(("LAS Files", "*.las"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        self.loadedLASFile = lashandler.loadLASFile(self.inputfilepath)
        self.T.delete(1.0, END)
        self.T.insert(END, "File: [" + self.inputfilepath + "] Loaded Successfully")

    def about(self):
        tkMessageBox.showinfo("LiDAR Compression System",
                              "LiDAR Compression System is an adaptable system for compressing LiDAR data."
                              "LiDAR Compression System Version 0.1")

    def histogram(self):
        lashandler = LASHandler.LASHandler()
        lashandler.generateLASFileHistogram(self.loadedLASFile)

    def metadata(self):
        inputfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Input File",
                                                     filetypes=(("LAS Files", "*.las"), ("LAZ Files", "*.laz"),
                                                                ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        lashandler.viewfileinfo(self.CONST_LASTOOLS_PATH, inputfilepath)
        data = inputfilepath.split('.')
        infofilepath = data[0] + "_info.txt"
        infofile = open(infofilepath, "r")
        self.T.delete(1.0, END)
        for line in infofile:
            self.T.insert(END, line)
        infofile.close()

    def compresslas(self):
        root = Tk()
        root.geometry("600x250")
        app = CompressLASFileFrame(root)
        root.mainloop()

    def decompresslaz(self):
        root = Tk()
        root.geometry("600x250")
        app = DecompressLAZFileFrame(root)
        root.mainloop()

    def compressascii(self):
        root = Tk()
        root.geometry("600x250")
        app = CompressASCIIFileFrame(root)
        root.mainloop()

    def decompressascii(self):
        root = Tk()
        root.geometry("600x250")
        app = DecompressASCIIFileFrame(root)
        root.mainloop()
