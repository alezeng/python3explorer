from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = []
        points.sort()
        for start, end in points:
            if result and result[-1][1] >= start:
                result[-1] = [max(result[-1][0], start), min(result[-1][1], end)]
            else:
                result.append([start, end])
        return len(result)

def main():
    sol = Solution()

    # Test Case 1: Basic overlap
    points = [[10,16],[2,8],[1,6],[7,12]]
    assert sol.findMinArrowShots(points) == 2, f"Test Case 1 Failed"

    # Test Case 2: No overlap
    points = [[1,2],[3,4],[5,6],[7,8]]
    assert sol.findMinArrowShots(points) == 4, f"Test Case 2 Failed"

    # Test Case 3: Complete overlap
    points = [[1,10],[2,9],[3,8],[4,7]]
    assert sol.findMinArrowShots(points) == 1, f"Test Case 3 Failed"

    # Test Case 4: Single balloon
    points = [[1,2]]
    assert sol.findMinArrowShots(points) == 1, f"Test Case 4 Failed"

    # Test Case 5: Empty list
    points = []
    assert sol.findMinArrowShots(points) == 0, f"Test Case 5 Failed"

    # Test Case 6: Partial overlap
    points = [[1,5], [2,6], [5,10], [7,12]]
    assert sol.findMinArrowShots(points) == 2, f"Test Case 6 Failed"

    # Test Case 7: Sequential touching balloons
    points = [[1,2], [2,3], [3,4], [4,5]]
    assert sol.findMinArrowShots(points) == 2, f"Test Case 7 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    main()