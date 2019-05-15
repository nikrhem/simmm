chars = {1:'user',2:'bot'}
a = str(input("user:"))
if (a=="hi"):
  print(chars[2])
  print("hi. what is your name?")
  n = str(input("user:"))
  print(chars[2])
  print("Would you like to make a reservation at Sansbay?")
a = str(input("user:"))
if(a=="yes"):
  print(chars[2])
  print("what is the preferrable time slot?")
a = str(input("user:"))
if(a=="yes"):
  print(chars[2])
  print("what is the preferrable time slot?")
  m = str(input("user:"))
  print(chars[2])
  print("Reservation for how many people?")
  s = int(input("user:"))
  print(chars[2])
  print("Your reservation is successful. Would you like to have the reservation summary?")
  a=str(input("user:"))
  if(a=="yes"):
    print(chars[2])
    print("Hello! Mr/Ms.",n,"You have a table reserved at Sansbay at",m,"for",s,"People. Please be there on time. Reservation holds till 15 mins if late ")