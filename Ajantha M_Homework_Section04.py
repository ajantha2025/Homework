#15.Using the Datetime module to get full month name.

import datetime as dt

# Get the current date and time
a = dt.datetime.now()

# Extract the full month name
full_month_name = a.strftime("%B")

# Print the result
print("Current Month:", full_month_name)

#16.Write a function that takes 2 parameters -- a first name and a day name.

def My_Message(first_name, day_name="Sunday"):
    print(f"Hi {first_name}! Happy {day_name}!")

My_Message("Ajantha", "Monday")  
My_Message("Ajantha")            

#17.using the try,except, else, and finally components to handle index error.

numbers = [10, 20, 30]
try:
    print("Accessing index 5...")
    print(numbers[5])  # This index doesn't exist!
except IndexError:
    print("IndexError: That index is out of range.")
else:
    print("Successfully accessed the number.")
finally:
    print("Index check complete.\n")
