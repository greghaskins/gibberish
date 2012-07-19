==================================
Gibberish: a pseudo-word generator
==================================

The ``gibberish`` module let's you generate random, pronounceable pseudo-words. It started life as an `answer on StackOverflow <http://stackoverflow.com/a/5502875/356942>`_ about password generators , but it's also a fun way to coin words or just spark some lexical creativity.

Usage
-----

``gibberish`` creates pseudo-words which consist of one consonant-vowel-consonant syllable that sounds like it could be English. Sometimes it spits out real words; most of the time not::

  >>> import gibberish
  >>> gibberish.generate_word()
  'zept'
  >>> gibberish.generate_word()
  'prast'
  >>> gibberish.generate_words(3)
  ['yink', 'glunt', 'skim', 'jask']

It also works as a console script::

  ~$ gibberish 6
  strit druf doct vel dosk flomp
  ~$ gibberish
  brank
