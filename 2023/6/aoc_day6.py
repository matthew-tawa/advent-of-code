from pathlib import Path
import math


def quadratic_formula(a, b, c) -> list:
    result1 = (-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    result2 = (-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return [result1, result2]
    


def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    # file_name = 'races.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    races = myfile.read_text().split('\n')
    # *****************************

    multiply_permutations = 1

    times = races[0].split()
    distances = races[1].split()

    for i in range (1, len(times)):
        result = quadratic_formula(1, -1*float(times[i]), float(distances[i])+1)

        multiply_permutations *= math.floor(max(result)) - math.ceil(min(result)) + 1



    print("multiply combinations: " + str(multiply_permutations))



def main2():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    # file_name = 'races.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    races = myfile.read_text().split('\n')
    # *****************************

    multiply_permutations = 1

    time = races[0].replace(' ', '').split(':')[1]
    distance = races[1].replace(' ', '').split(':')[1]

    result = quadratic_formula(1, -1*float(time), float(distance)+1)

    multiply_permutations *= math.floor(max(result)) - math.ceil(min(result)) + 1

    print("multiply combinations: " + str(multiply_permutations))






main1()
main2()



