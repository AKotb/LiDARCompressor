import os
import tkFileDialog
from Tkinter import *

from src.main import LASHandler


class ClassificationViewer(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        parentlastoolsdir = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\LAStools")
        self.CONST_LASTOOLS_PATH = os.path.join(parentlastoolsdir, "bin")
        self.init_window()

    def init_window(self):
        self.master.title("Classification-LiDAR Compression System")
        self.pack(fill=BOTH, expand=1)

        inputfilelbl = Label(self.master, text="Input File")
        inputfilelbl.place(x=20, y=50)
        self.inputfiletxtfield = Text(self.master, height=1, width=50)
        self.inputfiletxtfield.place(x=100, y=50)
        inputfilebtn = Button(self.master, text="Browse", command=self.selectinputfile)
        inputfilebtn.place(x=520, y=50)

        self.displaylasfileclassesbtn = Button(self.master, text="Display LAS File Classes", command=self.displaylasfileclasses)
        self.displaylasfileclassesbtn.place(x=370, y=100)
        self.cancelbtn = Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=520, y=100)

        self.S = Scrollbar(self.master)
        self.S.pack_forget()
        self.T = Text(self.master, height=400, width=360)
        self.T.pack_forget()

    def exit(self):
        self.master.destroy()

    def selectinputfile(self):
        inputfilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Input File",
                                                          filetypes=(("LAS Files", "*.las"), ("LAZ Files", "*.laz"), ("ASCII Files", "*.txt"), ("All Files", "*.*")))
        self.inputfiletxtfield.delete(1.0, END)
        self.inputfiletxtfield.insert(END, inputfilepath)

    def displaylasfileclasses(self):
        inputfilepath = self.inputfiletxtfield.get("1.0", 'end-1c')
        lashandler = LASHandler.LASHandler()
        lashandler.viewfileinfo(self.CONST_LASTOOLS_PATH, inputfilepath)
        data = inputfilepath.split('.')
        infofilepath = data[0] + "_info.txt"
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        infofile = open(infofilepath, "r")
        self.T.delete(1.0, END)
        classificationfile = open(data[0] + "_classify.txt", "w+")
        for line in infofile:
            if 'unclassified' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'ground' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'low vegetation' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'medium vegetation' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'high vegetation' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'building' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'noise' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'water' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'rail' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'bridge deck' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
            if 'Reserved for ASPRS Definition' in line:
                self.T.insert(END, line)
                classificationfile.write(line)
        infofile.close()
        classificationfile.close()