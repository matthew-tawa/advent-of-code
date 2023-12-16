from pathlib import Path
















def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    file_name = 'scratchcards.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    scratchcards = myfile.read_text().split('\n')
    # *****************************

    total_points = 0
    for card in scratchcards:
        nums = card.split(' ')
        nums = [x for x in nums if x != ''] # removing unwanted empty strings

        num_winning = nums[2:12]
        num_winning = [x for x in num_winning if x != ''] # removing unwanted empty strings
        num_have    = nums[13:]
        num_have    = [x for x in num_have if x != ''] # removing unwanted empty strings
        
        num_matches = len([x for x in num_have if x in num_winning])
        total_points += 2**(num_matches-1) if num_matches > 0 else 0



    print("sum of scratchcards: " + str(total_points))







main1()

