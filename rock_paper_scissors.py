import random
print("---rock","paper","scissors game ---")
options = ["rock","paper","scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter your choice (rock,paper,scissors):).lower()
print(f"\nAapne chuna : {user_choice}")
print(f"\computer ne chuna: {computer_choice}\n")
if user_choice == "rock":
      print("aap jeet gaye!")
                    else:
print("computer jeet gaya")
elif user _choice =="paper":
 if computer_choice == "rock":
     print("Aap jeet gaye!)
           else:
   print("computer jeet gaya")
elif user choice == "scissors":
if computer_choice =="paper":
  print("aap jeet gaye")
else:
  print("computer jeet gaya!")
else:
print("invalid input! kripiya rock,paper ya scissors hi likhen.")
