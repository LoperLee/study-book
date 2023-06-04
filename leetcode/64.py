from collections import deque
import heapq

class Solution:
    def minPathSum(self, grid) -> int:
        width = len(grid[0]) -1
        height = len(grid) -1
        queue = [ (grid[0][0], (0, 0)) ]
        while queue:
            now_value, (now_width, now_height) = heapq.heappop(queue)
            if now_width+1 <= width:
                heapq.heappush(queue, (now_value+grid[now_height][now_width+1], (now_width+1, now_height)))
            if now_height+1 <= height:
                heapq.heappush(queue, (now_value+grid[now_height+1][now_width], (now_width, now_height+1)))
            if now_width == width and now_height == height:
                return now_value
    
sol = Solution()
#print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum([[1,2,3],[4,5,6]]))