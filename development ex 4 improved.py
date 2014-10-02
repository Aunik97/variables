#Aunik Hussain
#27-09-2014
#Development exercise 4 improved

print("This programme will ask you for the length width and height of your swimming pool and produce the voulume")

length = int(input("Please enter the length of your swimming pool: "))
width = int(input("Please enter the width of your swimming pool: "))
height = int(input("Please enter the height of your swimming pool: "))

volume = length * width * height

print("The volume of your swimming pool is:  {0} * {1} * {2} is {3}.".format(length, width, height, volume))
