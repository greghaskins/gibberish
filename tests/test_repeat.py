from gibberish import Gibberish

gib = Gibberish()


def test_generate_word(rep=50):
    for _ in range(rep):
        print(gib.generate_word())


def test_generate_word_start_vowel(rep=50):
    for _ in range(rep):
        print(gib.generate_word(start_vowel=True))


def test_generate_word_end_vowel(rep=50):
    for _ in range(rep):
        print(gib.generate_word(end_vowel=True))


def test_generate_words(rep=50):
    for _ in range(rep):
        print(gib.generate_words(3))


if __name__ == '__main__':
    test_generate_word()
    test_generate_words()
    test_generate_word_start_vowel()
    test_generate_word_end_vowel()
