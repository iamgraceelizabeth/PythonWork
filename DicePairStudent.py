
## class DicePair rolls two dice and tallies the number of doubles rolled.
# @author: Grace Merry

from random import randint

class DicePair:
    
    ## Constructor
    # @param numSides The number of sides for each die. The default is 6.
    #
    def __init__(self, numSides = 6):
        self._die1 = 0
        self._die2 = 0
        self.setTotalDoubles(0)
        self.setNumSides(numSides)

    ## setNumSides sets the number of sides for each die to the same value
    # as long as the value is greater than 2, if not, then the number of sides
    # will be set to 2
    # @param numSides The number of sides for both the die used in the class.
    # 
    def setNumSides(self, numSides):
        if numSides < 2:
            self._numSides = 2
        else:
            self._numSides = numSides    
            
    ## getTotalDoubles returns the current value of _totalDoubles
    #  @return the current value for the number of doubles rolled
    def getTotalDoubles(self):
        return self._totalDoubles     
    
    ## getDie1 returns the current roll for die1
    #  @return the current value for the roll of die1
    def getDie1(self):
        return self._die1
    
    ## getDie2 returns the current roll for die2
    #  @return the current value for the roll of die2
    def getDie2(self):
        return self._die2
    
    ## setTotalDoubles sets the number of doubles to the value passed 
    #  in as numDoubles as long as it's positive. Else it sets 
    #  the instance variable for totalDoubles to zero.
    # @param numDoubles The number of doulbes.
    #     
    def setTotalDoubles(self, numDoubles):
        if numDoubles >= 0:
            self._totalDoubles = numDoubles
        else:
            self._totalDoubles = 0
        
    ## roll Generates a random number in the range [1, _numSides] 
    # for both die1 and die2. I.e. assigns the value to
    # _die1 and _die2 instance variables
    # This method also checks to see if a double has been rolled
    # and if 'yes' then 1 is added to the totalDoubles instance
    # variable
    #      
    def roll(self) :
        self._die1 = randint(1, self._numSides)
        self._die2 = randint(1, self._numSides)
        if self._die1 == self._die2:
            self._totalDoubles = self._totalDoubles + 1
        
