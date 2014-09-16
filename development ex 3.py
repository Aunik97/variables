#Aunik Hussain
#16-09-2104
#Development Ex 3

print("This programme will conver your height and weight from inches and stones to centimetres and kilograms")
height_inch = float(input("Please enter your height in inches"))
weight_stones = float(input("Please enter you weight in stone"))
height_centimeters = height_inch * 2.54
weight_kilogram = weight_stones * 6.364
print("Your height in centimeters is {0} = {2}, your weight in kilograms is {1} = {3}.".format(height_inch,weight_stones,height_centimeters,weight_kilogram))

