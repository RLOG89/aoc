from helpers import data_loading
import re

data = data = data_loading.load_data(4, 1)

def part1():
    total = 0
    
    for ln in data:
        a1, a2, b1, b2 = map(int, re.findall(r'(\d+)', ln))
               
        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            total += 1
    return total

def part2():
    total = 0
    
    for ln in data:
        a1, a2, b1, b2 = map(int, re.findall(r'(\d+)', ln))
               
        if a1 <= b2 and b1 <= a2:
            total += 1
    return total