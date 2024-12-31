class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = x
            rx = 0
            while temp > 0:
                rx = rx*10 + temp%10
                temp = temp//10
            return x == rx
