from tkinter import *

PHI = (1 + 5**0.5) / 2


root = Tk()
root.title("Chaty Chat")
WIDTH = int(350)
HEIGHT = int(350 * PHI)
root.geometry(f"{WIDTH}x{HEIGHT}")

line = 0
nonvalid_message = ['', 'Enter to send message', ' ']
user_name = 'Bert'


def msgbox_focus(event):
    if event.widget == root.nametowidget(msg_box):
        if msg_box.get() in nonvalid_message:
            msg_box.delete(0, END)
    elif event.widget != root.nametowidget(msg_box):
        if msg_box.get() in nonvalid_message:
            msg_box.delete(0, END)
            msg_box.insert(0, 'Enter to send message')
            root.focus()
    return None


def send_message(event):
    global line
    msg = msg_box.get()
    if msg not in nonvalid_message:
        msg_box.delete(0, END)
        user_text = Label(user_frame, text=line, bg='black', fg='white').grid(row=line, column=0, sticky=E)
        msg_text = Label(msg_frame, text=msg, bg='black', fg='white').grid(row=line, column=0, sticky=W)
        line += 1
        #print('chat_frame: ' + str(chat_frame.winfo_height()))
        #print('msg_text: ' + str(msg_text.winfo_height()))


buttons_frame = Frame(root)
buttons_frame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)
button = Button(buttons_frame, text="Adios")
button.pack(fill=BOTH)


chat_frame = Frame(root, bg='black')
chat_frame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2)

user_frame = Frame(chat_frame, bg='black', width=70, height=482)
user_frame.grid(row=0, column=0, sticky=EW)

msg_frame = Frame(chat_frame, bg='black', width=268, height=482)
msg_frame.grid(row=0, column=1, sticky=EW)


msgbox_frame = Frame(root)
msgbox_frame.grid(row=2, column=0, sticky=NSEW, padx=2, pady=2)
msg_box = Entry(msgbox_frame, bd=3)
msg_box.pack(expand=1, fill=BOTH, padx=2, pady=2)
msg_box.insert(0, "Enter to send message")


root.bind('<Button-1>', msgbox_focus)
msg_box.bind('<Return>', send_message)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=200)
root.grid_rowconfigure(2, weight=1)
user_frame.grid_columnconfigure(0, weight=1)
msg_frame.grid_columnconfigure(0, weight=2)

user_frame.grid_propagate(False)
msg_frame.grid_propagate(False)


root.mainloop()
