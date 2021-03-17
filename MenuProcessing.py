## This program implements a simple menu processing system
# for student grades
# @author: Grace Merry

def main() :
 # Menu options
 ADD_STUDENT = 1
 REMOVE_STUDENT = 2
 LIST_STUDENTS = 3
 EXIT = 4

 # Create a dictionary of 3 students, each associated with a letter grade.
 # For simplicity, associate a first name (key) with a letter grade (value). 
 # Example “Ally” --> “C”
 students = {"Ally": "C", "Jack": "A", "Jose": "B"}

 # Continue to process requests until the user decides to exit.
 userChoice = 0
 while (userChoice != EXIT) :
  # Display the menu choices
  print("1) Add student and grade\n"
        "2) Remove student\n"
        "3) list all students\n"
        "4) Exit")
  
  # Prompt for and retrieve the user choice.
  userChoice = int(input("Your choice: "))
             
  # Depending upon the choice, either add a student/ grade, remove a student, or
  # list all students with their grades in sorted order by their name.
  #
  # Adds a new student and grade
  if userChoice == ADD_STUDENT:
     newStudent = input("Student name: ")
     newStudentGrade = input("Letter grade: ")
     students[newStudent] = newStudentGrade
     print()
     
  # Removes a student
  elif userChoice == REMOVE_STUDENT:
     studentRemoved = input("Student to remove: ")
     if studentRemoved in students:
        students.pop(studentRemoved)
     print()
    
  # Gives a list of all students
  elif userChoice == LIST_STUDENTS:
     for student in sorted(students):
        print("%s: %s" % (student, students[student]))
     print()
     
# Start Program      
main()