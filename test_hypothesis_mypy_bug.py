from hypothesis import given
from hypothesis.strategies import floats, tuples


@given(tuples(floats(), floats()).map(sorted).filter(lambda x: x[0] < x[1]))
def test_map_filter(value):
    assert len(value) == 2


@given(tuples(floats(), floats()).filter(lambda x: x[0] != x[1]).map(sorted))
def test_filter_map(value):
    assert len(value) == 2
