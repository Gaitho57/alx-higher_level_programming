# Python - More Data Structures: Set, Dictionary

In this project, we explore the concepts of sets and dictionaries in Python. We practice using these data structures along with the `lambda`, `map`, `filter`, and `reduce` methods.

## Tests ✔️
* [tests](./tests): This folder contains the test files provided by Holberton School.

## Function Prototypes 💾
Here are the function prototypes for the Python files in this project:

| File                           | Function Prototype                                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`                                                               |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`                                                      |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                                                                          |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`                                                                 |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`                                                              |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                                                                     |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`                                                         |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):`                                                   |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`                                                           |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                                                                   |
| `10-best_score.py`             | `def best_score(a_dictionary):`                                                                      |
| `11-multiply_list_map.py`      | `def multiply_list_map(my_list=[], number=0):`                                                       |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                                                                    |
| `100-weight_average.py`        | `def weight_average(my_list=[]):`                                                                    |
| `101-square_matrix_map.py`     | `def square_matrix_map(matrix=[]):`                                                                  |
| `102-complex_delete.py`        | `def complex_delete(a_dictionary, value):`                                                           |
| `103-python.c`                 | `void print_python_list(PyObject *p);`<br>`void print_python_bytes(PyObject *p);`                     |

## Tasks 📃
The following tasks are included in this project:

* **0. Squared simple**
  * [0-square_matrix_simple.py](./0-square_matrix_simple.py): This Python function computes the square value of all integers in a matrix.
  * The `matrix` parameter is a two-dimensional array.
  * The function returns a matrix of the same size as `matrix` where each value is the square of the corresponding input value.
  * The initial matrix is not modified.
  * No modules are imported.

* **1. Search and replace**
  * [1-search_replace.py](./1-search_replace.py): This Python function replaces all occurrences of an element with another element in a new list.
  * The `my_list` parameter is the initial list.
  * The `search` parameter is the element to replace in the list.
  * The `replace` parameter is the new element.
  * No modules are imported.

* **2. Unique addition**
  * [2-uniq_add.py](./2-uniq_add.py): This Python function adds all unique integers in a list (each integer once).
  * No modules are imported.

* **3. Present in both**
  * [3-common_elements.py](./3-common_elements.py): This Python function returns a set of common
4. Only differents

4-only_diff_elements.py: This Python function returns a set of all elements that are present in only one of two sets.
No modules are imported.
5. Number of keys

5-number_keys.py: This Python function returns the number of keys in a dictionary.
No modules are imported.
6. Print sorted dictionary

6-print_sorted_dictionary.py: This Python function prints a dictionary by ordered keys.
The function assumes all keys are strings.
Keys are printed in alphabetical order.
Keys are sorted only on the first level.
Dictionary values can have any type.
No modules are imported.
7. Update dictionary

7-update_dictionary.py: This Python function replaces or adds key/value pairs in a dictionary.
The key parameter is always a string.
The value parameter can be any type.
If a key exists in the dictionary, its value is replaced.
If a key does not exist in the dictionary, it is created.
No modules are imported.
8. Simple delete by key

8-simple_delete.py: This Python function deletes a key from a dictionary.
The key parameter is always a string.
If the key does not exist, the dictionary remains unchanged.
No modules are imported.
9. Multiply by 2

9-multiply_by_2.py: This Python function returns a new dictionary with all values multiplied by 2.
The function assumes all values are integers.
No modules are imported.
10. Best score

10-best_score.py: This Python function returns the key with the highest integer value in a dictionary.
The function assumes all values are integers.
The function assumes all students have a different score.
If no score is found, None is returned.
No modules are imported.
11. Multiply by using map

11-multiply_list_map.py: This Python function returns a list with all values multiplied by a given number using map.
The function returns a new list of the same length as my_list with each value multiplied by number.
The initial list is not modified.
No loops are used, and no modules are imported.
12. Roman to Integer

12-roman_to_int.py: This Python function converts a Roman numeral to an integer.
The function assumes the number will be between 1 and 3999.
If the roman_string parameter is not a string or is None, the function returns 0.
13. Weighted average!

100-weight_average.py: This Python function returns the weighted average of all integers in a list of tuples.
Each tuple in the list follows the format (<score>, <weight>).
If the list is empty, 0 is returned.
No modules are imported.
14. Squared by using map

101-square_matrix_map.py: This Python function computes the square value of all integers in a matrix using map.
The matrix parameter is a two-dimensional array.
The function returns a new matrix of the same size as matrix with each value squared.
The initial matrix is not modified.
No loops are used, and no modules are imported.
15. Delete by value

102-complex_delete.py: This Python function deletes keys with a specific value from a dictionary.
If the value does not exist, the dictionary remains unchanged.
All keys that have the searched value are deleted.
No modules are imported.
16. CPython #1: PyBytesObject

103-python.c: This file contains C functions that print basic information about Python lists and Python bytes objects.
