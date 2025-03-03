class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# Example usage
n = int(input("Enter a number: "))
print(Solution().isHappy(n))
