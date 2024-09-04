
# To check that the user is allowed to access the network: 
user_id = input("enter your user id: ")
user_name = input("enter your user name: ")
user_password = input("enter your password: ")

if int(user_id) == 95 and user_name == "amardagaura" and user_password == "Amar":
    print("\n" * 2)
    print("Welcome to Dish Media Network Pvt. Ltd.")
else:
    print("Invalid user!")
    print("Please contact your administrator")
print("Thank You!")