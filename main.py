import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_BLUE = "#C0EEE4"
LIGHT_PINK = "#FFCAC8"
DARK_PINK = "#CB1C8D"
YELLOW = "#F8F988"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    win.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_click():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text='Break', fg=DARK_PINK)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_label.config(text='Break', fg=DARK_PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work', fg='blue')
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    counter_text = f'{count_min}:{count_sec}'
    canvas.itemconfig(timer_text, text=counter_text)
    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        if REPS <= 8:
            marks = ''
            for _ in range(int(REPS / 2)):
                marks += checkmark_template
                checkmark_label.config(text=marks)
            start_click()


# ---------------------------- UI SETUP ------------------------------- #
# Window
win = tk.Tk()
win.title("Pomodoro")
win.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Labels
# Timer label
timer_label = tk.Label(text='Timer', bg=YELLOW, fg=DARK_PINK, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(column=1, row=0)
# Counter label
checkmark_template = '✔'
checkmark_label = tk.Label(bg=YELLOW, fg='green', font=('Arial', 12, 'bold'))
checkmark_label.grid(column=1, row=3)

# Buttons
# Start Button
start_button = tk.Button(text='Start', width=10, highlightthickness=0, command=start_click)
start_button.grid(column=0, row=2)
# Reset Button
reset_button = tk.Button(text='Reset', width=10, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Timer code


win.mainloop()
