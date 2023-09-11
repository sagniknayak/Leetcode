class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = dict()
        groups = list()
        for i in range(len(groupSizes)):
            group[groupSizes[i]] = group.get(groupSizes[i],[])+[i]
            if len(group[groupSizes[i]]) == groupSizes[i]:
                groups.append(group[groupSizes[i]])
                group[groupSizes[i]] = []
        print(groups)
        
        # for key in group.keys():
        #     members = group[key]
        #     for i in range(0,len(members),key):
        #         groups.append(members[i:key+i])
        return groups
        