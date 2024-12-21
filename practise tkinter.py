from tkinter import *
tk =Tk()


tk.geometry ("500x500")
tk.config (background ="pink")
tk.title("choose a smiley")


heading = Label (tk , text = "how is your day going on ? " , bg= "lavender" , fg="IndianRed",
                padx=50 ,pady=50 , bd=10 , relief="ridge"  )
heading.grid(row=0,column=0,columnspan=2,padx=10,pady=20)


heading1= Label (tk , text = "smile with a smiley " , bg= "yellow" , fg="IndianRed",
                padx=50 ,pady=50 , bd=10 , relief="ridge"  )
heading1.grid(row=2,column=0,columnspan=2,padx=10,pady=20)


button1 =Button  (tk ,text="smile!" , command=tk.destroy,font=("Arial",12) ,
                 fg="red",bg="white",width=4,height=1,relief="ridge" ,
                 state="active",padx=20 ,pady=20)
button1.grid(row=4,column=0,columnspan=2,padx=2,pady=2)

button2 =Button  (tk ,text="laugh!" , command=tk.destroy,font=("Arial",12) ,
                 fg="red",bg="white",width=4,height=1,relief="ridge" ,
                 state="active",padx=20 ,pady=20)
button2.grid(row=4,column=1,columnspan=4,padx=2,pady=2)


button3 =Button  (tk ,text="giggle" , command=tk.destroy,font=("Arial",12) ,
                 fg="red",bg="white",width=4,height=1,relief="ridge" ,
                 state="active",padx=20 ,pady=20)
button3.grid(row=4,column=2,columnspan=6,padx=2,pady=2)
tk.mainloop()

