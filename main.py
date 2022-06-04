num1 = int(input("1st num :-  "))
num2 = int(input("2ed num :-  "))
num3 = int(input("3ed num :-  "))

if(num1>num2 and num1 > num3):
  leg = num1
elif (num2>num1 and num2>num3):
  leg = num2
else:
  leg = num3
print(leg , "is lergest number")  
  