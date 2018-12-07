from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk


root = Tk()
root.title("Leave Policy Viewer")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# ---- Variables ---- #

policy_path = "leave_policy.txt"

# test data

# ---- Methods ---- #


def close_form ():
    root.destroy()

# ---- Frame ---- #


Policy = Frame(root, width=900, height=350, relief="raise")
Policy.pack(side=TOP, padx=20)

CloseButton = Frame(root, width=900, height=150, relief="raise")
CloseButton.pack(side=BOTTOM)

# ---- Buttons ---- #

btn_close = Button(CloseButton, width=15, font=('Arial', 20), text="Close", command=close_form)
btn_close.pack(side=RIGHT,  anchor=SE)

# ---- Text Boxes ---- #

txt_policy = Text(Policy, width=76, height=23, font=('Arial', 15))
txt_policy.pack(side=LEFT, anchor=NW)
txt_policy.insert(END, open(policy_path).read())
txt_policy.configure(state=DISABLED)
txt_scroll = ttk.Scrollbar(Policy, orient="vertical", command=txt_policy.yview)

txt_policy.configure(yscrollcommand=txt_scroll.set)

txt_scroll.pack(side=RIGHT, anchor=E, fill="y",)


# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
