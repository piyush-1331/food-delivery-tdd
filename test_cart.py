from cart import calculate_total

def test_calculate_total():
    assert calculate_total(100, 2) == 200

def test_calculate_total_for_multiple_items():
    assert calculate_total(50, 3) == 150

def test_calculate_total_zero_quantity():
    assert calculate_total(100, 0) == 0

def test_calculate_total_single_item():
    assert calculate_total(250, 1) == 250
