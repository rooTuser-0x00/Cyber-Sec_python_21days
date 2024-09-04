#global variables
global_var = "This is a global variable"

def function1():
   #local variable
   local_var = "This is a local variable"
   print(local_var)
function1() 

print(global_var)
print("\n")

### another example of global and local variables
x = 10
def myfun():
   x = 20 
   print("Your local variable values is", x)# call location variable which can be used inside the function
myfun()

print("your global variable", x) # call global variable which can be used anywhere in side the program 


name_ = "amar"

def loca_var():
   name_ = "AMAR"
   print(name_)
loca_var()

print(name_)


name = "dagaura" # not printing this variable because global variable can be used called in function
def fun():
   global name
   name = "DAGAURA"
   print(name)
fun()
print(name)
