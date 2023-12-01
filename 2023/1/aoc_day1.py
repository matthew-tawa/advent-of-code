from pathlib import Path
import re



def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    file_name = 'calibrations.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    f = myfile.read_text().split('\n')
    #f = open('9\\input.txt', 'r')
    # *****************************

    calib_sum = 0

    pattern_text = r"\d"
    pattern = re.compile(pattern_text)

    for line in f:
        matches = pattern.findall(line)
        
        first_digit = matches[0]    # first digit
        last_digit  = matches[-1]   # last digit

        calib_sum += int(first_digit + last_digit)


    print("sum of calibrations: " + str(calib_sum))



main1()

