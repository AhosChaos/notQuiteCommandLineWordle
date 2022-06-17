# Created 6/16/2022
# William Mori
# Game Base

from english_words import english_words_lower_alpha_set
from time import sleep
from termcolor import cprint


class almostWordleGame:
    def __init__(self, limit: bool, limit_value: int = 7, debug: bool = False):
        self.limit = limit
        self.limit_value = limit_value
        self.word_len = 5
        self.debug = debug

        self.word = self._select_word()
        self.history = []
        self.last_guess = ""

        if self.debug:
            print(self.limit, self.limit_value)

    def _select_word(self):
        while True:
            sample_word = english_words_lower_alpha_set.pop()
            english_words_lower_alpha_set.add(sample_word)
            if len(sample_word) == self.word_len:
                if self.debug:
                    print(sample_word)

                for i in sample_word:
                    if sample_word.count(i) > 2:
                        if self.debug: print("skipped", sample_word)
                        continue

                return sample_word

    def run(self):
        print("Start\t"+ "_"*self.word_len)
        while self.last_guess != self.word:
            if self.limit and len(self.history) == self.limit_value - 1:
                print("Final Guess")
            elif self.limit and len(self.history) >= self.limit_value:
                break
            self.last_guess = self._take_guess()
            self.history.append(self.last_guess)
            self._print_state()
        if self.last_guess == self.word:
            print("SUCCESS!")
            self._print_guess(self.word)
        else:
            print("GAME OVER")
            print("Answer:\t", end="")

            for i in self.word:
                cprint(i, "grey", "on_red", end="")

    def _take_guess(self):
        guess = self._take_input()
        while True:
            if len(guess) != self.word_len or guess.isalpha() is False:
                self._print_error("Enter a " + str(self.word_len) + " letter word")
                self._print_state()
                guess = self._take_input()
            elif guess not in english_words_lower_alpha_set:
                self._print_error("Not a recognized word")
                self._print_state()
                guess = self._take_input()
            else:
                break
        return guess

    def _take_input(self):
        return input("Guess:\t").lower()

    @staticmethod
    def _print_error(error_msg):
        print("", end='\r')
        print(error_msg, end="")
        sleep(1)
        print("", end='\r')

    def _print_state(self):
        i = 1
        for guess in self.history:
            print(str(i) + ".\t\t", end="")
            self._print_guess(guess)
            i += 1

    def _print_guess(self, guess):
        color_guide = []
        for i in range(self.word_len):
            if guess[i] == self.word[i]:
                color_guide.append('on_green')
            elif guess[i] in self.word:
                color_guide.append('on_yellow')
            else:
                color_guide.append('on_white')
        for i in range(self.word_len):
            cprint(guess[i], "grey", color_guide[i], end="")
        print()
