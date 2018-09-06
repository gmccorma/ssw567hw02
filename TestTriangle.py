# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

# Homework 02: Testing a Legacy Program and Reporting on Test Results
# Author: Gabrielle McCormack
# Date Completed: 09.06.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(8, 6, 10), 'Right', '8,6,10 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(199, 199, 199), 'Equilateral', '199,199,199 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(13, 6, 8), 'Scalene', '13,6,8 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(2, 6, 7), 'Scalene', '2,6,7 is a Scalene triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(39, 6, 40), 'Scalene', '39,6,40 is a Scalene triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(4, 4, 7), 'Isosceles', '4,4,7 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4, 7, 4), 'Isosceles', '4,7,4 is an Isosceles triangle')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(7, 4, 4), 'Isosceles', '7,4,4 is an Isosceles triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'a,b,c is an Invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(1, 1, 'c'), 'InvalidInput', '1,1,c is an Invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle('a', 1, 1), 'InvalidInput', 'a,1,1 is an Invalid input')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(1, 'b', 1), 'InvalidInput', '1,b,1 is an Invalid input')

    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle('a', 'b', 1), 'InvalidInput', 'a,b,1 is an Invalid input')

    def testInvalidInputF(self):
        self.assertEqual(classifyTriangle(1, 'b', 'c'), 'InvalidInput', '1,b,c is an Invalid input')

    def testInvalidInputG(self):
        self.assertEqual(classifyTriangle('a', 1, 'c'), 'InvalidInput', 'a,1,c is an Invalid input')

    def testInvalidInputH(self):
        self.assertEqual(classifyTriangle(200, 300, 120), 'InvalidInput', '200,300,120 is an Invalid input')

    def testInvalidInputI(self):
        self.assertEqual(classifyTriangle(4, 1, -10), 'InvalidInput', '4,1,-10 is an Invalid input')

    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(4, 1, 10), 'NotATriangle', '4,1,10 is not a triangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(8, 3, 3), 'NotATriangle', '8,3,3 is not a triangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(20, 4, 15), 'NotATriangle', '20,4,15 is not a triangle')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

