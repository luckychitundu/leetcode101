from collections import deque 
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        queue = deque([i for i in range(1, len(skills))])
        current_winner = 0
        streak = 0 
        while streak < k:
            next_player = queue.popleft() 
            if skills[current_winner] > skills[next_player]:
                streak += 1 
                queue.append(next_player) 
            else:
                streak = 1 
                queue.append(current_winner)
                current_winner = next_player 
            if streak >= len(skills) - 1:
                return current_winner     
        return current_winner         








        