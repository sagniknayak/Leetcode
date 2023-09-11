class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = dict()
        for i in range(len(groupSizes)):
            group[groupSizes[i]] = group.get(groupSizes[i],[])+[i] 
        groups = list()
        for key in group.keys():
            members = group[key]
            for i in range(0,len(members),key):
                groups.append(members[i:key+i])
        return groups
        