import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import ttk
from db import initialize_database, load_tasks, add_task, edit_task, delete_task


# Функция для загрузки задач в Listbox
def load_tasks_listbox():
    tasks = load_tasks()
    list_box_1.delete(0, tk.END)
    for task in tasks:
        list_box_1.insert(tk.END, task)

# Функция для добавления новой задачи
def add_text():
    text = entry_1.get()
    add_task(text)
    load_tasks_listbox()
    entry_1.delete(0, tk.END)

# Функция для редактирования выбранной задачи
def edit_text():
    field = list_box_1.curselection()
    index = field[0]
    text = list_box_1.get(index)
    new_value = askstring(
        "Edit", "Add text:", 
        initialvalue=text,)

    edit_task(text, new_value)
    load_tasks_listbox()

# Функция для удаления выбранной задачи
def del_text():
    field = list_box_1.curselection()
    index = field[0]
    text = list_box_1.get(index)
    delete_task(text)
    list_box_1.delete(index)

# Инициализация базы данных при запуске приложения
initialize_database()

# Создание главного окна Tkinter
window = tk.Tk()
window.title("To-Do List")
window.geometry('800x600')
photo = tk.PhotoImage(file='image/iconsnew.png')
window.iconphoto(False, photo)

# Создание фреймов
frame_1 = tk.Frame(window, padx=20, pady=40,)
frame_1.pack()

frame_2 = tk.Frame(window, padx=5, pady=5, bg='#c9dee0')
frame_2.place(relx=.5, rely=.4, anchor="c")

# Создание элементов интерфейса (Label, Entry, Listbox, Scrollbar, Button)
label_1 = tk.Label(
    frame_1, text="Daily Tasks",
    font=("Arial", 25),
)
label_1.pack(pady=(0, 300),)

entry_1 = tk.Entry(
    frame_2, width=85,
    font=("Arial", 10),
)
entry_1.pack(pady=(0,2))

list_box_1 = tk.Listbox(
    frame_2, width=75,
    height=10,
    font=("Arial", 10),
)
list_box_1.pack(pady=(0, 10), ipady=20,
                side='left', fill='both', expand=1)

scrollbar = ttk.Scrollbar(frame_2,orient="vertical", command = list_box_1.yview)
scrollbar.pack(side='right', fill='y', pady=(1, 10))
list_box_1["yscrollcommand"]=scrollbar.set

button_1 = tk.Button(
    frame_1, text='Add',
    bg='#2796c4', font=("Arial", 10),
    width=60, height=1,
    activebackground='#b84219',
    command=add_text,
)
button_1.pack(pady=(0, 20),)

button_2 = tk.Button(
    frame_1, text='Edit',
    bg='#2796c4', font=("Arial", 10),
    width=60, height=1,
    activebackground='#b84219',
    command=edit_text,
)
button_2.pack(pady=(0, 20),)

button_3 = tk.Button(
    frame_1, text='Delete',
    bg='#2796c4', font=("Arial", 10),
    width=60, height=1,
    activebackground='#b84219',
    command=del_text,
)
button_3.pack()

# Вызов Функции для загрузки задач в Listbox
load_tasks_listbox()

window.mainloop()
