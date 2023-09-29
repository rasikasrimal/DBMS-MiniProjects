from tkinter import *
import time
import ttkthemes
from tkinter import ttk

count = 0
text = ''
# Function to handle slider
def slider():
    global count, text
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(60, slider)

# Function to handle login button click
def clock():
    date=time.strftime('%d:%m:%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'{date}\n{current_time}') 
    datetimeLabel.after(1000, clock)



# GUI Part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')


root.geometry('1174x680+0+0')
root.resizable(False, False)
root.title('Student Management System')

datetimeLabel = Label(root, text = 'Hello', font=('Helvetica', 20, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Management System'
sliderLabel = Label(root, font=('Helvetica', 30, 'bold'), relief=RIDGE, width = 30)
sliderLabel.place(x=200, y=0)
slider()  # Start the animation

connectButton = ttk.Button(root, text='Connect Database')
connectButton.place(x=980, y=0)

leftFrame = Frame(root, relief=RIDGE)
leftFrame.place(x=10, y=70, width=300, height=600)

logo_image = PhotoImage(file='images/student2.png')
logo_label=Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25)
addstudentButton.grid(row=1, column=0, padx=10, pady=0)

searchtudentButton = ttk.Button(leftFrame, text='Search Student', width=25)
searchtudentButton.grid(row=2, column=0, padx=10, pady=0)

deletetudentButton = ttk.Button(leftFrame, text='Delete Student', width=25)
deletetudentButton.grid(row=3, column=0, padx=10, pady=0)

updatetudentButton = ttk.Button(leftFrame, text='Update Student', width=25)
updatetudentButton.grid(row=4, column=0, padx=10, pady=0)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25)
showstudentButton.grid(row=5, column=0, padx=10, pady=0)

exportDataButton = ttk.Button(leftFrame, text='Export Data', width=25)
exportDataButton.grid(row=6, column=0, padx=10, pady=0)

exitButton = ttk.Button(leftFrame, text='Exit', width=25)
exitButton.grid(row=7, column=0, padx=10, pady=0)

rightframe = Frame(root, bg='white', relief=RIDGE)
rightframe.place(x=320, y=70, width=800, height=550)

student_table = ttk.Treeview(rightframe, columns=('ID', 'Name', 'Mobile No', 'Email', 'Address', 'Gender'
                                  'DOB', 'Added Date', 'Added Time' ))
student_table.pack(fill=BOTH, expand=1)



root.mainloop()