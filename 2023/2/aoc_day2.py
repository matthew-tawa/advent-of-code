from pathlib import Path
import re

num_tokens = {
    'red'  : 12,
    'green': 13,
    'blue' : 14,
}

def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    file_name = 'record.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    game_log = myfile.read_text().split('\n')
    # *****************************

    possible_game_id_sum = 0

    pattern_text = r" (?P<num>\d+) (?P<color>[a-z]+)(?P<delim>,|;|\n)"
    pattern = re.compile(pattern_text)

    for game in game_log:
        id = int(re.search(r"\d+", game)[0])
        
        matches = pattern.findall(game)

        game_possible = True
        playing = True
        pull = 0
        while playing & (pull < len(matches)):
            if int(matches[pull][0]) > num_tokens[matches[pull][1]]:
                # num pulled > num available, game not possible!
                game_possible = False
                break
            
            pull += 1
            
        if game_possible:
            possible_game_id_sum += id



    print("sum of possible games: " + str(possible_game_id_sum))



main1()

