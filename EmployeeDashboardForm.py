from tkinter import*
import datetime
import calendar
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

now = datetime.datetime.now()
cursor = conn.execute("SELECT Name, Days_Of_Leave, RolloverDays from Employee Where EmployeeID = ?", (EmpID,))
for row in cursor:
   user_name = row[0]
   num_days = row[1]
   Rollover = row[2]
root = Tk()
root.title("Employee Leave Dashboard")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# ---- Variables ----

day_of_week = calendar.day_abbr[now.weekday()]
day = now.day
month = calendar.month_name[now.month]
year = now.year

# test data

days_expiring_soon = (num_days - Rollover) #NOT SURE HOW


# ---- Methods ----


def check_days_expiring_soon():

    if days_expiring_soon > 0:
        lbl_notify_expire.configure(bg='#e6586f')
        lbl_notify_expire.configure(fg='white')
        if days_expiring_soon == 1:
            lbl_notify_expire.configure(
                text="! You have " + str(days_expiring_soon) + " day which need to be booked soon")
        else:
            lbl_notify_expire.configure(text="! You have " + str(days_expiring_soon) + " days which need to be booked soon")


def open_leave_request ():
    print("Opening Leave Request Form")
    #exec(open('LeaveRequestForm.py').read())
    os.startfile(r'LeaveRequestForm.py')


def open_request_viewer():
    print("Opening Request Viewer")
    os.startfile(r'RequestViewerForm.py')


def open_employee_calendar():
    print("Opening Employee Calendar")
    os.startfile(r'EmployeeCalendarForm.py')


def open_policy_viewer():
    print("Opening Leave Policy Viewer")
    os.startfile(r'ViewPolicyForm.py')


# ---- Frame ----


TopLabels = Frame(root, width=900, height=400, relief="raise")
TopLabels.pack(side=TOP, padx=20)

TopLabels.grid_rowconfigure(0, weight=1)
TopLabels.grid_columnconfigure(0, weight=1)

Notification = Frame(root, width=900, height=70, relief="raise")
Notification.pack(side=TOP, padx=20, pady=20)
Buttons = Frame(root, width=900, height=180, relief="raise")
Buttons.pack(side=BOTTOM, fill=BOTH, expand=YES)

Buttons.grid_rowconfigure(0, weight=1)
Buttons.grid_columnconfigure(0, weight=1)

# ---- Labels ----

lbl_title = Label(TopLabels, justify=LEFT, anchor=W, width=100, font=('Arial', 20), text="Welcome " + user_name + "\n\nYou currently have " + str(num_days) + " days of leave remaining.")
lbl_title.grid(row=0, column=0)

lbl_notify_expire = Label(Notification, width=100, height=2, font=('Arial', 20), text="")
lbl_notify_expire.pack()


mini_calendar = PhotoImage(file="calendar.png")
pic_mini_calendar = Label(TopLabels, anchor=NE, image=mini_calendar)

pic_mini_calendar.grid(row=0, column=3)


ufix_logo = PhotoImage(file="UfixLogo.png")
pic_ufix_logo = Label(Buttons, anchor=SE, justify=RIGHT, image=ufix_logo)

pic_ufix_logo.grid(row=2, column=3)

lbl_current_date = Label(TopLabels, width=11, bg="#fff", font=('Arial', 15), text=day_of_week + " " + str(day) + "\n" + month + "\n" + str(year))
lbl_current_date.grid(row=0, column=3)


# ---- Buttons ----
btn_createRequest = Button(Buttons, width=15, font=('Arial', 20), text="Request Leave",
                           command=open_leave_request)
btn_createRequest.grid(row=0, column=1, padx=2)

btn_viewRequests = Button(Buttons, width=15, font=('Arial', 20), text="View Requests",
                          command=open_request_viewer)
btn_viewRequests.grid(row=0, column=2, padx=2)

btn_viewCalendar = Button(Buttons, width=15, font=('Arial', 20), text="View Calendar", padx=20,
                          command=open_employee_calendar)
btn_viewCalendar.grid(row=0, column=3, padx=2)

btn_viewPolicy = Button(Buttons, width=20, font=('Arial', 20), text="View UFix Ltd. Leave Policy", padx=20,
                        command=open_policy_viewer)

btn_viewPolicy.grid(row=2, column=2)

# ---- Initialization ----

# Works like Form.Load in C#
if __name__ == '__main__':
    check_days_expiring_soon()
    root.mainloop()
