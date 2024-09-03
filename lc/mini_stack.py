"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] #save the min at that moment

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)  
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

def main():
    # Test Case 1: Basic operations
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3, f"Test Case 1 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.top() == 0, f"Test Case 1 Failed: top() returned {minStack.top()}"
    assert minStack.getMin() == -2, f"Test Case 1 Failed: getMin() returned {minStack.getMin()}"

    # Test Case 2: Pushing elements in increasing order
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(3)
    assert minStack.getMin() == 1, f"Test Case 2 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.top() == 2, f"Test Case 2 Failed: top() returned {minStack.top()}"
    assert minStack.getMin() == 1, f"Test Case 2 Failed: getMin() returned {minStack.getMin()}"

    # Test Case 3: Pushing elements in decreasing order
    minStack = MinStack()
    minStack.push(3)
    minStack.push(2)
    minStack.push(1)
    assert minStack.getMin() == 1, f"Test Case 3 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.top() == 2, f"Test Case 3 Failed: top() returned {minStack.top()}"
    assert minStack.getMin() == 2, f"Test Case 3 Failed: getMin() returned {minStack.getMin()}"

    # Test Case 4: Pushing and popping the same element multiple times
    minStack = MinStack()
    minStack.push(2)
    minStack.push(2)
    minStack.push(2)
    assert minStack.getMin() == 2, f"Test Case 4 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 2, f"Test Case 4 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 2, f"Test Case 4 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    # Here, stack is empty, so no valid getMin() or top().

    # Test Case 5: Stack becomes empty after popping
    minStack = MinStack()
    minStack.push(5)
    minStack.push(3)
    minStack.push(7)
    assert minStack.getMin() == 3, f"Test Case 5 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 3, f"Test Case 5 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 5, f"Test Case 5 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    # After the last pop, the stack is empty. If we were to call top() or getMin() now, it would be an edge case.

    # Test Case 6: All elements in the stack are the same
    minStack = MinStack()
    minStack.push(2)
    minStack.push(2)
    minStack.push(2)
    minStack.push(2)
    assert minStack.getMin() == 2, f"Test Case 6 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 2, f"Test Case 6 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 2, f"Test Case 6 Failed: getMin() returned {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 2, f"Test Case 6 Failed: getMin() returned {minStack.getMin()}"

    print("All test cases passed!")

if __name__ == "__main__":
    main()