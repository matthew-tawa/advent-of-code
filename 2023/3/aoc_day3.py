from pathlib import Path



# return: true if symbol, false if non-symbol
def tileIsSymbol(tile):
    return tile not in ["0","1","2","3","4","5","6","7","8","9","."]

# return: true if number, false if non-number
def tileIsNumber(tile):
    return tile in ["0","1","2","3","4","5","6","7","8","9"]

# return: true is blank (.), false if non-blank
def tileIsBlank(tile):
    return tile in ["."]



# return: id if valid, -1 otherwise
def tryGetID(sch, row, col, valid=False):
    _r_min = max(row-1, 0)
    _r_max = min(row+1, len(sch)-1)
    _c_min = max(col-1, 0)
    _c_max = min(col+1, len(sch[0])-1)

    another_digit = (_c_max != col) and tileIsNumber(sch[row][_c_max])

    # iterate over adjacent tiles to find symbol (valid marker)
    for _r in range(_r_min, _r_max+1):
        for _c in range(_c_min, _c_max+1):
            if ((_r != row) or (_c != col)) and not valid:
                valid = tileIsSymbol(sch[_r][_c])
                if valid:
                    break

    if another_digit:
        result_valid, result_num = tryGetID(sch,row,col+1,valid)
        id = sch[row][col] + result_num
    else:
        result_valid = valid
        id = sch[row][col]

    return [result_valid, id]



# determines a PN to add and the offset that we dont need to recheck
def process(sch, row, col):
    pn = 0
    offset = 0
    if tileIsNumber(sch[row][col]):
        _valid, _pn = tryGetID(sch, row, col)
        
        if _valid:
            pn = int(_pn)

        offset = len(_pn)-1
    return [pn, offset]





def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    file_name = 'schematic.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    schematic = myfile.read_text().split('\n')
    # *****************************

    pn_sum = 0
    offset = 0
    for row in range(0, len(schematic)):
        for col in range(0, len(schematic[0])):
            if offset > 0:
                offset -= 1
                continue
            
            pn, offset = process(schematic, row, col)
            pn_sum += pn


    
    print("sum of valid IDs: " + str(pn_sum))





main1()

