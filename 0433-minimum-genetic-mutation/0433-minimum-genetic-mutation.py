class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def score(gene1, gene2):
            score = 0
            for i in range(8):
                if gene1[i] != gene2[i]:
                    score += 1
            return score
        if start == end:
            return 0
        if end not in bank:
            return -1
        else:
            options = list(filter(lambda gene: score(start, gene) == 1, bank))
            print(f'options: {options}')
            if options == []:
                return -1
            distance = list(map(lambda gene: score(end, gene), options))
            choices = list()
            mindist = min(distance)
            for i in range(len(distance)):
                if distance[i] == mindist:
                    choices.append(options[i])
            print(f'choices: {choices}')
            ult_scores = list()
            for choice in choices:
                new_bank = bank.copy()
                new_bank.remove(choice)
                ult_scores.append(self.minMutation(choice, end, new_bank))
            print(ult_scores)
            min_score = min(ult_scores)
            if min_score == -1:
                return min_score
            else:
                return 1 + min_score