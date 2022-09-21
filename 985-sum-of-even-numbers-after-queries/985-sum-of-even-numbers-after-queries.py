class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        checklist = list(map(lambda x: x%2, nums))
        total = 0
        for i in range(len(nums)):
            if not(checklist[i]):
                total += nums[i]
        
        output = list()
        for value, index in queries:
            checklistval = checklist[index]
            mod2 = abs(value)%2
            if not(checklistval | mod2):
                total += value
            elif checklistval & mod2:
                total += nums[index] + value
            elif checklistval & (not mod2):
                pass
            else:
                total -= nums[index]
            print(checklistval, value, total, nums[index]+value)
            output.append(total)
            nums[index] += value
            checklist[index] ^= mod2
        return output