class Solution:
    def isPalindrome(self, s: str) -> bool:
        bi = 0
        ei = len(s) - 1

        while bi < ei:
            while bi < ei and not s[bi].isalnum():
                bi += 1
            while bi < ei and not s[ei].isalnum():
                ei -= 1
            if s[bi].lower() != s[ei].lower():
                return False
            ei -= 1
            bi += 1
    
        return True
        