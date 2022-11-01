# Python Test Driven Development

### What is the Python unittest?
Unit testing is a technique in which particular module is tested to check by developer himself whether there are any errors. The primary focus of unit testing is test an individual unit of system to analyze, detect, and fix the errors

### The doctest module:

Searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.



Files|Content
------|------
[0-add_integer.py](./0-add_integer.py)| Python function that returns the integer addition of two numbers.
[2-matrix_divided.py](./2-matrix_divided.py)| ython function that divides al elements of a matrix by a common divisor.
[3-say_my_name.py](./3-say_my_name.py)| Python function that prints a name in the format `My name is <first_name> <last_name>`
[4-print_square.py](./4-print_square.py)| Python function that prints a square using the `#` character.
[5-text_indentation.py](./5-text_indentation.py)| Python function that prints text with indentation.
[100-matrix_mul.py](./100-matrix_mul.py)| Python class/script that runs unittests for the function `def max_integer(list=[]):`
[101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py)| Python function that multiplies two matrices. Returns a new matrix representing the multiplication of `m_a` by `m_b`. If either of `m_a` or `m_b` is empty (ie. `== []` or `== [[]]`)
[102-python.c](./102-python.c)|Pyt hon function that multiplies two matrices using the module `NumPy`.
