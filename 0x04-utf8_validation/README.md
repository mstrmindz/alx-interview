# 0x09\. UTF-8 Validation

<small>Specializations - Interview Preparation ― Algorithms</small>

_<small>by Carrie Ybay, software engineer at Holberton School</small>_

<small>Ongoing project - started 06-18-2020, must end by 06-25-2020 (in 7 days) - you're done with <span id="student_task_done_percentage">0</span>% of tasks.</small>

<small>Checker will be released at 06-21-2020 12:00 PM</small>

<small>QA review fully automated.</small>

<small><span class="badge badge-tag">bit manipulation</span> <span class="badge badge-tag">python</span></small>

<article id="description" class="gap formatted-content">

## Resources

**Read or watch**:

*   [UTF-8](/rltoken/qVyzvKu0K89D0Aiz2Ssvgw "UTF-8")
*   [Characters, Symbols, and the Unicode Miracle](/rltoken/fZDmbf_oigBn5Ziy7ai0pg "Characters, Symbols, and the Unicode Miracle")

## Requirements

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `PEP 8` style (version 1.7.x)
*   All your files must be executable


* * *

## Tasks



#### 0\. UTF-8 Validation <span class="alert alert-warning mandatory-optional">mandatory</span>

Write a method that determines if a given data set represents a valid UTF-8 encoding.

*   Prototype: `def validUTF8(data)`
*   Return: `True` if data is a valid UTF-8 encoding, else return `False`
*   A character in UTF-8 can be 1 to 4 bytes long
*   The data set can contain multiple characters
*   The data will be represented by a list of integers
*   Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
```
    carrie@ubuntu:~/0x09-utf8_validation$ cat 0-main.py
    #!/usr/bin/python3
    """
    Main file for testing
    """

    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

    carrie@ubuntu:~/0x09-utf8_validation$

    carrie@ubuntu:~/0x09-utf8_validation$ ./0-main.py
    True
    True
    False
    carrie@ubuntu:~/0x09-utf8_validation$
```
**Repo:**

*   GitHub repository: `holbertonschool-interview`
*   Directory: `0x09-utf8_validation`
*   File: `0-validate_utf8.py`