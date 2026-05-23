import random
import string

ret=True

while ret:
  
  count=0
  password_length=int(input("how long should the password be?"))
  pool=""
  password=''
  uppercase=input("do you want uppercase ")
  lowercase=input("do you want lowercase ")
  digit=input("do you want digits ")
  punctuations=input("do you want punctuations ")
  if uppercase=='yes':
    pool+=string.ascii_uppercase
    password+=random.choice(string.ascii_uppercase)
    count+=1
  if lowercase=='yes':
    pool+=string.ascii_lowercase
    password+=random.choice(string.ascii_lowercase)
    count+=1
  if digit=='yes':
    pool+=string.digits
    password+=random.choice(string.digits)
    count+=1
  if punctuations=='yes':
    pool+=string.punctuation
    password+=random.choice(string.punctuation)
    count+=1
  if count==0:
    print("enter atleast something")
    continue
  password+="".join(random.choices(pool,k=password_length-count))
  password=list(password)
  random.shuffle(password)
  password="".join(password)
  print(f"password is {password}")
  boolean=input("do you need another password")
  
  ret=boolean=='yes'

  

