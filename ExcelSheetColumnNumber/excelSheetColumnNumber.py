class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
    
columnTitle = input("Enter a column title:")
columnNumber = Solution().titleToNumber(columnTitle)
print(f"Result: {columnNumber}")