# Python Exceptions


A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception. In this article, you will see what an exception is and how it differs from a syntax error. After that, you will learn about raising exceptions and making assertions. Then, you’ll finish with a demonstration of the try and except block.

##### Raising exceptions: 
We can use raise to throw an exception if a condition occurs. The statement can be complemented with a custom exception.

```
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```


Files | Conntent
------|--------
[0-safe_print_list.py](./0-safe_print_list.py)| Python function that prints `x` elements
[1-safe_print_integer.py](./1-safe_print_integer.py)| Python function that prints an integer in `"{:d}".format()` format.
[2-safe_print_list_integers.py](./2-safe_print_list_integers.py)| Python function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
[3-safe_print_division.py](./3-safe_print_division.py)| Python function that divides two integers and prints the result using `finally:`.
[4-list_division.py](./4-list_division.py)| Python function that divides two lists element by element.
[5-raise_exception.py](./5-raise_exception.py)| Python function that raises
[6-raise_exception_msg.py](./6-raise_exception_msg.py)| Python function that raises a name exception with a message.
[100-safe_print_integer_err.py](./100-safe_print_integer_err.py)| Python function that prints an integer with type-checking in `"{:d}".format())` format.
[101-safe_function.py](./101-safe_function.py)| Python function that executes a function safely.
