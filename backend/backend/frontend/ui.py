import tkinter as tk
import random
from backend.game_logic import LANES, HEIGHT, check_collision
from backend.ai_logic import choose_lane

class RailRushUI:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=500, bg="black")
        self.canvas.pack()

        self.lane = 1
        self.score = 0

        self.player = self.canvas.create_rectangle(
            LANES[self.lane]-15, 420,
            LANES[self.lane]+15, 460,
            fill="cyan"
        )

        self.spawn_obstacle()
        self.move_obstacle()

    def spawn_obstacle(self):
        self.obs_lane = random.randint(0, 2)
        self.obstacle = self.canvas.create_rectangle(
            LANES[self.obs_lane]-20, 0,
            LANES[self.obs_lane]+20, 40,
            fill="red"
        )

    def move_obstacle(self):
        self.canvas.move(self.obstacle, 0, 6)

        if check_collision(
            self.canvas.coords(self.player),
            self.canvas.coords(self.obstacle)
        ):
            self.canvas.create_text(200, 250, text="GAME OVER",
                                    fill="yellow", font=("Arial", 24))
            return

        if self.canvas.coords(self.obstacle)[1] > HEIGHT:
            self.canvas.delete(self.obstacle)
            self.spawn_obstacle()
            self.score += 10

        self.root.after(30, self.move_obstacle)
