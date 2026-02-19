import re

def isPalindrome(s):
    # remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # check palindrome
    return cleaned == cleaned[::-1]


# Example test
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
