
import re

# gets a monkey's number
def get_monkey_number(name: str):
    global data, known_numbers

    # if the monkey's number is already calculated, return
    if name in known_numbers:
        return known_numbers[name]

    for line in data:
        words = line.split()
        _name = words[0][:-1]

        # if the read data is not the desired monkey, go to next data line
        if _name != name:
            continue

        result = 0

        if len(words) > 2: # we have a monkey with an op code
            arg1 = int(known_numbers[words[1]] if words[1] in known_numbers else get_monkey_number(words[1]))
            op = words[2]
            arg2 = int(known_numbers[words[3]] if words[3] in known_numbers else get_monkey_number(words[3]))

            match op:
                case "+":
                    result = arg1 + arg2
                case "-":
                    result = arg1 - arg2
                case "*":
                    result = arg1 * arg2
                case "/":
                    result = arg1 / arg2
                case _:
                    pass
            
        else: # we have a monkey with a number
            result = words[1]

        known_numbers[name] = result
        return result
        



#f = '21\\monkey_math.txt'
f = '21\\input.txt'
data_str = open(f).read().strip()
data = data_str.split('\n')

known_numbers = {}

print("root will yell: " + str(get_monkey_number("root")))