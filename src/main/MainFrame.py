import os
import tkFileDialog
import tkMessageBox
from Tkinter import *

from src.main import LASHandler


class MainFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        parentlastoolsdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\LAStools")
        self.CONST_LASTOOLS_PATH = os.path.join(parentlastoolsdir, "bin")
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
        compressmenu.add_command(label='ASCII')
        toolsmenu.add_command(label="Decompress", command=self.decompresslaz)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

    def exit(self):
        exit()

    def loadfile(self):
        inputLASFilePath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAS File",
                                                        filetypes=(("LAS Files", "*.las"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        self.loadedLASFile = lashandler.loadLASFile(inputLASFilePath)

    def about(self):
        tkMessageBox.showinfo("LiDAR Compression System",
                              "LiDAR Compression System is an adaptable system for compressing LiDAR data."
                              "LiDAR Compression System Version 0.1")

    def histogram(self):
        lashandler = LASHandler.LASHandler()
        lashandler.generateLASFileHistogram(self, self.loadedLASFile)

    def metadata(self):
        lashandler = LASHandler.LASHandler()
        lashandler.showLASFileMetadata(self, self.loadedLASFile)

    def compresslas(self):
        inputlasfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAS File",
                                                        filetypes=(("LAS Files", "*.las"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        data = inputlasfilepath.split('.')
        outputlazfilepath = data[0] + ".laz"
        print(self.CONST_LASTOOLS_PATH)
        lashandler.compresslasfile(self.CONST_LASTOOLS_PATH, inputlasfilepath, outputlazfilepath)

    def decompresslaz(self):
        inputlazfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAZ File",
                                                        filetypes=(("LAZ Files", "*.laz"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        data = inputlazfilepath.split('.')
        outputlasfilepath = data[0] + ".las"
        lashandler.decompresslazfile(self.CONST_LASTOOLS_PATH, inputlazfilepath, outputlasfilepath)
