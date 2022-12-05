from helpers import data_loading

def get_totals(data, num_elves):
    total = 0
    high_scores = [0] * num_elves
    for ln in data:
        try:
            total += int(ln)
        except ValueError:
            if total > high_scores[0]:
                high_scores [0] = total
                high_scores.sort()
            total = 0
    return sum(high_scores)

def part1():
    data = data_loading.load_data(1, 1)
    return get_totals(data, 1)

def part2():
    data = data_loading.load_data(1, 1)
    return get_totals(data, 3)