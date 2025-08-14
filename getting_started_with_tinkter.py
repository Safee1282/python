# from tkinter import * 

# window= Tk()
# window.title('geometry dash')
# window.geometry('400x300')
# window.mainloop() 

from tkinter import *
from datetime import date

a=Tk()
a.title('hello widgets')
a.geometry('400x300')
lbl= Label(text="read carefully",fg="green",bg="orange",height=3,width=300)
name_lbl= Label(text="full name", bg="pink")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message 
    message="Welcome to the application!!\nTodays date is : "
    greet="Hello" + name +"\n"


    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
btn=Button(text="Begin",command=display , height=1 , bg="yellow", fg="dark green")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()    
text_box.pack()

a.mainloop()