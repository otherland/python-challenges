"""
 A quine is a computer program which takes no input and produces a copy of its own source code as the only output. These types of programs are often known as "self-replicating programs", "self-reproducing programs", or"self-copying programs" in the computer sciences fields.

You should implement a function (this function will be called “quine”) which will reproduce itself within an environment. Lets refer to the entire code as ANSWER_CODE, and this code contains the quine function definition. If we execute quine(), the result should be a string which is a copy of ANSWER_CODE. You can check this in your local environment with the following:

In this mission, there is only one test. You should be careful with newlines, tabs and white-spaces, because the test compares ANSWER_CODE and the functions result as they are. In this mission the main goal is to develop an original and creative solution. This missions rewards are based on peer reviews, so the votes from other users, will give you increased exp points.

Input: Nothing.

Output: The code as a string.

"""

ANSWER_CODE = "quine=lambda:ANSWER_CODE"
exec(ANSWER_CODE)
print quine() == ANSWER_CODE