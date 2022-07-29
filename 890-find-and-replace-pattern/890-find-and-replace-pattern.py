class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        op = list()
        length = len(pattern)
        for word in words:
            w_map = dict()
            p_map = dict()
            flag = True
            for i in range(length):
                key1 = w_map.get(word[i], None)
                key2 = p_map.get(pattern[i], None)
                if key1 is None and key2 is None:
                    w_map[word[i]] = pattern[i]
                    p_map[pattern[i]] = word[i]
                elif key1 == pattern[i] and key2 == word[i]:
                    pass
                else:
                    flag = False
                    break
            if flag:
                op.append(word)
        return op
        