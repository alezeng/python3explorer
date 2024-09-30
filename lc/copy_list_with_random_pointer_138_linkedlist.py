'''
138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # use hashmap
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}

        # create the new nodes and save it in map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # set the next and random in the new nodes 
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]
# Complexity Analysis
# Time Complexity: O(n) — Each node is visited twice.
# Space Complexity: O(n) — To store the hash map.

    # Interweaving Nodes
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # create the new nodes and save it in between the current node and the current node's next
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # set the random pointers for the new nodes 
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # separating lists
        curr = head
        new_head = head.next
        new_curr = new_head
        while curr:
            curr.next = curr.next.next
            new_curr.next = new_curr.next.next if new_curr.next else None

            curr = curr.next
            new_curr = new_curr.next
        return new_head
    #  Complexity Analysis
    #   Time Complexity: O(n) — Each node is visited multiple times but it's still linear time.
    #   Space Complexity: O(1) — No additional memory is used for mapping; we only allocate nodes for the new list.

# Helper function to convert list to linked list
def build_linked_list(arr):
    if not arr:
        return None
    nodes = [Node(val) for val, _ in arr]
    for i, (_, random_index) in enumerate(arr):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]

# Helper function to convert linked list to list (to compare results)
def linked_list_to_list(head):
    result = []
    curr = head
    nodes = []
    while curr:
        nodes.append(curr)
        curr = curr.next
    for node in nodes:
        random_index = None if not node.random else nodes.index(node.random)
        result.append([node.val, random_index])
    return result

# Test cases
def main():
    solution = Solution()

    # Test Case 1
    head1 = build_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copied_head1 = solution.copyRandomList(head1)
    assert linked_list_to_list(copied_head1) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], "Test Case 1 Failed"

    # Test Case 2
    head2 = build_linked_list([[1, 1], [2, 1]])
    copied_head2 = solution.copyRandomList(head2)
    assert linked_list_to_list(copied_head2) == [[1, 1], [2, 1]], "Test Case 2 Failed"

    # Test Case 3
    head3 = build_linked_list([[3, None], [3, 0], [3, None]])
    copied_head3 = solution.copyRandomList(head3)
    assert linked_list_to_list(copied_head3) == [[3, None], [3, 0], [3, None]], "Test Case 3 Failed"

    # Test Case 4: Empty list
    head4 = build_linked_list([])
    copied_head4 = solution.copyRandomList(head4)
    assert copied_head4 is None, "Test Case 4 Failed"

    print("All test cases passed.")

if __name__ == "__main__":
    main()