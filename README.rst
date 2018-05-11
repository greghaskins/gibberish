==================================
Gibberish: a pseudo-word generator
==================================

The ``gibberish`` module let's you generate random, pronounceable pseudo-words. It started life as an `answer on StackOverflow <http://stackoverflow.com/a/5502875/356942>`_ about password generators , but it's also a fun way to coin words or just spark some lexical creativity.

Usage
-----

``gibberish`` creates pseudo-words which consist of one consonant-vowel-consonant syllable that sounds like it could be English. Sometimes it spits out real words; most of the time not::

  >>> from gibberish import Gibberish
  >>> gib = Gibberish()
  >>> gib.generate_word()
  'zept'
  >>> gib.generate_word()
  'prast'
  >>> gib.generate_words(3)
  ['sqiounn', 'nuil', 'hydrieucks']

It also works as a console script::

  ~$ gibberish 6
  strit druf doct vel dosk flomp
  ~$ gibberish
  brank
  ~$ gibberish 1 -l large
  fabaduk
  ~$ gibberish 2 -l medium
  voskot koontan

Installation
------------

To install the ``gibberish`` module and console script globally, clone this repository and run:

  ~$ python setup.py install

Updates
-------

- (2017.5.11)
   - Analyze the components from CMUdict (``nltk.corpus.cmudict``) entries.
   - Use ``secrets`` module if Python version 3.6 or later.

Contributions
-------------

Please help edit entry the ``gibberish/database/components.yaml`` as which of the characters is an initial consonant, final consonants, or vowels is opinionated.
