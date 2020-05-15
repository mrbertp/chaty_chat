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
myLabel2.grid(row=1, column=3)
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

# ICONS

pass

# STATUS BAR

status = Label(root,
               text="pype is eugh",
               bd=2,
               relief=SUNKEN,
               anchor=E)

status.grid(row=4, column=0, columnspan=4, sticky=W+E)

# FRAMES

frame = LabelFrame(root, text=" this is a frame ", padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

button1 = Button(frame, text="Here")
button1.grid(row=0, column=0)

# RADIO BUTTONS

var = IntVar()
var.set(0)


def clicked(value):
    mylab = Label(frame, text=var.get())
    mylab.grid(row=0, column=1)


rb1 = Radiobutton(frame,
                  text="Option 1",
                  variable=var,
                  value=1,
                  command=lambda: clicked(var.get()))
rb2 = Radiobutton(frame,
                  text="Option 2",
                  variable=var,
                  value=2,
                  command=lambda: clicked(var.get()))

rb1.grid(row=0, column=2)
rb2.grid(row=0, column=3)

modes = [
    ("a", "a"),
    ("b", "b"),
    ("c", "c"),
    ("d", "d")
]

pizza = StringVar()
pizza.set("pepperoni")

for text, mode in modes:
    pb = Radiobutton(frame, text=text, variable=pizza, value=mode)
    pb.grid(row=1, column=0)

# main loop of root window
root.mainloop()
