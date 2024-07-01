print("WELCOME TO YOUR CALCULATOR")
num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
choice=(input("Enter your choice:"))

if choice == "1":
  print("YOUR ANSWER IS:",num1+num2)
elif choice == "2":
 print("YOUR ANSWER IS:",num1-num2)
elif choice =="3":
  print("YOUR ANSWER IS:",num1*num2)
elif choice =="4":
  print("YOUR ANSWER IS:",num1/num2)
else:
  print("Please Enter a Valid Operation")  

print("THANK YOU FOR USING THE CALCULATOR")