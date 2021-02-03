import tkinter as tk
#import mp3play

# Pomodoro Timer
def timer(count):
    timer_label['text'] = count
    if count > 0:
        app.after(1000, timer, count-1)

#Key down function
def click():
    entered_time = time_input.get()
    start = timer(int(entered_time))
    #start_sound = mp3play.load('PopSoundEffect.mp3'); play = lambda: f.play()

#Window
app = tk.Tk()
app.title("PomoTasks")
app.configure(background="#769fcd")
app.geometry("600x700")

#Labels
timer_label = tk.Label(app,bg="#769fcd", font="none 12 bold", fg="#f7fbfc")
timer_label.grid(row=0,column=0)

#Text box
time_input = tk.Entry(app, width=20, bg="#d6e6f2")
time_input.grid(row=1, column=0)

#Button
timer_button = tk.Button(app, text="START", width=6, command=click) .grid(row=3,column=0)

#Run the app
app.mainloop()
