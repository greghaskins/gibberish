#!/usr/bin/env python
import string
import random
import itertools

__all__ = ('list_all_words', 'generate_word', 'generate_words')

vowels = list(set('aeiou')
          | set("""
          ai au aw ay ea ee eu ew ey ia ie igh oa oe oi oo ou ow oy ue ui y
          """.split()))

initial_consonants = list(set(string.ascii_lowercase) - set(vowels)
                      # remove those easily confused with others
                      - set('qxc')
                      # add some crunchy clusters
                      | set("""
                      bl br ch cl cr dr dw fl fr gl gr pl pr qu sc sch scr sh
                      shr sk sl sm sn sp sph spl spr squ st str sw thr tr tw
                      """.split())
                      )

final_consonants = list(set(string.ascii_lowercase) - set(vowels)
                    # remove the confusables
                    - set('qxcsj')
                    # crunchy clusters
                    | set("""
                    ch ck ct ft ld lf lk ll lm lp lt mp nd ng nk nt pt sh sk sp
                    ss st tch
                    """.split())
                    )


def list_all_words():
    """Returns an iterable of all possible pseudo-words."""
    return itertools.imap(''.join, itertools.product(initial_consonants,
                                                     vowels,
                                                     final_consonants))


def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word."""
    return ''.join(random.choice(s) for s in (initial_consonants,
                                              vowels,
                                              final_consonants))


def generate_words(wordcount):
    """Returns a list of ``wordcount`` pseudo-words."""
    return [generate_word() for _ in xrange(wordcount)]


def console_main():
    import sys
    try:
        wordcount = int(sys.argv[1])
    except (IndexError, ValueError):
        wordcount = 1
    print(' '.join(generate_words(wordcount)))


if __name__ == '__main__':
    console_main()
