# elf leaderboard dict
cal_lb = {
    "elf0": 0,
    "elf0_cal": 0,
    "elf1": 0,
    "elf1_cal": 0,
    "elf2": 0,
    "elf2_cal": 0
}

def main():
    #f = open('elf_calorie_list.txt', 'r')
    f = open('input.txt', 'r')

    # current elf we are checking
    cur_elf = 1
    cur_cal = 0

    input = f.readline()
    alive = True
    while alive:
        if (input == "\n" or input == ""):
            # we have a new elf
            # compare current elf data to max
            if (cur_cal > cal_lb["elf2_cal"]):
                if (cur_cal > cal_lb["elf1_cal"]):
                    if (cur_cal > cal_lb["elf0_cal"]):
                        new_lb_entry(cur_cal, cur_elf, 0)
                    else:
                        new_lb_entry(cur_cal, cur_elf, 1)
                else:
                    new_lb_entry(cur_cal, cur_elf, 2)

            # go to next elf
            cur_elf += 1
            cur_cal = 0
            alive = (input != "") # keep going unless we are at the end
        else:
            # same elf, increment calories carried
            cur_cal += int(input)

        input = f.readline()

    f.close()

    print("    elf 1: " + str(cal_lb["elf0"]))
    print("calories : " + str(cal_lb["elf0_cal"]))
    print("    elf 2: " + str(cal_lb["elf1"]))
    print("calories : " + str(cal_lb["elf1_cal"]))
    print("    elf 3: " + str(cal_lb["elf2"]))
    print("calories : " + str(cal_lb["elf2_cal"]))
    print("----------------")
    temp = int(cal_lb["elf0_cal"]) + int(cal_lb["elf1_cal"]) + int(cal_lb["elf2_cal"])
    print("   total : " + str(temp))


# adds val to the given pos (0=first, 1=second, 2=third)
def new_lb_entry(cal: int, elf: int, pos: int):
    iter = 2 - pos
    # 1st   _pos=2
    # 2nd   _pos=1
    # 3rd   _pos=0
    while (iter > 0):
        cal_lb["elf" + str(pos+iter)]          = cal_lb["elf" + str(pos+iter-1)]
        cal_lb["elf" + str(pos+iter) + "_cal"] = cal_lb["elf" + str(pos+iter-1) + "_cal"]
        iter -= 1

    cal_lb["elf" + str(pos)] = elf
    cal_lb["elf" + str(pos) + "_cal"] = cal




main()