from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk
import sqlite3
from sqlite3 import Error

root = Tk()
root.title("Leave Request Manager Form")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



# ---- Variables ----
listbox_headers = ('RequestID', 'Date', 'EmpID', 'Name')


# test data
request_id = 1234
emp_id = 1012
leave_date = "13/06/19"
submission_date = "03/05/19"
leave_type = "Holiday"
emp_name = "Abel Maclead"
emp_comment = "I am going on holiday"
signed_off = "No"
mgr_comment = "All employees must attend on this date"
mgr_name = "Steven Tasks"

# ---- Methods ----

try:
    conn = sqlite3.connect('draft.s3db')
    c = conn.cursor()
except Error as e:
    print(e)

f=open("EmpNo.txt", "r")
if f.mode == 'r':
    EmpID =f.read()


def accept_request():

    result = message_box.askquestion("Accept Request", "Are you sure you want to accept this request?", icon='warning')

    if result == 'yes':
        message_box.showinfo("", "Request Accepted")
        print("Request Accepted")
    else:
        print("Request Acceptance Canceled")


def deny_request():

    comment = txt_comments.get("1.0", END)

    result = message_box.askquestion("Deny Request", "Are you sure you want to deny this request?", icon='warning')
    if result == 'yes':
        message_box.showinfo("", "Request Denied")
        print("Request #" + str(request_id) + " Denied by " + mgr_name + " with comment: " + comment)
    else:
        print("Request Denial Canceled")


def populate_listbox():
    cursor = conn.execute("SELECT RequestID, LeaveDate, EmployeeID, SignedOff from Request Where ManagerID = ?", (EmpID,))
    for row in cursor:
        print(row[0])
        lst_leave_req.insert('', 'end', values=(("1"), (row[1]), (row[2])))


def update_label():
    lbl_title.configure(text="Details for request # " + str(
                          request_id) + " submitted on " + submission_date + "\n\n" + "EmployeeID: " + str(
                          emp_id) + "\nEmployee Name: " + emp_name + "\nLeave Date: " + leave_date + "\nLeave Type: " + leave_type + "\nEmployee Comment: \n" + emp_comment)


# ---- Frame ----


fraListBox = Frame(root, width=300, height=500, relief="raise")
fraListBox.pack(side=LEFT, anchor=NW)


fraInfo = Frame(root, width=450, height=500, relief="raise")
fraInfo.pack(side=RIGHT, anchor=NE)

fraInfo.grid_rowconfigure(0, weight=1)
fraInfo.grid_columnconfigure(0, weight=1)

fraInfo.grid_rowconfigure(0, weight=1)
fraInfo.grid_columnconfigure(0, weight=1)



# ---- Labels ---- #

lbl_title = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 16), text="")
lbl_title.grid(row=1, column=0, columnspan=4)

lbl_mgr_detail = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 16), text="\nYour Response: ")
lbl_mgr_detail.grid(row=2, column=0, columnspan=4)

ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(fraInfo, anchor=S, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=3, column=4,)

# ---- Listbox ---- #

lst_leave_req = ttk.Treeview(fraListBox, columns=listbox_headers, show="headings", height=26)
lst_leave_req.pack(side=TOP)

lst_leave_req.heading('#1', text='RequestID', anchor=CENTER)
lst_leave_req.heading('#2', text='Date', anchor=CENTER)
lst_leave_req.heading('#3', text='EmpID', anchor=CENTER)
lst_leave_req.heading('#4', text='Name', anchor=CENTER)

lst_leave_req.column('#1', stretch=YES, minwidth=50, width=100)
lst_leave_req.column('#2', stretch=YES, minwidth=50, width=100)
lst_leave_req.column('#3', stretch=YES, minwidth=50, width=100)
lst_leave_req.column('#4', stretch=YES, minwidth=50, width=100)

populate_listbox()

# ---- Multi-Line Text Box ---- #

txt_comments = Text(fraInfo, width=20, height=5, font=('Arial', 18))
txt_comments.grid(row=3, column=0, rowspan=2, columnspan=3)

# ---- Buttons ---- #

btn_amend = Button(fraInfo, width=10, font=('Arial', 18), text="Accept", command=accept_request)
btn_amend.grid(row=4, column=1, rowspan=2)

btn_revoke = Button(fraInfo, width=10, font=('Arial', 18), text="Decline", command=deny_request)
btn_revoke.grid(row=4, column=2, rowspan=2)



# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
