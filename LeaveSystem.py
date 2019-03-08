from tkinter import*
import tkinter.messagebox as message_box
from tkinter import ttk
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

now = datetime.datetime.now()


# ---- Variables ----

day_of_week = calendar.day_abbr[now.weekday()]
day = now.day
month = calendar.month_name[now.month]
year = now.year
policy_path = "leave_policy.txt"
emp_no = 0
num_pending_requests = 1
half_day=0 #0 for full day, 1 for half day
# test data
num_days = 15
request_id = 1234
emp_id = 1011
leave_date = "13/06/19"
submission_date = "03/05/19"
leave_type = "Holiday"
emp_name = "Abel Maclead"
emp_comment = "I am going on holiday"
signed_off = "No"
mgr_comment = "All employees must attend on this date"
mgr_name = "Steven Tasks"
viewer_listbox_headers = ('RequestID', 'Date', 'Signed Off')
manager_listbox_headers = ('RequestID', 'Date', 'EmpID', 'Name')


# ---- Methods ----

def open_leave_request ():
    print("Opening Leave Request Form")
    ShowLeaveRequestForm()
    leaverequestform.mainloop()


def open_request_viewer():
    print("Opening Request Viewer")
    ShowRequestViewerForm()
    requestviewerform.mainloop()


def open_employee_calendar():
    print("Opening Employee Calendar")
    os.startfile(r'EmployeeCalendarForm.py')


def open_policy_viewer():
    print("Opening Policy Viewer Form")
    ShowPolicyViewerForm()
    policyviewerform.mainloop()

def open_manager_calendar():
    print("Opening Manager Calendar")
    #print("*Actually opens calendar options form* LIKE A BOSS")
    #os.startfile(r'CalendarOptionsForm.py')
    os.startfile(r'ManagerCalendarForm.py')


def open_request_manager():
    print("Opening Leave Request Manager")
    os.startfile(r'RequestManagerForm.py')

def close_policy_form ():
    policyviewerform.destroy()

def submit_request ():
    message_box.showinfo("", "Leave Request Submitted")
    leaverequestform.destroy()

def cancel_request():
    print("Leave Request Cancelled")
    leaverequestform.destroy()

def amend_request ():
    print("Amending Request")
    ShowLeaveRequestForm()
    leaverequestform.mainloop()

def revoke_request():

    result = message_box.askquestion("Revoke Request", "Are you sure you want to revoke this request?", icon='warning')

    if result == 'yes':
        message_box.showinfo("", "Request Revoked")
        print("Request Revoked")
    else:
        print("Request Revoke Canceled")



def ShowEmployeeDashboardForm():
    global employeedashboardform
    employeedashboardform = Toplevel()
    employeedashboardform.title("Employee Leave Dashboard")
    screen_width = employeedashboardform.winfo_screenwidth()
    screen_height = employeedashboardform.winfo_screenheight()
    empFrmwidth = 900
    empFrmheight = 500
    x = (screen_width / 2) - (empFrmwidth / 2)
    y = (screen_height / 2) - (empFrmheight / 2)
    employeedashboardform.geometry('%dx%d+%d+%d' % (empFrmwidth, empFrmheight, x, y))
    employeedashboardform.resizable(0, 0)
    employeedashboardform.geometry("%dx%d+%d+%d" % (empFrmwidth, empFrmheight, x, y))
    EmployeeDashboardForm()

def ShowManagerDashboardForm():
    global managerdashboardform
    managerdashboardform = Toplevel()
    managerdashboardform.title("Manager Leave Dashboard")
    screen_width = managerdashboardform.winfo_screenwidth()
    screen_height = managerdashboardform.winfo_screenheight()
    manFrmWidth = 900
    manFrmHeight = 650
    x = (screen_width / 2) - (manFrmWidth / 2)
    y = (screen_height / 2) - (manFrmHeight / 2)
    managerdashboardform.geometry('%dx%d+%d+%d' % (manFrmWidth, manFrmHeight, x, y))
    managerdashboardform.resizable(0, 0)
    managerdashboardform.geometry("%dx%d+%d+%d" % (manFrmWidth, manFrmHeight, x, y))
    ManagerDashboardForm()

