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
    parser = argparse.ArgumentParser(description="A command line version of wordle")
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

    args = parser.parse_args()

    if args.unlimited:
        gameBase.almostWordleGame(False, debug=args.debug).run()
    else:
        gameBase.almostWordleGame(True, args.guesses, args.debug).run()


