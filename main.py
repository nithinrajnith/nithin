
from tkinter import*
def sel():
    selection="you selected the option"+str(var.get())
    Label.config(text=selection)
root=Tk()
var=IntVar()
l1=Label(text="FAVOURITE programming language")
l1.pack()
R1=Radiobutton(root,text="python",variables=var,value=1,command=sel)
R1.pack(anchor=W)
R2=Radiobutton(root,text="C",variable=var,value=2,command=sel)
R2.pack(anchor=W)
R3=Radiobutton(root,text="java",variable=var,value=3,command=sel)
R3.pack(anchor=W)
label=Label(root)
Label.pack()
root.mainloop()
