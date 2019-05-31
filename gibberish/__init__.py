#!/usr/bin/env python
import string
import yaml
try:
    from secrets import choice
except ImportError:
    from random import choice

from gibberish.dir import database_path

__all__ = ('Gibberish', )


class Gibberish:
    def __init__(self, component_file=database_path('components.yaml')):
        with open(component_file) as f:
            components = yaml.safe_load(f)

        self.initial_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                                  # remove those easily confused with others
                                  - set('qxc')
                                  # add some crunchy clusters
                                  | set(sum(components['initials'], []))
                                  )

        self.final_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                                # remove the confusables
                                - set('qxcsj')
                                # crunchy clusters
                                | set(sum(components['finals'], []))
                                )

        self.vowels = list(set(sum(components['vowels'], []))) # "oo" because google

    def generate_word(self, vowel_consonant_repeats=1, start_vowel=False, end_vowel=False):
        """Returns a random consonant-(vowel-consonant)*wc pseudo-word."""
        if not start_vowel:
            letter_list = [self.initial_consonants]
        else:
            letter_list = []
        for i in range(vowel_consonant_repeats):
            letter_list.extend([self.vowels, self.final_consonants])
        if end_vowel:
            letter_list.pop()
        return ''.join(choice(s) for s in letter_list)

    def generate_words(self, wordcount=1, vowel_consonant_repeats=1):
        """Returns a list of ``wordcount`` pseudo-words."""
        # range for Python 3 compatibility
        return [self.generate_word(vowel_consonant_repeats=vowel_consonant_repeats if vowel_consonant_repeats else choice(range(1,4))) for _ in range(wordcount)]


def console_main():
    import argparse
    len_options = {'random': 0, 'small': 1, 'medium': 2, 'large': 3}
    parser = argparse.ArgumentParser(description='Generate gibberish!')
    parser.add_argument(
        "wordcount", type=int, default=1, nargs='?',
        help="Number of words to print.")

    parser.add_argument(
        "-l", "--word_length", type=str, default='small', metavar='',
        choices=['random', 'small', 'medium', 'large'],
        help="Length of the words")
    args = parser.parse_args()

    print(' '.join(Gibberish().generate_words(
        args.wordcount, len_options[args.word_length])))


if __name__ == '__main__':
    console_main()
