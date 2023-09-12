class Solution:
    def minDeletions(self, s: str) -> int:
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        print(freq)
        freq_unique = list()
        val = 0
        for key,value in freq.items():
            temp = value
            if temp in freq_unique:
                while temp in freq_unique and temp>0:
                    temp -= 1
                    val += 1
            freq_unique.append(temp)
        return val