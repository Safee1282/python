# from tkinter import *
# root=Tk()
# root.title('Number Pad')
# root.geometry('250x300')
# frame=Frame(master=root,height=200,width=360,bg='black')
# nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
# for i in range(4):
#     root.columnconfigure(i,weight=1,minsize=75)
#     root.rowconfigure(i,weight=1,minsize=50)
#     for j in range(0,3):
#         frame=Frame(
#             master=root,
#             relief=SUNKEN,
#             borderwidth=1
#         )
#         frame.grid(row=i,column=j)
#         label=Label(master=frame,text=nums[i][j],bg='black')
#         label.pack(padx=3,pady=3)


from tkinter import *
root=Tk()
root.title('Login App')
root.geometry('400x400')
frame=Frame(master=root,height=200,width=360,bg='black')  

lbl1=Label(frame,text="Full Name ",bg='black',fg='white',width=12)
lbl2=Label(frame,text="Email ID ",bg='black',fg='white',width=12)
lbl3=Label(frame,text="Enter Password ",bg='black',fg='white',width=12)

name_entry=Entry(frame)
mail_entry=Entry(frame)
pass_entry=Entry(frame,show='*')

def display():
    name=name_entry.get
    greet="Hey "+ name
    message="\n congratulations for your new account "
    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(bg='white',fg='black')
btn=Button(text="Create Account ", command=display,bg="red")
frame.place(x=20,y=0)    
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
mail_entry.place(x=150,y=80)
lbl3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)