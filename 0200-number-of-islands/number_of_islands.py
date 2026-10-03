"""LeetCode 200 · Number of Islands — flood fill.

Scan the grid. Each new land cell starts a new island: count +1, then sink the
whole island so it is never counted again. Only the four directions connect.
Time O(rows x cols). For big grids in Python prefer the BFS version
(no recursion limit).
"""
from collections import deque


def islands_dfs(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r, c):
        if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count


def islands_bfs(grid):
    if not grid:
        return 0
    rows, cols, seen, count = len(grid), len(grid[0]), set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            count += 1
            queue = deque([(r, c)]); seen.add((r, c))
            while queue:
                x, y = queue.popleft()
                for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                        seen.add((nx, ny)); queue.append((nx, ny))
    return count
