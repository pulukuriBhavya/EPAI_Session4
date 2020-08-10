# EPAI_Session4
Session 4 is concentarted on **Numeric Types II**
***
- **Numeric Types II** is all about Floats, Decimals, Complex numbers and Booleans

## Getting Started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose.

### Prerequisites
***
Before string session check if all the required packages (pytest) are installed. Packages can be installed using the following code.
```
 pip install pytest
 
 ```

### Session 4.py
***

Session4.py consists of a class called Qualean which is a combination of Quantum and Boolean numbers. This class consists of different methods to perform operations on Qualean numbers.

- or function takes two different parameters and performs logical or operation.
- and function takes two different parameters and performs logical and operation.
- repr function returns the printable representation of the given object.
- str function returns the informal string representation of the given object.
- add function returnts the sum of given Qualean numbers. 
- eq checks for equality between the given Qualean numbers.
- compare_strings_new is a function where two strings are interned and are repeated over 200 times and compared, also look for a particular character in one of the strings after converting the string to a char_set
- The computational time difference between the two functions (compare_strings_old and compare_strings_new) varies ten fold since we are using interning also search in sets in computationally
 faster than lists since sets are hash based.
- sleep function is used in compare_strings_new to suspend the execution for a given number of seconds, here it is 6.

### test_session4.py

***

test_session4.py consists of 10 test cases which will get passed once we make the required modifications to the session2.py.

- test_qualean_functions_avaiable to check if the class has implemented all the functions
- test_class_repr to check for objects returing from repr functions
- test_fourspace and test_function_name_had_cap_letter to check for indentation and function name having capital letter.
 

