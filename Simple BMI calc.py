#inputs by user
height - input("enter your height in m: ")
weight - input("enter your weight in kg: ")

#calculation of bmi
bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)
#print below
print(bmi_as_int)
