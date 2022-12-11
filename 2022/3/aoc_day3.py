

# class to hold rucksacks
class Rucksack:
    def __init__(self, _items: str) -> None:
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


def main():
    #f = open('rucksacks.txt', 'r')
    f = open('input.txt', 'r')
    
    erroneous_priority_counter = 0

    input = f.readline()
    alive = True
    while alive:
        r = Rucksack(input[:-1]) # ignore the newline character
        erroneous_priority_counter += getPriority(r.properlySorted())

        input = f.readline()
        alive = input != ""

    f.close()

    print("final score: " + str(erroneous_priority_counter))


main()