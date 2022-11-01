# Python import modules

### Importing Modules

To make use of the functions in a module, you’ll need to import the module with an import statement.

An import statement is made up of the import keyword along with the name of the module.

In a Python file, this will be declared at the top of the code, under any shebang lines or general comments.

```
import random
```

```
import random
import math


for i in range(5):
    print(random.randint(1, 25))

print(math.pi)
```



Files | Content
-------- | -----------
[0-add.py](./ 0-add.py)| Import a simple function from a simple file
[1-calculation.py](./1-calculation.py) | Python program that imports functions from the file calculator_1.py and prints the result of the addition, subtraction, multiplication and division of 10 and 5. 
[2-args.py](./2-args.py)| Python program that prints the number of and list of its arguments.
[3-infinite_add.py]( 3-infinite_add.py)| Python program that prints the result of the addition of all arguments. 
[4-hidden_discovery.py](./4-hidden_discovery.py) | Python program that prints all the names defined by the compiled module hidden_4.pyc 
[5-variable_load.py](./5-variable_load.py)| Python program that imorts the variable a from the file variable_load_5.py and prints its value 
[100-my_calculator.py](./100-my_calculator.py)| Python program that imports all functions from the file calculator_1.py and handles basic operations
[101-easy_print.py](./101-easy_print.py) | Python program that prints #pythoniscool followed by a new line in the standard output.
