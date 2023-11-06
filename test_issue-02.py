from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result", [
        ('... --- ...', 'SOS'),
        ('.... . .-.. .--.', 'HELP'),
        ('.- .- .-', 'AAA'),
        ('.- -... -.-. -..', 'ABCD'),
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result
