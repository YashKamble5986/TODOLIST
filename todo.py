from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do_List")
        self.root.geometry("650x410+300+150")

        self.label = Label(
            self.root,
            text="To-Do-List-App",
            font=("ariel", 25, "bold"),
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )

        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(
            self.root,
            text="Add Task",
            font=("ariel", 18, "bold"),
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )

        self.label2.place(x=40, y=54)

        self.label3 = Label(
            self.root,
            text="Task",
            font=("ariel", 18, "bold"),
            width=10,
            bd=5,
            bg="orange",
            fg="black",
        )

        self.label3.place(x=325, y=54)

        self.main_text = Listbox(
            self.root,
            height=9,
            width=23,
            bd=5,
            font=("ariel", 20, "bold"),
        )

        self.main_text.place(x=280, y=100)

        self.text = Text(
            self.root,
            height=2,
            width=30,
            bd=5,
            font=("ariel", 10, "bold"),
        )

        self.text.place(x=20, y=120)

        # ================================= Add task ==========================

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)

            with open("data.txt", "w") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as file:
                new_f = file.readlines()
                file.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        file.write(line)
                file.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button = Button(
            self.root,
            text="Add",
            font=("serif", 20, "bold italic"),
            width=10,
            bd=5,
            bg="orange",
            fg="black",
            command=add,
        )

        self.button.place(x=30, y=180)
        
        self.button2 = Button(
            self.root,
            text="Delete",
            font=("serif", 20, "bold italic"),
            width=10,
            bd=5,
            bg="orange",
            fg="black",
            command=delete,
        )

        self.button2.place(x=30, y=280)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
