from random import random
import argparse
import sys

def main(*args):
    parser = argparse.ArgumentParser(description="Play Mastermind")
    parser.add_argument('-a', '--attempts', type=int,
                        help='the number of attempts', default=20)
    parser.add_argument('-c', '--code', type=str,
                        help='the code to guess', default=None)
    parser.add_argument('-l', '--length', type=int,
                        help='the length of the code', default=4)
    parser.add_argument('--hide', action='store_true',
                        help='hides the input into terminal')
    args = parser.parse_args()

    length = args.length
    t = args.code
    attempts = args.attempts
    if t is None:
        t = str(int(((10 ** length) - 1) * random()))
        t = '0'*(length - len(t)) + t

    if args.hide:
        print("\n"*75)

    play(t, attempts)


def play(code, attempts):
    game = Mastermind(code, attempts)
    print("Type in q anytime to quit.") 
    game.run()


class Mastermind:

    def __init__(self, code, attempts):
        self._code = list(code)
        self.attempts = attempts

    def run(self):
        for i in range(self.attempts):
            self.take_guess()
            if self.has_quit():
                return
            self.give_hint()
            if self.has_won():
                print("# You Win!")
                print("You took " + str(i + 1) + " attempts")
                return
        print("# You lose. The code was: " + self.code)

    def has_won(self):
        return self.guess == self._code

    def has_quit(self):
        return ''.join(self.guess) in ('q', 'quit', 'Quit', 'QUIT', 'Q', 'Fuck this shit')


    def take_guess(self):
        self.guess = list(input("> Guess: "))

    def give_hint(self):
        print("> " + self.hint())

    def hint(self):
        if len(self.guess) != len(self._code):
            print("Guess must be " + str(len(self._code)) + " long.")
            self.take_guess()
            self.has_quit
            self.hint()
        hint = ""
        code, guess = self._code[:], self.guess[:]
        for i in range(len(self._code)):
            if code[i] == guess[i]:
                code[i], guess[i] = 'p', 'q'
                hint += 'X'
        for g in guess:
            if g in code:
                code.remove(g)
                hint += 'O'
        for _ in range(len(self._code) - len(hint)):
            hint += '_'
        return hint


if __name__ == "__main__":
    main(sys.argv[1:])