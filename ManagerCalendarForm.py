from tkinter import*
import ttkCalendar
from tkinter import ttk
import os


root = Tk()
root.title("Manager Calendar")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# ---- Variables ---- #

listbox_headers = ('EmpID', 'Employee')
# test data
request_id = 1234
emp_id = 1100
leave_date = "13/06/19"
submission_date = "03/05/19"
leave_type = "Holiday"
emp_comment = "I am going on holiday"
signed_off = "No"
mgr_comment = "All employees must attend on this date"
mgr_name = "Steven Tasks"
emp_name = "Abel Maclead"

# ---- Methods ---- #


def close_form ():
    root.destroy()

def show_cal ():
    lbl_cal_info.configure(text=mgr_name + "'s Calendar")

def open_cal_options ():
    print("Opening Calendar Options Form")
    os.startfile(r'CalendarOptionsForm.py')

# ---- Frame ---- #

fraListBox = Frame(root, width=200, height=500, relief="raise")
fraListBox.pack(side=LEFT, fill=BOTH)

fraCalendar = Frame(root, width=500, height=500, relief="raise")
fraCalendar.pack(side=LEFT, fill=BOTH)

fraKey = Frame(root, width=200, height=300, relief="raise")
fraKey.pack(side=RIGHT, fill=BOTH)

fraKey.grid_rowconfigure(0, weight=1)
fraKey.grid_columnconfigure(0, weight=1)


# ---- Labels ---- #

lbl_select_cal = Label(fraListBox, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Select Calendar")
lbl_select_cal.pack()

lbl_cal_info = Label(fraCalendar, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text=emp_name + "'s Calendar")
lbl_cal_info.pack()


lbl_key_cur_date = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#5883e6', text="")
lbl_key_cur_date.grid(row=0, column=0)

lbl_name_cur_date = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Current Date")
lbl_name_cur_date.grid(row=0, column=1)

lbl_key_bank_hol = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#e6586f', text="")
lbl_key_bank_hol.grid(row=1, column=0)

lbl_name_bank_hol = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Bank Holiday")
lbl_name_bank_hol.grid(row=1, column=1)

lbl_key_emp_leave = Label(fraKey, justify=LEFT, anchor=W, width=4, bg='#58d5e6', text="")
lbl_key_emp_leave.grid(row=2, column=0)

lbl_name_emp_leave = Label(fraKey, justify=LEFT, anchor=W, width=20, font=('Arial', 16), text="Employee Leave")
lbl_name_emp_leave.grid(row=2, column=1)

ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(fraKey, anchor=SE, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=5, column=1)


# ---- Buttons ---- #

btn_show_calendar = Button(fraKey, width=15, font=('Arial', 20), text="Show My Calendar", command=show_cal)
btn_show_calendar.grid(row=3, column=1)

btn_cal_opt = Button(fraKey, width=15, font=('Arial', 20), text="Calendar Options", command=open_cal_options)
btn_cal_opt.grid(row=4, column=1)

btn_closeForm = Button(fraKey, width=15, font=('Arial', 20), text="Close", command=close_form)
btn_closeForm.grid(row=5, column=0, rowspan=20)



# ---- Listbox ---- #

lst_cal_select = ttk.Treeview(fraListBox, columns=listbox_headers, show="headings", height=26)
lst_cal_select.pack(side=TOP)

lst_cal_select.heading('#1', text='EmpID', anchor=CENTER)
lst_cal_select.heading('#2', text='Employee', anchor=CENTER)

lst_cal_select.column('#1', stretch=YES, minwidth=50, width=100)
lst_cal_select.column('#2', stretch=YES, minwidth=50, width=100)

lst_cal_select.insert('', 'end', values=("#1005", "Donette Foller"))
lst_cal_select.insert('', 'end', values=("#1012", "Abel Maclead"))
lst_cal_select.insert('', 'end', values=("#1208", "Steven Tasks"))



# ---- Calendar Widget ---- #

cal_empCalendar=ttkCalendar.Calendar(fraCalendar)

cal_empCalendar.pack()

# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
