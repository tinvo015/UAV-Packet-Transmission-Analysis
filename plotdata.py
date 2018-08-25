# This program takes in the telementary datalog text file
# and plots the running amplitude average as well as the pass rate
# at each time stamp.

import matplotlib.pyplot as plt

amplitudeSum = 0 # keeps track of sum of the amplitude to find the average
amplitudeAverages = [] # stores avg amplitude for each time stamp
amplitudeList = [] #stores amplitude at each time stamp
timeList = [] # stores each time stamp value
passRate = [] # stores the pass rate at each time stamp


# puts line into array and splits the line to get
# the amplitude value by itself and
# returns the amplitude value as an int
def processAmplitude(line):
    line1 = line.split(",")
    return int(line1[5].split()[1])


# plots the data on 2 separate plots: one for the running amplitude avg
#                                     the other for the pass rate at each time stamp
def graph():
    global timeList
    plt.ion()
    plt.figure(1); plt.xlabel('Time Stamp'); plt.ylabel('Running Amplitude Average')
    plt.figure(2); plt.xlabel('Time Stamp'); plt.ylabel('Pass Rate (%)')
    plt.figure(3); plt.xlabel('Time Stamp'); plt.ylabel('Amplitude')
    global amplitudeAverages
    for i in range(len(timeList)):
        plt.figure(1); plt.scatter(timeList[i], amplitudeAverages[i], s = 10, color = 'r') # plots the amplitude averages
        plt.figure(2); plt.scatter(timeList[i], passRate[i], s = 10, color = 'b', ) # plots the pass rate values
        plt.figure(3); plt.scatter(timeList[i], amplitudeList[i], s = 10, color = 'g') # plots amplitude
        plt.pause(0.001)
    plt.show()


# puts the line into an array and continues to split the string to
# get the pass rate value by itself. Returns that value as a float
def processPassRate(line):
    line1 = line.split(",")
    percentage = (line1[8].split(":")[1])
    split2 = (percentage.split())
    return (float(split2[0]))


# takes in the file and graphs the running amplitude avg and pass rate
# at each time stamp
def main():
    file = open("RF_G200_H200_DD_H_North_2495.txt", "r") #reads the input file
    for line in file:
        if 'Timestamp' in line: # processes the line that includes the amplitude and pass rate values
            global amplitudeSum
            global amplitudeAverages
            global amplitudeList
            global passRate
            amplitudeList.append(processAmplitude(line))
            amplitudeSum += amplitudeList[-1] # updates the sum of all amplitudes
            amplitudeAverages.append(amplitudeSum/(len(amplitudeAverages) + 1)) # adds running average amplitude
            passRate.append(processPassRate(line))
        else: # processes the time stamp of the data
            global timeList
            line = line.split()
            line = float(line[0]) # splits the line into array to get time stamp value by itself
            timeList.append(line) # the float time stamp cuts off last 4 decimal points
    graph()


main() # performs main function
