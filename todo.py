import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Todo_list")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!!", message="Add a task")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning(title="Attention!!!", message="Select a task to delete")

def update_task():
    try:
        index_todo = todo_box.curselection()[0]
        updated_task = task_add.get()
        if updated_task != "":
            todo_box.delete(index_todo)
            todo_box.insert(index_todo, updated_task)
            task_add.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Attention!!!", message="Add a task to update")
    except IndexError:
        tkinter.messagebox.showwarning(title="Attention!!!", message="Select a task to update")

def remove_all_tasks():
    todo_box.delete(0, tkinter.END)

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=40)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=todo_box.yview)

task_add = tkinter.Entry(window, width=70)
task_add.pack()

add_task_btn = tkinter.Button(window, text="Add Task", font=("arial", 20, "bold"), background="pink", width=40, command=task_adding)
add_task_btn.pack()

remove_task_btn = tkinter.Button(window, text="Remove Task", font=("arial", 20, "bold"), background="light green", width=40, command=task_removing)
remove_task_btn.pack()

update_task_btn = tkinter.Button(window, text="Update Task", font=("arial", 20, "bold"), background="light blue", width=40, command=update_task)
update_task_btn.pack()

remove_all_tasks_btn = tkinter.Button(window, text="Remove All Tasks", font=("arial", 20, "bold"), background="red", width=40, command=remove_all_tasks)
remove_all_tasks_btn.pack()

window.mainloop()
