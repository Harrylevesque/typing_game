import random
import tkinter as tk
from tkinter import messagebox

recipes = [
    "Pancakes\n1. Mix flour, sugar, baking powder, and salt.\n2. Whisk in milk, egg, and melted butter.\n3. Heat a skillet over medium heat.\n4. Pour batter onto skillet.\n5. Cook until bubbles form, flip, and cook until golden.",
    "Grilled Cheese Sandwich\n1. Butter one side of two bread slices.\n2. Place cheese between unbuttered sides.\n3. Heat a skillet over medium heat.\n4. Cook sandwich until golden brown on both sides.\n5. Slice and serve warm.",
    "Spaghetti Aglio e Olio\n1. Boil spaghetti in salted water.\n2. Heat olive oil in a pan.\n3. Add sliced garlic and red pepper flakes.\n4. Toss cooked spaghetti in the pan.\n5. Garnish with parsley and serve.",
    "Omelette\n1. Beat eggs with salt and pepper.\n2. Heat butter in a nonstick pan.\n3. Pour eggs into the pan.\n4. Cook until almost set, add fillings.\n5. Fold omelette and serve.",
    "Fruit Salad\n1. Chop apples, bananas, and grapes.\n2. Add orange segments and berries.\n3. Squeeze lemon juice over fruit.\n4. Toss gently to combine.\n5. Chill before serving."
]

class TypingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Game")
        self.selected_recipe = random.choice(recipes)
        self.lines = self.selected_recipe.split('\n')
        self.current_line = 0

        self.label = tk.Label(master, text="Type this line:", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.text_display = tk.Text(master, font=("Times", 26), height=1, width=80, bd=0, bg=master.cget('bg'))
        self.text_display.pack(pady=5)
        self.text_display.config(state=tk.DISABLED)

        self.entry = tk.Entry(master, font=("Helvetica", 36), width=80)
        self.entry.pack(pady=5)
        self.entry.bind("<KeyRelease>", self.update_colored_text)
        self.entry.bind("<Return>", self.check_input)
        self.entry.focus_set()

        self.feedback = tk.Label(master, text="", font=("Times", 36))
        self.feedback.pack(pady=5)

        self.update_colored_text()  # Show first line

    def update_colored_text(self, event=None):
        expected = self.lines[self.current_line]
        user_input = self.entry.get()
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete("1.0", tk.END)
        for i, c in enumerate(expected):
            if i < len(user_input):
                if user_input[i] == c:
                    self.text_display.insert(tk.END, c, "correct")
                else:
                    self.text_display.insert(tk.END, c, "incorrect")
            else:
                self.text_display.insert(tk.END, c)
        self.text_display.tag_config("correct", foreground="green")
        self.text_display.tag_config("incorrect", foreground="red")
        self.text_display.config(state=tk.DISABLED)

    def check_input(self, event):
        user_input = self.entry.get()
        expected = self.lines[self.current_line]
        if user_input.strip() == expected.strip():
            self.feedback.config(text="Correct!", fg="green")
            self.current_line += 1
            if self.current_line < len(self.lines):
                self.entry.delete(0, tk.END)
                self.update_colored_text()
            else:
                messagebox.showinfo("Congratulations!", "You completed the recipe!")
                self.master.destroy()
        else:
            self.feedback.config(text="Incorrect. Try to be more accurate.", fg="red")
            messagebox.showerror("Game Over", f"Expected: {expected}\nGot: {user_input}")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
