# This program takes in the data file from the hovering drone
# and discards all file that do not correspond with when
# the drone is at a height in multiple of 50

from math import cos, asin, sqrt

takeoff_lat = -1000;
takeoff_long = -1000;
time1 = -100 ; 
time2 = -100 ; 
filename = '56 4-27-2017 1-24-08 PM.bin.log';
f_read = open(filename, 'r');
f_write = open('temp.log', 'w');
flag = -1 ; 
x_tell = -1 ; 
x2_tell = -1 ; 
prev_altitude = 0 ; 

# finds the distance between end and starting points
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))*1000*3.28084 ;  #2*R*asin...

def writing_takeoff():
	global f_read; 
	global f_write; 
	global takeoff_lat ; 
	global takeoff_long ; 
	global x_tell ; 
	global x2_tell; 
	global time1; 
	global time2 ; 

	ty = ''; 
	while(ty != 'GPS'):
		tem = f_read.readline() ;
		temp = tem.strip().split(','); 
		f_write.write(tem); 
		ty = temp[0] ; 
		if(ty == 'GPS'):
			if(takeoff_lat == -1000 and takeoff_long == -1000):
				x_tell = f_read.tell() ; 
				takeoff_lat  = float(temp[6]);  
				takeoff_long = float(temp[7]); 
				time1 = int(temp[13]); 				

def main():
	global takeoff_lat; 
	global takeoff_long; 
	writing_takeoff() ;
	tt = 1 ;  
	f_read.close(); 
	f_write.close(); 
	f_special = open(filename,'r'); 
	f2 = open('trimmed_time.log','w');
	height = 0 ; 
	out_distance = 0 ; 
	tem = f_special.readline() ; 
	while(tem != ''): 
		temp = tem.strip().split(',');   
		if(temp[0] == 'GPS'):
			height = float(temp[8])*3.28084 ; 
			out_distance = distance(takeoff_lat,takeoff_long,float(temp[6]),float(temp[7])); 
			f2.write(tem)
		else : 
			f2.write(tem.strip() + ',' + str(height) + ',' + str(out_distance) + '\n'); 	
		tem = f_special.readline(); 

	
    

    


main()


