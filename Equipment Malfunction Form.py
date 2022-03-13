from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import csv

main_screen = Tk()
main_screen.geometry("1000x750")
main_screen.title("Equipment Malfunction Form")


# help button text
def help_screen():
    mb.showinfo('Help Guide', 'Select which device you are having an issue with on the main screen. '
                              'After you select which device, please fill out the form completely and submit it.')


def opencamera():
    camera = Toplevel()
    camera.geometry('520x540')
    camera.title("Camera Form")
    camera.configure(background='grey')

    # message boxes to make sure user imputs all information
    def msg():
        if name_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your name.')
        elif enumber_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your IGC number.')
        elif number_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter the camera number.')
        elif issue_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the issue the camera is having.')
        elif date_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the date the camera started having the issue.')
        else:
            mb.showinfo('Success', 'Error report submitted successfully')

    # save to csv file
    def save():
        with open('Equipment Malfunction Log.csv', 'a') as fs:
            w = csv.writer(fs, dialect='excel-tab')
            w.writerow([name_entry.get(), enumber_entry.get(), number_entry.get(), date_entry.get(), issue_entry.get()])
            fs.close()

    def saveinfo():
        msg()
        save()

    # labels and input boxes for the users
    header_label = Label(camera, text="Camera Malfunction Form", width=25, font=("times", 20, "bold"),
                         bg='blue', fg='white')
    header_label.place(x=70, y=50)

    name_label = Label(camera, text="Full Name", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    name_label.place(x=70, y=130)
    name_entry = Entry(camera, width=30, bd=2)
    name_entry.place(x=240, y=130)

    enumber_label = Label(camera, text="Employee Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    enumber_label.place(x=70, y=180)
    enumber_entry = Entry(camera, width=30, bd=2)
    enumber_entry.place(x=240, y=180)

    number_label = Label(camera, text="Camera Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    number_label.place(x=70, y=230)
    number_entry = Entry(camera, width=30, bd=2)
    number_entry.place(x=240, y=230)

    issue_label = Label(camera, text="Issue", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    issue_label.place(x=70, y=280)
    issue_entry = Entry(camera, width=30, bd=2)
    issue_entry.place(x=240, y=280)

    date_label = Label(camera, text="Date", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    date_label.place(x=70, y=330)
    date_entry = Entry(camera, width=30, bd=2)
    date_entry.place(x=240, y=330)

    submit = Button(camera, text='Submit', command=saveinfo, width=10, bg='green', fg='white',
                    font=("times", 12, "bold"))
    submit.place(x=120, y=440)
    cancel = Button(camera, text='Cancel', command=camera.destroy, width=10, bg='maroon', fg='white',
                    font=("times", 12, "bold"))
    cancel.place(x=240, y=440)
    close = Button(camera, text='Exit', command=camera.destroy, width=10, bg='blue', fg='white',
                   font=("times", 12, "bold"))
    close.place(x=360, y=440)

    camera.mainloop()


def openmonitor():
    monitor = Toplevel()
    monitor.geometry('520x540')
    monitor.title("Monitor Form")
    monitor.configure(background='grey')

    def msg():
        if name_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your name.')
        elif enumber_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your Employee number.')
        elif number_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter the monitor number.')
        elif issue_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the issue the monitor is having.')
        elif date_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the date the monitor started having the issue.')
        else:
            mb.showinfo('Success', 'Error report submitted successfully')

    def save():
        with open('Equipment Malfunction Log.csv', 'a') as fs:
            w = csv.writer(fs, dialect='excel-tab')
            w.writerow([name_entry.get(), enumber_entry.get(), number_entry.get(), date_entry.get(), issue_entry.get()])
            fs.close()

    def saveinfo():
        save()
        msg()

    header_label = Label(monitor, text="Monitor Malfunction Form", width=25, font=("times", 20, "bold"),
                         bg='blue', fg='white')
    header_label.place(x=70, y=50)

    name_label = Label(monitor, text="Full Name", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    name_label.place(x=70, y=130)
    name_entry = Entry(monitor, width=30, bd=2)
    name_entry.place(x=240, y=130)

    enumber_label = Label(monitor, text="Employee Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    enumber_label.place(x=70, y=180)
    enumber_entry = Entry(monitor, width=30, bd=2)
    enumber_entry.place(x=240, y=180)

    number_label = Label(monitor, text="Monitor Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    number_label.place(x=70, y=230)
    number_entry = Entry(monitor, width=30, bd=2)
    number_entry.place(x=240, y=230)

    issue_label = Label(monitor, text="Issue", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    issue_label.place(x=70, y=280)
    issue_entry = Entry(monitor, width=30, bd=2)
    issue_entry.place(x=240, y=280)

    date_label = Label(monitor, text="Date", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    date_label.place(x=70, y=330)
    date_entry = Entry(monitor, width=30, bd=2)
    date_entry.place(x=240, y=330)

    submit = Button(monitor, text='Submit', command=saveinfo, width=10, bg='green', fg='white',
                    font=("times", 12, "bold"))
    submit.place(x=120, y=440)
    cancel = Button(monitor, text='Cancel', command=monitor.destroy, width=10, bg='maroon', fg='white',
                    font=("times", 12, "bold"))
    cancel.place(x=240, y=440)
    close = Button(monitor, text='Exit', command=monitor.destroy, width=10, bg='blue', fg='white',
                   font=("times", 12, "bold"))
    close.place(x=360, y=440)

    monitor.mainloop()


def openkeyboard():
    keyboard = Toplevel()
    keyboard.geometry('520x540')
    keyboard.title("Keyboard Form")
    keyboard.configure(background='grey')

    def msg():
        if name_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your name.')
        elif enumber_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter your employee number.')
        elif number_entry.index("end") == 0:
            mb.showwarning('Missing details', 'Please enter the keyboard number.')
        elif issue_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the issue the keyboard is having.')
        elif date_entry.index("end") == 0:
            mb.showinfo('Missing details', 'Please enter the date the keyboard started having the issue.')
        else:
            mb.showinfo('Success', 'Error report submitted successfully')

    def save():
        with open('Equipment Malfunction Log.csv', 'a') as fs:
            w = csv.writer(fs, dialect='excel-tab')
            w.writerow([name_entry.get(), enumber_entry.get(), number_entry.get(), date_entry.get(), issue_entry.get()])
            fs.close()

    def saveinfo():
        save()
        msg()

    header_label = Label(keyboard, text="Keyboard Malfunction Form", width=25, font=("times", 20, "bold"),
                         bg='blue', fg='white')
    header_label.place(x=70, y=50)

    name_label = Label(keyboard, text="Full Name", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    name_label.place(x=70, y=130)
    name_entry = Entry(keyboard, width=30, bd=2)
    name_entry.place(x=240, y=130)

    enumber_label = Label(keyboard, text="Employee Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    enumber_label.place(x=70, y=180)
    enumber_entry = Entry(keyboard, width=30, bd=2)
    enumber_entry.place(x=240, y=180)

    number_label = Label(keyboard, text="Keyboard Number", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    number_label.place(x=70, y=230)
    number_entry = Entry(keyboard, width=30, bd=2)
    number_entry.place(x=240, y=230)

    issue_label = Label(keyboard, text="Issue", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    issue_label.place(x=70, y=280)
    issue_entry = Entry(keyboard, width=30, bd=2)
    issue_entry.place(x=240, y=280)

    date_label = Label(keyboard, text="Date", width=20, font=("times", 12, "bold"), anchor="w", bg='grey')
    date_label.place(x=70, y=330)
    date_entry = Entry(keyboard, width=30, bd=2)
    date_entry.place(x=240, y=330)

    submit = Button(keyboard, text='Submit', command=saveinfo, width=10, bg='green', fg='white',
                    font=("times", 12, "bold"))
    submit.place(x=120, y=440)
    cancel = Button(keyboard, text='Cancel', command=keyboard.destroy, width=10, bg='maroon', fg='white',
                    font=("times", 12, "bold"))
    cancel.place(x=240, y=440)
    close = Button(keyboard, text='Exit', command=keyboard.destroy, width=10, bg='blue', fg='white',
                   font=("times", 12, "bold"))
    close.place(x=360, y=440)

    keyboard.mainloop()


# program menus
main_menu = Menu(main_screen)
main_screen.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=main_screen.quit)

help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="About", command=help_screen)
main_menu.add_cascade(label="Help", menu=help_menu)

# main screen labels
heading = Label(text="Equipment Malfunction Form", bg="blue", fg="white", width="500", height="2")
heading.pack()

select_label = Label(text="Please select the device you are having issues with below:")
select_label.pack()

camera_image = Image.open("Camera.jpg")
resize_camera = camera_image.resize((175, 175), Image.ANTIALIAS)
new_camera = ImageTk.PhotoImage(resize_camera)

monitor_image = Image.open("monitor.png")
resize_monitor = monitor_image.resize((175, 175), Image.ANTIALIAS)
new_monitor = ImageTk.PhotoImage(resize_monitor)

keyboard_image = Image.open("keyboard.jpg")
resize_keyboard = keyboard_image.resize((175, 175), Image.ANTIALIAS)
new_keyboard = ImageTk.PhotoImage(resize_keyboard)

# main screen buttons

Button(main_screen, text='Camera', image=new_camera, command=opencamera, compound=BOTTOM, width=200,
       height=200).pack()
Button(main_screen, text='Monitor', image=new_monitor, compound=BOTTOM, command=openmonitor, width=200,
       height=200).pack()
Button(main_screen, text='Keyboard', image=new_keyboard, compound=BOTTOM, command=openkeyboard, width=200,
       height=200).pack()
Button(main_screen, text='Exit', command=main_screen.destroy, width=15, bg='maroon', fg='white',
       font=("times", 12, "bold")).pack()

main_screen.mainloop()