def ShowPolicyViewerForm():
    global policyviewerform
    policyviewerform = Toplevel()
    policyviewerform.title("Leave Policy Viewer")
    screen_width = policyviewerform.winfo_screenwidth()
    screen_height = policyviewerform.winfo_screenheight()
    viewFrmWidth = 900
    viewFrmHeight = 600
    x = (screen_width / 2) - (viewFrmWidth / 2)
    y = (screen_height / 2) - (viewFrmHeight / 2)
    policyviewerform.geometry('%dx%d+%d+%d' % (viewFrmWidth, viewFrmHeight, x, y))
    policyviewerform.resizable(0, 0)
    policyviewerform.geometry("%dx%d+%d+%d" % (viewFrmWidth, viewFrmHeight, x, y))
    PolicyViewerForm()

def ShowLeaveRequestForm():
    global leaverequestform
    leaverequestform = Toplevel()
    leaverequestform.title("Leave Request Form")
    screen_width = leaverequestform.winfo_screenwidth()
    screen_height = leaverequestform.winfo_screenheight()
    requestFrmWidth = 900
    requestFrmHeight = 550
    x = (screen_width / 2) - (requestFrmWidth / 2)
    y = (screen_height / 2) - (requestFrmHeight / 2)
    leaverequestform.geometry('%dx%d+%d+%d' % (requestFrmWidth, requestFrmHeight, x, y))
    leaverequestform.resizable(0, 0)
    leaverequestform.geometry("%dx%d+%d+%d" % (requestFrmWidth, requestFrmHeight, x, y))
    LeaveRequestForm()

def ShowRequestViewerForm():
    global requestviewerform
    requestviewerform = Toplevel()
    requestviewerform.title("Leave Request Viewer Form")
    screen_width = requestviewerform.winfo_screenwidth()
    screen_height = requestviewerform.winfo_screenheight()
    viewerFrmWidth = 900
    viewerFrmHeight = 500
    x = (screen_width / 2) - (viewerFrmWidth / 2)
    y = (screen_height / 2) - (viewerFrmHeight / 2)
    requestviewerform.geometry('%dx%d+%d+%d' % (viewerFrmWidth, viewerFrmHeight, x, y))
    requestviewerform.resizable(0, 0)
    requestviewerform.geometry("%dx%d+%d+%d" % (viewerFrmWidth, viewerFrmHeight, x, y))
    RequestViewerForm()

def EmployeeDashboardForm():

    ufix_logo = PhotoImage(file="UfixLogo.png")
    mini_calendar = PhotoImage(file="calendar.png")

    TopLabels = Frame(employeedashboardform, width=900, height=400, relief="raise")
    TopLabels.pack(side=TOP, padx=20)

    TopLabels.grid_rowconfigure(0, weight=1)
    TopLabels.grid_columnconfigure(0, weight=1)

    Notification = Frame(employeedashboardform, width=900, height=70, relief="raise")
    Notification.pack(side=TOP, padx=20, pady=20)
    Buttons = Frame(employeedashboardform, width=900, height=180, relief="raise")
    Buttons.pack(side=BOTTOM, fill=BOTH, expand=YES)

    Buttons.grid_rowconfigure(0, weight=1)
    Buttons.grid_columnconfigure(0, weight=1)

    lbl_title = Label(TopLabels, justify=LEFT, anchor=W, width=100, font=('Arial', 20),
                      text="Welcome " + user_name + "\n\nYou currently have " + str(
                          num_days) + " days of leave remaining.")
    lbl_title.grid(row=0, column=0)

    lbl_notify_expire = Label(Notification, width=100, height=2, font=('Arial', 20), text="")
    lbl_notify_expire.pack()

    pic_mini_calendar = Label(TopLabels, anchor=NE, image=mini_calendar)

    pic_mini_calendar.grid(row=0, column=3)

    pic_ufix_logo = Label(Buttons, anchor=SE, justify=RIGHT, image=ufix_logo)

    pic_ufix_logo.grid(row=2, column=3)

    lbl_current_date = Label(TopLabels, width=11, bg="#fff", font=('Arial', 15),
                             text=day_of_week + " " + str(day) + "\n" + month + "\n" + str(year))
    lbl_current_date.grid(row=0, column=3)

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

    if days_expiring_soon > 0:
        lbl_notify_expire.configure(bg='#e6586f')
        lbl_notify_expire.configure(fg='white')
        if days_expiring_soon == 1:
            lbl_notify_expire.configure(
                text="! You have " + str(days_expiring_soon) + " day which need to be booked soon")
        else:
            lbl_notify_expire.configure(text="! You have " + str(days_expiring_soon) + " days which need to be booked soon")


