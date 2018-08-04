import tkFileDialog
from Tkinter import *

from src.main import ZIP7Compressor


class ZIP7DecompressFileFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Decompress 7Z File using 7-ZIP - LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        input7zlbl = Label(self.master, text="7Z File")
        input7zlbl.place(x=20, y=50)
        self.input7ztxtfield = Text(self.master, height=1, width=50)
        self.input7ztxtfield.place(x=100, y=50)
        input7zbtn = Button(self.master, text="Browse", command=self.select7z)
        input7zbtn.place(x=520, y=50)

        outputfilelbl = Label(self.master, text="Extract Into")
        outputfilelbl.place(x=20, y=100)
        self.outputfiletxtfield = Text(self.master, height=1, width=50)
        self.outputfiletxtfield.place(x=100, y=100)
        outputfilebtn = Button(self.master, text="Browse", command=self.selectoutputfiledir)
        outputfilebtn.place(x=520, y=100)

        self.startdecompressbtn = Button(self.master, text="Start", command=self.decompress7z)
        self.startdecompressbtn.place(x=480, y=200)
        self.canceldecompressbtn = Button(self.master, text="Cancel", command=self.exit)
        self.canceldecompressbtn.place(x=520, y=200)

    def exit(self):
        self.master.destroy()

    def select7z(self):
        input7zfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select 7Z",
                                                        filetypes=(("7Z Files", "*.7z"), ("All Files", "*.*")))
        self.input7ztxtfield.delete(1.0, END)
        self.input7ztxtfield.insert(END, input7zfilepath)

    def selectoutputfiledir(self):
        outputfilepath = tkFileDialog.askdirectory(initialdir="/", title="Select Output File Directory")
        self.outputfiletxtfield.delete(1.0, END)
        self.outputfiletxtfield.insert(END, outputfilepath)

    def decompress7z(self):
        self.canceldecompressbtn.place_forget()
        self.startdecompressbtn.place_forget()
        input7zfilepath = self.input7ztxtfield.get("1.0", 'end-1c')
        outputfilepath = self.outputfiletxtfield.get("1.0", 'end-1c')
        zip7ompressor = ZIP7Compressor.ZIP7Compressor()
        returneddata = zip7ompressor.decompressfile(input7zfilepath, outputfilepath)
        self.okbtn = Button(self.master, text="OK", command=self.exit)
        self.okbtn.place(x=480, y=200)
        self.compressiontimelbl = Label(self.master, text="Decompression Time: %s Sec" % returneddata[0])
        self.compressiontimelbl.place(x=20, y=150)
