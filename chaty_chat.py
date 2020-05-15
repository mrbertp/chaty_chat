from tkinter import *

PHI = (1+5**0.5)/2

root = Tk()
root.title("Chaty Chat")
root.geometry(f"{int(350)}x{int(350*PHI)}")

message_box = Entry(root, text="Aquí tu mensaje")
message_box.pack(padx=5, pady=5, side=BOTTOM, fill=BOTH)

root.mainloop()
