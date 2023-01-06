
import re

# main part 1
def main1():
    #f = open('10\\instructions.txt', 'r')
    f = open('10\\input.txt', 'r')

    pattern_text = "(?P<cmd>.+) (?P<arg>-?\d*)"
    pattern = re.compile(pattern_text)

    hold = False
    regx = 1
    sum_of_signal_strengths = 0

    for cycle in range(1, 221):
        if (not hold):
            # 1- start of cycle
            input = f.readline()

        matches = pattern.match(input)
        cmd = matches.group("cmd") if matches else ""
        
        # 2- during cycle
        sum_of_signal_strengths += (cycle * regx) if ((cycle-20) % 40 == 0) else 0

        # 3- after cycle
        match cmd:
            case "noop":
                pass # do nothing on this cycle
            case "addx":
                hold = not hold
                regx += int(matches.group("arg")) if (not hold) else 0
                    
            case _:
                # if unknown command encountered on this cycle, pass
                pass

    f.close()
    print("final sum of signal strengths: " + str(sum_of_signal_strengths))



# main part 2
def main2():
    #f = open('10\\instructions.txt', 'r')
    f = open('10\\input.txt', 'r')

    pattern_text = "(?P<cmd>.+) (?P<arg>-?\d*)"
    pattern = re.compile(pattern_text)

    hold = False
    regx = 1
    sum_of_signal_strengths = 0
    sprite_width = 1 # distance from center of sprite outwards

    alive = True
    cycle = 1
    while alive:
        if (not hold):
            # 1- start of cycle
            input = f.readline()
            alive = input != ""

        matches = pattern.match(input)
        cmd = matches.group("cmd") if matches else ""
        
        # 2- during cycle
        pixel_lit = (cycle-1)%40 in range(regx-sprite_width, regx+sprite_width+1)

        print(("\nSCREEN " + str(int((cycle-1)/240)) + ":\n") if (cycle-1) % 240 == 0 else "", end="")
        print("#" if pixel_lit else ".", end="")
        print("\n" if cycle % 40 == 0 else "", end="")

        # 3- after cycle
        match cmd:
            case "noop":
                pass # do nothing on this cycle
            case "addx":
                hold = not hold
                regx += int(matches.group("arg")) if (not hold) else 0
                    
            case _:
                # if unknown command encountered on this cycle, pass
                pass

        cycle += 1

    f.close()



#main1()
main2()