#Using different properties to specify where a widget and texts to be positioned
#fonts, dimensions, colors- backgrounds and font colors 

from tkinter import *

tk = Tk()
tk.config(background = "black")
tk.geometry("745x450")

label1 = Label(tk, text = "Label1", 
               bg="red", fg="white", 
               height = 4, width=20,
               font=("comic sans ms", 15, "bold"))
label1.grid(row = 0, column = 0)

label2 = Label(tk, text = "Label2", 
               bg="blue", fg="white", 
               height = 4, width=20,   
               font=("comic sans ms", 15, "bold"))
label2.grid(row = 0, column = 1)

label3 = Label(tk, text = "    Label3", 
               bg="orange", fg="white", 
               height = 4, width=20,
               font=("comic sans ms", 15, "bold"))
label3.grid(row = 0, column = 2)

label4 = Label(tk, text = "Label4", 
               bg="steel blue", fg="white", 
               height = 4, width=40,
               font=("comic sans ms", 15, "bold"))
label4.grid(row = 1, column = 0, columnspan = 2, ipadx= 3)

label5 = Label(tk, text = "Label5", 
               bg="pink", fg="white", 
               height = 4, width=20,
               font=("comic sans ms", 15, "bold"))
label5.grid(row = 1, column = 2)

tk.mainloop()