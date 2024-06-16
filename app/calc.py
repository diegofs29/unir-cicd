import app, math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        if x == 0 and y < 0:
            raise TypeError("Negative power of zero is not possible: Division by zero is not possible")
        else:
            return x ** y
    
    def sqrt(self, x):
        self.check_types(x)
        if x >= 0:
            return math.sqrt(x)
        else:
            raise TypeError("Square root of negative number is not possible")
        
    def log10(self, x):
        self.check_types(x)
        if x > 0:
            return math.log10(x)
        else:
            raise TypeError("Logarithm of negative or zero is not possible")

    def check_types(self, *args):
        for n in args:
            if not isinstance(n, (int, float)):
                raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
