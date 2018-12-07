import os

# ---- Variables ----
#job_role = "Employee"
#job_role = "Manager"

# ---- Methods ----

job_role = input("Please enter job role (Either Employee or Manager)")

# Get Job role to know which form to load
if job_role == "Manager":
    # load Manager Form
    print("Opening Manager Form")
    #exec(open("ManagerDashboardForm.py").read())
    os.startfile(r'ManagerDashboardForm.py')
elif job_role == "Employee":
    # load Employee Form
    print("Opening Employee Form")
    #exec(open("EmployeeDashboardForm.py").read())
    os.startfile(r'EmployeeDashboardForm.py')
else:
    print("Invalid Job Role")

