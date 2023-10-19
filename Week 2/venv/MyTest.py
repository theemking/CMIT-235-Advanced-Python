############################################################################################################################
'''
                                           ********** WEEK 1 **********
 This is the my test page
 This page is used to practice and display the output

 The Program Objectives:

1.  Demonstrate an understanding of modular programming where you separate the functionality of a program into independent
    packages and modules.
2.  Demonstrate an understanding of the Python List data type, Loops, and Slicing.
3.  Extend the functionality of Python by making use of a third-party package.
4.  Demonstrate an understanding of how to locate and use PyPI package documentation.
5.  Demonstrate an understanding of NumPy Arrays.


                                           ********** WEEK 2 **********

NOTE: In Week 1, we added three lists to the CMIT235_Tools.py. That is reused for this assignment.
We are also adding to the MyTest.py file and will do so throughout the class. In your weekly submissions,
it is very important to not delete or comment out code from a previous week's assignment.
Some future assignments will make use of code written in previous weeks.

In this assignment, you will practice creating a class (NetworkCheck) with methods,
creating an object which is an instance of that class, and then calling methods on your object to perform an action.
You will also work on increasing your understanding of loops and dictionaries.

Assignment Objectives:
1.  Demonstrate an understanding of Python Functions and Dictionaries.
2.  Demonstrate an understanding of Object Oriented Programming (OOP) concepts - Classes, Objects, and Methods.
'''
############################################################################################################################

import array

# Importing my personal information
import myInfo as mi

# Importing the CMIT235_Package class
import CMIT235_Package.CMIT235_Tools as cm
import CMIT235_Package.NetworkCheck as nc

# Import numpy
import numpy as np

# Displaying my personal information
#mi.displayInfo()

# Creating def to Combine the three sublists lists into one list

def combine(subList):
    # Store the combined list into a new variable.
    subarray = np.array(subList)
    # Print the combined list.
    print("Printing the combined list")
    print(subList)

    # Print the minimum value.
    print("\nThe minimum value is: ", subarray.min())

    # Print the maximum value.
    print("The maximum value is: ", subarray.max())

    # Print the unique values
    print("Unique values ", np.unique(subarray))

'''
Create a loop which iterates each of the three sublists 
and perform the following (NOTE: One loop (i.e. for loop) 
with three iterations, one iteration for each sublist).  
On each iteration of the loop:
'''

def allSubArray(subsArray):
    """Performs basic analysis on the provided numpy array."""

    # we'll start with some basic dimensional information

    print("\nPrinting the array \n", subsArray)

    print(f"\nPrinting the dimensions: {subsArray.ndim}")
    print(f"\nPrinting the shape: {subsArray.shape}")

    # Make use of Slicing to print the last number (item),
    print("Makeing use of Slicing to print the last number ")
    print("\nPrinting the last number", subsArray[-1, -1])
    print("Printing the first Column (column 0):", subsArray[:, 0])
    print("Printing the second row of the array:", subsArray[1])

# Combine the three sublists lists into one list
'''
allSub = [
    cm.allSublist,
    cm.mySubList3,
    cm.mySubList3,
]
'''
# This is how the sub lists are combined
combine(cm.mySubList1 + cm.mySubList2 + cm.mySubList3)
#print(allSub)

# Making use of Slicing to for the sub lists
# I have converted the sub lists to numpy arrays
for sublist in (cm.mySubList1, cm.mySubList2, cm.mySubList3):
    allSubArray(np.array(sublist))

############################################################################################################################
#                                   ********** WEEK 2 **********
# printing header for week 2
mi.week2()
'''
Will edit MyTest.py program and append the following to your code from the previous week.  
'''
# Will also Create an object of the NetworkCheck class and using that object
NetworkCheck = nc.NetworkCheck()

# Combining list for week 2
combineWeek2 = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
week2Array = NetworkCheck.convertList2NpArray(combineWeek2)

# Print the minimum value for week 2.
print("\nThe minimum value for week 2 is: ", NetworkCheck.getMin(week2Array))

# Print the maximum value  for week 2.
print("The maximum value for week 2 is: ", NetworkCheck.getMax(week2Array))

# Print the unique values  for week 2
print("Unique values for week 2 ", NetworkCheck.getUniqueValues(week2Array))

# printing Descriptive info function
print("\nPrinting description info fr week 2")
week2Descrip = NetworkCheck.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
for i, value in week2Descrip.items():
    print(" {} = {}".format(i, value))