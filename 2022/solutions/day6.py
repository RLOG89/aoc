from helpers import data_loading

data = data_loading.load_raw(6, 1)

def is_unique(arr):
    return len(arr) == len(set(arr))

def get_position(chunk):
    offset = 0
    arr = list(data)
    
    while not is_unique(arr[offset:offset + chunk]):
        offset += 1
    return offset + chunk

def part1():
    return get_position(4)

def part2():
    return get_position(14)