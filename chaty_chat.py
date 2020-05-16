from tkinter import *

PHI = (1+5**0.5)/2

root = Tk()
root.title("Chaty Chat")
root.geometry(f"{int(350)}x{int(350*PHI)}")


def msgbox_focus(event):
    print(".!", event.widget)
    if str(event.widget) == ".!entry":
        print("pipo")
        message_box.delete(0, END)
    elif str(event.widget) != ".!entry":
        message_box.delete(0, END)
        message_box.insert(0, "Aquí tu mensaje")
    return None


message_box = Entry(root)
message_box.insert(0, "Aquí tu mensaje")
message_box.pack(padx=5,
                 pady=5,
                 side=BOTTOM,
                 fill=BOTH)
root.bind("<Button-1>", msgbox_focus)


root.mainloop()
