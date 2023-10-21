def fact(n):
  """This is a recursive function to find the factorial of an integer"""
  if n == 0:
    return 1
  else:
    return (n * fact(n - 1))
    fact(5)


year = int(input("Enter year to be checked:"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("The year is a leap year!")
    else:
      print("The year is not a leap year!")
  else:
    print("The year is a leap year!")
else:
  print("The year is not a leap year!")
