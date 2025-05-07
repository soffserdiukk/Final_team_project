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


if name == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.config(bg="#f0f0f0")
    game = MemoryGame(root)
    root.mainloop()