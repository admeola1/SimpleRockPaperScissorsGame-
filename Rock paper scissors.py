# Game Rock paper scissors 
# Ask user to type Rock paper scissors or R P S
# Computer randomley generates RPS 
# Logic is used to determine winner then message is displayed after. 
import random 

PlayerOption = input("Enter r:Rock p:paper or s:scissors:")
Options = ["r","p","s"]
randomGen = random.choice(Options) 

#draws
if (PlayerOption == randomGen):
    print("Draw!!")
elif(PlayerOption == ("r") and randomGen == ("s")):
    print("Player wins!")
elif(PlayerOption == ("r") and randomGen == ("p")):
    print("Computer wins!")
elif(PlayerOption == ("s") and randomGen == ("r")):
    print("Computer wins!")
elif( PlayerOption == ("s") and randomGen == ("p")):
    print("Player Wins!") 
elif ( PlayerOption == ("p") and randomGen == ("s") ):
    print("comuter wins") 
elif( PlayerOption == ("p") and randomGen == ("r")):
    print("Player Wins")    
elif(PlayerOption != ("r","p","s")):
    print("what are you doing mate" + "computer chose:" + randomGen)
    
    
    
    
print("computer chose:" +  randomGen)
    



    
    
    
    
     
     
     
   
       
           
           
           
    
    
    
    
    
    
    
    
    
    









