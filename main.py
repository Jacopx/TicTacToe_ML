# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *                          TicTacToe_ML by Jacopx                         *
# *                  https://github.com/Jacopx/TicTacToe_ML                 *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Public Libraries
import threading
import random
import datetime
import time

# Personal Libraries
import element

# Global Variable
dim = 3

# Starting point
def main():
    game = element.Board()
    playerbrain = element.Brain()
    print("The board game is the following:")
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game.setboard(board)
    game.printboard(1)

    # Create two threads for gaming
    try:
        # Starting a random player
        init = random.randrange(0, 2, 1)
        if init == 0:
            rpsem = threading.Semaphore(1)
            bpsem = threading.Semaphore(0)
        else:
            rpsem = threading.Semaphore(0)
            bpsem = threading.Semaphore(1)

        print("INI: %d" % init)

        randomth = threading.Thread(target=randomplayer, args=(game, bpsem, rpsem))
        brainth = threading.Thread(target=brainedplayer, args=(game, bpsem, rpsem, playerbrain))

        randomth.start()
        brainth.start()

        randomth.join()
        brainth.join()
    except:
        print("Error: Unable to start threads")


def randomplayer(game, bpsem, rpsem):
    while True:
        rpsem.acquire()
        print('RANDOM: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        time.sleep(1)
        bpsem.release()



def brainedplayer(game, bpsem, rpsem, playerbrain):
    while True:
        bpsem.acquire()
        print('BRAINED: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        time.sleep(1)
        rpsem.release()


if __name__ == "__main__":
    main()
