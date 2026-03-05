from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('main')
root.geometry('400x400')

def topwin():
    top = Toplevel()
    top.title("toplevel")
    top.geometry('400x400')
    
    Label = Label(top, text= "this is the toplevel window")
    Label.pack()

root.mainloop()

l = Label(root, text = "this is the main window")
btn = Button(root, text = "click here to open another window", command = topwin)

l.pack()
btn.pack()
