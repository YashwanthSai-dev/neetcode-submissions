class Solution:
    def isPalindrome(self, s: str) -> bool: 
        chars = [] 
        for ch in s: 
            if ch.isalnum(): 
                chars.append(ch.lower())
        c = "".join(chars)
        return  c == c[::-1]