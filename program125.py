import sys

print("Enter the value : ")
variable = input()

print(type(variable))
print(id(variable))
print(sys.getsizeof(variable))

if variable.isdigit():
    variable = int(variable)
elif variable.replace('.','',1).isdigit() and variable.count('.')==1:
    variable = float(variable)
else:
    value = str(variable)

print(type(variable))
print(id(variable))
print(sys.getsizeof(variable))