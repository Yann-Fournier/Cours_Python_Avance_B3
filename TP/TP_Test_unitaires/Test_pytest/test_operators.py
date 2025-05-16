from calculate.operators import Operators

def test_is_symbole_valid():
    """
    Test the _is_symbol_valid() method of the Operators class.
    This method checks if the symbol of the operation is valid.
    """
    # Addition
    add1 = Operators()
    add1.operation = "1 + 2+3.0"
    add1.signe = "+"
    add2 = Operators()
    add2.operation = "1 - 2*3"
    add2.signe = "+"
    assert add1._is_symbol_valid() == True
    assert add2._is_symbol_valid() == False
    
    # Substraction
    sub1 = Operators()
    sub1.operation = "1 - 2-3.0"
    sub1.signe = "-"
    sub2 = Operators()
    sub2.operation = "1 + 2*3"
    sub2.signe = "-"
    assert sub1._is_symbol_valid() == True
    assert sub2._is_symbol_valid() == False
    
    # Multiplication
    mul1 = Operators()
    mul1.operation = "1 * 2*3.0"
    mul1.signe = "*"
    mul2 = Operators()
    mul2.operation = "1 + 2-3"
    mul2.signe = "*"
    assert mul1._is_symbol_valid() == True
    assert mul2._is_symbol_valid() == False
    
    # Division
    div1 = Operators()
    div1.operation = "1 / 2/3.0"
    div1.signe = "/"
    div2 = Operators()
    div2.operation = "1 + 2*3"
    div2.signe = "/"
    assert div1._is_symbol_valid() == True
    assert div2._is_symbol_valid() == False
    
    # Puissance
    pui1 = Operators()
    pui1.operation = "1 ^ 2^3.0"
    pui1.signe = "^"
    pui2 = Operators()
    pui2.operation = "1 + 2*3"
    pui2.signe = "^"
    assert pui1._is_symbol_valid() == True
    assert pui2._is_symbol_valid() == False
    
    # Racine carree
    rac1 = Operators()
    rac1.operation = "v81"
    rac1.signe = "v"
    rac2 = Operators()
    rac2.operation = "v81v9.0"
    rac2.signe = "v"
    rac3 = Operators()
    rac3.operation = "v81v9*5"
    rac3.signe = "v"
    assert rac1._is_symbol_valid() == True
    assert rac2._is_symbol_valid() == True
    assert rac3._is_symbol_valid() == False
    
    # Factorielle
    fac1 = Operators()
    fac1.operation = "5.0!"
    fac1.signe = "!"
    fac2 = Operators()
    fac2.operation = "5!+2"
    fac2.signe = "!"
    fac3 = Operators()
    assert fac1._is_symbol_valid() == True
    assert fac2._is_symbol_valid() == False
    
    # Logarithme
    log1 = Operators()
    log1.operation = "l2"
    log1.signe = "l"
    log2 = Operators()
    log2.operation = "l2l3.0"
    log2.signe = "l"
    log3 = Operators()
    log3.operation = "l2+3"
    log3.signe = "l"
    assert log1._is_symbol_valid() == True
    assert log2._is_symbol_valid() == True
    assert log3._is_symbol_valid() == False
    
    # Exponentielle
    exp1 = Operators()
    exp1.operation = "e2"
    exp1.signe = "e"
    exp2 = Operators()
    exp2.operation = "e2e3.0"
    exp2.signe = "e"
    exp3 = Operators()
    exp3.operation = "e2+3"
    exp3.signe = "e"
    assert exp1._is_symbol_valid() == True
    assert exp2._is_symbol_valid() == True
    assert exp3._is_symbol_valid() == False
    

