# @author: Grace Merry
# Modified by Dan Horner
#

# Import the DicePair class
from DicePairStudent import DicePair

            
def main():
    MAX_ROLLS = 10
    player1 = DicePair()
    player2 = DicePair()
    
    # Roll the dice 10 times for each player
    for i in range(MAX_ROLLS):
        player1.roll()
        player2.roll()
         
        # Roll for player 1
        print("Player 1 rolled: %d, %d" % \
              (player1.getDie1(), player1.getDie2()))
        if (player1.getDie1() == player1.getDie2()) :
            print("  Double rolled for player 1")
        
        # Roll for player 2          
        print("Player 2 rolled: %d, %d" % \
              (player2.getDie1(), player2.getDie2()))        
        if (player2.getDie1() == player2.getDie2()) :
            print("  Double rolled for player 2")
        print()
    
    # Display the final results for the number of doubles rolled 
    # by each player.  Use the getTotalDoubles method.
    #
    print("Player 1 total doubles: ", player1.getTotalDoubles())
    print("Player 2 total doubles: ", player2.getTotalDoubles())
    
    # Also display who won.  Player 1, Player2 or was it a tie?
    # Use the getTotalDoubles method for this as well.
    #
    if player1.getTotalDoubles() > player2.getTotalDoubles():
        print("Player 1 wins!")
    elif player1.getTotalDoubles() < player2.getTotalDoubles():
        print("Player 2 wins!")
    else:
        print("Tie!")
        
    
main()