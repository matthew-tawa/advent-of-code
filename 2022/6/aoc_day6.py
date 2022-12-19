



def main():
    #f = open('6\datastream.txt', 'r')
    f = open('6\input.txt', 'r')

    signal = f.readline()

    #marker_len = 4     # part 1
    marker_len = 14    # part 2
    for i in range(marker_len, len(signal)-marker_len):
        if (len(set(signal[i-marker_len:i])) == marker_len):
            print("marker found at: " + str(i))
            break

    f.close()

    

main()