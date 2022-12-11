

# class to hold rucksacks
class Rucksack:
    def __init__(self, _items: str) -> None:
        self.items: str = _items
        self.compartment1 = _items[:int(len(_items)/2)]
        self.compartment2 = _items[int(len(_items)/2):]

    # determines if rucksack was properly sorted
    # return -> the wrongly sorted item (or blank string if properly sorted)
    def properlySorted(self) -> str:
        for item1 in self.compartment1:
            for item2 in self.compartment2:
                if item1 == item2:
                    return item1

        # otherwise compartments properly sorted
        return ""


# given an item, returns its priority
def getPriority(item: str) -> int:
    offset = 0
    if (ord(item) < 97): # we are a uppercase letter
        offset = 64 - 26
    else: # we are a lowercase letter
        offset = 96

    return ord(item) - offset

# given three ruckscks, determine the badge (common element)
# return -> the badge item (or blank string if no common element between all three rucksacks)
def getBadge(r1: Rucksack, r2: Rucksack, r3: Rucksack) -> str:
    for item1 in r1.items:
        for item2 in r2.items:
            if (item1 == item2):  
                for item3 in r3.items:
                    if (item1 == item3):
                        return item1

    return ""


def main():
    #f = open('rucksacks.txt', 'r')
    f = open('input.txt', 'r')
    
    erroneous_priority_counter = 0

    input = f.readline()
    alive = True
    while alive:
        #input = f.readline()
        rucksack1 = Rucksack(input[:-1]) # end-1 to ignore the newline character

        input = f.readline()
        rucksack2 = Rucksack(input[:-1])

        input = f.readline()
        rucksack3 = Rucksack(input[:-1])

        erroneous_priority_counter += getPriority(getBadge(rucksack1, rucksack2, rucksack3))

        input = f.readline()
        alive = input != ""

    f.close()

    print("sum of priorities: " + str(erroneous_priority_counter))


main()