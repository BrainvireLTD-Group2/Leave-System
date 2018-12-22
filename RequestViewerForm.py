from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk
import os
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('draft.s3db')
    c = conn.cursor()
except Error as e:
    print(e)

f=open("EmpNo.txt", "r")
if f.mode == 'r':
    EmpID =f.read()
    
root = Tk()
root.title("Leave Request Viewer Form")
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

# ---- Methods ----


def amend_request ():
    print("Amending Request")

    os.startfile(r'LeaveRequestForm.py')


def revoke_request():

    result = message_box.askquestion("Revoke Request", "Are you sure you want to revoke this request?", icon='warning')

    if result == 'yes':
        message_box.showinfo("", "Request Revoked")
        print("Request Revoked")
    else:
        print("Request Revoke Canceled")


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

lbl_title = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 18), text="Details for request # " + str(request_id) + " submitted on " + submission_date + "\n\n" + "Leave Date: " + leave_date + "\nLeave Type: " + leave_type + "\nYour Comments: \n" + emp_comment)
lbl_title.grid(row=0, column=0, columnspan=4)

lbl_mgr_detail = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 18), text="\nSigned off: " + signed_off + "\nManager's Comment:\n''" + mgr_comment + "''\nManager: " + mgr_name)
lbl_mgr_detail.grid(row=1, column=0, columnspan=4)

ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(fraInfo, anchor=SE, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=5, column=3)

# ---- Listbox ---- #

lst_leave_req = ttk.Treeview(fraListBox, columns=listbox_headers, show="headings", height=26)
lst_leave_req.pack(side=TOP)

lst_leave_req.heading('#1', text='RequestID', anchor=CENTER)
lst_leave_req.heading('#2', text='Date', anchor=CENTER)
lst_leave_req.heading('#3', text='Signed Off', anchor=CENTER)

lst_leave_req.column('#1', stretch=YES, minwidth=50, width=100)
lst_leave_req.column('#2', stretch=YES, minwidth=50, width=100)
lst_leave_req.column('#3', stretch=YES, minwidth=50, width=100)

cursor = conn.execute("SELECT RequestID, LeaveDate, SignedOff from Request Where EmployeeID = ?", (EmpID,))
for row in cursor:
    print (row[0])
    lst_leave_req.insert('', 'end', values=(("1"), (row[1]), (row[2])))


ttk.Scrollbar(orient="vertical",command=lst_leave_req.yview)

# ---- Buttons ---- #

btn_amend = Button(fraInfo, width=15, font=('Arial', 18), text="Amend Request", command=amend_request)
btn_amend.grid(row=3, column=1, rowspan=8)

btn_revoke = Button(fraInfo, width=15, font=('Arial', 18), text="Revoke Request", command=revoke_request)
btn_revoke.grid(row=3, column=2, rowspan=8)



# ---- Initialization ---- #

# Works like Form.Load in C#
if __name__ == '__main__':

    root.mainloop()
