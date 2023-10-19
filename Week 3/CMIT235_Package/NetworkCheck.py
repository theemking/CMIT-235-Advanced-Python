'''
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

# Create a module under the CMIT235_Package and naming it NetworkCheck.py.

import numpy as np
from scapy.contrib.gxrp import mac
from scapy.utils import rdpcap
from scapy.layers.l2 import Ether
from scapy.layers.inet import UDP

# creating a new Python Class named NetworkCheck
class NetworkCheck:
    '''
    Edit the NetworkCheck.py module,
    in the constructor add private, protected, and public attributes,
    and outside the constructor add four getters and two setter methods:
    '''
    def __init__(self):
        self.__mac_count =0
        self.__sport_count =0
        self.__message1 = "Welcome to message 1"
        self._message2 = "Welcome to message 2"
        self.message3 = "Welcome to message 3"

    def convertList2NpArray(self, source) -> np.ndarray:
        return np.array(source)

    '''
    This getMax function will get and return the maximum value of an array. 
    This will take a nparray as input.
    '''
    def getMax(self, nparray: np.ndarray):
        return np.amax(nparray)

    '''
    This getMin function will get and return the maximum  value of an array. 
    This will take a nparray as input.
    '''
    def getMin(self, nparray: np.ndarray):
        return np.amin(nparray)

    '''
    This getUniqueValues function will get and return the unique value of an array. 
    This will take a nparray as input.
    '''
    def getUniqueValues(self, nparray: np.ndarray):
        return np.unique(nparray)

    '''
    The getDescriptiveInfo function will return a dictionary of key:value 
    pairs for the number of dimensions, shape, and slices of the last item, 
    first column (column zero), and the second row of each list.  
    If there are three lists, and five values (i.e. number of dimensions, shape, last item...) 
    for each list, then the returned dictionary would contain 15 key value pairs.
    This should take all three lists as input.
    '''
    def getDescriptiveInfo(self, *lists):
        listDic ={}

        # Will iterate over the lists
        for i, lis in enumerate(lists, start=1):
            nparray = np.array(lis)

            # Preparing Dimension, shape, last number and column 0 for Display
            listDic["The Dimension is: "] = nparray.ndim
            # Displaying the shape
            listDic["The shape is: "] = nparray.shape
            # Displaying the last number
            listDic["The last number is: "] = nparray[-1, -1]
            # Displaying Column 0
            listDic["Column 0: "] = nparray[:, 0]

            return listDic

    ##############################   WEEK 3     ##############################
    '''
    Will create the following functions within the class :
    The function will take the combined lists
    (mySubList1 + mySubList2 + mySubList3)  as input (one parameter value).
    '''

    # this getter will return the welcome message
    def getMessage1(self):
        return self.__message1

    # this getter will return the welcome message
    def getMessage2(self):
        return self._message2

    # this getter will return the welcome message
    def getMessage3(self):
        return self.message3
    # Creating getter method for sport
    def getSourcePortCount(self):
        return self.__sport_count

    # Creating setter  method for sport
    '''
    The setSourcePortCount takes two parameters, the contents of the pcap file and a port number. 
    Iterate over all the packets and calculate the number of UDP packets with an sport 
    of the port number passed into the method.  Set the private attribute sport_count 
    to the value you just calculated.
    '''
    def setSourcePortCount(self, pcap, port):
        count = 0
        packet = rdpcap(pcap)
        for pk in packet:
            if pk.haslayer(UDP) and pk[UDP].sport == port:
                count += 1
        self.__sport_count = count

    '''
    getSourceMacCount takes two parameters, the contents of the pcap file and an MAC address. 
    Iterate over all the packets and calculate the number of packets with a source MAC address of the 
    MAC addressed passed into the method.  Set the private attribute mac_count the value you just calculated.
    '''
    def getSourceMacCount(self):
        return self.__mac_count
    '''
    setSourceMacCount takes two parameters, the contents of the pcap file and an MAC address. 
    Iterate over all the packets and calculate the number of packets with a source MAC address of the 
    MAC addressed passed into the method.  Set the private attribute mac_count the value you just calculated.
    '''
    def setSourceMacCount(self, pcap, mac):
        count = 0
        packet = rdpcap(pcap)
        for pk in packet:
            if pk.haslayer(Ether) and pk[Ether].src == mac:
                count += 1
        self.__mac_count = count












