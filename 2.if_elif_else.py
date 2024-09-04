
# To check that the user is allowed to access the network: 
first_name = input("first_name: ")
last_name = input("last_name: ")
email = input("Email: ")
age = input("Age: ")
height = input("Height: ")

if str(first_name) == "amar" and str(last_name) =="dagaura" and str(email) == "amar@gmail.com" and int(age) == 24 and int(height) == 5.2 or int(height) >= 5:
    print("Valid user")
else:
    print("Invalid user")