def test_is_float():
    """
    Test the _is_float() method of the Operators class.
    This method checks if the operation is a float.
    """
    assert Operators()._is_float("1.0") == True
    assert Operators()._is_float("1.0453") == True
    assert Operators()._is_float("-1") == True
    assert Operators()._is_float("10") == True
    assert Operators()._is_float("1+2") == False
    assert Operators()._is_float("1-2") == False
    assert Operators()._is_float("1*2") == False
    assert Operators()._is_float("1/2") == False
    assert Operators()._is_float("1^2") == False
    assert Operators()._is_float("1v2") == False
    assert Operators()._is_float("1!") == False
    assert Operators()._is_float("l2") == False
    assert Operators()._is_float("e2") == False

def test_calculate_addition():
    """
    Test the _calculate_addition() method of the Operators class.
    This method checks if the addition calculation is correct.
    """
    add1 = Operators()
    add1.numbers = ["1", "2", "3.0"]
    add1._calculate_addition()
    assert add1.result == 6.0

def test_calculate_substraction():
    """
    Test the _calculate_substraction() method of the Operators class.
    This method checks if the substraction calculation is correct.
    """
    sub1 = Operators()
    sub1.numbers = ["5", "2", "3.0"]
    sub1._calculate_substraction()
    assert sub1.result == 0.0

def test_calculate_multiplication():
    """
    Test the _calculate_multiplication() method of the Operators class.
    This method checks if the multiplication calculation is correct.
    """
    mul1 = Operators()
    mul1.numbers = ["2", "3", "4.0"]
    mul1._calculate_multiplication()
    assert mul1.result == 24.0

def test_calculate_division():
    """
    Test the _calculate_division() method of the Operators class.
    This method checks if the division calculation is correct.
    """
    div1 = Operators()
    div1.numbers = ["8", "4"]
    div1._calculate_division()
    assert div1.result == 2.0
    
    div1 = Operators()
    div1.numbers = ["8", "0"]
    div1._calculate_division()
    assert div1.result == None

def test_calculate_puissance():
    """
    Test the _calculate_puissance() method of the Operators class.
    This method checks if the puissance calculation is correct.
    """
    pui1 = Operators()
    pui1.numbers = ["2", "8"]
    pui1._calculate_puissance()
    assert pui1.result == 256.0

def test_calculate_racine_carree():
    """
    Test the _calculate_racine_carree() method of the Operators class.
    This method checks if the racine carree calculation is correct.
    """
    rac1 = Operators()
    rac1.numbers = ["16"]
    rac1._calculate_racine_carree()
    assert rac1.result == 4.0
    
    rac2 = Operators()
    rac2.numbers = ["-16"]
    rac2._calculate_racine_carree()
    assert rac2.result == None
    
    rac3 = Operators()
    rac3.numbers = ["0"]
    rac3._calculate_racine_carree()
    assert rac3.result == 0.0

def test_calculate_factorielle():
    """
    Test the _calculate_factorielle() method of the Operators class.
    This method checks if the factorielle calculation is correct.
    """
    fac1 = Operators()
    fac1.numbers = ["5"]
    fac1._calculate_factorielle()
    assert fac1.result == 120
    
    fac2 = Operators()
    fac2.numbers = ["0"]
    fac2._calculate_factorielle()
    assert fac2.result == 1

def test_calculate_logarithme():
    """
    Test the _calculate_logarithme() method of the Operators class.
    This method checks if the logarithme calculation is correct.
    """
    log1 = Operators()
    log1.numbers = ["2"]
    log1._calculate_logarithme()
    assert log1.result == 0.6931471805599453
    
    log2 = Operators()
    log2.numbers = ["1"]
    log2._calculate_logarithme()
    assert log2.result == 0

def test_calculate_exponentielle():
    """
    Test the _calculate_exponentielle() method of the Operators class.
    This method checks if the exponentielle calculation is correct.
    """
    exp1 = Operators()
    exp1.numbers = ["2"]
    exp1._calculate_exponentielle()
    assert exp1.result == 7.38905609893065
    
    exp2 = Operators()
    exp2.numbers = ["0"]
    exp2._calculate_exponentielle()
    assert exp2.result == 1
    
    