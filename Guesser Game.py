import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x200")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low. Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high. Try again.")
        else:
            self.result_label.config(
                text=f"Correct! You guessed it in {self.attempts} attempts."
            )
            self.button.config(state="disabled")
            self.entry.config(state="disabled")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
