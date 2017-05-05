import tkinter, time
from tkinter.constants import *
from tkinter import messagebox
class Window():
    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title("Clarizen Tasks")
        self.frame = tkinter.Frame(self.tk, borderwidth=2)
        self.finish_frame = tkinter.Frame(self.tk, borderwidth=2)
        self.frame.grid()
        self.finish_frame.grid(sticky="e")
        self.tk.rowconfigure(0, pad=10)
        self.tk.columnconfigure(0, pad=10)
        self.task_count = 1

class Task():
    def __init__(self, name):
        self.name = name
        self.row = window.task_count
        window.task_count += 1
        self.total_time = 0
        self.start_time = 0
        self.label = tkinter.Label(window.frame, text=self.name)
        self.start_button = tkinter.Button(window.frame, text="Start", command=self.start)
        self.end_button = tkinter.Button(window.frame, text="End", command=self.end, state="disabled")
        self.time_display = tkinter.Label(window.frame, text="0:0:0")
        self.label.grid(column=0, row=self.row, sticky="w")
        self.start_button.grid(column=1, row=self.row, padx=5, pady=5)
        self.end_button.grid(column=2, row=self.row, padx=5, pady=5)
        self.time_display.grid(column=3, row=self.row, padx=5, pady=5)
    def start(self):
        self.start_time = time.time()
        self.end_button.config(state="active")
        self.start_button.config(state="disabled")
    def end(self):
        time_spent = (time.time() - self.start_time)
        self.total_time += time_spent
        minutes, seconds = divmod(self.total_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_string = "%d:%d:%d" % (hours, minutes, seconds)
        self.time_display = tkinter.Label(window.frame, text=time_string)
        self.time_display.grid(column=3, row=self.row)
        self.start_button.config(state="active")
        self.end_button.config(state="disabled")

def create_title_row():
    title = tkinter.Label(window.frame, text="Task")
    title.grid(pady=5, sticky="w")
    new_task_name = tkinter.StringVar()
    new_task_input = tkinter.Entry(window.frame, textvariable=new_task_name)
    new_task_input.grid(row=0, column=1, columnspan=2)
    add_button = tkinter.Button(window.frame, text="+", command=lambda: create_task(new_task_name))
    add_button.grid(row=0, column=3, stick="nwse")

def create_task(new_task_name):
    if new_task_name.get()!="":
        new_task = Task(new_task_name.get())
        new_task_name.set("")
    else:
        messagebox.showinfo(message="Cannot create a task without a name.")

def create_finish_button():
    finish_button = tkinter.Button(window.finish_frame, text="Finish", command=exit_confirm)
    finish_button.grid(column=3, padx=5, pady=5)

def exit_confirm():
    result = messagebox.askyesno(message="Are you sure you want to quit?", icon="question", title="Quit")
    if result:
        window.tk.destroy()
        
window = Window()
create_title_row()
SendPro_Testing = Task("SendPro Testing")
SmartLink = Task("SmartLink Program Construction")
create_finish_button()
window.tk.mainloop()
