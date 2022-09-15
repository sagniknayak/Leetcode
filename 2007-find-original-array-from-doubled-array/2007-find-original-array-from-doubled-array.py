class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        numberofzeros, leftoutzeros = divmod(count[0],2)
        if leftoutzeros:
            return []
        res = [0]*numberofzeros
        
        for key in sorted(count.keys()):
            if count[key] > count[2*key]:
                return []
            count[2*key] -= count[key]
            res.extend([key]*count[key])
        return res