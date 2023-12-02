from pathlib import Path
import re

text2num = {
    'one'  : 1,
    'two'  : 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six'  : 6,
    'seven': 7,
    'eight': 8,
    'nine' : 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    file_name = 'calibrations.txt'
    file_name = 'calibrations2.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    f = myfile.read_text().split('\n')
    # *****************************

    calib_sum = 0

    pattern_text = r"\d|one|two|three|four|five|six|seven|eight|nine"
    pattern = re.compile(pattern_text)

    for line in f:
        matches = pattern.findall(line)
        
        first_digit = text2num[matches[0]]    # first digit
        last_digit  = text2num[matches[-1]]   # last digit

        calib_sum += first_digit*10 + last_digit


    print("sum of calibrations: " + str(calib_sum))



main1()

