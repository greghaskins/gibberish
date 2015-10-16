#!/usr/bin/env python
"""Python pseudo-word generator."""
import argparse
import random
import string

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

vowels = 'aeiou'


def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word."""
    return ''.join(random.choice(s) for s in (initial_consonants,
                                              vowels,
                                              final_consonants))


def generate_words(wordcount):
    """Returns a list of ``wordcount`` pseudo-words."""
    return [generate_word() for _ in xrange(wordcount)]


def parser_setup():
    """Instantiate and return an ArgumentParser instance."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("wordcount", nargs="?", default=3, type=int,
                    help="Number of words to generate (default: %(default)s).")
    args = ap.parse_args()

    return args


def console_main():
    args = parser_setup()
    print(' '.join(generate_words(args.wordcount)))


if __name__ == '__main__':
    console_main()
