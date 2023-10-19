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

                                            ********** WEEK 3 **********

In this exercise, you will work with a file (cmit235_network_data.pcapng) which contains a dump of data packets
captured over a network. You will read a data packet file, iterate over every packet in the file,
and get the number of packets meeting a certain condition.

As with every assignment, please be sure to submit all your code (three .py files) and a screenshot of the code executing
in your environment, and do not delete any code from a previous week's submissions as you are appending code to your
Week 2 submission.

Assignment Objectives:
1.  Demonstrate an understanding of Object Oriented Programing (OOP) concepts - Attributes/Properties, Getters,
and Setters.
1.  Demonstrate how to read package documentation and implement features using the package documentation (scapy)


                                            ********** WEEK 4 **********

In this exercise, you will demonstrate an understanding of overloading and overriding.
Please be sure to submit the four .py files and a screenshot of the code executing in your environment.
It is important to submit both.

Assignment Objectives:
Demonstrate an understanding of Object Oriented Programming (OOP) concepts - Overloading and Overriding.
'''
############################################################################################################################

import array

# Importing my personal information
import myInfo as mi

# Importing the CMIT235_Package class
import CMIT235_Package.CMIT235_Tools as cm
import CMIT235_Package.NetworkCheck as nc
import scapy.all as scapy
# Import numpy
import numpy as np
from CMIT235_Package.NewNetworkCheck import NewNetworkCheck

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

############################################################################################################################
#                                   ********** WEEK 2 **********
# printing header for week 3
mi.week3()

'''
Will Try to directly get the private message1 attribute. I will be using a TRY/EXCEPT.
'''
try:
    messageOne = NetworkCheck.message1
except AttributeError:
    print("\nCould not message 1 because it's private")

try:
    messageOne = NetworkCheck.__message1
except AttributeError:
    print("Could not message 1 because it's private")

# Using the getter method to get the private message1 attribute.
message1 = NetworkCheck.getMessage1()

# Using the getter method to get the private message2 attribute.
message2 = NetworkCheck.getMessage2()

# Using the getter method to get the private message3 attribute.
message3 = NetworkCheck.message3
print(f"\nMessage1: {message1}\tMessage2:{message2}\tMessage3:{message3}")
print("Packet Data")

# Calling setSource with pcap and mac address perameter
NetworkCheck.setSourceMacCount(cm.pcap, cm.mac_address)
macCount = NetworkCheck.getSourceMacCount()
# Printing the mac info
print(f"Number of packets with a source MAC address {cm.mac_address}: {macCount}")

# Call the getter and setter to obtain and print the private value of mac_count
NetworkCheck.setSourcePortCount(cm.pcap, cm.sport)
portCount = NetworkCheck.getSourcePortCount()
# Printing the port infor
print(f"Number of UDP packets with source port {cm.sport}: {portCount}")

############################################################################################################################
#                                   ********** WEEK 4 **********
# printing header for week 4
mi.week4()

# Create an object for the NewNetworkCheck class and use that object:
subWorkCheck = NewNetworkCheck()
'''
Call the getDescriptiveInfo method passing all three sublists 
to the method, to obtain a dictionary of key:value pairs 
for the dimension, shape, mean, median, and standard deviation.
How to code this is up to you, however you should be accessing 
values in your returned dictionary by a key, and printing 15 values.
'''
week4Descrip = subWorkCheck.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
for i, val in week4Descrip.items():
    print(" {} = {}".format(i, val))

# Calling checkCounts and passing the csv_data file and feature3.
print('\nPrinting the Features')
ft3Count = subWorkCheck.checkCounts(cm.csv_data, cm.feature3)
print(f"{cm.feature3}:\n{ft3Count}")

# Call checkCounts passing the csv_data file and feature1, feature2, and feature3.
print("Printing feature1, feature2, and feature3")
allFeatures = subWorkCheck.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3)
for ft, counts in allFeatures.items():
    print(f"{ft}:\n{counts}\n")