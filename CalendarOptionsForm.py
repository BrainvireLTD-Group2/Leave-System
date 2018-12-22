from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk
import sqlite3


root = Tk()
root.title("Calendar Options Form")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



# ---- Variables ----
listbox_headers = ('RequestID', 'Date', 'Signed Off')


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
date_name = "TestHoliday"
date_to_remove = "01/02/19"

# ---- Methods ----


def add_date():

    date_name_to_add = txt_date_name.get("1.0", END)
    date_to_add = "DATE"

    result = message_box.askquestion("Add date", "Are you sure you want to add bank holiday ''" + str(date_name_to_add) + "'' on " + str(date_to_add) + "?", icon='warning')

    if result == 'yes':
        message_box.showinfo("", str(txt_date_name) + "has been successfully added!")
        print("New holiday ''" + str(date_name_to_add) + "'' on " + str(date_to_add) + " added  by " + mgr_name)
    else:
        print("New Holiday Date creation canceled")


def remove_date():
    date_name_to_remove = "DATE_NAME"
    date_to_remove = "DATE"

    result = message_box.askquestion("Add date",
                                     "Are you sure you want to remove bank holiday ''" + str(date_name_to_remove) + "'' on " + str(date_to_remove) + "?",
                                     icon='warning')

    if result == 'yes':
        message_box.showinfo("", date_name_to_remove + "has been successfully removed.")
        print("''" + str(date_name_to_remove) + "'' on " + str(date_to_remove) + " removed  by " + mgr_name)
    else:
        print("Holiday Date deletion canceled")


def remove_all_bank_holidays():

    result = message_box.askquestion("Remove All Bank Holidays", "Are you sure you want to remove ALL bank holidays from the calendar?", icon='warning')

    if result == 'yes':
        message_box.showinfo("", "All Bank Holidays Removed")
        print("All Bank Holidays Removed by " + mgr_name)
    else:
        print("All Bank Holiday Removal Canceled")


# ---- Frame ----


fraBankHol = Frame(root, width=900, height=150, relief="raise")
fraBankHol.pack(side=TOP, anchor=N)

fraAddRemove = Frame(root, width=900, height=200, relief="raise")
fraAddRemove.pack(side=TOP, anchor=N, fill=BOTH)

fraAddDate = Frame(fraAddRemove, width=350, height=200, bd=6, relief="raise")
fraAddDate.pack(side=LEFT, anchor=CENTER)

fraAddDate.grid_rowconfigure(0, weight=0)
fraAddDate.grid_columnconfigure(0, weight=0)

fraRemoveDate = Frame(fraAddRemove, width=350, height=200, bd=6, relief="raise")
fraRemoveDate.pack(side=RIGHT, anchor=CENTER)

fraRemoveDate.grid_rowconfigure(0, weight=0)
fraRemoveDate.grid_columnconfigure(0, weight=0)

fraAnualRollover = Frame(root, width=900, height=150, relief="raise")
fraAnualRollover.pack(side=TOP, anchor=N)

fraAnualRollover.grid_rowconfigure(0, weight=0)
fraAnualRollover.grid_columnconfigure(0, weight=0)


# ---- Labels ---- #

lbl_bankhol = Label(fraBankHol, justify=LEFT, anchor=W, width=100, font=('Arial', 20), text="Bank Holiday Date Options")
lbl_bankhol.pack()

lbl_add_date = Label(fraAddDate, justify=LEFT, anchor=W, width=10, font=('Arial', 15), text="Add Date")
lbl_add_date.grid(column=0, row=0)

lbl_adddate_date = Label(fraAddDate, justify=LEFT, anchor=W, width=5, font=('Arial', 18), text="Date:")
lbl_adddate_date.grid(column=0, row=1)

lbl_adddate_name = Label(fraAddDate, justify=LEFT, anchor=W, width=5, font=('Arial', 18), text="Name:")
lbl_adddate_name.grid(column=0, row=2)

lbl_remove_date = Label(fraRemoveDate, justify=LEFT, anchor=W, width=15, font=('Arial', 15), text="Remove Date")
lbl_remove_date.grid(column=0, row=0)

lbl_removedate_date = Label(fraRemoveDate, justify=LEFT, anchor=W, width=5, font=('Arial', 18), text="Date:")
lbl_removedate_date.grid(column=0, row=1)

lbl_removedate_name = Label(fraRemoveDate, justify=LEFT, anchor=W, width=5, font=('Arial', 18), text="Name:")
lbl_removedate_name.grid(column=0, row=2)

lbl_removedate_name_actual = Label(fraRemoveDate, justify=LEFT, anchor=W, width=20, font=('Arial', 18), text=date_name)
lbl_removedate_name_actual.grid(column=1, row=2)

lbl_anual_rollover = Label(fraAnualRollover, justify=LEFT, anchor=W, width=60, font=('Arial', 20), text="Anual Rollover Options")
lbl_anual_rollover.grid(column=0, row=0, columnspan=20)

lbl_num_days = Label(fraAnualRollover, justify=LEFT, anchor=W, width=40, font=('Arial', 16), text="Number of leave days to roll over to the next year:")
lbl_num_days.grid(column=0, row=1)

ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(fraAnualRollover, anchor=S, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=0, column=5, rowspan=2)

# ---- Checkboxes ---- #
chk_online_dates = Checkbutton(fraBankHol, font=('Arial', 16), text="Automatically get Bank Holiday dates from the internet")
chk_online_dates.pack(anchor=W)

# ---- Spinbox ---- #
spn_num_days = ttk.Spinbox(fraAnualRollover, from_=0, to=30)
spn_num_days.grid(column=1, row=1)

# --- Comboboxes ---- #

cmb_date_picker = ttk.Combobox(fraAddDate, width=20, font=('Arial', 18))
cmb_date_picker['values'] = "peekaboo"
cmb_date_picker.grid(row=1, column=1)

cmb_remove_date = ttk.Combobox(fraRemoveDate, width=20, font=('Arial', 18))
cmb_remove_date['values'] = "peekaboo"
cmb_remove_date.grid(row=1, column=1)

# ---- TextBox ---- #

txt_date_name = Text(fraAddDate, width=20, height=1, font=('Arial', 18))
txt_date_name.grid(row=2, column=1, rowspan=2, pady=1)

# ---- Buttons ---- #

btn_removeAllBankHol = Button(fraBankHol, width=23, font=('Arial', 18), text="Remove All Bank Holiday Dates", padx=20, command=remove_all_bank_holidays)
btn_removeAllBankHol.pack()

btn_addDate = Button(fraAddDate, width=10, font=('Arial', 18), text="Add", padx=20, command=add_date)
btn_addDate.grid(row=5, column=1)

btn_removeDate = Button(fraRemoveDate, width=10, font=('Arial', 18), text="Delete", padx=20, command=remove_date)
btn_removeDate.grid(row=5, column=1)


# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
