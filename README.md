# ssw567hw02

This homework assignment corresponds to SSW 567 HW 02a: Testing a Legacy Program and Reporting on Testing Results

The original files were first committed to this repository, then the files were updated with appropriate testing and bug fixes.

Finally, the updated files were committed to this repository.

Assignment Summary

1.	Assignment Description: Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.  In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.  You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.  In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.  Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.  Capture and then report on those results in a formal test report described below.  For this first part you should not make any changes to the classify triangle program.  You should only change the test program.  Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.  Run one final execution of the test program and capture and then report on those results in a formal test report described below.  
2.	Author: Gabrielle McCormack
3.	Summary: The purpose of this homework assignment was to test a legacy program that was already created that had multiple bugs, causing tests that would normally pass to fail.  I was tasked with creating tests for the code that would provide as much coverage as possible, while also fixing any bugs that were in the original code.  I found a few minor bugs in the code including for example misplaced variables or code blocks that were placed in the wrong order.  I found this assignment quite interesting.  I enjoyed the different sets of tasks that had to be completed, as it was not just completing one task specifically.  Having multiple steps to the homework has allowed me to practice multiple skills that will be valuable in the workplace, including using GitHub, writing test cases, fixing bugs, and generating test reports.
4.	Honor Pledge: “I pledge my honor that I have abided by the Stevens Honor System.” – Gabrielle McCormack
5.	Detailed Results: When completing this assignment, it was assumed that multiple simple bugs would be found in the code that would allow it to fail, but it would not be faulty enough to be fundamentally incorrect, resulting in reworking of the code.  As inputs for the test cases, I made sure to use all values that I deemed necessary to test, including non-integer values, negative numbers, integers less than 200 and integers greater than 200.  This was done to test the ‘InvalidInput’ return, which would return as such if a non-integer value such as ‘a’, a negative number, or a number greater than 200 was inputted.  I began by ensuring that I had at least three test cases for each scenario including ‘Right’, ‘Equilateral’, ‘Scalene’, ‘Isosceles’, ‘InvalidInput’, ad ‘NotATriangle’.  Once all of my test cases were written which I made sure was complete before I modified the original code of Triangle.py, I ran the test cases.  All 25 of my tests failed because of the bugs that were within the Triangle.py code originally.  See below for the test reports for the original test case source code and the revised test case source code.

Written Test Report (Original Triangle.py and TestTriangle.py)
Test ID	| Input |	Expected Results |	Actual Result |	Pass or Fail
testRightTriangleA	3,4,5	‘Right’	‘InvalidInput’	Fail
testRightTriangleB	5,3,4	‘Right’	‘InvalidInput’	Fail
testEquilateralTriangles	1,1,1	‘Equilateral’	‘InvalidInput’	Fail

Written Test Report (Revised Triangle.py and TestTriangle.py)
Test ID	Input |	Expected Results |	Actual Result |	Pass or Fail
testRightTriangleA	3,4,5	‘Right’	‘Right’	Pass
testRightTriangleB	4,3,5	‘Right’	‘Right’	Pass
testRightTriangleC	6,8,10	‘Right’	‘Right’	Pass
testRightTriangleD	8,6,10	‘Right’	‘Right’	Pass
testEquilateralTriangleA	1,1,1	‘Equilateral’	‘Equilateral’	Pass
testEquilateralTriangleB	199,199,199	‘Equilateral’	‘Equilateral’	Pass
testEquilateralTriangleC	5,5,5	‘Equilateral’	‘Equilateral’	Pass
testScaleneTriangleA	13,6,8	‘Scalene’	‘Scalene’	Pass
testScaleneTriangleB	2,6,7	‘Scalene’	‘Scalene’	Pass
testScaleneTriangleC	39,6,40	‘Scalene’	‘Scalene’	Pass
testIsoscelesTriangleA	4,4,7	‘Isosceles’	‘Isosceles’	Pass
testIsoscelesTriangleB	4,7,4	‘Isosceles’	‘Isosceles’	Pass
testIsoscelesTriangleC	7,4,4	‘Isosceles’	‘Isosceles’	Pass
testInvalidInputA	‘a’, ‘b’, ‘c’	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputB	1,1, ‘c’	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputC	‘a’,1,1	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputD	1, ‘b’,1	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputE	‘a’, ‘b’,1	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputF	1, ‘b’, ‘c’	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputG	‘a’,1, ‘c’	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputH	200,300,120	‘InvalidInput’	‘InvalidInput’	Pass
testInvalidInputI	4,1,-10	‘InvalidInput’	‘InvalidInput’	Pass
testNotTriangleA	4,1,10	‘NotATriangle’	‘NotATriangle’	Pass
testNotTriangleB	8,3,3	‘NotATriangle’	‘NotATriangle’	Pass
testNotTriangleC	20,4,15	‘NotATriangle’	‘NotATriangle’	Pass

