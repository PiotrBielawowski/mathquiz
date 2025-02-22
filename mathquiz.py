import customtkinter as ctk
import random
import time
from PIL import Image
# GUI
window = ctk.CTk()
window.title("Simple Math Exercises")
window.geometry("600x400")

# Appearance
ctk.set_appearance_mode("system")
#image = Image.open("mathquiz/backgroundmathquiz.png")
#background_image = ctk.CTkImage(image, size=(600, 400))

# Variables
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
operators = ["+", "-", "*"]
score_value = 0

    

# Functions
def generate_exercise():
    global number, number2, operator, correct_answer
    number = random.choice(numbers)
    number2 = random.choice(numbers)
    operator = random.choice(operators)

    if operator == "+":
        correct_answer = number + number2
    elif operator == "-":
        correct_answer = number - number2
    elif operator == "*":
        correct_answer = number * number2
 

    math_label.configure(text=f"{number} {operator} {number2}")


def check():
    global score_value
    try:
        user_input = float(entry.get())
        if round(user_input, 2) == round(correct_answer, 2):
            result_label.configure(text="✅ Correct!", text_color="green")
            score_value += 1
            score_label.configure(text=f"Score: {score_value}", text_color="green")
        else:
            result_label.configure(text=f"❌ Wrong! Correct: {round(correct_answer, 2)}", text_color="red")
            score_value -= 1
            score_label.configure(text=f"Score: {score_value}", text_color="red")
    except ValueError:
        result_label.configure(text="⚠️ Please enter a number!", text_color="orange")

    entry.delete(0, 'end')  
    generate_exercise()     


# Widgets
label = ctk.CTkLabel(window, text="Simple Math Exercises", fg_color='transparent', font=("Arial", 24))
label.pack(pady=10)


math_label = ctk.CTkLabel(window, text="", fg_color='transparent', font=("Arial", 24))
math_label.pack(pady=10)

entry = ctk.CTkEntry(window, width=200, font=("Arial", 16))
entry.pack(pady=10)

button = ctk.CTkButton(window, text="Check", fg_color='blue', font=("Arial", 16), command=check)
button.pack(pady=10)

result_label = ctk.CTkLabel(window, text="", fg_color='transparent', font=("Arial", 18))
result_label.pack(pady=10)

score_label = ctk.CTkLabel(window, text=f"Score: {score_value}", fg_color='transparent', font=("Arial", 18))
score_label.pack(pady=10)

# Initialize the first exercise
generate_exercise()

# Run
window.mainloop()
