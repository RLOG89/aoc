from helpers import data_loading

def shape_score(shape):
    scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    return scores[shape]

def result_score(shapes):
    win = 6
    draw = 3
    lose = 0
    
    if shapes[0] == shapes[1]:
        outcome = draw
    else:
        match shapes:
            case ['rock', 'scissors'] | ['scissors', 'paper'] | ['paper', 'rock']:
                outcome = lose
            case _:
                outcome = win
    return outcome

def total_score(shapes):
    total = 0
    total += shape_score(shapes[1])
    total += result_score(shapes)
    return total

def define_shape(opponent_shape, result):
    match result:
        case 'win':
            if opponent_shape == 'rock':
                shape = 'paper'
            elif opponent_shape == 'scissors':
                shape = 'rock'
            elif opponent_shape == 'paper':
                shape = 'scissors'
        case 'draw':
            shape = opponent_shape
        case 'lose':
            if opponent_shape == 'paper':
                shape = 'rock'
            elif opponent_shape == 'rock':
                shape = 'scissors'
            elif opponent_shape == 'scissors':
                shape = 'paper'
    return shape
    
def part1():
    data = data_loading.load_data(2, 1)
    shapes = {'A' : 'rock', 'B' : 'paper', 'C' : 'scissors',
              'X' : 'rock', 'Y' : 'paper', 'Z' : 'scissors'}
    data_arr = [[shapes[i] for i in ln.split(' ')] for ln in data]
    total = sum([total_score(ln) for ln in data_arr])
    return total

def part2():
    data = data_loading.load_data(2, 1)
    shapes = {'A' : 'rock', 'B' : 'paper', 'C' : 'scissors',
              'X' : 'lose', 'Y' : 'draw', 'Z' : 'win'}
    result_arr = [[shapes[i] for i in ln.split(' ')] for ln in data]
    data_arr = [[ln[0], define_shape(ln[0], ln[1])] for ln in result_arr]
    total = sum([total_score(ln) for ln in data_arr])
    return total