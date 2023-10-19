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


                                            ********** WEEK 5 **********
Assignment Objectives:
Demonstrate an understanding of Object Oriented Programming (OOP) concepts - Inheritance.

Part 1. Demonstrate an understanding of inheritance by showing how the existing NewNetworkCheck inherits
from NetworkCheck

Part 2. Demonstrate an understanding of inheritance where one class (AddedNetworkCheck) inherits the attributes
and methods from another class (NewNetworkCheck).
Edit MyTest.py program and append the following to your code from the previous week.

                                            ********** WEEK 6 **********
This week's assignment involves working with logging and error handling. You will not add any additional classes
or methods; instead, you will add logging and additional error handling to your existing code in MyTest.py.

                                            ********** WEEK 7 **********

'''
############################################################################################################################

import array

# Importing my personal information
import myInfo as mi

# Importing the CMIT235_Package class
import CMIT235_Package.CMIT235_Tools as cm
import CMIT235_Package.NetworkCheck as nc
import scapy.all as scapy
import numpy as np
from CMIT235_Package.NewNetworkCheck import NewNetworkCheck
from CMIT235_Package.NetworkCheck import NetworkCheck
from CMIT235_Package.AddedNetworkCheck import AddedNetworkCheck
import sys
import logging

# Displaying my personal information

# Creating a log file and set the level to logging.DEBUG.
logging.basicConfig(filename="CIT23_Network.log", level=logging.DEBUG)

# Adding a logging INFO statement
logging.info("The MyTest Program is starting!")


# This function will print logs and error message then exit
def abortFile(message, exit_code=1):
    logging.error(message)
    print(f"\nERROR - {message} - ABORTING")
    sys.exit(exit_code)

#seting up print heading
def print_heading(phweek7):
    print(f"\n{'-' * 25}{phweek7} {'-' * 25}\n")

# Creating def to Combine the three sublists lists into one list
def combine(subList):
    # Store the combined list into a new variable.
    subarray = np.array(subList)
    # Print the combined list.
    print("\nPrinting the combined list")
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
    print("Making use of Slicing to print the last number ")
    print("\nPrinting the last number", subsArray[-1, -1])
    print("Printing the first Column (column 0):", subsArray[:, 0])
    print("Printing the second row of the array:", subsArray[1])


# Combine the three sublists lists into one list
'''
combined the three sublists into one list and stored the combined list into a new variable 
(i.e. combined_list). Update this code to print and log an error message (logging.error) and exit the program 
(sys.exit) when your combined list is not of the type list.
'''
combined_list = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
if not isinstance(combined_list, list):
    abortFile(f"The combined list is a type instead of a list {type(combined_list)}")

# This is how the sub lists are combined
combine(cm.mySubList1 + cm.mySubList2 + cm.mySubList3)
# print(allSub)

# Making use of Slicing to for the sub lists
# I have converted the sub lists to numpy arrays
for sublist in (cm.mySubList1, cm.mySubList2, cm.mySubList3):
    allSubArray(np.array(sublist))

############################################################################################################################
#                                   ********** WEEK 2 **********
# printing header for week 2
mi.week2()

'''
creating an object that should be an instance of the NetworkCheck class and 
Updating this code to print and log an error message and exit the program when the 
object is not an instance of the NetworkCheck class.
Will edit MyTest.py program and append the following to your code from the previous week.  
'''
# Will also Create an object of the NetworkCheck class and using that object
networkCheckW2 = nc.NetworkCheck()
if not isinstance(networkCheckW2, nc.NetworkCheck):
    abortFile(f"This is a type. The object is not an instance of the NetworkCheck class. {type(NetworkCheck)}")

logging.info("The Networkcheck is created")

# Combining list for week 2
combineWeek2 = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
week2Array = networkCheckW2.convertList2NpArray(combineWeek2)

# This will raise an exception when the minimum value is less than -100.
week2min = networkCheckW2.getMin(week2Array)
if week2min < -100:
    raise RuntimeError(f"Invalid minimum {week2min} The minimum should be at lease -100")

# This will raise an exception when the minimum value is less than -100.
week2max = networkCheckW2.getMax(week2Array)
if week2max > 100:
    raise RuntimeError(f"Invalid maximum {week2max} The minimum should be not be more 100")

# Print the minimum value for week 2.
print("The minimum value is: ", week2min)
# Print the maximum value  for week 2.
print("The maximum value is: ", week2max)
# Print the unique values  for week 2
print("Unique values for week 2 ", networkCheckW2.getUniqueValues(week2Array))

# printing Descriptive info function
print("\nPrinting description info for week 2")
week2Descrip = networkCheckW2.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
if not isinstance(week2Descrip, dict):
    abortFile(f"Week2Descrip should be a dic but it's a type {type(week2Descrip)}")

for i, value in week2Descrip.items():
    print(" {} = {}".format(i, value))

############################################################################################################################
#                                   ********** WEEK 3 **********
# printing header for week 3
mi.week3()

'''
Will Try to directly get the private message1 attribute. I will be using a TRY/EXCEPT.
'''
try:
    messageOne = networkCheckW2.message1
except AttributeError:
    print("\nCould not access message 1 because it's private")

try:
    messageOne = networkCheckW2.__message1
except AttributeError:
    print("Could not access message 1 because it's private")

# Using the getter method to get the private message1 attribute.
message1 = networkCheckW2.getMessage1()

# Using the getter method to get the private message2 attribute.
message2 = networkCheckW2.getMessage2()

# Using the getter method to get the private message3 attribute.
message3 = networkCheckW2.message3
print(f"\nMessage1: {message1}\tMessage2:{message2}\tMessage3:{message3}")
print("Packet Data")

'''
Updating this code to print and log an error message 
 and exit the program for the following two conditions:
