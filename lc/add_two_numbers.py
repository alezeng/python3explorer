"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

"""
There's better solution by loop through both list at the same time and using a carry over number
"""

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumber(l: Optional[ListNode]):
            num = 0
            i = 0
            while l:
                num += l.val*10**i
                i += 1
                l = l.next
            return num
        
        def genList(num: int):
            snum = str(num)
            last = None
            for s in snum:
                new = ListNode(int(s), last)
                last = new
            return last

        total = getNumber(l1) + getNumber(l2)
        return genList(total)

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# create a main function with all kinds of test cases using assert function
def main():
    solution = Solution()

    # Test case 1: l1 = [2, 4, 3], l2 = [5, 6, 4]
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8], "Test case 1 failed"
    print("Test case 1 passed!")

    # Test case 2: l1 = [0], l2 = [0]
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0], "Test case 2 failed"
    print("Test case 2 passed!")

    # Test case 3: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1], "Test case 3 failed"
    print("Test case 3 passed!")

    # Additional Test Case: Large numbers
    l1 = list_to_linkedlist([1, 8])
    l2 = list_to_linkedlist([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [1, 8], "Test case 4 failed"
    print("Test case 4 passed!")

    # Additional Test Case: Carry over
    l1 = list_to_linkedlist([9, 9])
    l2 = list_to_linkedlist([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 1], "Test case 5 failed"
    print("Test case 5 passed!")

if __name__ == "__main__":
    main()