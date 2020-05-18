from tkinter import *

PHI = (1 + 5**0.5) / 2


root = Tk()
root.title("Chaty Chat")
WIDTH = int(350)
HEIGHT = int(350 * PHI)
root.geometry(f"{WIDTH}x{HEIGHT}")

line = 0
username = 'Bert'


def msgbox_focus(event):
    if event.widget == root.nametowidget(msg_box):
        msg_box.delete(0, END)
    elif event.widget != root.nametowidget(msg_box):
        msg_box.delete(0, END)
        msg_box.insert(0, 'Enter to send message')
        root.focus()
    return None


def send_message(event):
    # TODO: do not delete message if you click again in message box while writing
    global line
    msg = msg_box.get()
    if msg not in ['', 'Enter to send message', ' ']:
        msg_box.delete(0, END)
        Label(user_frame, text=f"{msg.split('. ')[0]}:", bg='black', fg='white', relief=SUNKEN).grid(row=line, column=0, sticky=E, padx=2, pady=2)
        Label(msg_frame, text=msg.split('. ')[1], bg='black', fg='white', relief=SUNKEN).grid(row=line, column=0, sticky=W, padx=2, pady=2)
        line += 1


buttons_frame = Frame(root)
buttons_frame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)
button = Button(buttons_frame, text="Adios")
button.pack(fill=BOTH)


chat_frame = Frame(root, bg='red')
chat_frame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2)

user_frame = Frame(chat_frame, bg='green', width=70, height=482)
user_frame.grid(row=0, column=0, sticky=EW, padx=2, pady=2)

msg_frame = Frame(chat_frame, bg='green', width=268, height=482)
msg_frame.grid(row=0, column=1, sticky=EW, padx=2, pady=2)


msgbox_frame = Frame(root)
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
user_frame.grid_columnconfigure(0, weight=1)
msg_frame.grid_columnconfigure(0, weight=2)

user_frame.grid_propagate(False)
msg_frame.grid_propagate(False)


root.mainloop()
