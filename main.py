import random

card_faces = (
  "ace",
  "two",
  "thre",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "jack",
  "queen",
  "king")

colors= (
"spades",
"hearts",
"clubs",
"diamonds"
)

tuple_of_all_hands=(
  ("high card","1"),
  ("pair","2"),
  ("two pairs","3"),
  ("three of a kind","4"),
  ("straight","5"),
  ("flush", "6"),
  ("full house",),
  ("four of a kind","7"),
  ("straight flush","8"),
  ("royal flush","9")
)

cards = []
player1_hand=[]
player2_hand=[]
player3_hand=[]
player4_hand=[]
player5_hand=[]
player6_hand=[]
player7_hand=[]
player8_hand=[]

flop=[]
turn=[]
river=[]

#END OF DECLARATIONS.
#FUNCTION DEFINITIONS BELOW

def create_full_deck():
  i=0
  j=0
  k=0
  global cards
  cards = []
  while i<4:
    while j<13:
      cards.append([card_faces[j],colors[i]])
      j+=1
      k+=1
    j=0
    i+=1

def print_current_deck():  
  i=0
  while i<len(cards):
    print(str(i+1)+". "+cards[i][0] + " of " +cards[i][1])
    i+=1

def draw_two_cards():  
  hand =[]
  hand.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(hand[0])
  hand.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(hand[1])
  return(hand) 

def draw_flop():  
  global flop
  flop = []
  flop.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(flop[0])
  flop.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(flop[1])
  flop.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(flop[2])

def draw_one(place_for_one):
  place_for_one.append(cards[random.randint(0,len(cards)-1)])
  cards.remove(place_for_one[len(place_for_one)-1])
  return place_for_one

def print_table():
  print()
  print("////////////////////////////////")
  if(flop==[]):
    print("Still PRE-FLOP")
  elif(turn==[]):
    print("Cards on table: ")
    temp_string ="Flop: "
    temp = 0
    while temp<3:
      temp_string += flop[temp][0]
      temp_string += " of "
      temp_string += flop[temp][1]
      temp_string +="  "
      temp+=1
    print(temp_string)
  elif(river==[]):
    print("Cards on table: ")
    temp_string ="Flop: "
    temp = 0
    while temp<3:
      temp_string += flop[temp][0]
      temp_string += " of "
      temp_string += flop[temp][1]
      temp_string +="  "
      temp+=1
    print(temp_string)
    print("Turn: "+ turn[0][0] + " of " + turn[0][1])
  else:
    print("Cards on table: ")
    temp_string ="Flop: "
    temp = 0
    while temp<3:
      temp_string += flop[temp][0]
      temp_string += " of "
      temp_string += flop[temp][1]
      temp_string +="  "
      temp+=1


    print(temp_string)
    print("Turn: "+ turn[0][0] + " of " + turn[0][1])
    print("River: "+ river[0][0] + " of " + river[0][1])

#END OF DEFINITIONS
#LOGIC BELOW

create_full_deck()

player1_hand = draw_two_cards()
player2_hand = draw_two_cards()
player3_hand = draw_two_cards()
player4_hand = draw_two_cards()


# print("Deck:")
# print_current_deck()

print("Player 1 hand: ")
print(player1_hand)
print("Player 2 hand: ")
print(player2_hand)
print("Player 3 hand: ")
print(player3_hand)
print("Player 4 hand: ")
print(player4_hand)


river = []
draw_one(river)
turn = []
draw_one(turn)
flop = []
draw_flop()

print_table()

#TODO
# Recognizing current hands
# Comparing hand strength
# Determining which hand is winning at a given time
# Resetting the entire table and deck
# Adding the ability to select cards for each set
# Determining the player's percentage chance of a given hand based on their hand and the table

# IN THE FUTURE

# Determining the percentage chance of other players' hands appearing based on the table
# Comparing the player's chances of hands and the chances from the table for the strongest hands
# Determining the player's chance of winning
# Adding a gui