from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk
import datetime
import calendar


now = datetime.datetime.now()


root = Tk()
root.title("Leave Request Form")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 550
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



# ---- Variables ----

day_of_week = calendar.day_abbr[now.weekday()]
day = now.day
month = calendar.month_name[now.month]
year = now.year
half_day=0 #0 for full day, 1 for half day

# test data
num_days = 15
request_id = 1234
emp_id = 1011

# ---- Methods ----


def submit_request ():
    message_box.showinfo("", "Leave Request Submitted")
    root.destroy()


def cancel_request():
    print("Leave Request Cancelled")
    root.destroy()


# ---- Frame ----


TopLabels = Frame(root, width=900, height=400, relief="raise")
TopLabels.pack(side=TOP, padx=20)

TopLabels.grid_rowconfigure(0, weight=1)
TopLabels.grid_columnconfigure(0, weight=1)

Options = Frame(root, width=450, height=180, relief="raise")
Options.pack(side=TOP, fill=BOTH, expand=YES)

Options.grid_rowconfigure(0, weight=1)
Options.grid_columnconfigure(0, weight=1)

Buttons = Frame(root, width=800, height=180, relief="raise")
Buttons.pack(side=LEFT, fill=BOTH, expand=YES)

Buttons.grid_rowconfigure(0, weight=1)
Buttons.grid_columnconfigure(0, weight=1)

Logo = Frame(root, width=100, height=180, relief="raise")
Logo.pack(side=RIGHT, fill=BOTH, expand=YES)

Logo.grid_rowconfigure(0, weight=1)
Logo.grid_columnconfigure(0, weight=1)

# ---- Labels ---- #

lbl_title = Label(TopLabels, justify=LEFT, anchor=W, width=100, font=('Arial', 20), text="You currently have " + str(num_days) + " days of leave remaining.\n\n" + "Request ID: #" + str(request_id) + "\nEmployee ID: " + str(emp_id))
lbl_title.grid(row=0, column=0)


mini_calendar = PhotoImage(file="calendar.png")
pic_mini_calendar = Label(TopLabels, anchor=NE, image=mini_calendar)

pic_mini_calendar.grid(row=0, column=3)


ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(Logo, anchor=SE, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=0, column=0)


lbl_current_date = Label(TopLabels, width=11, bg="#fff", font=('Arial', 15), text=day_of_week + " " + str(day) + "\n" + month + "\n" + str(year))
lbl_current_date.grid(row=0, column=3)

lbl_leave_date = Label(Options, width=11, font=('Arial', 20), text="Leave Date: ", justify=LEFT)
lbl_leave_date.grid(row=0, column=0)

lbl_comments = Label(Options, width=11, font=('Arial', 20), text="Comments: ", justify=LEFT)
lbl_comments.grid(row=0, column=2)

lbl_leave_type = Label(Options, width=11, font=('Arial', 20), text="Leave Type: ", justify=LEFT)
lbl_leave_type.grid(row=2, column=0)


# ---- Buttons ---- #

btn_submit = Button(Buttons, width=15, font=('Arial', 20), text="Submit", command=submit_request)
btn_submit.grid(row=0, column=0, padx=2)

btn_cancel = Button(Buttons, width=15, font=('Arial', 20), text="Cancel", command=cancel_request)
btn_cancel.grid(row=0, column=1, padx=2)

# ---- Combo-boxes ---- #

cmb_date_picker = ttk.Combobox(Options, width=15, font=('Arial', 20))
cmb_date_picker['values'] = "peekaboo"
cmb_date_picker.grid(row=0, column=1)

cmb_leave_type = ttk.Combobox(Options, width=15, font=('Arial', 20))
cmb_leave_type['values'] = ("Holiday", "Paternity", "Emergency", "Sickness", "Bereavement")
cmb_leave_type.grid(row=2, column=1)

# ---- Multi-Line Text Box ---- #

txt_comments = Text(Options, width=20, height=5, font=('Arial', 20))
txt_comments.grid(row=0, column=3, padx=2)

# ---- Radio Buttons ---- #

opt_full_day = ttk.Radiobutton(Options, width=20, variable=half_day, value=0, text="Full Day")
opt_full_day.grid(row=1, column=0, padx=2)


opt_half_day = ttk.Radiobutton(Options, width=20, variable=half_day, value=1, text="Half Day")
opt_half_day.grid(row=1, column=1, padx=2)


# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
