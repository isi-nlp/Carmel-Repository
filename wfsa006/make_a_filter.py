__author__ = 'aderi'

import sys

ALPHABET = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper()


def get_alphabet():
    alphabet = ALPHABET.split()

    for i, letter in enumerate(alphabet):
        alphabet[i] = '\"' + letter + '\"'
    alphabet = set(alphabet)
    return alphabet


def prepare_word(word):
    # if '_' in word:
    # word.remove('_')
    for i, letter in enumerate(word):
        word[i] = '\"' + letter + '\"'

    return word


def make_a_filter(word, outfile_name):
    """
    creates the component word filter (or, really any filter)
    :param word: the word to filter out
    :param outfile_name: the file to write to
    """
    alphabet = get_alphabet()

    """capitalize word"""
    word = list(word.upper())

    word = prepare_word(word)
    with open(outfile_name, 'w') as outfile:
        """write end state"""
        outfile.write("0\n")

        """go through word"""
        for i, letter in enumerate(word):
            start_state = i + 1
            end_state = i + 2

            s = "(" + str(start_state) + " (" + str(end_state) + " " + letter + " 1.0)"

            for alphabet_letter in alphabet:
                if alphabet_letter != letter:
                    s += " (0 " + alphabet_letter + " 1.0)"

            s += ")\n"
            outfile.write(s)
            # print s

        """write last state of word, all letters of alphabet to 0"""

        start_state = len(word) + 1
        s = "(" + str(start_state)
        for alphabet_letter in alphabet:
            s += " (0 " + alphabet_letter + " 1.0)"

        s += ")\n"
        outfile.write(s)

        start_state = 0
        s = "(" + str(start_state)
        for alphabet_letter in alphabet:
            s += " (0 " + alphabet_letter + " 1.0)"

        s += ")\n"
        outfile.write(s)


if __name__ == "__main__":
    make_a_filter(sys.argv[1], 'filter.wfsa')
