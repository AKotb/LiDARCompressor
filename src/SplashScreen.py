import Tkinter as Tk

from src.MainFrame import MainFrame


class SplashScreen(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("Home-LiDAR Compression System")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        lbl1 = Tk.Label(root, text="Welcome to LiDAR Data Compression System", bg='red')
        lbl1.place(x=110, y=120)
        lbl1.config(font=("calibri", 16))
        lbl2 = Tk.Label(root, text="Ahmed Kotb", bg='red')
        lbl2.place(x=240, y=160)
        lbl2.config(font=("calibri", 16))
        lbl3 = Tk.Label(root, text="FCI_NARSS", bg='red')
        lbl3.place(x=245, y=200)
        lbl3.config(font=("calibri", 16))
        btn = Tk.Button(root, text="Enter to System", bg='red', command=self.openFrame)
        btn.pack(side=Tk.BOTTOM, fill=Tk.X, padx=10)
        btn.config(font=("calibri", 16))

    def hide(self):
        self.root.withdraw()

    def openFrame(self):
        self.hide()
        root = Tk.Tk()
        root.geometry("600x400")
        app = MainFrame(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("600x400+100+100")
    root.overrideredirect(1)
    root.config(bg="blue")
    app = SplashScreen(root)
    root.mainloop()
