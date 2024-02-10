import pytest
from src import utils
def test_get_operations():
    pass


def test_encode_account():
    assert utils.get_sent("Счет 43241152692663622869") == "Счет **2869"


def encode_card():
    assert utils.get_sent("Maestro 7810846596785568") == "Maestro 7810 46** ****5568"