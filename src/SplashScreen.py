from Tkinter import *

from src.MainFrame import MainFrame


class SplashScreen(Frame):
    def __init__(self, master=None, width=0.4, height=0.2, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()

    def openmainframe(self):
        self.root.withdraw()
        root = Tk()
        app = MainFrame(root)
        app.pack()
        root.mainloop()


root = Tk()
sp = SplashScreen(root)
sp.config(bg="#3366ff")
m = Label(sp, text="LiDAR Data Compression System\n\n\nAhmed Kotb\nA.Kotb@narss.sci.eg")
m.pack(side=TOP, expand=YES)
m.config(bg="#3366ff", justify=CENTER, font=("calibri", 29))
Button(sp, text="Enter", bg='red', command=sp.openmainframe).pack(side=BOTTOM, fill=X)
root.mainloop()
