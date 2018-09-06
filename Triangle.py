# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

# Homework 02: Testing a Legacy Program and Reporting on Test Results
# Author: Gabrielle McCormack
# Date Completed: 09.06.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    # moved to the first test of InvalidInput so types other than int are caught first
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # changed from if a <= 0 or b <= b or c <= 0: to the following
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    # changed from if a == b and b == a: to the following
    if a == b and a == c:
        return 'Equilateral'
    # changed from elif ((a * 2) + (b * 2)) == (c * 2): to the following
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    # changed from elif (a != b) and (b != c) and (a != b): to the following
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    # changed from return 'Isoseles' to the following
    else:
        return 'Isosceles'
