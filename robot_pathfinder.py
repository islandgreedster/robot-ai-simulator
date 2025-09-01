import heapq
import random

class Grid:
    def __init__(self, width=10, height=10, obstacle_ratio=0.2):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(width)] for _ in range(height)]
        self.place_obstacles(obstacle_ratio)

    def place_obstacles(self, ratio):
        total = int(self.width * self.height * ratio)
        for _ in range(total):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.grid[y][x] = "#"

    def display(self, path=None):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if path and (x, y) in path:
                    row += "🟩"
                else:
                    row += self.grid[y][x]
            print(row)
        print()

    def is_free(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] == "."

class RobotPathfinder:
    def __init__(self, grid, start=(0, 0), goal=None):
        self.grid = grid
        self.start = start
        self.goal = goal if goal else (grid.width - 1, grid.height - 1)

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    def a_star(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if not self.grid.is_free(*neighbor) and neighbor != self.goal:
                    continue
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

if __name__ == "__main__":
    grid = Grid(10, 10, obstacle_ratio=0.2)
    robot = RobotPathfinder(grid)

    path = robot.a_star()
    if path:
        print("✅ Path found from", robot.start, "to", robot.goal)
        grid.display(path)
    else:
        print("❌ No path found")
        grid.display()


---

