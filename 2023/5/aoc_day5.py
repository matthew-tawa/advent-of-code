from pathlib import Path

class AlmanacMap:
    # dest, src, length must be lists of numbers, all with same length
    def __init__(self, _dst, _src, _len, max_src = None) -> None:

        # storing the ranges sorted by _dst
        self._dst, self._src, self._len = zip(*sorted(zip(_dst, _src, _len)))
        self._dst = list(self._dst)
        self._src = list(self._src)
        self._len = list(self._len)

        # adding non-mapped ranges as one-to-one mapping
        if self._src[0] != 0:
            # note the order of the following three statements is important
            self._len.insert(0, min(self._src))
            self._dst.insert(0, 0)
            self._src.insert(0, 0)
        
        if max_src != None and self._src[-1] < max_src:
            # note the order of the following three statements is important
            self._src.append(max(self._src) + self._len[self._src.index(max(self._src))])
            self._len.append(max(max_src - max(self._src) + 1, 0))
            self._dst.append(max(self._src))

        # storing the ranges sorted by _dst
        self._dst, self._src, self._len = zip(*sorted(zip(self._dst, self._src, self._len)))
        self._dst = list(self._dst)
        self._src = list(self._src)
        self._len = list(self._len)    
            
        self.num_ranges = len(_dst)

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
    
    # _val -> int to reverse map
    # return -> int that has been reversed through the map
    def map_rev(self, val: list) -> list:
        return [self._map_rev(x) for x in val]
    
    # _val -> int to reverse map
    # return -> int that has been reversed through the map
    def _map_rev(self, _val: int) -> list:
        rev_val = []
        for i in range(self.num_ranges):
            if self._len[i] != 0 and _val in range(self._dst[i], self._dst[i] + self._len[i]):
                rev_val.append(_val - self._dst[i] + self._src[i])
        
        if not rev_val:
            rev_val = [_val]

        return rev_val
    
    # # return -> return the map as a list. list[0] = destinations, list[1] = sources, list[2] = lengths
    # def get(self) -> list:
    #     return [self._dst, self._src, self._len]
    
    # return -> return list of sources
    def get_src(self) -> list:
        return self._src
    
    # return -> return list of sources
    def get_dst(self) -> list:
        return self._dst


# create a map and return it
# almanac  -> the almanac
# map_name -> name of map to find/create as a string
def createAlmanacMap(almanac, map_name, seed_max) -> AlmanacMap:
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
        
    return AlmanacMap(_dst, _src, _len, seed_max)


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


def main2():
    # ***** IMPORT INPUT FILE *****
    # obtaining the proper relative path
    script_location = Path(__file__).absolute().parent
    # file_name = 'almanac.txt'
    # file_name = 'testing.txt'
    file_name = 'input.txt'
    myfile = script_location / file_name

    # read the file into a list, split by the newline characters
    # note:  read_text() automatically closes file when done 
    almanac = myfile.read_text().split('\n')
    # *****************************

    seed_pairs = [int(x) for x in almanac[0].split(' ')[1:]]
    seed_pairs = [(seed_pairs[2*i], seed_pairs[2*i+1]) for i in range(int(len(seed_pairs)/2))]

    seed_max = 0
    for pair in seed_pairs:
        seed_max = pair[0]+pair[1] if pair[0]+pair[1] > seed_max else seed_max

    maps: AlmanacMap = []
    seed2soil = createAlmanacMap(almanac, 'seed-to-soil', seed_max)
    soil2fertilizer = createAlmanacMap(almanac, 'soil-to-fertilizer', seed_max)
    fertilizer2water = createAlmanacMap(almanac, 'fertilizer-to-water', seed_max)
    water2light = createAlmanacMap(almanac, 'water-to-light', seed_max)
    light2temperature = createAlmanacMap(almanac, 'light-to-temperature', seed_max)
    temperature2humidity = createAlmanacMap(almanac, 'temperature-to-humidity', seed_max)
    humidity2location = createAlmanacMap(almanac, 'humidity-to-location', seed_max)
    maps.append(seed2soil)
    maps.append(soil2fertilizer)
    maps.append(fertilizer2water)
    maps.append(water2light)
    maps.append(light2temperature)
    maps.append(temperature2humidity)
    maps.append(humidity2location)

    # finding all potentially interesting seeds
    interesting_seeds = set()

    # since the seeds are interesting at different map levels, reverse run all seeds through all maps
    i = 2
    for map in reversed(maps): # reversed() to start with humidity2location map
        if i > 0:
            interesting_seeds = interesting_seeds.union({x for x in map.get_dst()})
            i -= 1
        rev_seeds = map.map_rev(interesting_seeds)
        map_rev_tuples = tuple([tuple(x) for x in rev_seeds])
        interesting_seeds = interesting_seeds.union({x for x in map_rev_tuples})

    # making sure any interesting seeds are in the given seeds
    final_seeds = set()
    for seed in interesting_seeds:
        for pair in seed_pairs:
            if seed in range(pair[0], pair[0]+pair[1]):
                final_seeds.add(seed)
                break

    locations = humidity2location.map(temperature2humidity.map(light2temperature.map(water2light.map(fertilizer2water.map(soil2fertilizer.map(seed2soil.map(final_seeds)))))))

    print("smallest location: " + str(min(locations)))








# main1()
main2()


