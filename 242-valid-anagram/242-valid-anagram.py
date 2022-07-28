class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            set_s = set(s)
            set_t = set(t)
            if set_s != set_t:
                return False
            else:
                for elem in set_s:
                    if s.count(elem) != t.count(elem):
                        return False
            return True