class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        pre = 0

        for char in reversed(s):
            current = mapping[char]

            if current < pre:
                total -= current
            else:
                total += current
            pre = current
        
        return total