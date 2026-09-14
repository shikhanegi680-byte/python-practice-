x = int(input("enter your score"))
match(x):
  case 80:
      print("5 token")
  case 90:
      print("10 token")
  case 100:
      print("15 token")
  case _:
      print("better luck")
