"""
150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = None
        for str in tokens:
            if str not in ("+", "-", "*", "/"):
                stack.append(int(str))
                continue
            b = stack.pop()
            a = stack.pop()
            if str == "+":
                result =  a + b          
            elif str == "-":
                result =  a-b             
            elif str == "*":
                result =  a*b           
            elif str == "/":
                result =  int(a/b)
            stack.append(result)
        return stack.pop()
    
def main():
    # Create an instance of the solution
    sol = Solution()
    
    # Test cases with assert statements
    
    # 1. Basic addition
    assert sol.evalRPN(["2", "1", "+"]) == 3, "Test case 1 failed"

    # 2. Basic subtraction
    assert sol.evalRPN(["5", "3", "-"]) == 2, "Test case 2 failed"

    # 3. Basic multiplication
    assert sol.evalRPN(["2", "3", "*"]) == 6, "Test case 3 failed"

    # 4. Basic division
    assert sol.evalRPN(["6", "2", "/"]) == 3, "Test case 4 failed"

    # 5. Complex expression: ["4", "13", "5", "/", "+"]
    # 13 / 5 = 2 -> 4 + 2 = 6
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6, "Test case 5 failed"

    # 6. Expression with negative numbers: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # Complex expression resulting in 22
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, "Test case 6 failed"

    # 7. Division with negative result: ["4", "-2", "/"]
    # 4 / -2 = -2
    assert sol.evalRPN(["4", "-2", "/"]) == -2, "Test case 7 failed"

    # All test cases passed
    print("All test cases passed!")

if __name__ == "__main__":
    main()