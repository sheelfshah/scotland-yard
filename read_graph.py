import json
import pickle

class Station:
	def __init__(self, number):
		self.number=number
		self.taxi_conn=[]
		self.bus_conn=[]
		self.underground_conn=[]
		self.boat_conn=[]

def add_conn(station1, station2, vehicle):
	if vehicle=="taxi":
		station1.taxi_conn.append(station2.number)
		station2.taxi_conn.append(station1.number)
	elif vehicle=="bus":
		station1.bus_conn.append(station2.number)
		station2.bus_conn.append(station1.number)
	elif vehicle=="underground":
		station1.underground_conn.append(station2.number)
		station2.underground_conn.append(station1.number)
	if vehicle=="boat":
		station1.boat_conn.append(station2.number)
		station2.boat_conn.append(station1.number)

f=open("graph.txt", "r")
content=f.readlines()
useful_content=content[200:]

all_stations=[]
for i in range(1,200):
	station=Station(i)
	all_stations.append(station)


for connection in useful_content:
	conn_list=connection.split()
	vehicle=conn_list[-1].lower()
	num1=int(conn_list[0])
	num2=int(conn_list[1])
	station1=all_stations[num1-1]
	station2=all_stations[num2-1]
	add_conn(station1, station2, vehicle)

count=0
for station in all_stations:
	count+=(len(station.taxi_conn)+len(station.bus_conn)+len(station.underground_conn)+len(station.boat_conn))

pickle_saver=open('pickled_game.obj', 'wb')
pickle.dump(all_stations, pickle_saver)

def get_game():
	filehandler = open('pickled_game.obj', 'rb') 
	game = pickle.load(filehandler)
	return game