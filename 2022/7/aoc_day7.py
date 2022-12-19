import re

input_file = '7\\input.txt'
#input_file = '7\\terminal_output.txt'


f = open(input_file, 'r')
terminal_output = ""

sum_of_dir_sizes = 0    # holds sum of all dirs <= 100000
total_space_used = 0    # holds total sum of files
total_drive_space = 70000000    # total drive space
update_size = 30000000  # space required for update
min_space_to_clear = 0  # smallest amount of data to clear to be able to update
dir_with_min_size = total_drive_space   # size of smallest dir to delete to make enough room

cmd_format = "^\$ (?P<cmd>..) *(?P<arg>.*)"
result_format = "(?P<ftype>.*) (?P<name>.*)"


# adds the current dirs size to sum_of_dir_sizes if the dirs size is <=100000
# and finds the min dir size to remove to be able to update
def add_all_dir_sizes() -> int:
    current_dir_size = 0

    while True:
        terminal_output = f.readline()
        cmd_matches = re.search(cmd_format, terminal_output)
        result_matches = re.search(result_format, terminal_output)
        
        # code_word can be a command or result. All cases are handled by the match-case statement
        if (cmd_matches != None or result_matches != None):
            code_word = cmd_matches.group("cmd") if cmd_matches else result_matches.group("ftype")
        else:
            code_word = "end_of_file"
        
        match code_word:
            case "cd":
                if (cmd_matches.group("arg") == ".." or cmd_matches.group("arg") == "\n"):
                    __process_dir_size(current_dir_size)
                    return current_dir_size
                else: # we are going into a subdirectory
                    current_dir_size += add_all_dir_sizes()

            case "ls":
                pass # nothing to do
            case "dir":
                pass # nothing to do

            case "end_of_file":
                __process_dir_size(current_dir_size)
                return current_dir_size

            case _: # the code_word is a file size
                current_dir_size += int(code_word)


def __process_dir_size(dir_size: int):
    global sum_of_dir_sizes, dir_with_min_size

    dir_with_min_size = dir_size if (dir_size >= min_space_to_clear and dir_size <= dir_with_min_size) else dir_with_min_size

    sum_of_dir_sizes += dir_size if (dir_size <= 100000) else 0




def main():
    global f, total_space_used, min_space_to_clear

    # finding the total amount of space used
    input = f.readline()

    alive = True
    while alive:
        size_match = re.search("(?P<fsize>\d+) .*", input)

        if (size_match):
            total_space_used += int(size_match.group("fsize"))
        
        input = f.readline()
        alive = input != ""

    f.close()

    min_space_to_clear = total_space_used - (total_drive_space - update_size)

    # going through all the directoris one by one to figure out the min size we can delete
    f = open(input_file, 'r')
    alive = True
    while alive:
        
        add_all_dir_sizes()

        input = f.readline()
        alive = input != ""

    f.close()

    print("*************************************************************")
    print("sum of dirs less than 100000: " + str(sum_of_dir_sizes))
    print("*************************************************************")
    print("          min space to clear: " + str(min_space_to_clear))
    print("          min size to delete: " + str(dir_with_min_size))
    print("*************************************************************")



main()

