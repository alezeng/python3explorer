# Note: This is a shortcut solution similiar to merge_intervals
#  the solution could be improved by loop through the array as it's already sorted
#  the shorter version could reference arrow_shot.py

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort()
        start = None
        end = None
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
        result.append([start, end])
        return result
    

def main():
    # Initialize the solution instance
    sol = Solution()

    # Test Case 1: Inserting interval that overlaps with all existing intervals
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    expected_output = [[1, 5], [6, 9]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 2: Inserting interval that fits between existing intervals
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    expected_output = [[1, 2], [3, 10], [12, 16]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 3: Inserting interval that does not overlap with any existing intervals
    intervals = [[1, 3], [6, 9]]
    newInterval = [10, 12]
    expected_output = [[1, 3], [6, 9], [10, 12]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 4: Inserting interval that covers all existing intervals
    intervals = [[2, 3], [5, 7]]
    newInterval = [1, 8]
    expected_output = [[1, 8]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 5: Inserting interval when the list is empty
    intervals = []
    newInterval = [5, 7]
    expected_output = [[5, 7]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 6: Inserting interval that is identical to an existing interval
    intervals = [[1, 5]]
    newInterval = [1, 5]
    expected_output = [[1, 5]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 7: Inserting interval that only overlaps with some intervals
    intervals = [[1, 3], [4, 6], [8, 10]]
    newInterval = [5, 9]
    expected_output = [[1, 3], [4, 10]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 8: Inserting interval that fits before all existing intervals
    intervals = [[3, 5], [6, 8]]
    newInterval = [1, 2]
    expected_output = [[1, 2], [3, 5], [6, 8]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test Case 9: Inserting interval that fits after all existing intervals
    intervals = [[1, 2], [3, 4]]
    newInterval = [5, 6]
    expected_output = [[1, 2], [3, 4], [5, 6]]
    result = sol.insert(intervals, newInterval)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All test cases passed.")

if __name__ == "__main__":
    main()