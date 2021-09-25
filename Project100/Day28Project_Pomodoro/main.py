import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    def window_to_front():
        screen.lift()
        screen.attributes('-topmost', True)
        screen.after_idle(screen.attributes, '-topmost', False)

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        window_to_front()
        timer_label.config(text="Long Break", fg=RED)
        counter(long_break)

    elif reps % 2 == 0:
        window_to_front()
        timer_label.config(text="Short Break", fg=PINK)
        counter(short_break)

    else:
        timer_label.config(text="Work", fg=GREEN)
        counter(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = screen.after(1000, counter, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=pomodoro_img)
timer_count = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

screen.mainloop()
