#!/usr/bin/env python
import string
import random

__all__ = ('generate_word', 'generate_words')

initial_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                      # remove those easily confused with others
                      - set('qxc')
                      # add some crunchy clusters
                      | set(['bl', 'br', 'cl', 'cr', 'dr', 'fl',
                             'fr', 'gl', 'gr', 'pl', 'pr', 'sk',
                             'sl', 'sm', 'sn', 'sp', 'st', 'str',
                             'sw', 'tr', 'ch', 'sh'])
                      )

final_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                    # remove the confusables
                    - set('qxcsj')
                    # crunchy clusters
                    | set(['ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt',
                           'pt', 'sk', 'sp', 'ss', 'st', 'ch', 'sh'])
                    )

vowels = list('aeiou') + ['oo']  # "oo" because google


def generate_word(wc=1):
    """Returns a random consonant-(vowel-consonant)*wc pseudo-word."""
    letter_list = [initial_consonants]
    for i in range(wc):
        letter_list.extend([vowels, final_consonants])
    return ''.join(random.choice(s) for s in letter_list)


def generate_words(wordcount=1, word_length=1):
    """Returns a list of ``wordcount`` pseudo-words."""
    # range for Python 3 compatibility
    return [generate_word(wc=word_length) for _ in range(wordcount)]


def console_main():
    import argparse
    len_options = {'small': 1, 'medium': 2, 'large': 3}
    parser = argparse.ArgumentParser(description='Generate gibberish!')
    parser.add_argument(
        "wordcount", type=int, default=1, nargs='?',
        help="Number of words to print.")

    parser.add_argument(
        "-l", "--word_length", type=str, default='small', metavar='',
        choices=['small', 'medium', 'large'],
        help="Length of the words")
    args = parser.parse_args()

    print(' '.join(generate_words(
        args.wordcount, len_options[args.word_length])))


if __name__ == '__main__':
    console_main()
