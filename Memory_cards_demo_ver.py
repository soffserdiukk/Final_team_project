import tkinter as tk
from tkinter import messagebox, font
import random
from typing import List, Tuple, Optional


class MemoryGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Memory Game")

        # Game settings
        self.difficulty_levels = {
            "Easy": (3, 4),
            "Medium": (4, 5),
            "Hard": (5, 6)
        }

        # Colors and styles
        self.bg_color = "#f0f0f0"
        self.card_bg = "#3498db"
        self.card_fg = "white"
        self.card_font = ("Arial", 12, "bold")
        self.disabled_color = "#2ecc71"

        self._setup_menu()

    def _setup_menu(self) -> None:
        """Create start menu with difficulty options"""
        self.clear_window()

        menu_frame = tk.Frame(self.root, bg=self.bg_color)
        menu_frame.pack(expand=True)

        tk.Label(
            menu_frame,
            text="Memory Game",
            font=("Arial", 24, "bold"),
            bg=self.bg_color
        ).pack(pady=20)

        for level, (rows, cols) in self.difficulty_levels.items():
            tk.Button(
                menu_frame,
                text=f"{level} ({rows}x{cols})",
                font=self.card_font,
                command=lambda r=rows, c=cols: self.start_game(r, c),
                width=15,
                padx=10,
                pady=5
            ).pack(pady=5)

        tk.Button(
            menu_frame,
            text="Exit",
            font=self.card_font,
            command=self.root.quit,
            width=15,
            padx=10,
            pady=5
        ).pack(pady=20)

    def clear_window(self) -> None:
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self, rows: int, cols: int) -> None:
        """Initialize game with selected difficulty"""
        self.rows = rows
        self.cols = cols
        self.pairs_needed = (rows * cols) // 2

        # Generate symbols - emoji work better for visual appeal
        emoji_symbols = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼",
                         "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐵", "🐔",
                         "🐧", "🐦", "🐤", "🦄", "🐝", "🐛", "🦋", "🐌"]

        # Select required number of symbols and duplicate for pairs
        selected_symbols = random.sample(emoji_symbols, self.pairs_needed)
        self.symbols = selected_symbols * 2

        # Game state
        self.buttons: List[tk.Button] = []
        self.first_click: Optional[tk.Button] = None
        self.can_click = True
        self.moves = 0

        self._setup_board()

    def _setup_board(self) -> None:
        """Setup the game board with styled buttons"""
        self.clear_window()

        # Header with moves counter
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill="x", pady=10)

        self.moves_label = tk.Label(
            header_frame,
            text=f"Moves: {self.moves}",
            font=self.card_font,
            bg=self.bg_color
        )
        self.moves_label.pack(side="left", padx=20)

        tk.Button(
            header_frame,
            text="Menu",
            font=self.card_font,
            command=self._setup_menu,
            padx=10
        ).pack(side="right", padx=20)

        # Game board
        board_frame = tk.Frame(self.root, bg=self.bg_color)
        board_frame.pack(expand=True)

        random.shuffle(self.symbols)

        for i in range(self.rows):
            for j in range(self.cols):
                idx = i * self.cols + j
                if idx < len(self.symbols):
                    btn = tk.Button(
                        board_frame,
                        text="?",
                        font=self.card_font,
                        width=4,
                        height=2,
                        bg=self.card_bg,
                        fg=self.card_fg,
                        activebackground="#2980b9",
                        command=lambda x=idx: self._button_click(x)
                    )
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    self.buttons.append(btn)

if name == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.config(bg="#f0f0f0")
    game = MemoryGame(root)
    root.mainloop()




