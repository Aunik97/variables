#Aunik Hussain
#22-09-2014
#Function that asks the user how old they are and Tells them if they are old enough to vote

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are too young to vote")

retirement = 65 - age
print("You will retire in {0} years.".format(retirement, age))
