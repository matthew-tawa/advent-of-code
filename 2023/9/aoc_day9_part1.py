from pathlib import Path
import re

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
# file_name = 'history.txt'
file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
histories = myfile.read_text().split('\n')
# *****************************

# returns the extrapolated value
def extrapolate(_list: list) -> int:
    diff = [_list[i+1]-_list[i] for i in range(0,len(_list)-1)]

    if len(set(diff)) == 1 and 0 in diff :
        return _list[-1]
    else:
        return _list[-1] + extrapolate(diff)

extrapolated_values = []

for reading in histories:
    reading_list = [int(x) for x in reading.split()]

    extrapolated_values.append(extrapolate(reading_list))






print("sum of extrapolated values: " + str(sum(extrapolated_values)))









