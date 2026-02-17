# Problem: Valid Parentheses
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping.get(char):
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    s = "{[()]}"
    print(is_valid(s))
