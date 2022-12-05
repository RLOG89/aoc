from urllib.request import urlopen

def make_filename(day, star):
    return f'input/day{day}_{star}.py'

def save_data(day, filename):
    url = f'https://adventofcode.com/2022/day/{day}/input'
    print(url)
    r = urlopen(url)
    with open(filename, "w") as f:
        f.writelines(r)
    
def load_data(day, star):
    filename = make_filename(day, star)
    
    with open(filename) as f:
        return f.read().splitlines()
    
