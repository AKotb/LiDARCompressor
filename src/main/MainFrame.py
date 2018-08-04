import tkMessageBox
from Tkinter import *

from src.main.CompressASCIIFileFrame import CompressASCIIFileFrame
from src.main.CompressLASFileFrame import CompressLASFileFrame
from src.main.DecompressASCIIFileFrame import DecompressASCIIFileFrame
from src.main.DecompressLAZFileFrame import DecompressLAZFileFrame
from src.main.HistogramViewer import HistogramViewer
from src.main.MetadataViewer import MetadataViewer
from src.main.WinZIPCompressFileFrame import WinZIPCompressFileFrame
from src.main.WinZIPDecompressFileFrame import WinZIPDecompressFileFrame
from src.main.ZIP7CompressFileFrame import ZIP7CompressFileFrame
from src.main.ZIP7DecompressFileFrame import ZIP7DecompressFileFrame
from src.main.WinRARCompressFileFrame import WinRARCompressFileFrame
from src.main.WinRARDecompressFileFrame import WinRARDecompressFileFrame


class MainFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Main Window-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        toolsmenu = Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="View Metadata", command=self.metadata)
        toolsmenu.add_command(label="View Histogram", command=self.histogram)
        toolsmenu.add_separator()
        compressmenu = Menu(self, tearoff=False)
        toolsmenu.add_cascade(label="Compress", menu=compressmenu)
        laszipcompressmenu = Menu(self, tearoff=False)
        compressmenu.add_cascade(label="LASzip", menu=laszipcompressmenu)
        laszipcompressmenu.add_command(label='LAS', command=self.compresslas)
        laszipcompressmenu.add_command(label='ASCII', command=self.compressascii)
        compressmenu.add_command(label="WinZIP", command=self.winzipcompress)
        compressmenu.add_command(label="WinRAR", command=self.winrarcompress)
        compressmenu.add_command(label="7-ZIP", command=self.zip7compress)
        decompressmenu = Menu(self, tearoff=False)
        toolsmenu.add_cascade(label="Decompress", menu=decompressmenu)
        laszipdecompressmenu = Menu(self, tearoff=False)
        decompressmenu.add_cascade(label="LASzip", menu=laszipdecompressmenu)
        laszipdecompressmenu.add_command(label='LAS', command=self.decompresslaz)
        laszipdecompressmenu.add_command(label='ASCII', command=self.decompressascii)
        decompressmenu.add_command(label="WinZIP", command=self.winzipdecompress)
        decompressmenu.add_command(label="WinRAR", command=self.winrardecompress)
        decompressmenu.add_command(label="7-ZIP",  command=self.zip7decompress)
        menubar.add_cascade(label="Tools", menu=toolsmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)


    def exit(self):
        exit()

    def about(self):
        tkMessageBox.showinfo("LiDAR Compression System",
                              "LiDAR Compression System is an adaptable system for compressing LiDAR data."
                              "LiDAR Compression System Version 0.1")

    def histogram(self):
        root = Tk()
        root.geometry("600x150")
        app = HistogramViewer(root)
        root.mainloop()

    def metadata(self):
        root = Tk()
        root.geometry("600x400")
        app = MetadataViewer(root)
        root.mainloop()

#############################LASzip######################################
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


#############################WinZIP######################################
    def winzipcompress(self):
        root = Tk()
        root.geometry("600x250")
        app = WinZIPCompressFileFrame(root)
        root.mainloop()

    def winzipdecompress(self):
        root = Tk()
        root.geometry("600x250")
        app = WinZIPDecompressFileFrame(root)
        root.mainloop()


#############################WinRAR######################################
    def winrarcompress(self):
        root = Tk()
        root.geometry("600x250")
        app = WinRARCompressFileFrame(root)
        root.mainloop()

    def winrardecompress(self):
        root = Tk()
        root.geometry("600x250")
        app = WinRARDecompressFileFrame(root)
        root.mainloop()


#############################7-ZIP######################################
    def zip7compress(self):
        root = Tk()
        root.geometry("600x250")
        app = ZIP7CompressFileFrame(root)
        root.mainloop()

    def zip7decompress(self):
        root = Tk()
        root.geometry("600x250")
        app = ZIP7DecompressFileFrame(root)
        root.mainloop()