def ManagerDashboardForm():
    TopLabels = Frame(managerdashboardform, width=900, height=400, relief="raise")
    TopLabels.pack(side=TOP, padx=20)

    TopLabels.grid_rowconfigure(0, weight=1)
    TopLabels.grid_columnconfigure(0, weight=1)

    Notification = Frame(managerdashboardform, width=900, height=70, relief="raise")
    Notification.pack(side=TOP, padx=20, pady=20)

    Buttons = Frame(managerdashboardform, width=900, height=100, relief="raise")
    Buttons.pack(side=BOTTOM, fill=BOTH, expand=YES)

    Buttons.grid_rowconfigure(1, weight=1)
    Buttons.grid_columnconfigure(1, weight=1)

    lbl_title = Label(TopLabels, justify=LEFT, anchor=W, width=100, font=('Arial', 20),
                      text="Welcome " + user_name + "\n\nYou currently have " + str(
                          num_days) + " days of leave remaining.")
    lbl_title.grid(row=0, column=0)

    lbl_notify_expire = Label(Notification, width=100, height=2, font=('Arial', 20), text="")
    lbl_notify_expire.pack()

    lbl_notify_requests = Label(Notification, width=100, height=2, font=('Arial', 20), text="")
    lbl_notify_requests.pack(pady=4)

    mini_calendar = PhotoImage(file="calendar.png")
    pic_mini_calendar = Label(TopLabels, anchor=NE, image=mini_calendar)

    pic_mini_calendar.grid(row=0, column=3)

    ufix_logo = PhotoImage(file="UfixLogo.png")
    pic_ufix_logo = Label(Buttons, justify=RIGHT, image=ufix_logo)

    pic_ufix_logo.grid(row=3, column=2)

    lbl_current_date = Label(TopLabels, width=11, bg="#fff", font=('Arial', 15),
                             text=day_of_week + " " + str(day) + "\n" + month + "\n" + str(year))
    lbl_current_date.grid(row=0, column=3)

    btn_createRequest = Button(Buttons, width=15, font=('Arial', 20), text="Request Leave", command=open_leave_request)

    btn_createRequest.grid(row=0, column=0, padx=75)

    btn_viewRequests = Button(Buttons, width=15, font=('Arial', 20), text="View Your Requests",
                              command=open_request_viewer)
    btn_viewRequests.grid(row=2, column=0)

    btn_viewCalendar = Button(Buttons, width=15, font=('Arial', 20), text="View Calendar",
                              command=open_manager_calendar)
    btn_viewCalendar.grid(row=0, column=1)

    btn_manageRequests = Button(Buttons, width=15, font=('Arial', 20), text="Manage Requests",
                                command=open_request_manager)
    btn_manageRequests.grid(row=2, column=1)

    btn_viewPolicy = Button(Buttons, width=40, font=('Arial', 20), padx=30, text="View UFix Ltd. Leave Policy",
                            command=open_policy_viewer)
    btn_viewPolicy.grid(row=3, column=0, columnspan=2)

    if days_expiring_soon > 0:
        lbl_notify_expire.configure(bg='#e6586f')
        lbl_notify_expire.configure(fg='white')
        if days_expiring_soon == 1:
            lbl_notify_expire.configure(
                text="! You have " + str(days_expiring_soon) + " day which need to be booked soon")
        else:
            lbl_notify_expire.configure(text="! You have " + str(days_expiring_soon) + " days which need to be booked soon")

    if num_pending_requests > 0:
        lbl_notify_requests.configure(bg='#7bbc6e')
        lbl_notify_requests.configure(fg='white')
        if num_pending_requests == 1:
            lbl_notify_requests.configure(text="* There is " + str(num_pending_requests) + " pending leave request")
        else:
            lbl_notify_requests.configure(text="* There are " + str(num_pending_requests) + " pending leave requests")


