

# class to hold game inputs
class Game:
    def __init__(self, _me: str, _opp: str) -> None:
        # for both me and opp:
        # 1 -> rock
        # 2 -> paper
        # 3 -> scissors
        self.me = ord(_me) - 87
        self.opp = ord(_opp) - 64

    def getResult(self) -> int:
        # win/loss/tie points can be found from parabolic equation
        # generated from the three points:
        # (result,points) -> (win, 6) (tie, 3) (loss, 0)
        # where:
        # 0 -> win
        # 2 -> tie
        # 1 -> loss
        result = (self.me - self.opp + 2) % 3
        wlt_points = 4.5*result**2-10.5*result+6

        return self.me + wlt_points




def main():
    #f = open('strat_book.txt', 'r')
    f = open('input.txt', 'r')
    
    my_score = 0

    input = f.readline()
    alive = True
    while alive:
        g = Game(input[2], input[0])
        my_score += g.getResult()

        input = f.readline()
        alive = input != ""

    f.close()

    print("final score: " + str(my_score))


main()