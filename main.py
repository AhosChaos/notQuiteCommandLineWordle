# Created 6/16/2022
# William Mori
# main

import gameBase
import argparse


def valid_guess_input(value):
    try:
        guess = int(value)
        if guess <= 0:
            raise argparse.ArgumentTypeError("%s is not a positive integer" % value)
        return guess
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not a positive integer" % value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A command line version of wordle.  Rules for the game are at the "
                                                 "bottom.",
                                     epilog="Rules:  Guess the secret five letter word.  Letters in your guess will be "
                                            "colored depending on how close they are to the secret word.  "
                                            "Green means the letter appears in the secret word at that location, "
                                            "yellow means the letter is appears in the word, but not the location it "
                                            "is currently in, "
                                            "and grey means that letter does not appear in the secret word.  "
                                            "Some letters may appear in multiple locations in the word.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--limited", help="play notQuiteCommandLineWordle with a limited number of guesses,"
                                               " when neither -l or -u is specified, -l is treated as default",
                       default=True, action="store_true")
    group.add_argument("-u", "--unlimited", help="play notQuiteCommandLineWordle with an unlimited number of guesses, "
                                                 " when neither -l or -u is specified, -l is treated as default",
                       action="store_true")
    parser.add_argument("-g", "--guesses", type=valid_guess_input, default=7,
                        help="Number of guesses to solve the puzzle, this argument is ignored when -u is specified,"
                             " default number of guesses is 7")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="Debug mode, will print out the solution and other values, default value is False")
    parser.add_argument("-i", "--ics", action="store_true", default=False,
                        help="Use the Prof Kay's UCI ICS word list instead of a Python library dictionary.  If the "
                             "word list is not available, a message will be printed and the default Python library "
                             "dictionary will be used, default value is False")

    args = parser.parse_args()

    if args.unlimited:
        gameBase.almostWordleGame(False, debug=args.debug, ics=args.ics).run()
    else:
        gameBase.almostWordleGame(True, args.guesses, debug=args.debug, ics=args.ics).run()


