
import math


class SNAFU_Number:
    def __init__(self, num) -> None:
        self.SNAFU_num = ""
        self.set_SNAFU_num(num)


    def set_SNAFU_num(self, num) -> None:
        self.SNAFU_num = self.__build_SNAFU(num, 0)


    # build a SNAFU number recursively
    # num -> number to build
    # place -> current digit to build (0 is 1s position, 1 is 5s position, 2 is 25s position, etc)
    def __build_SNAFU(self, num, place) -> str:
        __remainder = num % 5**(place+1)
        __num_left_to_build = num - __remainder + (0 if __remainder<3*5**place else 5**(place+1))

        __current_digit = ""
        match __remainder/(5**place):
            case 3:
                __current_digit = "="
            case 4:
                __current_digit = "-"
            case _:
                __current_digit = str(int(__remainder/(5**place)))

        if __num_left_to_build == 0:
            return __current_digit
        else:
            place += 1
            return self.__build_SNAFU(__num_left_to_build, place) + __current_digit



        




#f = '25\\hot_air_balloons.txt'
f = '25\\input.txt'
data_str = open(f).read().strip()
data = data_str.split('\n')

sum_of_fuel = 0

for line in data:
    for place, digit in enumerate(reversed(line)):
        weight = 0
        match digit:
            case "=":
                weight = -2
            case "-":
                weight = -1
            case _:
                weight = int(digit)

        sum_of_fuel += weight * 5**place

SNAFU_sum_of_fuel = SNAFU_Number(sum_of_fuel)

print("Sum of fuel: " + str(sum_of_fuel) + " (" + SNAFU_sum_of_fuel.SNAFU_num + ")")



