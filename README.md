# The number checker

This project provides a set of Python functions for checking various properties of numbers, including integers, floats, and complex numbers. These functions can be useful for validating input, handling edge cases, and working with different number types in your Python projects.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install the_number
```

## Usage

Import the functions you need in your Python script:

```python
from the_number import isInteger, isInf, isNaN, isFinite, isNumber

# Example usage
print(isNumber(5))  # True
print(isNumber(3.14))  # True
print(isNumber(1 + 2j))  # True
print(isNumber(float('inf')))  # True
print(isNumber(float('nan')))  # False
```

## Functions

### isInteger(obj: complex | float | int) -> bool

Checks if the object is an integer, float, or complex number.

Example:
```python
print(isInteger(5))  # True
print(isInteger(3.14))  # True
print(isInteger(1 + 2j))  # True
print(isInteger("5"))  # False
```

### isInf(obj: complex | float | int) -> bool

Checks if the object is positive or negative infinity.

Example:
```python
print(isInf(float('inf')))  # True
print(isInf(float('-inf')))  # True
print(isInf(5))  # False
```

### isNaN(obj: complex | float | int) -> bool

Checks if the object is NaN (Not a Number).

Example:
```python
print(isNaN(float('nan')))  # True
print(isNaN(5))  # False
```

### isFinite(obj: complex | float | int) -> bool

Checks if the object is a finite number.

Example:
```python
print(isFinite(5))  # True
print(isFinite(3.14))  # True
print(isFinite(1 + 2j))  # True
print(isFinite(float('inf')))  # False
print(isFinite(float('nan')))  # False
```

### isNumber(obj: complex | float | int) -> bool

Checks if the object is a valid number (integer, float, or complex) and not NaN.

Example:
```python
print(isNumber(5))  # True
print(isNumber(3.14))  # True
print(isNumber(1 + 2j))  # True
print(isNumber(float('inf')))  # True
print(isNumber(float('nan')))  # False
```

## Testing

To run the tests, execute the following command in the project directory:

```bash
python -m unittest test_numbers.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - See the [LICENSE](LICENSE) file for details.
