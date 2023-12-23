from pathlib import Path
import re

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
# file_name = 'document2.txt'
file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
document = myfile.read_text().split('\n')
# *****************************

instructions = document[0]
maps = document[2:]

desertmap = {}
mylocations = []
pattern_text = "(...) = \((...), (...)\)"
pattern = re.compile(pattern_text)
for map in maps:
    matches = pattern.match(map)

    desertmap[matches[1]] = {'L': matches[2], 'R': matches[3]}
    
    if matches[1][2] == 'A':
        mylocations.append(matches[1])
    
denominators = []
for i, location in enumerate(mylocations):
    step_num = 0
    done = False
    while not done:
        step_num += 1

        mylocations[i] = desertmap[location][instructions[(step_num-1)%len(instructions)]]

        done = mylocations[i][2] == 'Z'
        
    denominators.append(step_num)

# wanted to find the smallest common denominator, but am now realizing that THIS WONT WORK!
# need to fina nother way........
# find greatest common factor
factors = []
for i, denominator in enumerate(denominators):
    factors[i] = set()
    for j in range(1, denominator+1):
        if  denominator % j == 0:
            factors[i].add(j)

gcf = 0
gcf = [x for x in factors[i] for i in range(1, len(factors))]

    


print("total steps: " + str(step_num))









