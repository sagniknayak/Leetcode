class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = dict()
        leng = len(s)
        palin[1] = [((i,i),s[i]) for i in range(leng)]
        palin[2] = list(filter(lambda x: x[1][0] == x[1][1],[((i,i+1),s[i]+s[i+1]) for i in range(leng-1)]))
        for i in range(3, leng+1):
            palin[i] = []
            if palin[i-1] == palin[i-2]:
                break
            if palin[i-2] == []:
                continue
            new_palin = list()
            for base in list(filter(lambda x: x[0][0]-1>=0 and x[0][1]+1<leng,palin[i-2])):
                if s[base[0][0]-1] == s[base[0][1]+1]:
                    new_palin.append(((base[0][0]-1,base[0][1]+1),s[base[0][0]-1]+base[1]+s[base[0][1]+1]))
            palin[i] = new_palin
        for i in range(max(palin.keys()),0,-1):
            if palin.get(i,[]) == []:
                continue
            else:
                return palin[i][0][1]
        return ""
        