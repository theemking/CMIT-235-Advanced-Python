'''
******************************************************
				 Dony Pierre
				 CMIT-235: Advanced Python
				 Week 5
				 October 1, 2023
******************************************************
'''
# Importing NetworkCheck from CMIT235_Package
from CMIT235_Package.NetworkCheck import NetworkCheck
import numpy as np

'''
To begin I will create a new Python Class named NewNetworkCheck which inherits from the NetworkCheck class.  
Within the class:
'''
class NewNetworkCheck(NetworkCheck):
    # Creating a constructor which calls the constructor in the parent.
    def __init__(self):
        super().__init__()

    '''
    Creating one new method getDescriptiveInfo which will override 
    the getDescriptiveInfo method in the NetworkCheck class. 
    '''
    def getDescriptiveInfo(self, *lists):
        '''
        getDescriptiveInfo will return a dictionary of key:value pairs for the number of
        dimensions, shape, mean, median, and standard deviation for each array
        (each list converted to an array).  If there are three lists and five values for each list,
        then the returned dictionary would contain 15 key-value pairs. This should take all three lists as input.
        :param lists:
        :return:
        '''
        listDic = {}
        for i, ls in enumerate(lists, start=1):
            nparray = np.array(ls)

            # Preparing Dimension, shape, last number and column 0 for Display
            listDic["The Dimension is: "] = nparray.ndim
            # Displaying the shape
            listDic["The shape is: "] = nparray.shape
            # Displaying the mean
            listDic["The mean is: "] = np.mean(nparray)
            # Displaying the mediam
            listDic["The shape is: "] = np.median(nparray)
            # Displaying the last number
            # Displaying the standard deviation
            listDic["Showing standard deviation: "] = np.std(nparray)

            return listDic