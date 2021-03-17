## This program illustrates aspects of driving a car.
# @author: Grace Merry

## class Car simulates a car by adding gasoline and decreasing gasoline 
# based upon estimated miles per gallon and miles driven.
class Car:
   ## Constructor
   # @param mpg The estimated fuel efficiency in miles per gallon
   # @param beginningGallons Amount of initial fuel in the tank
   def __init__(self, mpg = 0, beginningGallons = 0):
      self._mpg = mpg
      self._gallonsRemaining = beginningGallons

   ## addGas adds gasoline to the tank
   #  @param gallons The number of gallons to add  
   def addGas(self, gallons):
      self._gallonsRemaining = self._gallonsRemaining + gallons

   ## drive decrease gallons in the tank based upon  
   # estimated fuel efficiency and miles driven
   # @param milesDriven The number of miles driven
   def drive(self, milesDriven):
      self._gallonsRemaining = self._gallonsRemaining - milesDriven / self._mpg

   ## getGallonsRemaining returns the amount of fuel 
   #  remaining in the tank.
   # @return the number of gallons remaining
   def getGallonsRemaining(self):
      return self._gallonsRemaining

def main() :
   # Get initial fuel efficiency and gasoline
   mpg = float(input("Enter estimated fuel efficiency: "))
   gasToAdd = float(input("Enter initial fuel level (gallons): "))
   myCar = Car(mpg, gasToAdd)
   
   # Drive the car until the driver decides to quit
   driveMore = "y"
   while (driveMore[0].lower() == "y") :
      # Get miles driven adjust tank level
      milesDriven = float(input("Enter miles to drive: "))
      myCar.drive(milesDriven)
      print("Fuel remaining: %.2f gallons" % myCar.getGallonsRemaining())
      
      # Add any additional gasoline (could be 0)
      gasToAdd = float(input("Enter gas to add (gallons): "))
      myCar.addGas(gasToAdd)
      
      # Drive some more?
      driveMore = input("Drive more (y or n)? ")
      print()
   
   # Display final amount of fuel remaining
   print("Final fuel amount remaining: %.2f gallons" % \
          myCar.getGallonsRemaining())

main()