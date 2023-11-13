#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install nbimporter')


# In[8]:


# Import the necessary functions from the main code notebook
import nbimporter
from math_quiz_ import generate_random_integer, generate_operator, calculate_result

# Define and run your unit tests
def test_generate_random_integer():
    min_val = 1
    max_val = 10
    for _ in range(1000):
        rand_num = generate_random_integer(min_val, max_val)
        assert min_val <= rand_num <= max_val

def test_generate_operator():
    operators = ['+', '-', '*']
    for _ in range(1000):
        operator = generate_operator()
        assert operator in operators

def test_calculate_result():
    test_cases = [
        (5, 2, '+', '5 + 2', 7),
        (10, 3, '-', '10 - 3', 7),
        (4, 6, '*', '4 * 6', 24),
    ]

    for num1, num2, operator, expected_problem, expected_answer in test_cases:
        problem, answer = calculate_result(num1, num2, operator)
        assert problem == expected_problem
        assert answer == expected_answer

# Run the unit tests
test_generate_random_integer()
test_generate_operator()
test_calculate_result()


# In[ ]:




