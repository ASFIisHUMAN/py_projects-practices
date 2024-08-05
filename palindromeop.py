def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))   # Output: True
print(is_palindrome("22558785522"))    # Output: True
print(is_palindrome("A man, a plan, a canal, Panama"))   # Output: True
print(is_palindrome("hello"))    # Output: False
