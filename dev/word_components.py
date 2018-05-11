from nltk.corpus import cmudict
import string
from collections import Counter
import yaml


def initial_consonants():
    for word in cmudict.words():
        initial = ''
        for char in word:
            if char not in 'aeiou' and char in string.ascii_letters:
                initial += char
            else:
                if len(initial) != 0:
                    yield initial
                break


def final_consonants():
    for word in cmudict.words():
        final = ''
        for char in word[::-1]:
            if char not in 'aeiou' and char in string.ascii_letters:
                final += char
            else:
                if len(final) != 0:
                    yield final[::-1]
                break


def vowels():
    for word in cmudict.words():
        vowel = ''
        vowel_started = False
        for char in word:
            if char in 'aeiou':
                vowel_started = True
                vowel += char
            else:
                if vowel_started:
                    yield vowel
                break

        vowel = ''
        vowel_started = False
        for char in word[::-1]:
            if char in 'aeiou':
                vowel_started = True
                vowel += char
            else:
                if vowel_started:
                    yield vowel[::-1]
                break


if __name__ == '__main__':
    with open('../gibberish/raw_components.yaml', 'w') as f:
        yaml.safe_dump({
            'initials': [x[0] for x in Counter(initial_consonants()).most_common()],
            'vowels': [x[0] for x in Counter(vowels()).most_common()],
            'finals': [x[0] for x in Counter(final_consonants()).most_common()]
        }, f)
