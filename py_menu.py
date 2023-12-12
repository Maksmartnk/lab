from tkinter import *
root = Tk()

def hello():
    print("Привіт!")

menubar = Menu(root)
root.config(menu=menubar)

menubar.add_command(label="Привіт!", command=hello)
menubar.add_command(label="Вийти", command=quit)

root.mainloop()