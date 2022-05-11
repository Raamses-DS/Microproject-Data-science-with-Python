"""
Problem:

Use SciPy to declare 20 random values for random values and perform the following:

1. CDF-Cumulative Distribution Function for a random variable 10
2. PDF-Probability Density Function for a random variable 14.
"""

# Import required library

from scipy.stats import norm

# Use SciPy to declare 20 random values for random values and perform the following:

norm.rvs(loc=0,scale=1,size=20)

# 1. CDF – Cumulative Distribution Function for a random variable 10

norm.cdf(10,loc=1,scale=3)

# 2. PDF – Probability Density Function for a random variable 14.

norm.pdf(14,loc=1,scale=1)