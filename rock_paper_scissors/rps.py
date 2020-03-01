#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # pass
    outcomes = []
    options = ['rock', 'paper', 'scissors']

    def round_choice(rounds_left, result):
        if rounds_left == 0:
            return  outcomes.append(result)
        for option in options:
             round_choice(rounds_left - 1, result + [option])
    
    round_choice(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
