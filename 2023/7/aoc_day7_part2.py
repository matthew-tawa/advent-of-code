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
        # UTF-8: 123456789:;<=
        # hands: J23456789TKQA
        mymap = (str.maketrans("JTQKA", "1:;<="))
        return 1 if hand1[1].translate(mymap) > hand2[1].translate(mymap) else -1
    else:
        return 1 if hand1[0] > hand2[0] else -1

# return: hand type as an int from 0 to 6 (0 weakest, 6 strongest)
# hand  : hand as a string of 5 characters
def getType(hand):
    card_set = set(hand)

    num_jokers = hand.count('J')
    card_set.discard('J')

    card_set_len = len(card_set)

    # using <= in case we get a hand with 5 jokers
    if card_set_len <= 1:
        return 6 # five of a kind
    if card_set_len == 5:
        return 0 # high card
    elif card_set_len == 4 and num_jokers == 1:
        return 1 # one pair

    # only sets with 2,3, or 4 unique non-joker cards make it here
    best_hand = 0 # high card
    pair_found = False
    for card in card_set:
        count = hand.count(card)

        if (count+num_jokers) == 4:
            # can return right away since this is the best hand from here on out
            return 5 # four of a kind 
        elif card_set_len == 2 and ((count+num_jokers) == 2 or (count+num_jokers) == 3):
            best_hand = max(best_hand, 4) # full house
        elif card_set_len == 3 and (count+num_jokers) == 3:
            best_hand = max(best_hand, 3) # three of a kind
        elif (count+num_jokers) == 2 and pair_found:
            best_hand = max(best_hand, 2) # two pair
        elif (count+num_jokers) == 2:
            pair_found = True
            best_hand = max(best_hand, 1) # one pair

    return best_hand

    

            






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









