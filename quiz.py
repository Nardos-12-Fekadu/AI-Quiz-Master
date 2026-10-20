
import tkinter as tk
from tkinter import ttk
import random

# ---------- COLORS ----------
BG = "#151329"
PANEL = "#211D3B"
PURPLE = "#8B5CF6"
CYAN = "#38D9F8"
WHITE = "#F8FAFC"
MUTED = "#A9A6C4"
GREEN = "#34D399"
RED = "#FB7185"

# ---------- QUIZ QUESTIONS ----------
QUESTIONS = {
    "Easy": [
        {
            "question": "What does AI stand for?",
            "options": [
                "Automated Internet",
                "Artificial Intelligence",
                "Advanced Input",
                "Applied Information"
            ],
            "answer": 1,
            "topic": "AI basics",
            "explanation": "AI stands for Artificial Intelligence."
        },
        {
            "question": "Which language are we using?",
            "options": ["Java", "C++", "Python", "HTML"],
            "answer": 2,
            "topic": "Python",
            "explanation": "We are building this project with Python."
        },
        {
            "question": "Which symbol starts a Python comment?",
            "options": ["//", "#", "<!--", "**"],
            "answer": 1,
            "topic": "Python",
            "explanation": "Python comments usually begin with #."
        }
    ],
    "Medium": [
        {
            "question": "Which structure stores an ordered collection?",
            "options": ["list", "int", "bool", "float"],
            "answer": 0,
            "topic": "Python data structures",
            "explanation": "A list stores multiple items in order."
        },
        {
            "question": "Which keyword repeats code while a condition is true?",
            "options": ["if", "def", "while", "return"],
            "answer": 2,
            "topic": "Python loops",
            "explanation": "A while loop repeats while its condition is true."
        },
        {
            "question": "What does len([10, 20, 30]) return?",
            "options": ["2", "3", "10", "60"],
            "answer": 1,
            "topic": "Python functions",
            "explanation": "len() returns the number of items: 3."
        }
    ],
    "Hard": [
        {
            "question": "Which structure stores key-value pairs?",
            "options": ["tuple", "string", "dictionary", "integer"],
            "answer": 2,
            "topic": "Python data structures",
            "explanation": "A dictionary stores key-value pairs."
        },
        {
            "question": "What is the result of 3 * [2]?",
            "options": ["[6]", "[2, 2, 2]", "[3, 2]", "Error"],
            "answer": 1,
            "topic": "Python lists",
            "explanation": "Multiplying a list by 3 repeats its items."
        },
        {
            "question": "Which keyword defines a Python function?",
            "options": ["function", "fun", "def", "make"],
            "answer": 2,
            "topic": "Python functions",
            "explanation": "Python functions are defined using def."
        }
    ]
}


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Quiz Master")
        self.root.geometry("800x650")
        self.root.minsize(650, 580)
        self.root.configure(bg=BG)

        self.name = "Player"
        self.questions = []
        self.question_index = 0
        self.score = 0
        self.wrong_topics = []
        self.answered = False

        self.setup_styles()
        self.show_home()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Quiz.Horizontal.TProgressbar",
            troughcolor=PANEL,
            background=CYAN,
            bordercolor=PANEL,
            lightcolor=CYAN,
            darkcolor=CYAN
        )

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_label(self, parent, text, size=12, color=WHITE,
                   bold=False, wrap=650):
        return tk.Label(
            parent,
            text=text,
            font=("Segoe UI", size, "bold" if bold else "normal"),
            fg=color,
            bg=parent["bg"],
            wraplength=wrap,
            justify="center"
        )

    def make_button(self, parent, text, command,
                    bg=PURPLE, fg=WHITE):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 11, "bold"),
            bg=bg,
            fg=fg,
            activebackground=CYAN,
            activeforeground=BG,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=11
        )

    def show_home(self):
        self.clear_screen()

        self.make_label(
            self.root, "🧠 AI QUIZ MASTER", 27, CYAN, True
        ).pack(pady=(35, 5))

        self.make_label(
            self.root, "Learn. Think. Improve.", 13, MUTED
        ).pack(pady=(0, 25))

        card = tk.Frame(self.root, bg=PANEL, padx=35, pady=25)
        card.pack(padx=35, fill="x")

        self.make_label(
            card, "Welcome, Future Programmer!", 19, WHITE, True
        ).pack(pady=(0, 10))

        self.make_label(
            card,
            "Test your knowledge of Python and artificial intelligence.",
            11, MUTED
        ).pack(pady=(0, 20))

        self.make_label(
            card, "Enter your name", 11, WHITE, True
        ).pack(anchor="w")

        self.name_entry = tk.Entry(
            card,
            font=("Segoe UI", 12),
            bg=BG,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            justify="center"
        )
        self.name_entry.pack(fill="x", ipady=9, pady=(6, 18))
        self.name_entry.insert(0, "Player")

        self.make_label(
            card, "Choose your difficulty", 11, WHITE, True
        ).pack(pady=(0, 8))

        self.difficulty = tk.StringVar(value="Easy")

        difficulty_menu = tk.OptionMenu(
            card, self.difficulty, "Easy", "Medium", "Hard"
        )
        difficulty_menu.config(
            font=("Segoe UI", 11),
            bg=BG, fg=WHITE,
            activebackground=PURPLE,
            activeforeground=WHITE,
            relief="flat",
            highlightthickness=0
        )
        difficulty_menu["menu"].config(
            bg=PANEL, fg=WHITE, font=("Segoe UI", 11)
        )
        difficulty_menu.pack(fill="x", pady=(0, 20))

        self.make_button(
            card, "START QUIZ  →", self.start_quiz, CYAN, BG
        ).pack(fill="x")

        self.make_label(
            self.root,
            "9 questions available • Instant feedback • Personal practice tips",
            9, MUTED
        ).pack(pady=20)

    def start_quiz(self):
        self.name = self.name_entry.get().strip() or "Player"
        level = self.difficulty.get()

        self.questions = QUESTIONS[level][:]
        random.shuffle(self.questions)

        self.question_index = 0
        self.score = 0
        self.wrong_topics = []
        self.show_question()

    def show_question(self):
        self.clear_screen()
        self.answered = False

        question = self.questions[self.question_index]
        total = len(self.questions)
        number = self.question_index + 1

        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=30, pady=(20, 10))

        self.make_label(
            header, "🧠 AI QUIZ MASTER", 16, CYAN, True
        ).pack(side="left")

        self.make_label(
            header, f"Score: {self.score}", 12, GREEN, True
        ).pack(side="right")

        self.make_label(
            self.root, f"Hello, {self.name}!", 12, MUTED
        ).pack(pady=5)

        self.make_label(
            self.root, f"QUESTION {number} OF {total}", 10, CYAN, True
        ).pack(pady=(12, 5))

        progress = ttk.Progressbar(
            self.root,
            style="Quiz.Horizontal.TProgressbar",
            maximum=total,
            value=number - 1,
            length=500
        )
        progress.pack(fill="x", padx=45, pady=(0, 20))

        card = tk.Frame(self.root, bg=PANEL, padx=25, pady=20)
        card.pack(fill="both", expand=True, padx=35, pady=(0, 20))

        self.make_label(
            card, question["question"], 17, WHITE, True, 650
        ).pack(pady=(8, 20))

        self.option_buttons = []

        for index, option in enumerate(question["options"]):
            button = tk.Button(
                card,
                text=f"{chr(65 + index)}.  {option}",
                command=lambda i=index: self.check_answer(i),
                font=("Segoe UI", 11),
                bg=BG,
                fg=WHITE,
                activebackground=PURPLE,
                activeforeground=WHITE,
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=16,
                pady=10
            )
            button.pack(fill="x", pady=4)
            self.option_buttons.append(button)

        self.feedback = self.make_label(card, "", 11, WHITE, True, 650)
        self.feedback.pack(pady=(12, 4))

        self.explanation = self.make_label(
            card, "", 10, MUTED, False, 650
        )
        self.explanation.pack(pady=3)

        self.next_button = self.make_button(
            card, "NEXT QUESTION  →", self.next_question, PURPLE
        )
        self.next_button.pack(fill="x", pady=(12, 0))
        self.next_button.pack_forget()

    def check_answer(self, selected):
        if self.answered:
            return

        self.answered = True
        question = self.questions[self.question_index]

        for button in self.option_buttons:
            button.config(state="disabled")

        correct = question["answer"]

        self.option_buttons[correct].config(
            bg=GREEN, fg=BG
        )

        if selected == correct:
            self.score += 1
            self.feedback.config(text="✓ Correct! Great job!", fg=GREEN)
        else:
            self.option_buttons[selected].config(
                bg=RED, fg=BG
            )
            self.feedback.config(
                text=f"✗ Not quite. Correct answer: {chr(65 + correct)}",
                fg=RED
            )
            self.wrong_topics.append(question["topic"])

        self.explanation.config(text=question["explanation"])

        # Update the displayed score.
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label) and child.cget("text").startswith("Score:"):
                        child.config(text=f"Score: {self.score}")

        self.next_button.pack(fill="x", pady=(12, 0))

        if self.question_index == len(self.questions) - 1:
            self.next_button.config(text="SEE MY RESULTS  →")

    def next_question(self):
        if not self.answered:
            return

        if self.question_index < len(self.questions) - 1:
            self.question_index += 1
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        self.clear_screen()

        total = len(self.questions)
        percentage = self.score / total * 100

        self.make_label(
            self.root, "🏆 QUIZ COMPLETE!", 26, CYAN, True
        ).pack(pady=(35, 10))

        self.make_label(
            self.root, f"Well done, {self.name}!", 17, WHITE, True
        ).pack(pady=5)

        self.make_label(
            self.root, f"{self.score} / {total}", 38, GREEN, True
        ).pack(pady=(15, 0))

        self.make_label(
            self.root, f"You scored {percentage:.1f}%", 14, MUTED
        ).pack(pady=5)

        if percentage == 100:
            message = "Perfect score! Outstanding work!"
        elif percentage >= 70:
            message = "Great job! Keep strengthening your skills."
        elif percentage >= 40:
            message = "Good effort. Review and try again!"
        else:
            message = "Keep practicing. Every attempt helps you grow!"

        self.make_label(
            self.root, message, 12, WHITE
        ).pack(pady=12)

        card = tk.Frame(self.root, bg=PANEL, padx=20, pady=15)
        card.pack(fill="x", padx=40, pady=10)

        self.make_label(
            card, "YOUR PERSONAL PRACTICE PLAN", 12, CYAN, True
        ).pack(pady=(0, 8))

        if self.wrong_topics:
            topics = sorted(set(self.wrong_topics))
            suggestion = "\n".join(f"• Review {topic}" for topic in topics)
        else:
            suggestion = "No weak topics found this round. Excellent!"

        self.make_label(
            card, suggestion, 11, WHITE, False
        ).pack()

        self.make_button(
            self.root, "PLAY AGAIN  ↻", self.show_home, PURPLE
        ).pack(fill="x", padx=40, pady=(12, 5))

        self.make_button(
            self.root, "EXIT", self.root.destroy, PANEL, WHITE
        ).pack(fill="x", padx=40, pady=(5, 20))


if __name__ == "__main__":
    window = tk.Tk()
    app = QuizApp(window)
    window.mainloop()



