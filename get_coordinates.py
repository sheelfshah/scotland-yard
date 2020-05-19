import cv2
import pickle

f=open("pos.txt", "r")
content=f.readlines()
useful_content=content[1:]
coordinates=[]
for line in useful_content:
	num_list=line.split()
	for i in range(len(num_list)):
		num_list[i]=int(num_list[i])
	coordinates.append(num_list[1:])

im = cv2.imread('bm5.jpg')

for i in range(len(coordinates)):
	xy=coordinates[i]
	xy=[xy[0]*4, xy[1]*4]
	xy=[xy[0]*730.0/3236,xy[1]*1200/4072]
	xy=[xy[0]*1.31,xy[1]*0.765]
	xy=[xy[0],xy[1]+70]
	coordinates[i]=xy

def pickle_coordinates(coordinates):
	pickle_saver=open('pickled_coordinates.obj', 'wb')
	pickle.dump(coordinates, pickle_saver)

def get_coordinates():
	filehandler = open('pickled_coordinates.obj', 'rb') 
	coordinates = pickle.load(filehandler)
	return coordinates

pickle_coordinates(coordinates)