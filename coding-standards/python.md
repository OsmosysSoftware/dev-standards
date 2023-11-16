
# Python Coding Standards - Detailed Guide

## 1. Introduction
This document is designed to promote code consistency, readability, and quality in Python projects. It covers a range of best practices and conventions.

## 2. Code Layout

### 2.1 Indentation
- Always use 4 spaces for each level of indentation. Avoid using tabs.

### 2.2 Line Length
- The length of the line should not be greater than 79 characters. In the case of docstrings and comments where a block of text is large, it is limited to 72 characters. For long multiple case statements, the backslashes are permissible. For using log statements with binary operators, python suggests breaking the formula line before the binary operator for better readability.
```
def sample_function (arg1, arg2):

'''

The document string length for a single line should be less than
72 characters. So that long texts should be adjusted in a single
window
'''  

#  code has maximum lengths of 79 characters, can use backslash
# to break the line
list_of_subjects = [
'Physics', 'Chemistry', 'Mathematics', 'Biology',  ‘Bio’, \
]
```

### 2.3 WHITESPACES, TRAILING COMMAS, AND STRING QUOTES
- One should avoid extra white spaces, there must be a single white space around both sides of an operator, one after the comma and none inside opening or closing of parenthesis. Both single quotes and double quotes are acceptable in python web development, you should use both if you need quotes inside quotes to avoid syntax error and extra backslash.

```
# Examples of commas and whitespaces
    
x,  y = 30 ,  " text inside quote"
 z= 'text inside quote'
if x== 30: print(x, y, z)

# how to use quotes inside quotes 

text =  "This text is using 'the single quote' inside double quote"
 print(text)
```

### 2.4 Imports
- Group imports into three categories: standard library, third-party, and application-specific, separated by a blank line.
- The import should be in a particular sequence. At first, the standard libraries, then the third party, and at the last, the local libraries should be imported. If you only need a single function/class from the import, do an absolute import. 
```
# Don't forget to add a space between different group of imports

# first of all, the standard library imports

import standard_library_import_a
import standard_library_import_b

# then,the third party imports

import third_party_import_a
import third_party_import_b
import third_party_import_c

    
# at the last, local library import

from local library import local_a, local_b
from local_library_two import  local_c 


# two blank lines for top level functions 
def top_level_function(argument):
# A standard four space indent 
print(argument)
```

## 3. Naming Conventions

### 3.1 General Principles
- Choose names that are clear and descriptive over short and cryptic.
- Use grammatically correct variable names, the class name should start with an uppercase and must follow camelCase convention If more than two words are to be used.

### 3.2 Variables
- Use `snake_case` for variable names: `inventory_list`, `user_profile`.

### 3.3 Functions
- Function names should also follow `snake_case`: `calculate_tax`, `print_invoice`.

### 3.4 Classes
- Use `CapWords` convention for class names: `ShoppingCart`, `UserProfile`.

### 3.5 Constants
- Constants should be in `UPPERCASE_WITH_UNDERSCORES`: `MAX_SIZE`, `DEFAULT_COLOR`.
 
Example for Naming Conventions
```
# class name follows camelcase convention
class StudentDetails:
                
def __init__(self, first_name, last_name):
self.first_name = first_name
self.last_name = last_name
                
# Method name, variable names in lowercase joined with an underscore
def grade(self, marks_obtained):
# constants in capital
GRACE = 2
marks_obtained = GRACE + marks_obtained
if marks_obtained > 90:
self.student_grade = 'A'
elseif marks_obtained > 70:
student_grade = 'B'
else:
student_grade = 'C'
```

## 4. Programming Recommendations

- **Explicit over Implicit**: Avoid hidden side effects and always make your intentions clear in the code.
- **Simple is Better Than Complex**: Prioritize straightforward solutions over complex ones.
- **Readability Matters**: Write code as if it's meant for humans to read, not just for machines to execute.

## 5. Commenting and Documentation

### 5.1 Docstrings
- Use triple double quotes for docstrings. Document every public module, function, class, and method.

### 5.2 Inline Comments
- Use inline comments sparingly to explain why a particular piece of code is written.

## 6. Error Handling

- **Catching Exceptions**: Be as specific as possible in catching exceptions.
- **Raise Meaningful Errors**: When raising errors, provide clear and concise messages to help diagnose issues.

## 7. Linting and Formatting

- **PEP 8 Compliance**: Regularly run tools like `flake8` to ensure compliance with PEP 8.
- **Autoformatting**: Use tools like `black` to automatically format your code according to the standard guidelines.

## 8. Testing

- **Test Coverage**: Aim for high test coverage. Write tests for new features and bug fixes.
- **Test Frameworks**: Use tools like `pytest` for more advanced testing capabilities.

## 9. Version Control

- **Commit Messages**: Write clear and descriptive commit messages.
- **Branching Strategy**: Use strategies like Gitflow to manage branches in larger projects.

## 10. Security

- **Dependency Management**: Regularly update dependencies to address known vulnerabilities.
- **Code Analysis**: Use tools to analyze code for security flaws.

## 11. Performance

- **Optimize Algorithms**: Focus on algorithmic efficiency to improve overall performance.
- **Resource Management**: Be mindful of resource usage, like memory and file handles.

## 12. Dependency Management

- **Virtual Environments**: Use tools like `virtualenv` or `Pipenv` to isolate project dependencies.
- **Dependency Listing**: Maintain an up-to-date `requirements.txt` file.

## 13. CI/CD

- Integrate CI/CD pipelines for automated testing and deployment.
- Ensure all merges to the main branch are fully tested.

## 14. References

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

## 15. Appendix

- Detailed examples of good and bad coding practices.
- Troubleshooting common issues in Python development.
