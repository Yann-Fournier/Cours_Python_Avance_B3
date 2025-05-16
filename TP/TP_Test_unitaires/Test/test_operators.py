from calculate.operators import Operators

operators = Operators()

def test_is_symbole_valid():
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
    assert operators._is_symbol_valid(Operators().substraction("1 - 2-3.0")) == True
    assert operators._is_symbol_valid(Operators().substraction("1 + 2*3")) == False
    
    # Multiplication
    assert operators._is_symbol_valid(Operators().multiplication("1 * 2*3.0")) == True
    assert operators._is_symbol_valid(Operators().multiplication("1 + 2-3")) == False
    
    # Division
    assert operators._is_symbol_valid(Operators().division("1 / 2/3.0")) == True
    assert operators._is_symbol_valid(Operators().division("1 + 2*3")) == False
    
    # Puissance
    assert operators._is_symbol_valid(Operators().puissance("1 ^ 2^3.0")) == True
    assert operators._is_symbol_valid(Operators().puissance("1 + 2*3")) == False
    
    # Racine carree
    assert operators._is_symbol_valid(Operators().racine_carree("v81")) == True
    assert operators._is_symbol_valid(Operators().racine_carree("v81v9.0")) == True
    assert operators._is_symbol_valid(Operators().racine_carree("v81v9*5")) == False
    
    # Factorielle
    assert operators._is_symbol_valid(Operators().factorielle("5.0!")) == True
    assert operators._is_symbol_valid(Operators().factorielle("5!+2")) == False
    
    # Logarithme
    assert operators._is_symbol_valid(Operators().logarithme("l2")) == True
    assert operators._is_symbol_valid(Operators().logarithme("l2l3.0")) == True
    assert operators._is_symbol_valid(Operators().logarithme("l3+2")) == False
    
    # Exponentielle
    assert operators._is_symbol_valid(Operators().exponentielle("e2")) == True
    assert operators._is_symbol_valid(Operators().exponentielle("e2e3.0")) == True
    assert operators._is_symbol_valid(Operators().exponentielle("e2+3")) == False
    

# def test_is_float():
#     pass

# def test_calculate_addition():
#     pass

# def test_calculate_substraction():
#     pass

# def test_calculate_multiplication():
#     pass

# def test_calculate_division():
#     pass

# def test_calculate_puissance():
#     pass

# def test_calculate_racine_carree():
#     pass

# def test_calculate_factorielle():
#     pass

# def test_calculate_logarithme():
#     pass

# def test_calculate_exponentielle():
#     pass
    
    