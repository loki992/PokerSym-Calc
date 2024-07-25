# import random


# cards=["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
# colors=["spades","clubs","hearts","diamonds"]
# random_hand = [["",""],["",""]]

# def draw_random_hand():
#   global random_hand
#   random_hand[0].pop()
#   random_hand[0].pop()
#   random_hand[1].pop()
#   random_hand[1].pop()
#   random_hand[0].append(colors[random.randint(0,3)])
#   random_hand[0].append(cards[random.randint(0,12)])
#   random_hand[1].append(colors[random.randint(0,3)])
#   random_hand[1].append(cards[random.randint(0,12)])



# draw_random_hand()
# print(random_hand)
# draw_random_hand()
# print(random_hand)
# draw_random_hand()
# print(random_hand)
import random

def sorting(unsorted_list):
  unsorted_list.sort(key = lambda x : x[1])  
  return unsorted_list

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
cards=(tuple(("spades",card_faces)), tuple(("hearts",card_faces)), tuple(("clubs",card_faces)), tuple(("diamonds",card_faces)))

card_faces_stats_spades = [
  ["ace",0],
  ["two",0],
  ["thre",0],
  ["four",0],
  ["five",0],
  ["six",0],
  ["seven",0],
  ["eight",0],
  ["nine",0],
  ["ten",0],
  ["jack",0],
  ["queen",0],
  ["king",0]]

card_faces_stats_hearts = [
  ["ace",0],
  ["two",0],
  ["thre",0],
  ["four",0],
  ["five",0],
  ["six",0],
  ["seven",0],
  ["eight",0],
  ["nine",0],
  ["ten",0],
  ["jack",0],
  ["queen",0],
  ["king",0]]

card_faces_stats_clubs = [
  ["ace",0],
  ["two",0],
  ["thre",0],
  ["four",0],
  ["five",0],
  ["six",0],
  ["seven",0],
  ["eight",0],
  ["nine",0],
  ["ten",0],
  ["jack",0],
  ["queen",0],
  ["king",0]]

card_faces_stats_diamonds = [
  ["ace",0],
  ["two",0],
  ["thre",0],
  ["four",0],
  ["five",0],
  ["six",0],
  ["seven",0],
  ["eight",0],
  ["nine",0],
  ["ten",0],
  ["jack",0],
  ["queen",0],
  ["king",0]]

cards_stats=[["spades",card_faces_stats_spades], ["hearts",card_faces_stats_hearts], ["clubs",card_faces_stats_clubs], ["diamonds",card_faces_stats_diamonds]]

faces_stats_noface = [
  ["ace",0],
  ["two",0],
  ["thre",0],
  ["four",0],
  ["five",0],
  ["six",0],
  ["seven",0],
  ["eight",0],
  ["nine",0],
  ["ten",0],
  ["jack",0],
  ["queen",0],
  ["king",0]]
i=0
j=0
k=0
l=0

colors_list=[
["spades_sum",0],
["hearts_sum",0],
["clubs_sum",0],
["diamonds_sum",0]
]

while i<10000:
  r_col=random.randint(0,3)
  r_num=random.randint(0,12)
  #print(cards[r_col][1][r_num] + " of " + cards[r_col][0])

  # print(cards_stats[r_col])
  # print(cards_stats[r_col][1])
  # print(cards_stats[r_col][1][r_num])
  # print(cards_stats[r_col][1][r_num][1])
  # print("------------------------------")
  cards_stats[r_col][1][r_num][1]+=1
  faces_stats_noface[r_num][1]+=1
  colors_list[r_col][1]+=1
  i+=1

print("///////////////////////////////")
while j<4:
  print("     " + cards_stats[j][0].upper() + "  sum: "+ str(colors_list[j][1]))
  while k<13:
    print(cards_stats[j][1][k][0]+" of " + cards_stats[j][0] + ": " +str(cards_stats[j][1][k][1]))
    # print("=========="+"k:"+str(k)+"==========")
    k+=1
  k=0
  print("      ________________________")
  j+=1


while l<13:
  print("sum for " + card_faces[l].upper() + ":  " + str(card_faces_stats_clubs[l][1]+card_faces_stats_diamonds[l][1]+card_faces_stats_hearts[l][1]+card_faces_stats_spades[l][1]))
  l+=1
print("///////////////////////////////")

print("avg for color should be about " + str(i/4))
print("avg for face should be around " + str(int(i/13)))


print("Median for colors is : " + str((sorting(colors_list)[1][1]+sorting(colors_list)[2][1])/2))
print("should be " + str(i/4))

print("Median for faces is : " + sorting(faces_stats_noface)[7][0]+"("+str(card_faces.index(sorting(faces_stats_noface)[7][0])+1) + ")")

print("///////////////////////////////")



