import tkinter as tk
from tkinter import ttk
root = tk.Tk()

root.title("Widget")
root.geometry("800x400")
root.resizable(False,False)

def button_click_func():
    #entry_value=entry.get()
    lable.configure(text=entry.get())
    btn2.configure(state="disable")
#create entry field
entry = ttk.Entry(root)
entry.pack()

#btn1=tk.Button(root,text="Click me")#old type
#btn1.pack()

#new type
btn2=ttk.Button(root, text="Click me", command=button_click_func)
btn2.pack()

lable=ttk.Label(root)
lable.pack()


root.mainloop()