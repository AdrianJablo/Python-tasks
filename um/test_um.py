from um import count
import pytest

def test_upper_and_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_word_with_um():
    assert count('yummi') == 0

def test_surround_space():
    assert count('Hello um world') == 1
    assert count('um?') == 1

