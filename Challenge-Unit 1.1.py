def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


num = int(input("Enter a number: "))
if num < 0:
  print("Factorial is not defined for negative numbers.")
elif num == 0:
  print("The factorial of 0 is 1")
else:
  result = factorial(num)
  print("The factorial of {} is {}.".format(num,result))
