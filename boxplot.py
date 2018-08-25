# This program creates a boxplot for each
# waypoint .txt file that is inputted from the user

import matplotlib.pyplot as plt

overallData = [] # stores the amplitude value at each timestamp for each waypoint data
groundDistance = [] # stores the horizontal distance of the drone
heightDistance = []

# processes the input file and inputs the amplitude value to the list
def fillData(f, data):
    for line in f:
        line1 = line.split(",")
        value = int(line1[5].split()[1])
        data.append(value)
    return data

# takes the amplitude data and creates a boxplot for each waypoint file
def graph():
    global overallData
    global groundDistance
    global heightDistance
    plt.figure(1)
    plt.boxplot(overallData)
    plt.xlabel('Ground Distance')
    plt.ylabel('Amplitude')
    xvalues = list(range(len(groundDistance)+1))
    del xvalues[0]
    plt.xticks(xvalues, groundDistance, rotation=45) #names each boxplot with their corresponding ground distance

    plt.figure(2)
    plt.boxplot(overallData)
    plt.xlabel('Height Distance')
    plt.ylabel('Amplitude')
    plt.xticks(xvalues, heightDistance, rotation=45) #names each boxplot with their corresponding height distance
    plt.show()

def main():
    answer = input('Do you want to plot (Y/N)? ')
    while answer == 'Y' or answer == 'y' :
        data = [] #temporary list that stores the amplitude value from one waypoint file
        groundDistance.append(input('Enter ground distance:'))
        heightDistance.append(input('Enter height distsance:'))
        file = input('Enter in full file name: ')
        f = open(file, 'r')
        overallData.append(fillData(f, data))
        answer = input('Do you want to add another plot (Y/N)? ')
    graph()


main()
