import re



#f = open('7\\terminal_output.txt', 'r')
f = open('7\input.txt', 'r')
terminal_output = ""

sum_of_dir_sizes = 0
cmd_format = "^\$ (?P<cmd>..) *(?P<arg>.*)"
result_format = "(?P<ftype>.*) (?P<name>.*)"


# adds the current dirs size to sum_of_dir_sizes if the dirs size is <=100000
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
                    __add_to_sum_of_dir_sizes(current_dir_size)
                    return current_dir_size
                else: # we are going into a subdirectory
                    current_dir_size += add_all_dir_sizes()

            case "ls":
                pass # nothing to do
            case "dir":
                pass # nothing to do

            case "end_of_file":
                __add_to_sum_of_dir_sizes(current_dir_size)
                return current_dir_size

            case _: # the code_word is a file size
                current_dir_size += int(code_word)


def __add_to_sum_of_dir_sizes(dir_size: int):
    global sum_of_dir_sizes
    sum_of_dir_sizes += dir_size if (dir_size <= 100000) else 0




def main():

    alive = True
    while alive:
        
        add_all_dir_sizes()

        input = f.readline()
        alive = input != ""

    f.close()

    print("sum: " + str(sum_of_dir_sizes))




main()

