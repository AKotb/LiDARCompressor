import tkFileDialog
import tkMessageBox
from Tkinter import *

from src import LASHandler


class MainFrame(Frame):
    CONST_LASTOOLS_PATH = 'D:/Education/Master/Thesis/Sources/LAStools/bin'

    def __init__(self, master=None):
        Frame.__init__(self, master, relief=SUNKEN, bd=2)
        self.initUI()

    def initUI(self):
        self.menubar = Menu(self)

        filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load File", command=self.loadfile)
        filemenu.add_command(label="Exit", command=self.quit)

        toolsmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Tools", menu=toolsmenu)
        toolsmenu.add_command(label="View Metadata", command=self.metadata)
        toolsmenu.add_command(label="View Histogram", command=self.histogram)
        toolsmenu.add_separator()
        compressmenu = Menu(self, tearoff=False)
        toolsmenu.add_cascade(label="Compress", menu=compressmenu)
        compressmenu.add_command(label='LAS', command=self.compresslas)
        compressmenu.add_command(label='ASCII')
        toolsmenu.add_command(label="Decompress", command=self.decompresslaz)

        helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.about)

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(self.master, "config", "-menu", self.menubar)

        self.canvas = Canvas(self, bg="white", width=600, height=400,
                             bd=0, highlightthickness=0)
        self.canvas.pack()

    def about(self):
        tkMessageBox.showinfo("LiDAR Compression System",
                              "LiDAR Compression System is an adaptable system for compressing LiDAR data."
                              "LiDAR Compression System Version 0.1")

    def loadfile(self):
        inputLASFilePath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAS File",
                                                        filetypes=(("LAS Files", "*.las"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        self.loadedLASFile = lashandler.loadLASFile(inputLASFilePath)

    def quit(self):
        root.quit()

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
        lashandler.compresslasfile(self.CONST_LASTOOLS_PATH, inputlasfilepath, outputlazfilepath)

    def decompresslaz(self):
        inputlazfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select LAZ File",
                                                        filetypes=(("LAZ Files", "*.laz"), ("All Files", "*.*")))
        lashandler = LASHandler.LASHandler()
        data = inputlazfilepath.split('.')
        outputlasfilepath = data[0] + ".las"
        lashandler.decompresslazfile(self.CONST_LASTOOLS_PATH, inputlazfilepath, outputlasfilepath)


root = Tk()
app = MainFrame(root)
app.pack()
root.mainloop()
