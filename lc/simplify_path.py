class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        for part in parts:
            if part == "." or part == "":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)

def main():
    sol = Solution()

    # Test Case 1: Basic path with trailing slash
    path = "/home/"
    assert sol.simplifyPath(path) == "/home", f"Test Case 1 Failed: {sol.simplifyPath(path)}"

    # Test Case 2: Path with multiple consecutive slashes
    path = "/home//foo/"
    assert sol.simplifyPath(path) == "/home/foo", f"Test Case 2 Failed: {sol.simplifyPath(path)}"

    # Test Case 3: Path with parent directory navigation
    path = "/home/user/Documents/../Pictures"
    assert sol.simplifyPath(path) == "/home/user/Pictures", f"Test Case 3 Failed: {sol.simplifyPath(path)}"

    # Test Case 4: Root path with parent directory navigation
    path = "/../"
    assert sol.simplifyPath(path) == "/", f"Test Case 4 Failed: {sol.simplifyPath(path)}"

    # Test Case 5: Path with valid directory names like "..."
    path = "/.../a/../b/c/../d/./"
    assert sol.simplifyPath(path) == "/.../b/d", f"Test Case 5 Failed: {sol.simplifyPath(path)}"

    # Test Case 6: Root path without any directories
    path = "/"
    assert sol.simplifyPath(path) == "/", f"Test Case 6 Failed: {sol.simplifyPath(path)}"

    # Test Case 7: Complex path with multiple ".." and "."
    path = "/a/./b/../../c/"
    assert sol.simplifyPath(path) == "/c", f"Test Case 7 Failed: {sol.simplifyPath(path)}"

    # Test Case 8: Path that goes up to root and beyond
    path = "/a/b/c/../../../../d"
    assert sol.simplifyPath(path) == "/d", f"Test Case 9 Failed: {sol.simplifyPath(path)}"

    print("All test cases passed!")

if __name__ == "__main__":
    main()