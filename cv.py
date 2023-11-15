import random
player1 = random.randint(1000,9999)
player2 = guess_your_number = int(input("guess your number from 4 digit \n"))
if len(str(player2)) != 4 : 
 print("your num is not 4 digit")
elif player2 == player1 :
  print(" you  winer ")
elif guess_your_number != player1 :
  print(f"you lose and player 2 it gussed {player1}")
else : 
  print(f"you write {player2} it is not correct")