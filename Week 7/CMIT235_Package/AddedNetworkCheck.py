'''
******************************************************
				 Dony Pierre
				 CMIT-235: Advanced Python
				 Week 5
				 October 1, 2023
******************************************************
'''
from scapy.utils import rdpcap
from scapy.layers.inet import TCP

# Import NewNetworkCheck from CMIT235_Package.NewNetworkCheck
from CMIT235_Package.NewNetworkCheck import NewNetworkCheck
'''
Part 2. Demonstrate an understanding of inheritance where one class (AddedNetworkCheck) 
inherits the attributes and methods from another class (NewNetworkCheck).
'''

# Create a new Python Class named AddedNetworkCheck which inherits from the NewNetworkCheck class. Within the class:
class AddedNetworkCheck(NewNetworkCheck):
    #Create a constructor which calls the constructor in the parent.
    def __init__(self):
        super().__init__()

    '''
    Adding a new method, getPingCount which takes the pcap file as a parameter.
    terate over all the packets, calculating and returning the number of TCP packets 
    where the window property is 4095.
    '''
    def getPingCount(self, pcap):
        count =0
        for pc in rdpcap(pcap):
            if pc.haslayer(TCP) and pc[TCP].window == 4095:
                count += 1

        return count

    #Creating a method called callGrandparent which takes an array as a parameter
    def callGrandparent(self, gpArray7):
        #Call the grandparent’s getMax method.
        gpMax = super(NewNetworkCheck, self).getMax(self.convertList2NpArray(gpArray7))
        print(f"The maximum value result for Added Network Check is: {gpMax}")


