class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = list()
        leng = len(graph)
        check = [False for i in range(leng)]
        for i in range(leng):
            if graph[i] == []:
                terminal.append(i)
                check[i] = True
        safe = list()
        while(True):
            current_safe = list()
            for i in range(leng):
                if check[i] == False:
                    test = graph[i]
                    connection = list(map(lambda x:check[x], test))
                    op = reduce(lambda a,b: a & b, connection)
                    if op:
                        check[i] = True
                        current_safe.append(i)
            if current_safe != []:
                safe = safe + current_safe
            else:
                break
        safe += terminal
        safe.sort()
        return safe