The testing matrix below outlines the number of tests that I had planned to execute, had executed, how many passed, how many defects found, and how many defects fixed within the Triangle.py code.  

Test Run 1 was conducted with all 25 of my test cases written out, which all failed.  I began to remedy the failures by going down the line of test cases.  I started with testRightTriangleA through testRightTriangleD.  I looked at the original Triangle.py code that corresponded to checking for right triangles and noticed that the if statement was not squaring the values of a, b, and c, but multiplying them instead by 2.  I remedied that simply by entering the exponential operator where the multiplication operator once was.

Test Run 2 was conducted with all 25 of my test cases written out, which 4 passed.  I began to remedy the failures by going down the line of test cases.  I continued with testEquilateralTriangleA through testEquilateralTriangleC.  I looked at the original Triangle.py code that corresponded to checking for equilateral triangles and noticed that in the if statement checking for equilateral triangles, only the conditions for if a == b and b == a were written.  I then fixed that small bug by changing it to test all variables; a == b and a == c.

Test Run 3 was conducted with all 25 of my test cases written out, which 7 passed.  I began to remedy the failures by going down the line of test cases.  I continued with testScaleneTriangleA through testScaleneTriangleC.  I looked at the original Triangle.py code that corresponded to checking for scalene triangles and noticed that in the if statement, the parameter of a != b was repeated, which resulted in the condition not being satisfied.  A simple change was made so that one of the conditions was changed to a != c.

Test Run 4 was conducted with all 25 of my test cases written out, which 10 passed.  I began to remedy the failures by going down the line of test cases.  I continued with testIsoscelesTriangleA through testIsoscelesTriangleD.  I looked at the original Triangle.py code that corresponded to checking for isosceles triangles and noticed that the return for ‘Isosceles’ was spelled ‘Isoceles’ which is the incorrect spelling.  That was then changed to the correct spelling.

Test Run 5 was conducted with all 25 of my test cases written out, which 13 passed.  I began to remedy the failures by going down the line of test cases.  I continued with testInvalidInputA through testInvalidInputI.  I looked at the original Triangle.py code that corresponded to checking for invalid inputs and noticed that the checking of non-integer inputs should be placed before any variables are compared to see if they are less than 0 or greater than 200.  The if statement that corresponds to checking the type of the inputs was then moved before the if statement for checking if a variable is greater than 200.  The if statement of checking if a value is greater than 200 was implemented correctly, so no changes were needed to be made.  The if statement for checking if the variables a, b, and c are less than 0 was incorrect as the comparison check for b was checking if b <= b, rather than b <= 0.  This minor change was then made to remedy the situation.

Test Run 6 was conducted with all 25 of my test cases written out, which 21 passed.  I began to remedy the failures by going down the line of test cases.  I continued with testNotTriangleA through testNotTriangleC.  I looked at the original Triangle.py code that corresponded to checking for non-triangles and noticed only one condition of the three was correct in checking that the addition of two variables is greater than that of the third variable.  To fix this, the other two conditions, were changed to addition instead of subtraction.

Test Run 7, the final test run, was conducted with all 25 of my test cases written out, which all 25 passed.  From that, I now know that all of the test cases for which I had provided had proven the code was adequately tested with successful results.

Testing Matrix
Tests |	Test Run 1 |	Test Run 2 |	Test Run 3 |	Test Run 4 |	Test Run 5 |	Test Run 6 |	Test Run 7
Tests Planned	25	25	25	25	25	25	25
Tests Executed	25	25	25	25	25	25	25
Tests Passed	0	4	7	10	13	21	25
Defects Found	1	1	1	1	2	1	0
Defects Fixed	0	1	2	3	4	6	7

Repository Name: gmccorma/ssw567hw02
https://github.com/gmccorma/ssw567hw02

