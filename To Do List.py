from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To Do List Created by Smit')
ws.config(bg='white')
ws.resizable(False,False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(frame,width=25,height=8,font=('arial', 15),bd=3,fg='Black',background='#228B22',activestyle="none",)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(ws,font=('arail', 15),bd=5)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=10)

addTask_btn = Button(button_frame,text='Add Task',font=('times 14'),bg='#808080',padx=10,pady=10, command=newTask,bd=7)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame,text='Delete Task',font=('times 14'),bg='orange',padx=10,pady=10,command=deleteTask,bd=7)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
