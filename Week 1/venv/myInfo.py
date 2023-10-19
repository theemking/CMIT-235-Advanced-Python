''' This the info page '''
######################################################################
classInfo = {
    'name': 'Dony Pierre',
    'class': 'CMIT-235: Advanced Python',
    'week': 'Week 1',
    'date': 'September 3, 2023',
}

# Displaying my info

def displayInfo():
    keys = classInfo
    print("******************************************************")
    print("\t\t\t\t", keys['name'])
    print("\t\t\t\t", keys['class'])
    print("\t\t\t\t", keys['week'])
    print("\t\t\t\t", keys['date'])
    print("******************************************************")
    print("")

displayInfo()
######################################################################
