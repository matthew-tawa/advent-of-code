
import re
import numpy as np


# class to hold a head/tail pair and track their moves
class Rope2Knots:
    def __init__(self, head_x: int, head_y: int) -> None:
        self.hx = head_x
        self.hy = head_y
        self.tx = head_x
        self.ty = head_y
        self.__dx = 0   # +ve if H > T, -ve if H < T
        self.__dy = 0   # +ve if H > T, -ve if H < T
        
        self.h_visits: set = {(self.hx, self.hy)}
        self.t_visits: set = {(self.tx, self.ty)}
        

    # enter a move for the head
    def move(self, dir: str, dist: int, verbose_level: str = "quiet") -> None:
        match dir:
            case "U":
                self.__move_y(dist, 1, verbose_level)
            case "D":
                self.__move_y(dist, -1, verbose_level)
            case "L":
                self.__move_x(dist, -1, verbose_level)
            case "R":
                self.__move_x(dist, 1, verbose_level)
            case _:
                pass # should never occur

    # update the position of the head, and update tail accordingly
    def update_head(self, head_new_x: int, head_new_y: int) -> None:
        self.hx = head_new_x
        self.hy = head_new_y

        self.h_visits.add((self.hx, self.hy))

        self.__dx = self.hx - self.tx
        self.__dy = self.hy - self.ty

        self.__step_tail()
        pass

    # move the head in x
    def __move_x(self, dist: int, sign: int = 1, verbose_level: str = "quiet") -> None:
        for step in range(0, sign*dist, sign):
            self.hx += sign
            self.__dx += sign
            self.h_visits.add((self.hx, self.hy))
            self.__step_tail()

            if (verbose_level != "quiet"):
                self.__print_board()

    # move the head in y
    def __move_y(self, dist: int, sign: int = 1, verbose_level: str = "quiet") -> None:
        for step in range(0, sign*dist, sign):
            self.hy += sign
            self.__dy += sign
            self.h_visits.add((self.hx, self.hy))
            self.__step_tail()

            if (verbose_level != "quiet"):
                self.__print_board()

    # make the tail follow after each head step
    def __step_tail(self) -> None:
        if (self.__dx == 0 and abs(self.__dy) > 1):
            # move tail along y
            self.ty   += np.sign(self.__dy)
            self.__dy -= np.sign(self.__dy)

        elif (abs(self.__dx) > 1 and self.__dy == 0):
            # move tail along x
            self.tx   += np.sign(self.__dx)
            self.__dx -= np.sign(self.__dx)

        elif (self.__dx != 0 and self.__dy != 0 and (abs(self.__dx) + abs(self.__dy))>2):
            # we need to move diagonally
            self.tx += np.sign(self.__dx)
            self.ty += np.sign(self.__dy)

            self.__dx -= np.sign(self.__dx)
            self.__dy -= np.sign(self.__dy)

        else:
            # head overlaps tail, or
            # __dx=1 and __dy=0, or
            # __dx=0 and __dy=1, or
            # __dx=1 and __dy=1, or
            # do nothing
            pass

        self.t_visits.add((self.tx, self.ty))


    def __print_board(self) -> None:
        board_side_len = 6
        board = [["." for i in range(board_side_len)] for j in range(board_side_len)]

        board[board_side_len-1-self.ty][self.tx] = "T"
        board[board_side_len-1-self.hy][self.hx] = "H"

        print("\n")
        print(*board, sep="\n")
        


class Rope10Knots:
    def __init__(self, head_x: int, head_y: int) -> None:
        self.sections = [Rope2Knots(head_x,head_y) for _ in range(9)]

        self.__print_start_x = head_x
        self.__print_start_y = head_y

    # enter a move for the head
    def move(self, dir: str, dist: int, verbose_level: str = "quiet") -> None:
        for step in range(0, dist):
            self.sections[0].move(dir, 1, verbose_level)
            for pos, section in enumerate(self.sections[1:]):
                prev_rope_tail_x = self.sections[pos].tx
                prev_rope_tail_y = self.sections[pos].ty
                section.update_head(prev_rope_tail_x, prev_rope_tail_y)

    def print_board(self) -> None:
        board_side_len = 30
        board = [["." for i in range(board_side_len)] for j in range(board_side_len)]

        board[board_side_len-1-self.__print_start_y][self.__print_start_x] = "S"

        for i, section in enumerate(reversed(self.sections[1:])):
            board[board_side_len-1-section.ty][section.tx] = str(9-i)

        board[board_side_len-1-self.sections[0].ty][self.sections[0].tx] = "1"
        board[board_side_len-1-self.sections[0].hy][self.sections[0].hx] = "H"

        print("\n")
        print(*board, sep="\n")
                

        
        





def main1():
    #f = open('9\\moves.txt', 'r')
    f = open('9\\input.txt', 'r')

    # starting the rope arbitrarily at head(0,0) tail(0,0)
    rope = Rope2Knots(0,0)

    input = f.readline()

    pattern_text = "(?P<dir>.) (?P<dist>\d+)"
    pattern = re.compile(pattern_text)
    matches = pattern.match(input)

    alive = True
    while alive:
        matches = pattern.match(input)
        move_direction = matches.group("dir")
        move_distance  = int(matches.group("dist"))

        rope.move(move_direction, move_distance, "quiet")

        input = f.readline()
        alive = input != ""

    f.close()

    print("number of unique crossed squares for 2  knot rope: " + str(len(rope.t_visits)))


def main2():
    #f = open('9\\moves_10knot.txt', 'r')
    f = open('9\\input.txt', 'r')

    # starting the rope arbitrarily at head(0,0) tail(0,0)
    rope = Rope10Knots(10,10)

    input = f.readline()

    pattern_text = "(?P<dir>.) (?P<dist>\d+)"
    pattern = re.compile(pattern_text)
    matches = pattern.match(input)

    alive = True
    while alive:
        matches = pattern.match(input)
        move_direction = matches.group("dir")
        move_distance  = int(matches.group("dist"))

        rope.move(move_direction, move_distance, "quiet")
        #rope.print_board()

        input = f.readline()
        alive = input != ""

    f.close()

    print("number of unique crossed squares for 10 knot rope: " + str(len(rope.sections[-1].t_visits)))


main1()
main2()

