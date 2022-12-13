
import array
import re


# class to represent ship cargo
class ShipCargo:
    def __init__(self, cargo_arr) -> None:
        self.cargo_bay = [[1]]
        num_stacks = 10
        for i in range(2, num_stacks):
            self.cargo_bay.append([i])
        
        for i in range(len(cargo_arr)-1, 0, -1):
            # defining the pattern to match
            pattern = re.compile("\[(?P<cargo>.)\]")

            # getting an iterator of all matches
            iterator = pattern.finditer(cargo_arr[i])
            
            # iterating over all matches
            for match in reversed(list(iterator)):
                if (match):
                    self.cargo_bay[int((match.start())/4)].append(match.group("cargo"))


    def get_rows(self) -> int:
        pass

    def get_row_height(self) -> int:
        pass

    # move qty containers from stack1 to stack2
    # qty    -> qty of containers to move from stack1 to stack2
    # stack1 -> removes containers ONE AT A TIME from the top
    # stack2 -> adds containers ONE AT A TIME to the top
    def move_containers_1by1(self, qty: int, stack1: int, stack2: int):
        while (qty > 0):
            self.__move_top_container(stack1, stack2)
            qty -= 1
    
    # move container from top of stack1 to top of stack2
    def __move_top_container(self, stack1: int, stack2: int):
        self.cargo_bay[stack2-1].append(self.cargo_bay[stack1-1].pop())

    # move qty containers from stack1 to stack2
    # qty    -> qty of containers to move from stack1 to stack2
    # stack1 -> removes containers ALL AT ONCE from the top
    # stack2 -> adds containers ALL AT ONCE to the top
    def move_containers_xby1(self, qty: int, stack1: int, stack2: int):
        while (qty > 0):
            self.__move_any_container(qty, stack1, stack2)
            qty -= 1

    # move any one container from stack1 to top of stack2
    # offset_from_top -> 1 for top, 2 for second from top, 3 for third from top, etc...
    def __move_any_container(self, offset_from_top: int, stack1: int, stack2: int):
        self.cargo_bay[stack2-1].append(self.cargo_bay[stack1-1].pop(-1*offset_from_top))

    # return string with top cargo of each stack
    def top_cargos(self) -> str:
        rtn_str = ""
        for stack in self.cargo_bay:
            rtn_str += stack[len(stack)-1]
        
        return rtn_str



def main():
    #f = open('crates.txt', 'r')
    f = open('input.txt', 'r')
    
    # setting up crate list
    crate_setup = [f.readline]
    
    # *****
    # looping through input to generate initial cargo structure
    # *****
    input = f.readline()
    alive = True
    while alive:
        crate_setup.append(input)
        
        input = f.readline()
        alive = input != "\n"

    # *****
    # creating ship cargo bay
    # *****
    ship = ShipCargo(crate_setup)
    

    # *****
    # loop through instructions to process commands
    # *****
    pattern_text = "move (?P<qty>\d+) from (?P<stack1>\d+) to (?P<stack2>\d+)"
    pattern = re.compile(pattern_text)

    input = f.readline()
    alive = True
    while alive:
        matches = pattern.match(input)

        quantity = int(matches.group("qty"))
        stack_move_from = int(matches.group("stack1"))
        stack_move_to = int(matches.group("stack2"))

        #ship.move_containers_1by1(quantity, stack_move_from, stack_move_to)
        ship.move_containers_xby1(quantity, stack_move_from, stack_move_to)

        input = f.readline()
        alive = input != ""

    f.close()

    print("containers on top:\n" + ship.top_cargos())






main()

