import tkFileDialog
from Tkinter import *

from src.main import WinRARCompressor


class WinRARCompressFileFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Compress File using WinRAR - LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputfilelbl = Label(self.master, text="Input File")
        inputfilelbl.place(x=20, y=50)
        self.inputfiletxtfield = Text(self.master, height=1, width=50)
        self.inputfiletxtfield.place(x=100, y=50)
        inputfilebtn = Button(self.master, text="Browse", command=self.selectinputfile)
        inputfilebtn.place(x=520, y=50)

        outputrarlbl = Label(self.master, text="RAR File")
        outputrarlbl.place(x=20, y=100)
        self.outputrartxtfield = Text(self.master, height=1, width=50)
        self.outputrartxtfield.place(x=100, y=100)
        outputrarbtn = Button(self.master, text="Browse", command=self.selectrar)
        outputrarbtn.place(x=520, y=100)

        self.startcompressbtn = Button(self.master, text="Start", command=self.compressinputfile)
        self.startcompressbtn.place(x=480, y=200)
        self.cancelcompressbtn = Button(self.master, text="Cancel", command=self.exit)
        self.cancelcompressbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def selectinputfile(self):
        inputfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Input File")
        self.inputfiletxtfield.delete(1.0, END)
        self.inputfiletxtfield.insert(END, inputfilepath)

    def selectrar(self):
        outputrarfilepath = tkFileDialog.askdirectory(initialdir="/", title="Select RAR File Directory")
        self.outputrartxtfield.delete(1.0, END)
        self.outputrartxtfield.insert(END, outputrarfilepath)

    def compressinputfile(self):
        self.cancelcompressbtn.place_forget()
        self.startcompressbtn.place_forget()
        inputfilepath = self.inputfiletxtfield.get("1.0", 'end-1c')
        outputrarfilepath = self.outputrartxtfield.get("1.0", 'end-1c')
        winrarcompressor = WinRARCompressor.WinRARCompressor()
        returneddata = winrarcompressor.compressfile( inputfilepath, outputrarfilepath)
        self.okbtn = Button(self.master, text="OK", command=self.exit)
        self.okbtn.place(x=480, y=200)
        self.compressiontimelbl = Label(self.master, text="Compression Time: %s Sec" % returneddata[0])
        self.compressiontimelbl.place(x=20, y=150)
        self.compressionratiolbl = Label(self.master, text="Compression Ratio: %s " % returneddata[1])
        self.compressionratiolbl.place(x=20, y=175)
