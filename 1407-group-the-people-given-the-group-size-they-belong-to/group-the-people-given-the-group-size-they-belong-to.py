class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = dict()
        groups = list()
        for i,team in enumerate(groupSizes):
            group[team] = group.get(team,[]) + [i]
            if len(group[team]) == team:
                groups.append(group[team])
                del group[team]
        return groups
        