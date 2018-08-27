'''
This program will calculate the area of a shape
'''

print("Area calculator started!")

option = input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(input("Input the radius: "))
  area = 3.14159 * radius ** 2
  print(str(area))
  
elif option == "T":
  base = float(input("Input the base: "))
  height = float(input("Input the height: "))
  area = 0.5 * base * height
  print(str(area))
  
else:
  print("Invalid shape")
  
print("Program exiting!")
