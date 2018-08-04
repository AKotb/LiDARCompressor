import tkFileDialog
from Tkinter import *

from src.main import WinZIPCompressor


class WinZIPDecompressFileFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Decompress ZIP File using WinZIP-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputziplbl = Label(self.master, text="ZIP File")
        inputziplbl.place(x=20, y=50)
        self.inputziptxtfield = Text(self.master, height=1, width=50)
        self.inputziptxtfield.place(x=100, y=50)
        inputzipbtn = Button(self.master, text="Browse", command=self.selectzip)
        inputzipbtn.place(x=520, y=50)

        outputfilelbl = Label(self.master, text="Extract Into")
        outputfilelbl.place(x=20, y=100)
        self.outputfiletxtfield = Text(self.master, height=1, width=50)
        self.outputfiletxtfield.place(x=100, y=100)
        outputfilebtn = Button(self.master, text="Browse", command=self.selectoutputfiledir)
        outputfilebtn.place(x=520, y=100)

        self.startdecompressbtn = Button(self.master, text="Start", command=self.decompresszip)
        self.startdecompressbtn.place(x=480, y=200)
        self.canceldecompressbtn = Button(self.master, text="Cancel", command=self.exit)
        self.canceldecompressbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def selectzip(self):
        inputzipfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select ZIP File",
                                                        filetypes=(("ZIP Files", "*.zip"), ("All Files", "*.*")))
        self.inputziptxtfield.delete(1.0, END)
        self.inputziptxtfield.insert(END, inputzipfilepath)

    def selectoutputfiledir(self):
        outputfilepath = tkFileDialog.askdirectory(initialdir="/", title="Select Output File Directory")
        self.outputfiletxtfield.delete(1.0, END)
        self.outputfiletxtfield.insert(END, outputfilepath)

    def decompresszip(self):
        self.canceldecompressbtn.place_forget()
        self.startdecompressbtn.place_forget()
        inputzipfilepath = self.inputziptxtfield.get("1.0", 'end-1c')
        outputfilepath = self.outputfiletxtfield.get("1.0", 'end-1c')
        winzipcompressor = WinZIPCompressor.WinZIPCompressor()
        returneddata = winzipcompressor.decompressfile(inputzipfilepath, outputfilepath)
        self.okbtn = Button(self.master, text="OK", command=self.exit)
        self.okbtn.place(x=480, y=200)
        self.compressiontimelbl = Label(self.master, text="Decompression Time: %s Sec" % returneddata[0])
        self.compressiontimelbl.place(x=20, y=150)
