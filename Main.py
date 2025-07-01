# NOTE: This script requires a local Python environment with tkinter support.
# It will not work in environments where tkinter is unavailable (like some online IDEs).

try:
    import tkinter as tk
    from tkinter import messagebox
    from collections import Counter

    # --- Hack Functions ---
    def swap_numbers():
        a, b = 5, 10
        a, b = b, a
        messagebox.showinfo("Swap Result", f"After swap: a = {a}, b = {b}")

    def generate_squares():
        squares = [x**2 for x in range(6)]
        messagebox.showinfo("Squares", str(squares))

    def count_words():
        text = "python is simple and python is powerful"
        counts = Counter(text.split())
        messagebox.showinfo("Word Count", str(counts))

    def check_palindrome():
        word = "madam"
        result = word == word[::-1]
        messagebox.showinfo("Palindrome", f"Is '{word}' a palindrome? {result}")

    def lambda_sort():
        students = [("Kabilan", 85), ("Arjun", 90), ("Meena", 78)]
        students.sort(key=lambda x: x[1], reverse=True)
        messagebox.showinfo("Sorted Students", str(students))

    def zip_combine():
        names = ["Kabilan", "Arjun"]
        scores = [85, 90]
        combined = list(zip(names, scores))
        messagebox.showinfo("Zipped List", str(combined))

    def show_enumerate():
        langs = ["Python", "Java", "C++"]
        result = "\n".join([f"{i}: {v}" for i, v in enumerate(langs)])
        messagebox.showinfo("Enumerate", result)

    # --- GUI Setup ---
    root = tk.Tk()
    root.title("Python Hacks Toolkit")
    root.geometry("400x400")
    root.config(bg="#f0f0f0")

    btn_style = {"padx": 10, "pady": 5, "width": 30, "bg": "#4CAF50", "fg": "white"}

    tk.Label(root, text="Select a Python Hack", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

    btn1 = tk.Button(root, text="Swap Variables", command=swap_numbers, **btn_style)
    btn2 = tk.Button(root, text="Generate Squares", command=generate_squares, **btn_style)
    btn3 = tk.Button(root, text="Count Word Frequency", command=count_words, **btn_style)
    btn4 = tk.Button(root, text="Check Palindrome", command=check_palindrome, **btn_style)
    btn5 = tk.Button(root, text="Lambda Sort Students", command=lambda_sort, **btn_style)
    btn6 = tk.Button(root, text="Zip Names & Scores", command=zip_combine, **btn_style)
    btn7 = tk.Button(root, text="Show with Enumerate", command=show_enumerate, **btn_style)

    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7]:
        btn.pack(pady=5)

    root.mainloop()

except ModuleNotFoundError as e:
    print("Error: tkinter is not available in this environment. Please run this script in a local Python installation with GUI support.")
