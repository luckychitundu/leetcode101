from collections import deque 
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        queue = deque([i for i in range(1, n)])
        current_winner = 0
        streak = 0 
        while streak < k and streak < n:
            next_player = queue.popleft() 
            if skills[current_winner] > skills[next_player]:
                streak += 1 
                queue.append(next_player) 
            else:
                streak = 1 
                queue.append(current_winner)
                current_winner = next_player   
        return current_winner         








        