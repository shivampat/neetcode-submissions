from collections import Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        counts = Counter(senate)
        opposition = {'D': 'R', 'R': 'D'}
        banned = {'D': 0, 'R': 0}
        names = {'D': 'Dire', 'R': 'Radiant'}

        while len(q) > 1:
            party = q.popleft()

            if counts[opposition[party]] == 0:
                return names[party]

            if banned[party] > 0:
                banned[party] -= 1
                counts[party] -= 1
                continue
            
            banned[opposition[party]] += 1
            q.append(party)

        return names[q[-1]]