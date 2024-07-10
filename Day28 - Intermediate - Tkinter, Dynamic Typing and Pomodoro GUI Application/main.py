from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#5AB2FF"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        timer(long_break_sec)

    elif REPS % 2 == 0:
        timer_label.config(text="Short Break", fg=BLUE)
        timer(short_break_sec)

    else:
        timer_label.config(text="Working Time", fg=GREEN)
        timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count):
    timer_min = math.floor(count / 60)
    timer_sec = count % 60

    if timer_sec == 0:
        timer_sec = "00"
    elif timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, timer, count - 1)
    else:
        start()
        checkmarks = ""
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            checkmarks += "✅"
        tick_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro Technique")
window.config(padx=120, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

start_btn = Button(text="Start", command=start)
start_btn.grid(row=2, column=0)

tick_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"))
tick_label.grid(row=2, column=1)

restart_btn = Button(text="Reset", command=reset_timer)
restart_btn.grid(row=2, column=2)

window.mainloop()
