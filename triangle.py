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


def classify_triangle(s_a, s_b, s_c):
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
    # New change 9.26.18: combined all 'InvalidInput' if statements together
    if not all([isinstance(s_a, int), isinstance(s_b, int), isinstance(s_c, int)]) \
            or any([s_a > 200, s_b > 200, s_c > 200, s_a <= 0, s_b <= 0, s_c <= 0]):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (s_a >= (s_b + s_c)) or (s_b >= (s_a + s_c)) or (s_c >= (s_a + s_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    # changed from if a == b and b == a: to the following
    if s_a == s_b and s_a == s_c:
        return 'Equilateral'
    # changed from elif ((a * 2) + (b * 2)) == (c * 2): to the following
    # New change 9.26.18: change from elif to if
    if ((s_a ** 2) + (s_b ** 2)) == (s_c ** 2):
        return 'Right'
    # changed from elif (a != b) and (b != c) and (a != b): to the following
    # New change 9.26.18: change from elif to if
    if (s_a != s_b) and (s_b != s_c) and (s_a != s_c):
        return 'Scalene'
    # changed from return 'Isoseles' to the following
    # New change 9.26.18: omit else statement
    return 'Isosceles'
