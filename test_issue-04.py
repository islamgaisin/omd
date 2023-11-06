from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    "source,result", [
        (['Moscow', 'New York', 'Moscow', 'London'], [('Moscow', [0, 0, 1]),
                                                      ('New York', [0, 1, 0]),
                                                      ('Moscow', [0, 0, 1]),
                                                      ('London', [1, 0, 0])
                                                      ]),
        ('ab', [('ab', [1])]),
    ],
)
def test_fit_transform(source, result):
    assert fit_transform(source) == result


def test_empty_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform()
