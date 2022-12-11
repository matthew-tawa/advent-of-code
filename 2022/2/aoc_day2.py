

# class to hold game inputs
class Game:
    def __init__(self, _me: str, _opp: str) -> None:
        # for both me and opp:
        # 0 -> rock
        # 1 -> paper
        # 2 -> scissors
        self.me = ord(_me) - 88
        self.opp = ord(_opp) - 65

    def getResult(self) -> int:
        # win/loss/tie_modifier
        # 0x1 -> loss
        # 0x0  -> tie
        # 0x2 with mask -> win
        wlt_modifier = (self.opp - self.me) & 0x3

        if ((wlt_modifier & 0x2) == 2):
            wlt_modifier = 1
        else:
            wlt_modifier *= -1

        return (1 + self.me) + (3 + 3*wlt_modifier)




def main():
    f = open('strat_book.txt', 'r')
    #f = open('input.txt', 'r')
    
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