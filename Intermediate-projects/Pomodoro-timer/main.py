from tkinter import *
import math
########################################
# Improvements Needed/ideas
# Start button shouldn't be pushable twice, creates bug
# Window should pop or sound played when timer finishes
# Background image and color theme can be changed
# After work period completes, check marks should reset
# Show different images during work, break and long break
# After all fixes, make it an executable
#########################################

# Constants and global variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# If user presses reset-button, reset timer text, timer label, checkmarks, and cancel the timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00.00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")


# Timer gets triggered when start button is pressed, and we pass in the time we want to count down from
# in this function
def start_timer():
    global reps
    reps += 1

    # Calculates minutes to seconds
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If repetition is on 2,4,6 should be short break, if on 8th long break, and uneven numbers are for working time
    if reps % 2 == 0 and reps != 8:
        count_down(break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# When countdown is initiated the function will call upon itself (loop) until count is 0.
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Example of dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Sets clock layout
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        if reps % 2 == 0:
            marks += "✔"
        checkmark_label.config(text=marks)

# Create window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_background)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Buttons
start_button = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)


# Event driven mainloop.
window.mainloop()