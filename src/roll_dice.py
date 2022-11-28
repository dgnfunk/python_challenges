from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for roll in range(num_trials):
        print('Roll dice {}'.format(roll))
        for sides in dice:
            print('Sides {}'.format(randint(1, sides)))
            print('SUMS IN {}'.format(sum(randint(1, sides))))
        print('SUM {}'.format(sum((randint(1, sides) for sides in dice))))

if __name__ == '__main__':
    roll_dice(4, 5, 6, num_trials=30)
