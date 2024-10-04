"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

 0 [1,2,3,4,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # create a dummy list to avoid handle the edge case
        dummy = ListNode(0, head)
        prev = dummy

        # find the start point
        for _ in range(left-1):
            prev = prev.next

        # save the reverse list, keep pre unchanged
        stack = []
        curr = prev.next
        for _ in range(right - left +1): # +1 for inclusive
            stack.append(curr)
            curr = curr.next

        # read stack and link items reversely to pre
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        prev.next = curr  #curr is first one that don't need to reverse

        return dummy.next

# Helper function to convert a list to linked list
def list_to_linked_list(items):
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
def main():
    sol = Solution()

    # Test Case 1
    head = list_to_linked_list([1, 2, 3, 4, 5])
    left = 2
    right = 4
    result = sol.reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [1, 4, 3, 2, 5], "Test Case 1 Failed"

    # Test Case 2
    head = list_to_linked_list([5])
    left = 1
    right = 1
    result = sol.reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [5], "Test Case 2 Failed"

    # Test Case 3
    head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7])
    left = 3
    right = 6
    result = sol.reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [1, 2, 6, 5, 4, 3, 7], "Test Case 3 Failed"

    # Test Case 4
    head = list_to_linked_list([1, 2])
    left = 1
    right = 2
    result = sol.reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [2, 1], "Test Case 4 Failed"

    # Test Case 5
    head = list_to_linked_list([1, 2, 3])
    left = 2
    right = 3
    result = sol.reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [1, 3, 2], "Test Case 5 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    main()