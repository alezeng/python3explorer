"""
224. Basic Calculator
Attempted
Hard
Topics
Companies
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

"""

import re 
class Solution:
    def calculate(self, s: str) -> int:
        def cal(a: int, op: str, b: int):
            return a + b if op == "+" else a - b
        
        result = 0
        op = "+"
        tokens = re.findall(r'\d+|[()+\-]', s.replace(" ",""))
        tlen = len(tokens)
        stack = []
        pstack = []
        res = None
        for i in range(tlen):
            if tokens[i] in ("+", "-", "("):
                #print(stack)
                if tokens[i] == "-" and (not stack or (stack and stack[-1] == "(")):
                    stack.append(0) # add 0 before empty -
                stack.append(tokens[i])
            elif tokens[i] == ")":
                #print(stack)
                res = stack.pop() # last result
                if stack[-1] == "(":
                    stack[-1] = res
                while len(stack) > 1 and stack[-2] != "(":
                    # calculate it until last (, exmaple "(1+(4+5+2)-3)+(6+8)",  "- (3 + (4 + 5)-3)"
                    b = stack.pop()
                    op = stack.pop()
                    a = stack.pop() if len(stack) >=1 else 0
                    res = cal(a, op, res)
                    stack.append(res)
            else: # digit
                #print(stack)
                if stack and stack[-1] != "(": # calculate it
                    op = stack.pop()
                    res = stack.pop() if len(stack) >=1 else 0
                    res = cal(res, op, int(tokens[i]))
                    stack.append(res)
                else:
                    stack.append(int(tokens[i]))
        return stack[-1] if stack else None

    """
    [Python] Basic Calculator I, II, III easy solution, detailed explanation
    by DBabichev
    
    This algorithm works for Basic Calculator (BC I) problem, where we can have only + - ( ) operations, for Basic Calculator II (BC II), where we can have only + - * / operations and also for Basic Calculator III (BC III), where we can have all + - * / ( ) operations.

    Stack of monomials
    The idea is to use both stack and recursion (which can be seen as 2 stack, because recursion use implicit stack). First, let us consider, that we do not have any brackets. Then let us keep the stack of monomial, consider the example s = 1*2 - 3/4*5 + 6. Then we want our stack to be equal to [1*2, -3/4*5, 6], let us do it step by step:

        Put 1 into stack, we have stack = [1].
        We can see that operation is equal to *, so we pop the last element from our stack and put new element: 1*2, now stack = [1*2].
        Now, operation is equal to -, so we put -3 to stack and we have stack = [1*2, -3] now
        Now, operation is equal to /, so we pop the last element from stack and put -3/4 instead, stack = [1*2, -3/4]
        Now, operation is equal to *, so we pop last element from stack and put -3/4*5 instead, stack = [1*2, -3/4*5].
        Finally, operation is equal to +, so we put 6 to stack: stack = [1*2, -3/4*5, 6]
    Now, all we need to do is to return sum of all elements in stack.
    """
    def calculate2(self, s: str) -> int: 
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)

# Main function to run test cases
def main():
    sol = Solution()

    # Test cases with assert and failure messages

    # Test case 1: Simple addition
    assert sol.calculate("1 + 1") == 2, "Test case 1 failed"

    # Test case 2: Simple subtraction and addition
    assert sol.calculate(" 2-1 + 2 ") == 3, "Test case 2 failed"

    # Test case 3: Nested parentheses and multiple operators
    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23, "Test case 3 failed"

    # Test case 4: Expression with unary minus
    assert sol.calculate("-1 + 2") == 1, "Test case 4 failed"

    # Test case 5: Complex nested expression
    assert sol.calculate("((2+(3-1))+4)-5") == 3, "Test case 5 failed"

    # Test case 6: Larger numbers
    assert sol.calculate("100 + (200 - 50) + 75") == 325, "Test case 6 failed"

    # Test case 7: Expression with multiple parentheses
    assert sol.calculate("(1+(2-(3+(4-5))))") == 1, "Test case 7 failed"

    # Test case 8: Expression without spaces
    assert sol.calculate("10-(2+3)") == 5, "Test case 8 failed"

    # Test case 9: Nested parentheses with unary minus
    assert sol.calculate("-(3+(4-5))") == -2, "Test case 9 failed"

    print("All test cases passed!")

# Run all test cases
if __name__ == "__main__":
    main()