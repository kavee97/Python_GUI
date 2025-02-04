import tkinter as tk

#create a window
root = tk.Tk()
width,height=800,400
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()

left=int(screen_w/2-width/2)
top=int(screen_h/2-height/2)

root.geometry(f'{width}x{height}+{left}+{top}') #widthxheight+left+top
root.title("Dashboard")

#root.iconbitmap("OIP.ico")
root.resizable(False,False)

#run the window
root.mainloop()