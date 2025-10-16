import tkinter as tk
from tkinter import messagebox
import game_logic as gl

class Game2048:
    def __init__(self, master):
        self.master = master
        self.size = 4  # Fixed 4x4 board
        self.master.title("2048 Game")
        self.master.configure(bg="#faf8ef")
        self.board = gl.new_game(self.size)
        self.score = 0
        self.cells = []

        self.create_gui()
        self.update_gui()

        # Bind arrow keys for movement
        self.master.bind("<Key>", self.key_handler)

    def create_gui(self):
        # --- Title ---
        title_label = tk.Label(
            self.master,
            text="2048",
            font=("Helvetica", 48, "bold"),
            fg="#776e65",
            bg="#faf8ef",
        )
        title_label.pack(pady=(20, 10))

        # --- Score and Restart Section ---
        top_frame = tk.Frame(self.master, bg="#faf8ef")
        top_frame.pack(pady=(0, 20))

        self.score_label = tk.Label(
            top_frame, text="Score: 0",
            font=("Helvetica", 16, "bold"),
            bg="#bbada0", fg="white",
            width=10, height=2
        )
        self.score_label.pack(side="left", padx=10)

        restart_button = tk.Button(
            top_frame, text="Restart",
            font=("Helvetica", 14, "bold"),
            bg="#8f7a66", fg="white",
            width=10, height=2,
            command=self.restart
        )
        restart_button.pack(side="right", padx=10)

        # --- Game Board ---
        board_frame = tk.Frame(self.master, bg="#bbada0", bd=4, relief="ridge")
        board_frame.pack(padx=20, pady=10)

        for i in range(self.size):
            row = []
            for j in range(self.size):
                label = tk.Label(
                    board_frame,
                    text="",
                    width=4, height=2,
                    font=("Helvetica", 24, "bold"),
                    bg="#cdc1b4",
                    fg="#776e65",
                    relief="ridge"
                )
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.cells.append(row)

    def update_gui(self):
        """Update tile colors and numbers."""
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                cell = self.cells[i][j]
                cell.config(
                    text=str(value) if value != 0 else "",
                    bg=self.get_color(value),
                    fg="#776e65" if value <= 4 else "white"
                )
        self.score_label.config(text=f"Score: {self.score}")

    def get_color(self, value):
        """Return tile color based on value."""
        colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
            128: "#edcf72", 256: "#edcc61", 512: "#edc850",
            1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def key_handler(self, event):
        """Handle arrow key movement."""
        key = event.keysym
        moved = False
        score_gain = 0

        if key == "Up":
            self.board, score_gain = gl.move_up(self.board)
            moved = True
        elif key == "Down":
            self.board, score_gain = gl.move_down(self.board)
            moved = True
        elif key == "Left":
            self.board, score_gain = gl.move_left(self.board)
            moved = True
        elif key == "Right":
            self.board, score_gain = gl.move_right(self.board)
            moved = True

        if moved:
            self.score += score_gain
            gl.add_new_tile(self.board)
            self.update_gui()

            if any(2048 in row for row in self.board):
                messagebox.showinfo("2048", "🎉 You Win!")
            elif gl.game_over(self.board):
                messagebox.showinfo("2048", "❌ Game Over!")

    def restart(self):
        """Restart the game."""
        self.board = gl.new_game(self.size)
        self.score = 0
        self.update_gui()

if __name__ == "__main__":
    root = tk.Tk()
    Game2048(root)
    root.mainloop()
