from tkinter import*
from tkinter.ttk import*
screen=Tk()
screen.title("Math Cheat😈🧿🖤")
Title=Label(screen,text="Math Cheat😈🖤🧿🖤😈",font=("Brush Script Std",20,"bold"))
Title.grid(row=1,column=0,padx=140,pady=20)
Caption=Label(screen,text="Number & Range",font=("Brush Script Std",13))
Caption.grid(row=2,column=0,pady=0)
Number=IntVar()
numbers=Combobox(screen,textvariable=Number,width=7)
numbers.place(x=370,y=75)
numbers["values"]=tuple(range(101))
option=IntVar()
radio10=Radiobutton(screen,text="10",variable=option,value=10)
radio10.place(x=430,y=75)
radio20=Radiobutton(screen,text="20",variable=option,value=20)
radio20.place(x=430,y=100)
radio30=Radiobutton(screen,text="30",variable=option,value=30)
radio30.place(x=430,y=120)
def display_table():
    tables=""
    for i in range(option.get()+1):
        tables+=str(i)+"X"+str(Number.get())+"="+str(Number.get()*i)+"\n"
    table.configure(text=tables)
display=Button(screen,text="generate table",command=display_table)
display.place(x=370,y=145)
table=Label(screen,font=("Brush Script Std",13))
table.place(x=370,y=160)
screen.mainloop()
