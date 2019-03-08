# Write a function to swap a number in place (that is, without using temporary variables).

numberOne = 25
numberTwo = 35

print ("Number one = ",numberOne," Number two = ",numberTwo)
numberOne = numberOne + numberTwo
numberTwo = numberOne - numberTwo
numberOne = numberOne - numberTwo
print ("Swapped")
print ("Number one = ",numberOne," Number two = ",numberTwo)