'''
try:
    networkCheckW2.setSourceMacCount(cm.pcap, cm.mac_address)
except Exception as ex:
    abortFile(f"Unable to access File {cm.pcap}:{ex}")

sourceMacWeek6 = networkCheckW2.getSourceMacCount()
if not isinstance(sourceMacWeek6, int):
    abortFile(f"Source Mac should be an integer not a type {type(sourceMacWeek6)}")

# Printing the mac info
print(f"Number of packets with a source MAC address {cm.mac_address}: {sourceMacWeek6}")

try:
    networkCheckW2.setSourceMacCount(cm.pcap, cm.sport)
except Exception as ex:
    abortFile(f"Could not access {cm.pcap}: {ex}")

# Call the getter and setter to obtain and print the private value of mac_count
sourcePortWeek6 = networkCheckW2.getSourcePortCount()
if not isinstance(sourcePortWeek6, int):
    abortFile(f"The source port count should be an integer not a type {type(sourcePortWeek6)}")
# Printing the port infor
print(f"Number of UDP packets with source port {cm.sport}: {sourcePortWeek6}")

############################################################################################################################
#                                   ********** WEEK 4 **********
# printing header for week 4
mi.week4()

# Create an object for the NewNetworkCheck class and use that object:
subWorkCheck = NewNetworkCheck()

'''
Updating this code to print and log an error message and exit the program 
when your object is not an instance of the NewNetworkCheck class.
'''
if not isinstance(subWorkCheck, NewNetworkCheck):
    abortFile(f"The new network check should be a a network check not a type {type(networkCheckW2)}")

logging.info("A new network check instance was created")

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

############################################################################################################################
#                                   ********** WEEK 5 **********
# printing header for week 5
mi.week5()

week5CombineList = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
arrayWeek5 = subWorkCheck.convertList2NpArray(week5CombineList)

# Printing values for New network check object
print("This the minimum value for week 5: ", subWorkCheck.getMin(arrayWeek5))
print("This the maximum value for week 5: ", subWorkCheck.getMax(arrayWeek5))
print("This the unique value for week 5: ", subWorkCheck.getUniqueValues(arrayWeek5))

# Creating an object of the AddedNetworkCheck class and use that object
addNTCheck = AddedNetworkCheck()

'''
Update this code to print and log an error message and exit the program 
when the value returned from getPingCount is not of type int
'''
if not isinstance(addNTCheck, AddedNetworkCheck):
    abortFile(f"The Add Network should not be a type but a network check {type(addNTCheck)}")

logging.info("An Added Network Check was created")

# Calling getPingCount passing the pcap file.
# Set the return value to a variable and print the contents of the variable.
pingcount5 = addNTCheck.getPingCount(cm.pcap)
if not isinstance(pingcount5, int):
    abortFile(f"The ping count should be an int not a type {type(pingcount5)}")
print(f"\n The number of TCP packets with in the window size 4095 is: {pingcount5}")

# Call setSourceMacCount passing the pcap file and the mac address
addNTCheck.setSourceMacCount(cm.pcap, cm.mac_address)
print(f"\n The number of packets with sources MAC address {cm.mac_address}: {addNTCheck.getSourceMacCount()} ")
print(f"\n{cm.feature3}: \n{addNTCheck.checkCounts(cm.csv_data, cm.feature3)}")

############################################################################################################################
#                                   ********** WEEK 7 **********
# printing header for week 6
mi.week7()

# Checking inheritance
inherit = lambda child, parent: issubclass(child, parent) or \
                                (_ for _ in ()).throw(
                                    TypeError(parent.__name__ + "is not a parent of " + child.__name__))


# Creating a fuction and using recursive to go through the list
def recurList(arrList7):
    length = len(arrList7)
    if length == 1:
        print("\n\nThe Week 7 list value is:", arrList7[0])
    elif length > 0:
        arr = length // 2
        recurList(arrList7[:arr])
        recurList(arrList7[arr:])


# calling the “callSuper” method and order to pass the list mySubList2 .
subWorkCheck.callSuper(cm.mySubList2)
print("\nChecking New Network Check subclassing using anonymous function")
try:
    if inherit(NewNetworkCheck, NetworkCheck):
        print("The NewNetworkCheck is a subclass of NetworkCheck")
except TypeError as er:
    abortFile(str(er))

# Using the AddedNetworkCheck object, call the “callGrandparent” method.
print("\nCalling the grandparent method from Add Network Check")
addNTCheck.callGrandparent(cm.mySubList3)

'''Checking if AddedNetworkCheck is a subclass of NetworkCheck
and If it is, will print a message stating such'''
try:
    if inherit(addNTCheck, NetworkCheck):
        print("AddedNetworkCheck is a subclass of NetworkCheck")
except TypeError as ex:
    abortFile(str(ex))

print_heading("Printing the recursion")
recurList(cm.mySubList1[0])
