# The first demonstration will show how to apply decision-making with the use of IF, ELIF and ELSE functions.
# The program will begin by offering the user a type of transport for their journey.
# The program will have an attitude problem towards the user if the user continues to select a number that is not 1, 2 or 3.  

print("The following transport options are available for you:\n")
print("1. Bus")
print("2. Train")
print("3. Taxi")
choice1=int(input("\nPlease select your transport option.\n"))
if(choice1==1):
  print("You have selected Bus")
elif(choice1==2):
  print("You have selected Train")
elif(choice1==3):
  print("You have selected Taxi")
else:
  choice2=int(input("\nPerhaps you misunderstood.\nPlease type 1, 2 or 3.\n"))
  if(choice2==1):
    print("You have selected Bus")
  elif(choice2==2):
    print("You have selected Train")
  elif(choice2==3):
    print("You have selected Taxi")
  else:
    choice3=int(input("\nIf you do not type 1, 2 or 3 then you will have to walk!\n"))
    if(choice3==1):
      print("You have selected Bus")
    elif(choice3==2):
      print("You have selected Train")
    elif(choice3==3):
     print("You have selected Taxi")
    else:
      print("\nYou have opted to walk. Previous options are no longer available.\n\nGoodbye and good day!")

# By applying these built-in functions within Python,
# we can demonstrate how to create a program in which
# the user is given information and makes a choice, 
# from a set of parameters, where each choice issues a
# different response from the program.