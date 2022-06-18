# Created 6/18/2022
# William Mori
# Word List

from urllib.request import urlopen
from bs4 import BeautifulSoup


def gen_word_list():
    source = "https://www.ics.uci.edu/~kay/wordlist.txt"

    page = urlopen(source)
    soup = BeautifulSoup(page, 'html.parser')

    raw_string = soup.text
    string_list = raw_string.split()

    output = open("words.txt", "w+")

    for i in string_list:
        if len(i) == 5 and i.isalpha():
            output.write(i.lower() + '\n')

    output.close()


def __print_words():
    with open("words.txt", "r") as file:
        while word := file.readline().rstrip():
            print(word)


if __name__ == "__main__":
    gen_word_list()
    #__print_words()

