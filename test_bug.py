from bug import apply_discount


def test_applies_discount_once():
    assert apply_discount(1000, 10) == 900


def test_zero_discount():
    assert apply_discount(1000, 0) == 1000