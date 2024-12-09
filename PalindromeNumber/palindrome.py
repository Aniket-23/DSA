class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        check_x = x
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + (x % 10)
            x //=10

        return check_x == reversed_x