def PolicyViewerForm():
    Policy = Frame(policyviewerform, width=900, height=350, relief="raise")
    Policy.pack(side=TOP, padx=20)

    CloseButton = Frame(policyviewerform, width=900, height=150, relief="raise")
    CloseButton.pack(side=BOTTOM)

    btn_close = Button(CloseButton, width=15, font=('Arial', 20), text="Close", command=close_policy_form)
    btn_close.pack(side=RIGHT, anchor=SE)

    txt_policy = Text(Policy, width=76, height=23, font=('Arial', 15))
    txt_policy.pack(side=LEFT, anchor=NW)
    txt_policy.insert(END, open(policy_path).read())
    txt_policy.configure(state=DISABLED)
    txt_scroll = ttk.Scrollbar(Policy, orient="vertical", command=txt_policy.yview)

    txt_policy.configure(yscrollcommand=txt_scroll.set)

    txt_scroll.pack(side=RIGHT, anchor=E, fill="y", )

def LeaveRequestForm():
    TopLabels = Frame(leaverequestform, width=900, height=400, relief="raise")
    TopLabels.pack(side=TOP, padx=20)

    TopLabels.grid_rowconfigure(0, weight=1)
    TopLabels.grid_columnconfigure(0, weight=1)

    Options = Frame(leaverequestform, width=450, height=180, relief="raise")
    Options.pack(side=TOP, fill=BOTH, expand=YES)

    Options.grid_rowconfigure(0, weight=1)
    Options.grid_columnconfigure(0, weight=1)

    Buttons = Frame(leaverequestform, width=800, height=180, relief="raise")
    Buttons.pack(side=LEFT, fill=BOTH, expand=YES)

    Buttons.grid_rowconfigure(0, weight=1)
    Buttons.grid_columnconfigure(0, weight=1)

    Logo = Frame(leaverequestform, width=100, height=180, relief="raise")
    Logo.pack(side=RIGHT, fill=BOTH, expand=YES)

    Logo.grid_rowconfigure(0, weight=1)
    Logo.grid_columnconfigure(0, weight=1)

    lbl_title = Label(TopLabels, justify=LEFT, anchor=W, width=100, font=('Arial', 20),
                      text="You currently have " + str(
                          num_days) + " days of leave remaining.\n\n" + "Request ID: #" + str(
                          request_id) + "\nEmployee ID: " + str(emp_id))
    lbl_title.grid(row=0, column=0)

    mini_calendar = PhotoImage(file="calendar.png")
    pic_mini_calendar = Label(TopLabels, anchor=NE, image=mini_calendar)

    pic_mini_calendar.grid(row=0, column=3)

    ufix_logo = PhotoImage(file="UfixLogo.png")
    pic_ufix_logo = Label(Logo, anchor=SE, justify=RIGHT, image=ufix_logo)

    pic_ufix_logo.grid(row=0, column=0)

    lbl_current_date = Label(TopLabels, width=11, bg="#fff", font=('Arial', 15),
                             text=day_of_week + " " + str(day) + "\n" + month + "\n" + str(year))
    lbl_current_date.grid(row=0, column=3)

    lbl_leave_date = Label(Options, width=11, font=('Arial', 20), text="Leave Date: ", justify=LEFT)
    lbl_leave_date.grid(row=0, column=0)

    lbl_comments = Label(Options, width=11, font=('Arial', 20), text="Comments: ", justify=LEFT)
    lbl_comments.grid(row=0, column=2)

    lbl_leave_type = Label(Options, width=11, font=('Arial', 20), text="Leave Type: ", justify=LEFT)
    lbl_leave_type.grid(row=2, column=0)

    btn_submit = Button(Buttons, width=15, font=('Arial', 20), text="Submit", command=submit_request)
    btn_submit.grid(row=0, column=0, padx=2)

    btn_cancel = Button(Buttons, width=15, font=('Arial', 20), text="Cancel", command=cancel_request)
    btn_cancel.grid(row=0, column=1, padx=2)

    cmb_date_picker = ttk.Combobox(Options, width=15, font=('Arial', 20))
    cmb_date_picker['values'] = "peekaboo"
    cmb_date_picker.grid(row=0, column=1)

    cmb_leave_type = ttk.Combobox(Options, width=15, font=('Arial', 20))
    cmb_leave_type['values'] = ("Holiday", "Paternity", "Emergency", "Sickness", "Bereavement")
    cmb_leave_type.grid(row=2, column=1)

    txt_comments = Text(Options, width=20, height=5, font=('Arial', 20))
    txt_comments.grid(row=0, column=3, padx=2)

    opt_full_day = ttk.Radiobutton(Options, width=20, variable=half_day, value=0, text="Full Day")
    opt_full_day.grid(row=1, column=0, padx=2)

    opt_half_day = ttk.Radiobutton(Options, width=20, variable=half_day, value=1, text="Half Day")
    opt_half_day.grid(row=1, column=1, padx=2)

