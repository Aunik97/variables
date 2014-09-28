#Aunik Hussain
#27-09-2014
#Finnishing off spot check programme at home


print("This programme will ask you for a weight, so it can calculate how many of other weights are required to bance it") 

weight = int(input("Please enter the weight")) 

weight100 = weight // 100 
leftover100 = weight100 % 100 

weight50 = leftover100 // 50 
leftover50 = weight50 % 50

weight10 = leftover50 // 10 
leftover10 = weight10 % 10 

weight5 = leftover10 // 5 
leftover5 = weight5 % 5 

weight2 = leftover5 // 2 
leftover2 = weight2 % 2 

weight1 = leftover2 // 1 
leftover1 = weight1 % 1 


print("The amount of 100 needed is {0}.".format(weight100,leftover100)) 
print("The amount of 50 needed is {1}.".format(weight50,leftover50)) 
print("The amount of 10 needed is {2}.".format(weight10,leftover10)) 
print("The amount of 5 needed is {3}.".format(weight5,leftover5)) 
print("The amount of 2 needed is {4}.".format(weight2,leftover2)) 
print("The amount of 1 needed is {5}.".format(weight1,leftover1)) 
