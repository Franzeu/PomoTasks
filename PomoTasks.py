from tkinter import *
from tkinter import messagebox
from tkinter import font
from playsound import playsound
import time

#Main Window
window = Tk()
window.title("PomoTasks")
window.configure(background="#b9d7ea")
window.geometry("600x650")

#Logo
logo = PhotoImage(file="Assets\logo.png")
logo_label = Label(window,image=logo)
logo_label.place(x= 150, y = 20)

## Pomodoro Timer

#Variables
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("0")
minute.set("25")
second.set("0")

#Text Boxes
hourTextBox = Entry(window, width = 2, font = ("open sans",25, "bold"),bg="#d6e6f2",fg="#3f72af", textvariable = hour)
hourTextBox.place(x = 200, y = 125)
minuteTextBox = Entry(window, width = 2, font = ("open sans",25, "bold"),bg="#d6e6f2",fg="#3f72af", textvariable = minute)
minuteTextBox.place(x = 275, y = 125)
secondTextBox = Entry(window, width = 2, font = ("open sans",25, "bold"),bg="#d6e6f2",fg="#3f72af", textvariable = second)
secondTextBox.place(x = 350, y = 125)

def timer():
    playsound('Assets\PopSoundEffect.wav')
    try:
        #convert stores the input provided by the user
        convert = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        #If the user inputs an invalid or unknown value, it shows an error
        messagebox.showinfo("PomoTasks", "Error: Invalid value")

    temp_mins, temp_secs = divmod(convert,60)
    temp_hours = 0

    if (temp_mins > 60):
        #if mins is greater than 60, we use divmod again to obtain the amount of hours and store it into variable hours and 
        #then the remainder is stored into mins (minutes)
        temp_hours, temp_mins = divmod(temp_mins, 60)

    #Updates every 1 second
    while (convert > -1):
        #mins sores the first value (minutes) after divmod is used, and the remainder is stored in secs (seconds)
        mins, secs = divmod(convert,60)
        hours = 0

        if (mins > 60):
            #if mins is greater than 60, we use divmod again to obtain the amount of hours and store it into variable hours and 
            #then the remainder is stored into mins (minutes)
            hours, mins = divmod(mins, 60)

        if (temp_mins > 5 and temp_hours > 1) or temp_mins > 5:
        #We use format in order to store the values up to two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            #Everytime window gets updated every second through the use of time 
            window.update()
            time.sleep(1)

            #Once the timer reaches 0, a messagebox appears for the user to know that the time is up
            if (convert == 0):
                messagebox.showinfo("PomoTasks", "Time's Up! Break Time!")
                minute.set("5")

            #Decrements every 1 second
            convert -= 1
        elif temp_mins <= 5 and temp_hours < 1:
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            #Everytime window gets updated every second through the use of time 
            window.update()
            time.sleep(1)

            #Once the timer reaches 0, a messagebox appears for the user to know that the time is up
            if (convert == 0):
                playsound('Assets\SuccessSoundEffect.wav')
                messagebox.showinfo("PomoTasks", "Break time is over! ")
                minute.set("25")
            #Decrements every 1 second
            convert -= 1

#Button
btn = Button(window, text='Start', bd='5', width='10',bg="#d6e6f2",command= timer)
btn.place(x = 252,y = 189)

number = 1
# Add function
def add_button():
    global number
    entered_text = add_input.get() #this will collect the text from the text entry box
    task = list_of_tasks[number]=[entered_text]
    tasks.insert(END, str(number) + ' : ' + str(task) + '\n')
    number += 1

# Delete function
def delete_button():
    entered_text = int(delete_input.get())
    list_of_tasks.pop(entered_text, None)
    tasks.delete('1.0', END)
    for key in list_of_tasks:
        tasks.insert(END, str(key) + ' : ' + str(list_of_tasks[key]) + '\n')

##To Do list - Labels and Text/Text Boxes
tasks_label = Label(window, text='Tasks',bg="#d6e6f2",fg="#3f72af", font=("source sans pro", 15,"bold"))
tasks_label.place(x = 268, y = 270)
# Add labels & Text
add_label = Label(window, text='Add a task',bg="#d6e6f2",fg="#3f72af", font=("source sans pro", 12,"bold"))
add_label.place(x = 35, y = 330)

add_input = Entry(window, width = 58, bg ="#d6e6f2",fg="#3f72af",font=("source sans pro", 11,"bold"))
add_input.place(x = 35, y = 360)

Button(window, text="Add", width = 6, bg="#d6e6f2", command = add_button) .place (x = 515, y = 358)

tasks = Text(window, width = 59, height = 6, wrap = WORD, background = "#d6e6f2",fg="#3f72af", font=("source sans pro", 13,"bold"))
tasks.place(x=35, y = 400)

# Delete labels & Text
delete_label = Label(window, text='Delete a task',bg="#d6e6f2",fg="#3f72af", font=("source sans pro", 12,"bold"))
delete_label.place(x = 35, y = 555)

delete_input = Entry(window, width = 58, bg ="#d6e6f2",fg="#3f72af",font=("source sans pro", 11,"bold"))
delete_input.place(x = 35, y = 585)

Button(window, text="Delete", width = 6, bg="#d6e6f2", command = delete_button) .place (x = 515, y = 583)

#Dictionary 
list_of_tasks = {}

#Run Main Loop
window.mainloop()