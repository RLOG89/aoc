from helpers import data_loading
import string

def split_arr(arr):
    chunk_size = len(arr) // 2
    return [arr[i: i + chunk_size] for i in range(0, len(arr), chunk_size)]

def compare(arr1, *argv):
    return frozenset(arr1).intersection(*argv)

def generate_dict():
    lower = dict(zip(string.ascii_lowercase, [v + 1 for v in range(26)]))
    upper = dict(zip(string.ascii_uppercase, [v + 1 for v in range(26, 52)]))
    return lower | upper

def map_values(matches):
    letter_values = generate_dict()
    total = 0
    
    for i in range(len(matches)):
        for s in matches[i]:
            total += letter_values[s]
    
    return total
    
def part1():
    data = data_loading.load_data(3, 1)
    halves = [split_arr(ln) for ln in data]
    matches = [compare(ln[0], ln[1]) for ln in halves]
    total = map_values(matches)
    
    return total
    
def part2():
    data = data_loading.load_data(3, 1)
    matches = []
    for i in range(0, len(data), 3):
        matches.append(compare(data[i], data[i+1], data[i+2]))
    total = map_values(matches)
    
    return total