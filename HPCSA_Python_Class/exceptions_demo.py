"""-----------
Exception Handling
----------------"""
# without exceptions code 
input_var = int(input("Please enter a number "))
print("Adding 10 to your value entered is " , input_var+ 10)

# with exceptions code to demonstrate need of exceptions
try:
    input_var = int(input("Please enter a number "))
except Exception:
    try:
        input_var = int(input("You entered an incorrect number , Please try again ! "))
    except :
        input_var = int(input("You stupid please enter a number"))    
print("Adding 10 to your value entered is " , input_var+ 10)

# what if we dont write exception and try to do it with if else block
input_var = int(input("Please enter a number "))
print("I came at this line ")

if isinstance(input_var,int):
    print("Adding 10 to your value entered is " , input_var+ 10)
else:
    input_var = int(input("You entered an incorrect number , Please try again ! "))
    if isinstance(input_var,int):
        print("Adding 10 to your value entered is " , input_var+ 10)
    else:    
        input_var = int(input("You stupid please enter a number"))    
        if isinstance(input_var,int):
            print("Adding 10 to your value entered is " , input_var+ 10)

    

# with exceptions code  for a function to demonstrate exception propogation 
def my_simple_fun():
        return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"
        
try:
    print(my_simple_fun())
except Exception:
    try:
        print(my_simple_fun())
    except :
        print(my_simple_fun())



# with exceptions code  for a function but with other exception to demonstrate exception matching
def my_simple_fun():
        return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"
        
try:
    print(my_simple_fun())
except ImportError:
    try:
        print(my_simple_fun())
    except :
        print(my_simple_fun())

# a function within a function to demonstrate exception propogation
def inner_simple_func():
    return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"

def my_simple_fun():
        print("Doing Nothing here -- just try to handle exception if possible ")
        return inner_simple_func()
        
try:
    print(my_simple_fun())
except ImportError:
    try:
        print(my_simple_fun())
    except :
        print(my_simple_fun())

"""------------------------------------------------------------------
user defined exceptions demonstrate
-------------------------------------------------------------------"""

# create your exception and raise them
class mycustom_exception(Exception):
    pass

def check_age_greater_than_18(age):
    if age<18:
        print("Oops, A word of caution from me !!!")
        raise mycustom_exception
    print("All Good mate , Please proceed !!!")
    
check_age_greater_than_18(int(input("Please enter age which is greater than 18")))

# raise some system defined exception
def check_age_greater_than_18(age):
    if age<18:
        raise ValueError("Oops, A word of caution from me !!!")
    print("All Good mate , Please proceed !!!")
    
check_age_greater_than_18(int(input("Please enter age which is greater than 18")))


my_list = [200]
# Finally block
# exception handled code     
try:
    if my_list[1] == 100:
        print("I accessed the first subscript element of my list: " , my_list[1])
except Exception:
    print("Exception is now handled using Exception exception  ")        
finally:
    print("Finally block is executed no matter what -- with or without exception")    
    

# specific exception handled code     
try:
    if my_list[1] == 100:
        print("I accessed the first element of my list ")
except Exception:
    print("Exception is now handled using Exception exception ")        
except IndexError:
    print("Exception is now handled using IndexError exception  ")        
finally:
    print("Finally block is executed no matter what -- with or without exception")    
