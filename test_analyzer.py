import pytest
from analyzer import count_words, count_chars

def test_count_words():
    assert count_words("") == 0
    assert count_words("hello world") == 2
    assert count_words("it's it's")

def test_count_chars():
    assert count_chars("") == 0
    assert count_chars("warffafa") == 8
    assert count_chars("as34s'd;") == 8
    assert count_chars("fs esf") == 5