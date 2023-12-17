from pathlib import Path

class AlmanacMap:
    # dest, src, length must be lists of numbers, all with same length
    def __init__(self, _dst, _src, _len) -> None:
        if len(_dst) == len(_src) and len(_dst) == len(_len):
            self._dst = _dst
            self._src = _src
            self._len = _len
            self.num_ranges = len(_dst)
        else:
            self._dst = None
            self._src = None
            self._len = None
            self.num_ranges = None

    # val -> list to map
    # return -> list that has been passed through the map
    def map(self, val: list) -> list:
        return [self._map(x) for x in val]
    
    # _val -> int to map
    # return -> int that has been passed through the map
    def _map(self, _val: int) -> int:
        for i in range(self.num_ranges):
            if _val in range(self._src[i], self._src[i] + self._len[i]):
                return _val - self._src[i] + self._dst[i]
            
        return _val


# create a map and return it
# almanac  -> the almanac
# map_name -> name of map to find/create as a string
def createAlmanacMap(almanac, map_name) -> AlmanacMap:
    _dst = []
    _src  = []
    _len  = []
    map_found = False
    for line in almanac:
        if not map_name in line and not map_found:
            continue
        if not map_found:
            map_found = True
            continue
        if line == '' and map_found:
            break

        _range = line.split(' ')
        _dst.append(int(_range[0]))
        _src.append(int(_range[1]))
        _len.append(int(_range[2]))
        
    return AlmanacMap(_dst, _src, _len)


def main1():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    # file_name = 'almanac.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    almanac = myfile.read_text().split('\n')
    # *****************************

    seeds = [int(x) for x in almanac[0].split(' ')[1:]]

    seed2soil = createAlmanacMap(almanac, 'seed-to-soil')
    soil2fertilizer = createAlmanacMap(almanac, 'soil-to-fertilizer')
    fertilizer2water = createAlmanacMap(almanac, 'fertilizer-to-water')
    water2light = createAlmanacMap(almanac, 'water-to-light')
    light2temperature = createAlmanacMap(almanac, 'light-to-temperature')
    temperature2humidity = createAlmanacMap(almanac, 'temperature-to-humidity')
    humidity2location = createAlmanacMap(almanac, 'humidity-to-location')

    locations = humidity2location.map(temperature2humidity.map(light2temperature.map(water2light.map(fertilizer2water.map(soil2fertilizer.map(seed2soil.map(seeds)))))))

    print("smallest location: " + str(min(locations)))








main1()