def RequestViewerForm():
    fraListBox = Frame(requestviewerform, width=300, height=500, relief="raise")
    fraListBox.pack(side=LEFT, anchor=NW)

    fraInfo = Frame(requestviewerform, width=450, height=500, relief="raise")
    fraInfo.pack(side=RIGHT, anchor=NE)

    fraInfo.grid_rowconfigure(0, weight=1)
    fraInfo.grid_columnconfigure(0, weight=1)

    fraInfo.grid_rowconfigure(0, weight=1)
    fraInfo.grid_columnconfigure(0, weight=1)

    lbl_title = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 18),
                      text="Details for request # " + str(
                          request_id) + " submitted on " + submission_date + "\n\n" + "Leave Date: " + leave_date + "\nLeave Type: " + leave_type + "\nYour Comments: \n" + emp_comment)
    lbl_title.grid(row=0, column=0, columnspan=4)

    lbl_mgr_detail = Label(fraInfo, justify=LEFT, anchor=W, width=120, font=('Arial', 18),
                           text="\nSigned off: " + signed_off + "\nManager's Comment:\n''" + mgr_comment + "''\nManager: " + mgr_name)
    lbl_mgr_detail.grid(row=1, column=0, columnspan=4)

    ufix_logo = PhotoImage(file="UfixLogo.png")
    pic_ufix_logo = Label(fraInfo, anchor=SE, justify=RIGHT, image=ufix_logo)

    pic_ufix_logo.grid(row=5, column=3)


    lst_leave_req = ttk.Treeview(fraListBox, columns=viewer_listbox_headers, show="headings", height=26)
    lst_leave_req.pack(side=TOP)

    lst_leave_req.heading('#1', text='RequestID', anchor=CENTER)
    lst_leave_req.heading('#2', text='Date', anchor=CENTER)
    lst_leave_req.heading('#3', text='Signed Off', anchor=CENTER)

    lst_leave_req.column('#1', stretch=YES, minwidth=50, width=100)
    lst_leave_req.column('#2', stretch=YES, minwidth=50, width=100)
    lst_leave_req.column('#3', stretch=YES, minwidth=50, width=100)

    cursor = conn.execute("SELECT RequestID, LeaveDate, SignedOff from Request Where EmployeeID = ?", (emp_no,))
    for row in cursor:
        print(row[0])
        lst_leave_req.insert('', 'end', values=(("1"), (row[1]), (row[2])))

    ttk.Scrollbar(orient="vertical", command=lst_leave_req.yview)

    btn_amend = Button(fraInfo, width=15, font=('Arial', 18), text="Amend Request", command=amend_request)
    btn_amend.grid(row=3, column=1, rowspan=8)

    btn_revoke = Button(fraInfo, width=15, font=('Arial', 18), text="Revoke Request", command=revoke_request)
    btn_revoke.grid(row=3, column=2, rowspan=8)


# ---- Initialization ----


emp_no = input("Please enter EmpID")
Manager = "Not found"
cursor = conn.execute("SELECT Manager from Employee Where EmployeeID = ?", (emp_no,))
for row in cursor:
    Manager = row[0]

# Get Job role to know which form to load
if Manager == "Y":
    # load Manager Form
    print("Opening Manager Form")
    cursor = conn.execute("SELECT Name, Days_Of_Leave, RolloverDays from Employee Where EmployeeID = ?", (emp_no,))
    for row in cursor:
        user_name = row[0]
        num_days = row[1]
        Rollover = row[2]

    days_expiring_soon = (num_days - Rollover)  # NOT SURE HOW

    ShowManagerDashboardForm()
    managerdashboardform.mainloop()
elif Manager == "N":
    # load Employee Form
    print("Opening Employee Form")

    cursor = conn.execute("SELECT Name, Days_Of_Leave, RolloverDays from Employee Where EmployeeID = ?", (emp_no,))
    for row in cursor:
        user_name = row[0]
        num_days = row[1]
        Rollover = row[2]



    days_expiring_soon = (num_days - Rollover)  # NOT SURE HOW

    ShowEmployeeDashboardForm()
    employeedashboardform.mainloop()
elif Manager == "Not found":
    # not found
    print("Not found")
