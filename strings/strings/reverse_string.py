# Problem: Reverse String
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_string(s):
    left, right = 0, len(s) - 1
    s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

if __name__ == "__main__":
    s = "hello"
    print(reverse_string(s))
