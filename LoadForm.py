import os
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('draft.s3db')
    c = conn.cursor()
except Error as e:
    print(e)
    

# ---- Methods ----

EmpID = input("Please enter EmpID")
Manager = "Not found"
cursor = conn.execute("SELECT Manager from Employee Where EmployeeID = ?", (EmpID,))
for row in cursor:
   Manager =row[0]
   
f= open("EmpNo.txt","w+")
f.write(EmpID)
f.close() 

# Get Job role to know which form to load
if Manager == "Y":
    # load Manager Form
    print("Opening Manager Form")
    #exec(open("ManagerDashboardForm.py").read())
    os.startfile(r'ManagerDashboardForm.py')
elif Manager == "N":
    # load Employee Form
    print("Opening Employee Form")
    #exec(open("EmployeeDashboardForm.py").read())
    os.startfile(r'EmployeeDashboardForm.py')
elif Manager == "Not found":
    # not found
    print("Not found")
