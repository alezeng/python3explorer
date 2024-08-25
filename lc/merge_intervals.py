from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        start = None
        end = None
        intervals.sort()
        for arr in intervals:
            if start is None:
                start = arr[0]
                end = arr[1]
                continue
            if arr[0] <= end:
                end = max(arr[1], end)
            else:
                result.append([start, end])
                start = arr[0]
                end = arr[1]
        if start is not None:
            result.append([start, end])
        return result

def main():
    # Initialize the solution instance
    sol = Solution()

    # Test Case 1: Overlapping intervals
    intervals = [(0, 3), (1, 3), (0, 2), (0, 1), (2, 3)]
    expected_output = [[0, 3]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 2: Non-overlapping intervals
    intervals = [(1, 2), (3, 4), (5, 6)]
    expected_output = [[1, 2], [3, 4], [5, 6]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 3: Single interval
    intervals = [(1, 4)]
    expected_output = [[1, 4]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 4: Multiple intervals with some overlapping
    intervals = [(1, 4), (2, 5), (6, 8), (7, 9)]
    expected_output = [[1, 5], [6, 9]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 5: Fully nested intervals
    intervals = [(1, 10), (2, 6), (3, 4)]
    expected_output = [[1, 10]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 6: No intervals (empty list)
    intervals = []
    expected_output = []
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 7: Identical intervals
    intervals = [(2, 3), (2, 3), (2, 3)]
    expected_output = [[2, 3]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 8: Intervals with negative values
    intervals = [(-3, -1), (-2, 2), (-5, 0)]
    expected_output = [[-5, 2]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 9: Mixed positive and negative intervals
    intervals = [(-3, -1), (1, 3), (-2, 2)]
    expected_output = [[-3, 3]]
    result = sol.merge(intervals)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All test cases passed.")

if __name__ == "__main__":
    main()