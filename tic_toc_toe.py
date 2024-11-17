
import time
selection =[1,2,3,4,5,6,7,8,9]


def print_board():
	print("+----+----+----+")
	print("|    |    |    |\n|",selection[0]," |", selection[1], " |", selection[2]," |\n",\
	"+----+----+----+",\
	"\n|    |    |    |\n|",selection[3]," |", selection[4], " |", selection[5]," |\n",\
	"+----+----+----+",\
	"\n|    |    |    |\n|",selection[6]," |", selection[7], " |", selection[8]," |\n",\
	"+----+----+----+")
print_board()

print (" Start the game now. Player a has x and player b has o assign to them")


def updat(user):
		inpt = int  (input(f"User {user}  add your selection: " ))
		if user == 'a':
				selection[int(inpt) -1] = 'x'
		if user == 'b':
				selection[int(inpt) -1] = 'o'
		print("\n"*100)
		print_board()
		check()

def reset():
	selection[:]=[1,2,3,4,5,6,7,8,9]
	print("\n"*100)
	print_board()
	
	#	print_board()
#def IS_ON():
	#TODO chenk if game is over yet
def check():
	if selection[0]	== selection[1]	== selection[2]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[3]	== selection[4]	== selection[5]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[6]	== selection[7]	== selection[8]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[0]	== selection[3]	== selection[6]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[1]	== selection[4]	== selection[7]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[2]	== selection[5]	== selection[8]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[0]	== selection[4]	== selection[8]	:	
		print("Game over!: ")
		time.sleep(5)
		reset()
	if selection[2]	== selection[4]	== selection[6]	:
		print("Game over!: ")
		time.sleep(5)
		reset()
		
updat("a")
updat("b")
updat("a")
updat("b")
updat("a")
updat("b")
updat("a")
updat("b")
