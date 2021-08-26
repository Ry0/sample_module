import sample_module


def test_case1():
    a = sample_module.HogeHogeClass()
    result = a.add(1, 2)
    assert result == 3
