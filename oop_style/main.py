import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import ttk


class ToDoListApp:
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do List")
        self.window.geometry('800x600')
        photo = tk.PhotoImage(file='image/iconsnew.png')
        self.window.iconphoto(False, photo)
        self.create_gui()
    
    def create_gui(self):
        self.frame_1 = tk.Frame(self.window, padx=20, pady=40)
        self.frame_1.pack()

        self.frame_2 = tk.Frame(self.window, padx=5, pady=5, bg='#c9dee0')
        self.frame_2.place(relx=.5, rely=.4, anchor="c")

        self.label_1 = tk.Label(
            self.frame_1, text="Daily Tasks",
            font=("Arial", 25),
        )
        self.label_1.pack(pady=(0, 300))

        self.entry_1 = tk.Entry(
            self.frame_2, width=85,
            font=("Arial", 10),
        )
        self.entry_1.pack(pady=(0, 2))

        self.list_box_1 = tk.Listbox(
            self.frame_2, width=75,
            height=10,
            font=("Arial", 10),
        )
        self.list_box_1.pack(pady=(0, 10), ipady=20, side='left', fill='both', expand=1)

        self.scrollbar = ttk.Scrollbar(self.frame_2, orient="vertical", command=self.list_box_1.yview)
        self.scrollbar.pack(side='right', fill='y', pady=(1, 10))
        self.list_box_1["yscrollcommand"] = self.scrollbar.set

        self.button_1 = tk.Button(
            self.frame_1, text='Add',
            bg='#2796c4', font=("Arial", 10),
            width=60, height=1,
            activebackground='#b84219',
            command=self.add_text,
        )
        self.button_1.pack(pady=(0, 20))

        self.button_2 = tk.Button(
            self.frame_1, text='Edit',
            bg='#2796c4', font=("Arial", 10),
            width=60, height=1,
            activebackground='#b84219',
            command=self.edit_text,
        )
        self.button_2.pack(pady=(0, 20))

        self.button_3 = tk.Button(
            self.frame_1, text='Delete',
            bg='#2796c4', font=("Arial", 10),
            width=60, height=1,
            activebackground='#b84219',
            command=self.del_text,
        )
        self.button_3.pack()

    def add_text(self):
        text = self.entry_1.get()
        self.list_box_1.insert(tk.END, text)
        self.entry_1.delete(0, tk.END)

    def edit_text(self):
        field = self.list_box_1.curselection()
        index = field[0]
        text = self.list_box_1.get(index)
        new_value = askstring("Edit", "Add text:", initialvalue=text)
        self.list_box_1.delete(index)
        self.list_box_1.insert(index, new_value)

    def del_text(self):
        field = self.list_box_1.curselection()
        self.list_box_1.delete(field)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
