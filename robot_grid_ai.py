"""
Robot Grid AI Simulator
-----------------------
A robot that moves on a 2D grid, avoids obstacles, and can find a path.
Created by islandgreedster 🚀
"""

import random

class Grid:
    def __init__(self, width=10, height=10, obstacle_count=15):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(width)] for _ in range(height)]
        self.place_obstacles(obstacle_count)

    def place_obstacles(self, count):
        for _ in range(count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.grid[y][x] = "#"

    def display(self, robot=None):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if robot and robot.x == x and robot.y == y:
                    row += "🤖"
                else:
                    row += self.grid[y][x]
            print(row)
        print()


class Robot:
    def __init__(self, name="GridBot", x=0, y=0, grid=None):
        self.name = name
        self.x = x
        self.y = y
        self.grid = grid

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if (0 <= new_x < self.grid.width) and (0 <= new_y < self.grid.height):
            if self.grid.grid[new_y][new_x] != "#":  # Avoid obstacles
                self.x, self.y = new_x, new_y
            else:
                print(f"{self.name}: Obstacle at ({new_x}, {new_y})")
        else:
            print(f"{self.name}: Out of bounds!")

    def report(self):
        return f"{self.name} is at ({self.x}, {self.y})"


# Demo usage
if __name__ == "__main__":
    grid = Grid(width=10, height=6, obstacle_count=8)
    bot = Robot(name="GreedsterBot", grid=grid)

    print("🌍 Robot Grid AI Simulator\n")
    grid.display(bot)

    # Simulate random moves
    moves = [(0,1), (1,0), (0,-1), (-1,0)]  # Down, Right, Up, Left
    for _ in range(10):
        dx, dy = random.choice(moves)
        bot.move(dx, dy)
        grid.display(bot)

    print("Final position:", bot.report())


