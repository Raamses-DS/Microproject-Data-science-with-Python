"""
There is a test with 30 questions worth 150 marks. The test has two types of questions:

1. True or false-carries 4 marks each
2. Multiple-choice carries 9 marks each
Find the number of true or false and multiple-choice questions.
"""

# Import required libraries

import numpy as np
from scipy import linalg

# Formulate two linear equations based on the given scenario: The system of linear algebra is as follow:

system_variables = np.array([[1,1],[4,9]])
system_values = np.array([30,150])

# Apply a suitable method to solve the linear equation: Solve the system of equations and get the values x and y:

linalg.solve(system_variables,system_values)
