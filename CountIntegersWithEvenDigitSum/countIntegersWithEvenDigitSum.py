class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            n = i
            agg = 0
            while n!= 0:
                a = n % 10
                agg += a
                n //= 10
            if agg % 2 == 0:
                count += 1
        return count