import pytest
from game import process_input, check_letter, check_win


@pytest.mark.parametrize("l", ["a", "A", "lan",])
def test_process_input_valid(l):
    letter, valid = process_input(l)
    assert letter == l.lower()[0]
    assert valid

@pytest.mark.parametrize("l", ["1", "321asd", " a",])
def test_process_input_invalid(l):
    letter, valid = process_input(l)
    assert letter == l[0]
    assert not valid

def test_check_letter_in():
    res = check_letter("skillfactory", "l")
    assert res == [3, 4]

def test_check_letter_out():
    res = check_letter("blackbox", "d")
    assert not res

def test_check_win_true():
    assert check_win("pytest", list("pytest"))

def test_check_win_false():
    guess = list("coverage")
    guess[0] = "_"    
    assert not check_win("coverage", guess)

