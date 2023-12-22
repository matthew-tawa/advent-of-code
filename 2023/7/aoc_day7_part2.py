from pathlib import Path
from functools import cmp_to_key

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
# file_name = 'hands.txt'
file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
hands = myfile.read_text().split('\n')
# *****************************

# function to compare two hands. hands are tuples of 3, with the following fields:
# [0]: type, where 6 is strongest, 0 is weakest
# [1]: hand as string
# [2]: wager
# return -1: hand1 worse than hand2
# return +1: hand1 better than hand2
def compare(hand1, hand2):
    if hand1[0] == hand2[0]:
        # map based on UTF-8. from left to right is smallest to biggest:
        # UTF-8: 23456789:;<=>
        # hands: 23456789TJKQA
        mymap = (str.maketrans("TJQKA", ":;<=>"))
        return 1 if hand1[1].translate(mymap) > hand2[1].translate(mymap) else -1
    else:
        return 1 if hand1[0] > hand2[0] else -1

# return: hand type as an int from 0 to 6 (0 weakest, 6 strongest)
# hand  : hand as a string of 5 characters
def getType(hand):
    card_set = set(hand)
    card_set_len = len(card_set)

    if card_set_len == 1:
        return 6 # five of a kind
    elif card_set_len == 5:
        return 0 # high card

    # only sets with 2,3, or 4 unique cards make it here
    pair_found = False
    for card in card_set:
        count = hand.count(card)

        if count == 4:
            return 5 # four of a kind
        elif card_set_len == 2 and (count == 2 or count == 3):
            return 4 # full house
        elif card_set_len == 3 and count == 3:
            return 3 # three of a kind
        elif count == 2 and pair_found:
            return 2 # two pair
        elif count == 2:
            pair_found = True

    return 1 # one pair

    

            






# create a list of tuples (t,h,w) of each hand where:
# t = hand type as an int
# h = hand as a string
# w = wager as an int
hand_list = []
for hand in hands:
    hand_split = hand.split()
    hand_list.append((getType(hand_split[0]), hand_split[0], int(hand_split[1])))

hand_list = sorted(hand_list, key=cmp_to_key(compare))

# calculate total winnings
total_winnings = 0
for i, hand in enumerate(hand_list):
    total_winnings += (i+1) * hand[2]


print("total winnings: " + str(total_winnings))









