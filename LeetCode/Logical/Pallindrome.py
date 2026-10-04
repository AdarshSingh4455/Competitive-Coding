class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        if x % 10 == 0:
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))    
    print(sol.isPalindrome(-121))   
    print(sol.isPalindrome(10))     
    print(sol.isPalindrome(0))      
    print(sol.isPalindrome(1))      
    print(sol.isPalindrome(1001))   
    print(sol.isPalindrome(12321))  
    print(sol.isPalindrome(12345))  
