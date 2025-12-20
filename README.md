import tkinter as tk
import random

WIDTH, HEIGHT = 400, 500
LANES = [100, 200, 300]

class RailRush:
    def __init__(self, root):
        self.root = root
        self.root.title("Rail Rush - Visual Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.lane = 1
        self.score = 0

        self.player = self.canvas.create_rectangle(
            LANES[self.lane]-15, 420,
            LANES[self.lane]+15, 460,
            fill="cyan"
        )

        self.spawn_obstacle()

        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw",
            fill="white", font=("Arial", 14),
            text="Score: 0"
        )

        root.bind("<Left>", self.left)
        root.bind("<Right>", self.right)
        root.bind("<Up>", self.jump)
        root.bind("<Down>", self.duck)

        self.move_obstacle()

    def spawn_obstacle(self):
        self.obs_lane = random.randint(0, 2)
        self.obstacle = self.canvas.create_rectangle(
            LANES[self.obs_lane]-20, 0,
            LANES[self.obs_lane]+20, 40,
            fill="red"
        )

    def left(self, e):
        if self.lane > 0:
            self.lane -= 1
            self.update_player()

    def right(self, e):
        if self.lane < 2:
            self.lane += 1
            self.update_player()

    def jump(self, e):
        self.canvas.move(self.player, 0, -40)
        self.root.after(300, lambda: self.canvas.move(self.player, 0, 40))

    def duck(self, e):
        self.canvas.scale(self.player, 0, 0, 1, 0.6)
        self.root.after(300, lambda: self.canvas.scale(self.player, 0, 0, 1, 1.67))

    def update_player(self):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        cx = (x1 + x2) / 2
        self.canvas.move(self.player, LANES[self.lane] - cx, 0)

    def move_obstacle(self):
        self.canvas.move(self.obstacle, 0, 6)
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.obstacle)
        px1, py1, px2, py2 = self.canvas.coords(self.player)

        if ox1 < px2 and ox2 > px1 and oy1 < py2 and oy2 > py1:
            self.canvas.create_text(
                200, 250,
                fill="yellow",
                font=("Arial", 24, "bold"),
                text="GAME OVER"
            )
            return

        if oy1 > HEIGHT:
            self.canvas.delete(self.obstacle)
            self.spawn_obstacle()
            self.score += 10
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        self.root.after(30, self.move_obstacle)

root = tk.Tk()
RailRush(root)
root.mainloop()

