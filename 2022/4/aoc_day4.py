

import re

# class to hold a pair of elves cleaning sections
class RangePair:
    def __init__(self, _cleaningRangePairStr: str) -> None:
        pattern_text = "(?P<min1>\d+)-(?P<max1>\d+),(?P<min2>\d+)-(?P<max2>\d+)"
        pattern = re.compile(pattern_text)
        matches = pattern.match(_cleaningRangePairStr)

        self.cr1 = CleaningRange(int(matches.group("min1")), int(matches.group("max1")))
        self.cr2 = CleaningRange(int(matches.group("min2")), int(matches.group("max2")))

    # returns 1 if one of the ranges fully contains the other, 0 otherwise
    def rangeFullyContained(self) -> int:
        cr1_contains_cr2 = ((self.cr1.min <= self.cr2.min) and (self.cr1.max >= self.cr2.max))
        cr2_contains_cr1 = ((self.cr2.min <= self.cr1.min) and (self.cr2.max >= self.cr1.max))
        return int(cr1_contains_cr2 or cr2_contains_cr1)

    # returns 1 if the ranges overlap at all, 0 otherwise
    def rangeOverlaps(self) -> int:
        # two conditions for overlap of cr1
        condition1a = self.cr1.min <= self.cr2.max and self.cr1.min >= self.cr2.min
        condition1b = self.cr1.max >= self.cr2.min and self.cr1.max <= self.cr2.max

        # two conditions for overlap of cr2
        condition2a = self.cr2.min <= self.cr1.max and self.cr2.min >= self.cr1.min
        condition2b = self.cr2.max >= self.cr1.min and self.cr2.max <= self.cr1.max
        
        return int(condition1a or condition1b or condition2a or condition2b)


class CleaningRange:
    def __init__(self, _min: int, _max: int) -> None:
        self.min = _min
        self.max = _max




def main():
    #f = open('sections.txt', 'r')
    f = open('input.txt', 'r')
    
    fully_contained_counter = 0

    input = f.readline()
    alive = True
    while alive:
        rp = RangePair(input)

        #fully_contained_counter += rp.rangeFullyContained()
        fully_contained_counter += rp.rangeOverlaps()

        input = f.readline()
        alive = input != ""

    f.close()

    print("fully contained counter: " + str(fully_contained_counter))


main()

