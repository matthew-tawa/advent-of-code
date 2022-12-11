

# class to hold game inputs
from re import match


class Game:
    def __init__(self, _me: str = "V", _opp: str = "V", _res: str = "V") -> None:
        # for both me and opp:
        # 1 -> rock
        # 2 -> paper
        # 3 -> scissors
        self.me = ord(_me) - 87
        self.opp = ord(_opp) - 64

        if (_res == "X"): # loss
            self.res = 1
        elif (_res == "Y"): # tie
            self.res = 2
        elif (_res == "Z"): # win
            self.res = 0
        else:
            self.res = -1

    # determine result from me and opp
    def evaluateResult(self):
        # 0 -> win
        # 2 -> tie
        # 1 -> loss
        self.res = (self.me - self.opp + 2) % 3

    # determine me from opp and result
    def evaluateMe(self):
        if (self.res == 2):
            self.me = self.opp
        else:
            self.me = (self.res + self.opp) % 3 + 1

    def getPoints(self) -> int:
        # win/loss/tie points can be found from parabolic equationy
        # generated from the three points:
        # (result,points) -> (win, 6) (tie, 3) (loss, 0)
        # where:
        # 0 -> win
        # 2 -> tie
        # 1 -> loss

        if (self.res == -1):
            self.evaluateResult()

        wlt_points = 4.5*self.res**2-10.5*self.res+6

        return self.me + wlt_points





def main():
    #f = open('strat_book3.txt', 'r')
    f = open('input.txt', 'r')
    
    my_score = 0

    input = f.readline()
    alive = True
    while alive:
        g = Game("V", input[0], input[2])
        g.evaluateMe()
        my_score += g.getPoints()

        input = f.readline()
        alive = input != ""

    f.close()

    print("final score: " + str(my_score))


main()