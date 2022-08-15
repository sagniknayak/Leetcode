class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        flag4 = False
        for i in range(len(s)):
            if flag4:
                flag4 = False
                continue
            if i<len(s)-1:
                if value_map[s[i]]<value_map[s[i+1]]:
                    val += value_map[s[i+1]] - value_map[s[i]]
                    flag4 = True
            if not flag4:
                val += value_map[s[i]]
        return val
        