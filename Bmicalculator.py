#1st input: enter height in meters e.g: 1.65
height = input()
weight = input()
weight_as_int = int(weight)
height_as_int = float(height)
print(weight_as_int)
print(height_as_int)
bmi = weight_as_int / height_as_int ** 2
print(bmi)

bmi_as_int = int(bmi)
print(bmi_as_int)