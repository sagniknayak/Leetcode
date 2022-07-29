class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        op = list()
        length = len(pattern)
        for word in words:
            flag = True
            for i in range(length):
                if word.index(word[i]) != pattern.index(pattern[i]):
                    flag = False
                    break
            if flag:
                op.append(word)
        return op
        