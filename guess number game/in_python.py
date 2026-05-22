import random
number = random.randint(1,100)
count =0
while True:
  guess = int(input("enter guess: "))
  count+=1
  if guess>number:
    print("too high")
  elif guess<number:
    print("too low")
  else:
    print(f"it took you {count} tries")
    break  
