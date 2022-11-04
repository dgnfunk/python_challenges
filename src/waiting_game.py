import time
import random

def waiting_game():
    target = random.randint(1, 10)
    print('\nYour target time is {} seconds'.format(target))

    input('------------Press Enter to begin------------------')
    start = time.perf_counter()

    input('\n...Press Enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start

    print('\nElapsed time: {0} seconds'.format(elapsed))
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))

if __name__ == '__main__':
    waiting_game()