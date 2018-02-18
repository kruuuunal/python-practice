#Create a user dictionary by asking the user for first name, last name, DOB, address, email
#Import functions stored in another file (user_dictionary_functions.py) to check the DOB and email inputs

from user_dictionary_functions import checkdateofbirth, checkemail, checkstate, checkzip

userinfo = {} #creating a dictionary to be filled

firstname = input("First name: ")
userinfo["First name"] = firstname #add a key to the dictionary & make the user-input the value

lastname = input("Last name: ")
userinfo["Last name"] = lastname

dateofbirth = input("Date of Birth (format: mm/dd/yyyy): ")
userinfo["Date of birth"] = checkdateofbirth(dateofbirth)

address = input("Home address: ")
userinfo["Address"] = address

city = input("City: ")
userinfo["City"] = city

state = input("State (xx): ")
userinfo["State"] = checkstate(state)

zip = input("Zip Code: ")
userinfo["Zip"] = checkzip(zip) #need to add a function to check zip codes (length and if all values are integers)

email = input("Email: ")
userinfo["Email"] = checkemail(email)

print (userinfo)
