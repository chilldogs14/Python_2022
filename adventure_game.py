######################
#IMPORTS
######################
from adventurelib import *

######################
#DEFINE ROOOMS
######################
hanger = Room("you are standing in a hanger with stairs oposite you which are east. in the conner you see some lockers and a table and chairs.")
lockers = Room("you are standing in the middle of the row of lockers. one of the lockers are unlock.")
hallway_1 = Room("you are standing at the base of the stairs. in front of you a hallway and to your right there is another hallway.")
hallway_2 = Room("there are to doors on both sides of you and the hallway continues east.")
hallway_3 = Room("to your left there is a supply closet and to your right lab 2. the hallway ends.")
hallway_4 = Room("you are in the hallway there are no door but the hallway continues south.")
hallway_5 = Room("you are at the bend in the hallway. the hallway continues east.")
outside_vualt = Room("you are in front of the vualt. the door to the vualt looks huge. there is a pin pad.")
office_1 = Room("you are in the first office. there is a couch, a bookshelf, a desk with a chair.")
office_2 = Room("you are in the second office. it is almost the same as the first office but there is a folder on the desk.")
supply_closet = Room("you are in the supply closet. in here there are cleaning products, brooms, and a draw full of gloves.")
lab_1 = Room("you are in the first lab. there are test tubes and lab coats.")
lab_2 = Room("you are in the second lab. there are test tubes and lab coats. at one of the benches there is a scientist. there is an exit near the scienist.")
boiler_room = Room("you are in the boiler room. there are pipes, steam and water all over the floor. there is an exit in front of you.")
quarters = Room("you are in the caretakers quarters. there is a photo with the founders and on the end of the row the caretaker is there. there is a bed and a table and chair.")
vault_7 = Room("you are in the vualt and see broken containment pods and aliens all over the floor, walls and ceiling.")

######################
#DEFINE CONNECTIONS
######################
hanger.west = lockers
hanger.east = hallway_1
hallway_1.north = office_1
hallway_1.south = hallway_4
hallway_1.east = hallway_2
hallway_2.north = office_2
hallway_2.south = lab_1
hallway_2.east = hallway_3
hallway_3.north = supply_closet
hallway_3.south = lab_2
hallway_4.south = hallway_5
hallway_5.east = outside_vualt
lab_2.south = boiler_room
boiler_room.south = quarters
outside_vualt.south = vault_7

######################
#DEFINE ITEMS
######################
Item.description = ""
folder = Item("red folder","folder")
folder.description = "the folder says top secret on the front. you open it and it has a list of military officers"



######################
#DEFINE BAGSs
######################

######################
#ADD ITEMS TO BAGS
######################


######################
#DEFINE ANY VARIABLES
######################
current_room = office_2

######################
#BINDS
######################
@when("go DIRECTION")
@when("travel DIRECTION")
def  travel(direction):
	global current_room
	if direction in current_room.exits():
		#check if the current room list of exits has
		#the direction the player wants to go
		print(f"you go {direction}")
		print(current_room)
	else:
		print("there is no way you can go that way.")

@when("look")
def look():
	print(current_room)
	print(f"there are exits to the",current_room.exits())

######################
#MAIN FUNCTIONS
######################
def main():
	print(current_room)
	start()

main()