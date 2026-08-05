import random
print("---Guess the number game---")
print("maine 1 se 10 ke beech ek number socha hai.kya aap bata sakte hain?")
secret_number = random.randint(1,10)
user_guess = int(input("apna guess (number)dalein: "))
if user_guess == secret_number:
  print("wah! aapne bilkul sahi pehchana!")
elif user_guess > secret_number
    print(f"ohho!aapka guess thoda bada hai.sahi number{secret_number}tha!")
else:
  print(f"ohho! aapka guess thoda chhota hai.sahi number{secret_number}tha!")
