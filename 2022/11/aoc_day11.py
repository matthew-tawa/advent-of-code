
import re


class Monkey:
    def __init__(self, id, items, op_str, test_div_by, throw_to_true, throw_to_false) -> None:
        self.id = id
        self.items = items
        self.op_str = op_str
        self.test_div_by = test_div_by
        self.throw_to_true = throw_to_true
        self.throw_to_false = throw_to_false
        self.num_inspections = 0

    # inspect an individual item
    def __inspect_item():
        pass
    
    # make a monkey inspect all its items
    def inspect_items():
        for item in items:
            __inspect_item




# main part 1
def main1():
    f = open('11\\monkeys.txt', 'r')
    #f = open('11\\input.txt', 'r')

    monkeys = []

    pattern_text1 = "Monkey (?P<id>\d):\n"
    pattern_text2 = " *Starting items: (?P<items>.*)\n"
    pattern_text3 = " *Operation: new = (?P<op_str>.*)\n"
    pattern_text4 = " *Test: divisible by (?P<test>\d*)\n"
    pattern_text5 = " *If true: throw to monkey (?P<throw_to_true>\d*)\n"
    pattern_text6 = " *If false: throw to monkey (?P<throw_to_false>\d*)\n"
    pattern1 = re.compile(pattern_text1)
    pattern2 = re.compile(pattern_text2)
    pattern3 = re.compile(pattern_text3)
    pattern4 = re.compile(pattern_text4)
    pattern5 = re.compile(pattern_text5)
    pattern6 = re.compile(pattern_text6)

    input = f.readline()
    alive = True

    while alive:
        matches = pattern1.match(input)
        m_id = matches.group("id")

        input = f.readline()
        matches = pattern2.match(input)
        m_items = matches.group("items")

        input = f.readline()
        matches = pattern3.match(input)
        m_op = matches.group("op_str")

        input = f.readline()
        matches = pattern4.match(input)
        m_test = matches.group("test")

        input = f.readline()
        matches = pattern5.match(input)
        m_test_true = matches.group("throw_to_true")

        input = f.readline()
        matches = pattern6.match(input)
        m_test_false = matches.group("throw_to_false")

        monkeys.append(Monkey(m_id, m_items, m_op, m_test, m_test_true, m_test_false))

        input = f.readline()
        input = f.readline()
        alive = input != ""


    f.close()



    # making monkeys inspect and throw items
    for round in range(0, 20):
        for m in monkeys:
            m.inspect_items()

    highest_inspections = 0
    second_highest_inspections = 0
    for m in monkeys:
        if (m.num_inspections >= highest_inspections):
            second_highest_inspections = highest_inspections
            highest_inspections = m.num_inspections
        elif (m.num_inspections >= second_highest_inspections):
            second_highest_inspections = m.num_inspections

    print("monkey business: " + str(highest_inspections*second_highest_inspections))


main1()
#main2()