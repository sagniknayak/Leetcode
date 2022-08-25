class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = dict()
        for letter1 in magazine:
            mag_count[letter1] = mag_count.get(letter1, 0) + 1
        ransom_count = dict()
        for letter2 in ransomNote:
            ransom_count[letter2] = ransom_count.get(letter2, 0) + 1
        flag = True
        for letter in ransom_count.keys():
            if ransom_count[letter] > mag_count.get(letter, 0):
                flag = False
                break
        return flag
        