from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

listbox = Listbox(frame, selectmode="extended", height=10)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack()  



root.mainloop()