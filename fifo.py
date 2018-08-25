import queue
import io
import matplotlib.pyplot as plt

q = queue.Queue()
dataArray = []
amplitudeList = [] #stores amplitude at each time stamp
timeList = [] # stores each time stamp value
passRate = [] # stores the pass rate at each time stamp


# takes the file stream and puts it into a queue
def toQueue():
    global q
    file = io.open('File name', 'r')
    if file.readable():
        for line in file:
            q.put(line)
        return True
    else:
        return False

# transfers the data from the queue to an array to allow for easy
# access and manipulation
def queueToArray():
    global q
    while q.qsize() > 0:
        dataArray.append(q.get())


# puts line into array and splits the line to get
# the amplitude value by itself and
# returns the amplitude value as an int
def processAmplitude(line):
    line1 = line.split(",")
    return int(line1[5].split()[1])


# plots the data
def graph():
    global timeList
    plt.ion()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    global amplitudeAverages
    for i in range(len(timeList)):
        plt.scatter(timeList[i], amplitudeList[i], s = 10, color = 'g') # plots amplitude
        plt.pause(0.001)
    plt.show()


# puts the line into an array and continues to split the string to
# get the pass rate value by itself. Returns that value as a float
def processPassRate(line):
    line1 = line.split(",")
    percentage = (line1[8].split(":")[1])
    split2 = (percentage.split())
    return (float(split2[0]))

def main():
    if toQueue():
        queueToArray()
        for index in dataArray:
            if 'Timestamp' in index: # processes the line that includes the amplitude and pass rate values
                global amplitudeList
                global passRate
                amplitudeList.append(processAmplitude(index))
                passRate.append(processPassRate(index))
            else: # processes the time stamp of the data
                global timeList
                line = index.split()
                line = float(line[0]) # splits the line into array to get time stamp value by itself
                timeList.append(line) # the float time stamp cuts off last 4 decimal points
        graph()
    else:
        print('File is not readable')



main()



