import random



class Game:
	def __init__ (self,id):
		start_positions=[29,26,103,53,132,112,198,155,197,34,13,141,50,94,91,138,117,174]
		random.shuffle(start_positions)
		self.detectivesWent=[True, True, True, True, True]
		self.mrxWent=False
		self.ready=0	#number of players ready
		self.id=id
		self.moves=start_positions[:6]
		self.moveNumber=0
		self.lastKnownMove="Unknown"
		self.transports=[[4,3,3,5,2],[10,8,4],[10,8,4],[10,8,4],[10,8,4],[10,8,4]]
		self.mrxVehicle="null"
		self.dictionary={"taxi":0, "bus":1, "underground":2, "blackticket":3, "double": 4}
		self.gameOver=False

	def get_player_move(self, p):
		# p is 0,1,2,3,4,5 (mrx,d1,d2,...)
		# returns move played by that player 
		return self.moves[p]

	def play(self,player,move):
		#take care with player-number of detectives
		#assumes move is always valid
		if move[0]=="2":
			pos_list=move[1:].split()
			move1=pos_list[0]
			move2=pos_list[1]
			v1=self.play(player, move1)
			v2=self.play(player, move2)
			self.mrxVehicle=v1+", " +v2
			self.transports[player][4]-=1
		else:
			move, vehicle=pre_process(move, player)
			self.moves[player]=move
			vehicle_number=self.dictionary[vehicle]
			self.transports[player][vehicle_number]-=1
			if player==0:
				self.mrxWent=True
				self.moveNumber+=1
				self.mrxVehicle=vehicle
				if self.moveNumber in [3,8,13,18,24]:
					self.lastKnownMove=self.moves[0]
					if self.moveNumber==24:
						self.gameOver=True
				return vehicle
			else:
				self.detectivesWent[player-1]=True
				self.transports[0][vehicle_number]+=1

	def connected(self):
		return self.ready==6

	def allDetectivesWent(self):
		flag=True
		for i in range(5):
			flag=(flag and self.detectivesWent[i])
		return flag

	def caught(self):
		caught=False
		if self.moves[0] in self.moves[1:]:
			caught=True
		if self.moves[0]==None:
			return False
		return caught

	def resetDetectives(self):
		self.detectivesWent=[False, False, False, False, False]

	def resetMrx(self):
		self.mrxWent=False

def pre_process(string, player):
	string=string.lower()
	if player>0:
		if string[0]=="t":
			pos=string[1:]
			pos=int(pos)
			return pos,"taxi"
		elif string[0]=="b":
			pos=string[1:]
			pos=int(pos)
			return pos,"bus"
		elif string[0]=="u":
			pos=string[1:]
			pos=int(pos)
			return pos,"underground"
	else:
		if string[0]=="t":
			pos=string[1:]
			pos=int(pos)
			return pos,"taxi"
		elif string[0]=="b": 
			pos=string[1:]
			pos=int(pos)
			return pos,"bus"
		elif string[0]=="u":
			pos=string[1:]
			pos=int(pos)
			return pos,"underground"
		elif string[0]=="x":
			pos=string[1:]
			pos=int(pos)
			return pos,"blackticket"
         