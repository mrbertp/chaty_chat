from tkinter import *

PHI = (1+5**0.5)/2


root = Tk()
root.title("Chaty Chat")
WIDTH = int(350)
HEIGHT = int(350*PHI)
root.geometry(f"{WIDTH}x{HEIGHT}")

line = 0


def msgbox_focus(event):
    if event.widget == root.nametowidget(msg_box):
        msg_box.delete(0, END)
    elif event.widget != root.nametowidget(msg_box):
        msg_box.delete(0, END)
        msg_box.insert(0, 'Enter to send message')
        root.focus()
    return None


def send_message(event):
    global line
    msg = msg_box.get()
    if msg not in ['', 'Enter to send message', ' ']:
        msg_box.delete(0, END)
        Label(chat_frame, text=msg).grid(row=line, column=0, sticky=W)
        line += 1


buttons_frame = LabelFrame(root)
buttons_frame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)
button = Button(buttons_frame, text="Adios")
button.pack(fill=BOTH)


chat_frame = LabelFrame(root)
chat_frame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2)


msgbox_frame = LabelFrame(root)
msgbox_frame.grid(row=2, column=0, sticky=NSEW, padx=2, pady=2)
msg_box = Entry(msgbox_frame, bd=3)
msg_box.pack(expand=1, fill=BOTH, padx=2, pady=2)
msg_box.insert(0, "Enter to send message")


root.bind('<Button-1>', msgbox_focus)
root.bind('<Return>', send_message)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=200)
root.grid_rowconfigure(2, weight=1)


root.mainloop()
