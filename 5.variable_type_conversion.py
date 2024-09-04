#type conversion 

birth_year = input ("enter your date of birth:")
current_year = 2024
age = current_year - int(birth_year)
print(type(age))
print("You are currently",  age, "years old.") 
birth_date = current_year - age
print("Your birth date is:", birth_date)
