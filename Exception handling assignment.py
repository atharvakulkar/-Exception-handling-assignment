#!/usr/bin/env python
# coding: utf-8

# Q1. Explain why we have to use the Exception class while creating a Custom Exception.

# In[1]:


The exception class is the base class for all biult in functions in python. When you create a custom exception ,you should inherit 
from the exception class such that your custom exception is the subclass of the exception class.
By inheriting from the Exception class, your custom exception will be able to take advantage of the behavior and functionality that is already built into the Exception class. This includes the ability to be raised and caught with a try/except block, and the ability to store and retrieve error messages associated with the exception.

Inheriting from the Exception class also makes it easier to catch specific types of exceptions in your code. For example, you could catch all exceptions that are subclasses of Exception using a single except block, or you could catch only specific types of exceptions by catching their corresponding custom exceptions.


# Q2. Write a python program to print Python Exception Hierarchy.

# In[2]:


def print_exception_hierarchy(exception, indentation=0):
    print(" " * indentation + exception.__name__)
    for subclass in exception.__subclasses__():
        print_exception_hierarchy(subclass, indentation + 4)

print_exception_hierarchy(Exception)


# Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.

# In[3]:


The ArithmeticError class is a subclass of the Exception class in Python, and it represents a class of errors related to arithmetic operations. Some common errors that are defined as subclasses of ArithmeticError include:

OverflowError: This error is raised when a calculation produces a result that is too large to be represented as a number in Python. For example:


# In[4]:


print(10 ** 10000)


# In[5]:


ZeroDivisionError: This error is raised when an attempt is made to divide a number by zero. For example:


# In[6]:


print(10/0)


# Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.
# 
# The LookupError class is a subclass of the Exception class in Python, and it represents a class of errors related to looking up elements in data structures. Some common errors that are defined as subclasses of LookupError include:
# 
# KeyError: This error is raised when an attempt is made to access a dictionary element using a key that is not present in the dictionary. For example:

# In[7]:


d = {'a': 1, 'b': 2}
print(d['c'])
     


# IndexError: This error is raised when an attempt is made to access a list element using an index that is outside the range of valid indices for the list. For example:

# In[8]:


l = [1, 2, 3]
print(l[3]) # Raises IndexError
     


# Q5. Explain ImportError. What is ModuleNotFoundError?
# 
# ImportError is a built-in exception in Python that is raised when an attempt to import a module fails. This can happen for a variety of reasons, such as:
# 
# The module name is incorrect
# The module is not installed on the system
# The module is not in the search path
# A required dependency is missing
# ModuleNotFoundError is a subclass of ImportError that was introduced in Python 3.6.
# It is raised when a module is not found in the Python Standard Library or in a specific package or location. The main difference between ImportError and ModuleNotFoundError is that the former can be raised for other reasons besides a missing module, such as an incorrect module name or a missing required dependency, while the latter is specifically raised when a module cannot be found.

# Q6. List down some best practices for exception handling in python.
# 
# Here are some best practices for exception handling in Python:
# 
# Catch specific exceptions: Rather than catching the broad Exception class, it is recommended to catch specific exceptions that you expect to occur in your code. This allows you to handle different types of exceptions differently, and to provide more meaningful error messages.
# 
# Provide informative error messages: When raising or catching exceptions, it is helpful to include information about the error that has occurred. This can make it easier to diagnose and fix the problem.
# 
# Use exceptions for exceptional situations: Exceptions should be used to handle unexpected or exceptional situations that cannot be handled through normal control flow. Don't use exceptions for normal control flow, such as to check if a file exists before opening it.
# 
# Avoid using exceptions for control flow: Exceptions should not be used as a mechanism for control flow. Instead, use a simple if statement or another control flow construct to check for expected conditions.
# 
# Don't ignore exceptions: When you catch an exception, it is important to handle it properly, rather than just ignoring it. Ignoring exceptions can lead to unexpected behavior and can make it more difficult to diagnose and fix problems.
# 
# Use finally to clean up resources: The finally clause can be used to ensure that resources are properly cleaned up, even if an exception occurs. This can include closing files, releasing resources, and restoring the state of the program.
# 
# Consider using context managers: Context managers are a convenient way to manage resources in a Python program.  

# In[ ]:




