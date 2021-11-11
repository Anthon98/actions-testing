def test_add_both_param_ints():
    import sys
    sys.path.append('../')
    import main

    # Test 3 integer additions with both parameters.
    assert main.add(5, 3) == 8
    assert main.add(1, 2) == 3
    assert main.add(23, 59) == 82


def test_add_single_param_ints():
    import sys
    sys.path.append('../')
    import main

    '''Test 3 integer additions with a single parameter. 
    The second parameter is 2 by default.'''
    assert main.add(4) == 6
    assert main.add(7) == 9
    assert main.add(30) == 32


def test_multiply_both_param_ints():
    import sys
    sys.path.append('../')
    import main

    # Test 3 integer multiplications with both parameters.
    assert main.multiply(7, 6) == 42
    assert main.multiply(2, 23) == 46
    assert main.multiply(8, 3) == 24


def test_multiply_single_param_ints():
    import sys
    sys.path.append('../')
    import main

    '''Test 3 integer multiplications with a single parameter. 
    The second parameter is 2 by default.'''
    assert main.multiply(6) == 12
    assert main.multiply(25) == 50
    assert main.multiply(235) == 470
