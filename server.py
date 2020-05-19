import socket
from _thread import start_new_thread
import sys
import pickle
from game import Game

server=""
port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	print(e)

s.listen()
print("Waiting for a connection ... Server started")

connected=set()
games={}
idCount=0
lastGameId=0

def threaded_client(connection,player, gameId):
	global idCount
	connection.send(str.encode(str(player)))

	reply=""
	while True:
		try:
			data=connection.recv(4096).decode()
			if gameId in games:
				game= games[gameId]
				if not data:
					break
				else:
					if data=="mrxplayed":
						game.resetDetectives()
					elif data=="detectivesplayed":
						game.resetMrx()
					elif data !="get":
						game.play(player,data)

					reply=game
					connection.sendall(pickle.dumps(reply))
			else:
				break
		except:
			break

	print("Connection ended")
	#TODO: change game deletion behaviour to setting game as not ready when a player leaves
	#	   and deleting the game if all players leave
	if idCount%6==1:
		try:
			del games[gameId]
			print("Closing game ", gameId)
		except:
			pass
	else:
		games[gameId].ready-=1
	connection.close()

currentPlayer=0
while True:
	conn, addr= s.accept()
	print("Connected to ", addr)
	currentGameId=None
	for gameId in games:
		if not games[gameId].connected():
			currentGameId=gameId
			break
	if currentGameId==None:
		games[lastGameId+1]=Game(lastGameId+1)
		lastGameId+=1
		currentGameId=lastGameId
		print("New game being created ...")
	games[currentGameId].ready+=1
	p=(games[currentGameId].ready-1)%6
	start_new_thread(threaded_client, (conn,p,currentGameId))