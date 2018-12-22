from tkinter import*
import ttkCalendar



root = Tk()
root.title("Employee Calendar")
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


fraCalendar = Frame(root, width=700, height=500, relief="raise")
fraCalendar.pack(side=LEFT, fill=Y)

fraKey = Frame(root, width=200, height=300, relief="raise")
fraKey.pack(side=RIGHT, fill=BOTH)

fraKey.grid_rowconfigure(0, weight=1)
fraKey.grid_columnconfigure(0, weight=1)


# ---- Labels ---- #

lbl_key_cur_date = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#5883e6', text="")
lbl_key_cur_date.grid(row=1, column=0)

lbl_name_cur_date = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Current Date")
lbl_name_cur_date.grid(row=1, column=1)

lbl_key_bank_hol = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#e6586f', text="")
lbl_key_bank_hol.grid(row=2, column=0)

lbl_name_bank_hol = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Bank Holiday")
lbl_name_bank_hol.grid(row=2, column=1)

lbl_key_emp_leave = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#58d5e6', text="")
lbl_key_emp_leave.grid(row=3, column=0)

lbl_name_emp_leave = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Employee Leave")
lbl_name_emp_leave.grid(row=3, column=1)


ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(fraKey, anchor=SE, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=5, column=1)


# ---- Buttons ---- #

btn_closeForm = Button(fraKey, width=15, font=('Arial', 20), text="Close", command=close_form)
btn_closeForm.grid(row=5, column=0, rowspan=20)


# ---- Calendar Widget ---- #

cal_empCalendar = ttkCalendar.Calendar(fraCalendar)

cal_empCalendar.pack(fill=BOTH)

# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
