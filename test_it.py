import gibberish


def test_generate_word():
    word = gibberish.generate_word()
    assert len(word)
    assert word.isalpha()


def test_generate_words():
    word_list = gibberish.generate_word()

    assert len(word_list)

    for word in word_list:
        assert len(word)
        assert word.isalpha()
