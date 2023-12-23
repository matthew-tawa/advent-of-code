from pathlib import Path
import re

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
# file_name = 'document.txt'
file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
document = myfile.read_text().split('\n')
# *****************************

instructions = document[0]
maps = document[2:]

mymap = {}
pattern_text = "(...) = \((...), (...)\)"
pattern = re.compile(pattern_text)
for map in maps:
    matches = pattern.match(map)

    mymap[matches[1]] = {'L': matches[2], 'R': matches[3]}
    
final_location = 'ZZZ'
current_location = 'AAA'
step_num = 0
timeout = 100000
while step_num < timeout:
    step_num += 1

    current_location = mymap[current_location][instructions[(step_num-1)%len(instructions)]]

    if current_location == final_location:
        break


print("total steps: " + str(step_num))









