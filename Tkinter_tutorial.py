from tkinter import *


def myClick(complement="eres guapo"):

    message = f"Hello {entry.get()} {complement}"
    entry.delete(0, END)
    myLabel.config(text=message)


root = Tk()
root.title("Pype Master v0.2")

# LABELS
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Pipo is alive")
myLabel3 = Label(root, text="Pipo is dead")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

# BUTTONS
myButton = Button(root,
                  text="Click Me",
                  pady=30,
                  command=lambda: myClick("augh"),
                  fg="red",
                  bg="black")

myButton.grid(row=2, column=0)

# INPUT FIELDS

myLabel = Label(root, text="")
myLabel.grid(row=3, column=1)

entry = Entry(root,
              width=20,
              bg="white",
              fg="red",
              borderwidth=4)

entry.grid(row=2, column=2)
entry.insert(0, "Your name?")


# main loop of root window
root.mainloop()
