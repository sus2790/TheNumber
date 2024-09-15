# The Number

This library provides a set of pure Python functions for checking and validating numeric types, including complex numbers. It's designed to work without any external dependencies, making it easy to integrate into any Python project.
I have used LLM for this entire README.md.

## Features

- Check if a value is a numeric type (integer, float, or complex)
- Determine if a number is finite
- Validate if a value is a "number" (finite numeric type)
- Supports both real and complex numbers
- Pure Python implementation (no external dependencies)

## Functions

### `isInteger(obj: complex) -> bool`

Checks if the input is a numeric type (int, float, or complex).

### `isFinite(obj: complex) -> bool`

Determines if the input is a finite number. For complex numbers, both real and imaginary parts must be finite.

### `isNumber(obj: complex) -> bool`

Checks if the input is a finite numeric type.

## Usage

```python
from the_number import isInteger, isFinite, isNumber

# Examples
print(isInteger(5))        # True
print(isInteger(3.14))     # True
print(isInteger(2+3j))     # True
print(isInteger("5"))      # False

print(isFinite(10))        # True
print(isFinite(float('inf')))  # False
print(isFinite(1+2j))      # True
print(isFinite(1+float('inf')*1j))  # False

print(isNumber(42))        # True
print(isNumber(3.14159))   # True
print(isNumber(2+3j))      # True
print(isNumber(float('nan')))  # False
```

## Installation
```shell
>>> pip install the_number
>>> ...
```
That's all.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.