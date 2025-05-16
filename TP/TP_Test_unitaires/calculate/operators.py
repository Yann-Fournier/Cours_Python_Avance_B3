from math import log, exp, sqrt, factorial

class Operators:
    def __init__(self):
        self.operation = ""
        self.signe = ""
        self.result = 0.0

    def addition(self, operation):
        """
            Handles an addition operation.

            :param operation: The requested operation by user.
            :return: The addition result if the operation is valid.
        """
        self.operation = operation
        self.signe = "+"
        if self._is_operation_valid():
            self._calculate_addition()
            return self.result

    def substraction(self, operation):
        """
            Handles an substraction operation.

            :param operation: The requested operation by user.
            :return: The substraction result if the operation is valid.
        """
        self.operation = operation
        self.signe = "-"
        if self._is_operation_valid():
            self._calculate_substraction()
            return self.result

    def multiplication(self, operation):
        """
            Handles an multiplication operation.

            :param operation: The requested operation by user.
            :return: The multiplication result if the operation is valid.
        """
        self.operation = operation
        self.signe = "*"
        if self._is_operation_valid():
            self._calculate_multiplication()
            return self.result

    def division(self, operation):
        """
            Handles an division operation.

            :param operation: The requested operation by user.
            :return: The division result if the operation is valid.
        """
        self.operation = operation
        self.signe = "/"
        if self._is_operation_valid():
            self._calculate_division()
            return self.result
        
    def puissance(self, operation):
        """
            Handles an puissance operation.

            :param operation: The requested operation by user.
            :return: The puissance result if the operation is valid.
        """
        self.operation = operation
        self.signe = "^"
        if self._is_operation_valid():
            self._calculate_puissance()
            return self.result
    
    def racine_carree(self, operation):
        """
            Handles an racine carree operation.

            :param operation: The requested operation by user.
            :return: The racine carree result if the operation is valid.
        """
        self.operation = operation
        self.signe = "v"
        if self._is_operation_valid():
            print("Operation valide")
            self._calculate_racine_carree()
            return self.result
    
    def factorielle(self, operation):
        """
            Handles an factorielle operation.

            :param operation: The requested operation by user.
            :return: The factorielle result if the operation is valid.
        """
        self.operation = operation
        self.signe = "!"
        if self._is_operation_valid():
            self._calculate_factorielle()
            return self.result
    
    def logarithme(self, operation):
        """
            Handles an logarithme operation.

            :param operation: The requested operation by user.
            :return: The logarithme result if the operation is valid.
        """
        self.operation = operation
        self.signe = "l"
        if self._is_operation_valid():
            self._calculate_logarithme()
            return self.result
    
    def exponentielle(self, operation):
        """
            Handles an exponentielle operation.

            :param operation: The requested operation by user.
            :return: The exponentielle result if the operation is valid.
        """
        self.operation = operation
        self.signe = "e"
        if self._is_operation_valid():
            self._calculate_exponentielle()
            return self.result

    def _is_operation_valid(self):
        """
            Checks if the operation have the correct syntax.

            :return: True if the operation is valid
        """
        if self._is_symbol_valid():
            self.numbers = self.operation.split(self.signe[0])
            if self.signe == "v" or self.signe == "e" or self.signe == "l":
                self.numbers.pop(0)
            if self.signe == "!":
                self.numbers = self.numbers[0]
            for number in self.numbers:
                if not self._is_float(number):
                    return False
            return True
        return False

    def _is_symbol_valid(self):
        """
            Checks if the operation match with the type of operation request by the user.

            :return: True if all symbol in the operation is valid.
        """
        symbols = [symbol for symbol in self.operation if not symbol.isdigit()]
        for symbol in symbols:
            if symbol != self.signe and symbol != "." and symbol != " ":
                return False
        return True

    def _is_float(self, value):
        """
            Checks if all others symbols can be converted to float value.

            :return: True if all symbol can be converted to float value.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _calculate_addition(self):
        """
            Makes the addition calculation.
        """
        self.result = 0.0
        for number in self.numbers:
            self.result += float(number)

    def _calculate_substraction(self):
        """
            Makes the substraction calculation.
        """
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            self.result -= float(self.numbers[i])

    def _calculate_multiplication(self):
        """
            Makes the multiplication calculation.
        """
        self.result = 1.0
        for number in self.numbers:
            self.result *= float(number)

    def _calculate_division(self):
        """
            Makes the division calculation.
        """
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            try:
                self.result /= float(self.numbers[i])
            except ZeroDivisionError:
                self.result = None
                
    def _calculate_puissance(self):
        """
            Makes the puissance calculation.
        """
        self.result = float(self.numbers[0])
        for i in range(1, len(self.numbers)):
            self.result **= float(self.numbers[i])
            
    def _calculate_racine_carree(self):
        """
            Makes the racine carree calculation.
        """
        if len(self.numbers) == 1 and float(self.numbers[0]) >= 0:
            self.result = float(self.numbers[0]) ** 0.5
        else :
            self.result = None
        
    def _calculate_factorielle(self):
        """
            Makes the factorielle calculation.
        """
        if len(self.numbers) == 1 and float(self.numbers[0]) >= 0:
            self.result = 1
            number = int(self.numbers[0])
            for i in range(1, number + 1):
                self.result *= i
        else:
            self.result = None
    
    def _calculate_logarithme(self):
        """
            Makes the logarithme calculation.
        """
        if len(self.numbers) == 1 and float(self.numbers[0]) >= 0:
            try:
                self.result = log(float(self.numbers[0]))
            except ValueError:
                self.result = None
        else:
            self.result = None
    
    def _calculate_exponentielle(self):
        """
            Makes the exponentielle calculation.
        """
        if len(self.numbers) == 1:
            self.result = exp(float(self.numbers[0]))
        else:
            self.result = None
