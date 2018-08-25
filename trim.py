# This program takes in the data file from the hovering drone
# and discards all file that do not correspond with when
# the drone is at a height in multiple of 50

from math import cos, asin, sqrt

takeoff_lat = 0
takeoff_lon = 0
filename = 'test3.log'
f1 = open(filename, 'r')
f2 = open('(Filename).log', 'w')

# finds the distance between end and starting points
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))*1000*3.28084 ;  #2*R*asin...

def main():
    global f1; global f2;
    a = f1.readline().strip().split(',')
    while(a[0]!=''):
        if a[0] == 'GPS': # finds the starting point GPS data
            global takeoff_lat
            global takeoff_lon
            takeoff_lat = a[2] # used as starting latitude for height calculation
            takeoff_lon = a[3] # used as starting longitude for height calculation
            a = ','.join(map(str, a))
            f2.write(a + '\n')
            break
        a=f1.readline().strip().split(',')


    a = f1.readline().strip().split(',')
    while(a[0]!='GPS'): # writes all following data until second GPS data
        a = ','.join(map(str, a))
        f2.write(a + '\n')
        a = f1.readline().strip().split(',')

    while(a[0] == 'GPS'):
        if (distance(takeoff_lat, takeoff_lon, a[2], a[3]) % 50 == 0): # height is multiple of 50
            a = ','.join(map(str, a))
            f2.write(a + '\n')
            a = f1.readline().strip().split(',')
            while(a[0] != 'GPS' and a[0]!=''): # reads the rest of the data until it reaches new GPS data
                a = ','.join(map(str, a))
                f2.write(a + '\n')
                a = f1.readline().strip().split(',')
        else:
            while(a[0] != 'GPS' and a[0]!=''): # dumps the rest of the data until it reaches a new GPS data
                a=f1.readline().strip().split(',')
    print ('finish')


main()


