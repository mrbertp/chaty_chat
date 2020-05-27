from tkinter import *

PHI = (1 + 5**0.5) / 2


root = Tk()
root.title("Chaty Chat")
WIDTH = int(350)
HEIGHT = int(350 * PHI)
root.geometry(f"{WIDTH}x{HEIGHT}")

messages = []
max_line = 25
lines = list(range(max_line))

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


def send_message(event):
    global messages
    global nonvalid_message
    msg = msg_box.get()
    if msg not in nonvalid_message:
        msg_box.delete(0, END)
        messages.append(msg)
        line = zip(lines, messages)
        if len(messages) > max_line:
            print('límite alcanzado')
            messages.pop(0)
        for f in [user_frame, msg_frame]:
            for c in f.winfo_children():
                c.destroy()
        for l, m in line:
            user_text = Label(user_frame, text=l,
                              bg='black', fg='white', font=("Consolas", 9))
            user_text.grid(row=l, column=0, sticky=E)
            msg_text = Label(msg_frame, text=m,
                             bg='black', fg='white', font=("Consolas", 9))
            msg_text.grid(row=l, column=0, sticky=W)


# BUTTONS FRAME
buttons_frame = Frame(root)
buttons_frame.grid(row=0, column=0, sticky=NSEW, padx=2, pady=2)
button = Button(buttons_frame, text="Adios")
button.pack(fill=BOTH)

# CHAT FRAME

chat_frame = Frame(root, bg='black')
chat_frame.grid(row=1, column=0, sticky=NSEW, padx=2, pady=2)


user_frame = Frame(chat_frame, bg='green', width=70, height=500)
user_frame.grid(row=0, column=0, sticky=NS)

msg_frame = Frame(chat_frame, bg='blue', width=276, height=500)
msg_frame.grid(row=0, column=1, sticky=NS)


# MESSAGE BOX
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

root.update()
chat_height = chat_frame.winfo_height()

root.mainloop()
