#functions for user_dictionary.py

def checkdateofbirth(x): #creating lists of values to check the dateofbirth input using try/except
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
        "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    years = ["18", "19", "20"]
    
    while x[2] != "/": #checking format
        print ("Please input your date of birth in the proper format (mm/dd/yyyy)")
        x = input("Date of Birth (format: mm/dd/yyyy): ")

    while x[5] != "/":
        print ("Please input your date of birth in the proper format (mm/dd/yyyy)")
        x = input("Date of Birth (format: mm/dd/yyyy): ")
    
    while x[0:2] not in months:
        print ("Please input your date of birth in the proper format (mm/dd/yyyy)")
        x = input("Date of Birth (format: mm/dd/yyyy): ")

    while x[3:5] not in days:
        print ("Please input your date of birth in the proper format (mm/dd/yyyy)")
        x = input("Date of Birth (format: mm/dd/yyyy): ")

    while x[6:8] not in years:
        print ("Please input your date of birth in the proper format (mm/dd/yyyy)")
        x = input("Date of Birth (format: mm/dd/yyyy): ") 

def checkemail(x):        
    while x[-4] != ".":
        print ("Please input your email")
        x = input("Email: ")

    while len(x[-4:]) != 4:
        print ("Please input your email")
        x = input("Email: ")

    while "@" not in list(x):
        print ("Please input your email")
        x = input("Email: ")

def checkstate(x):
    stateabbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
        "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN",
        "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "GU", "PR", "VI"]
    
    while x.upper() not in stateabbreviations:
        print ("Please input your state")
        x = input("State: ")
