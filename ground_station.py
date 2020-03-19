from serial_reader import SerialReader
from tkinter import *

# tkinter program used to create an interactive interface that displays data from the rocket and sends commands
# to the rocket. Uses SerialReader object to interact with the arduino on the rocket.
#
# @author Ethan Visscher


# this method is needed in order to update the tkinter values (from the SerialReader object)
# after the tkinter mainloop executes and to save the data
def update_data(gui_root):
    if data.reading_data:
        data.get_data()
        # data.save_data()
    gui_root.after(100, lambda: update_data(gui_root))   # calls itself after main_loop every 100 milliseconds


# method used with the data_read_btn to start and stop data reading from the serial reader
def data_read_command():
    if not data.reading_data:
        data.start_reading()
        data.data_read_text.set('STOP')
    else:
        data.stop_reading()
        data.data_read_text.set('START')


# method used with the camera_btn to start and stop reading from the serial reader
def camera_command():
    if not data.camera_recording:
        data.start_camera()
        data.camera_text.set('STOP')
    else:
        data.stop_camera()
        data.camera_text.set('START')


root = Tk()
root.attributes('-fullscreen', True)

data = SerialReader()

frame = Frame(root, width=1920, height=1080)
frame.pack()

# place the background image
background_image = PhotoImage(file='background_image.png')
background_image_label = Label(frame, image=background_image)
background_image_label.place(x=0, y=0, relwidth=1, relheight=1)

# place all of the text
alt_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.alt, font=('Major Mono Display', 30), justify=CENTER)
alt_label.place(relx=.465, rely=.195, anchor='center')

speed_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.speed, font=('Major Mono Display', 30))
speed_label.place(relx=.818, rely=.538, anchor='center')

gforce_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.gforce, font=('Major Mono Display', 30))
gforce_label.place(relx=.818, rely=.195, anchor='center')

bat_temp_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.bat_temp, font=('Major Mono Display', 30))
bat_temp_label.place(relx=.146, rely=.31, anchor='center')

cube_temp_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.cube_temp, font=('Major Mono Display', 30))
cube_temp_label.place(relx=.146, rely=.58, anchor='center')

motor_temp_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.motor_temp, font=('Major Mono Display', 30))
motor_temp_label.place(relx=.146, rely=.81, anchor='center')

pressure_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.pressure, font=('Major Mono Display', 30))
pressure_label.place(relx=.465, rely=.538, anchor='center')

lat_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.lat, font=('Major Mono Display', 18))
lat_label.place(relx=.395, rely=.85, anchor='center')

long_label = Label(frame, fg='#000000', bg='#ffffff', textvariable=data.long, font=('Major Mono Display', 18))
long_label.place(relx=.505, rely=.85, anchor='center')

# button command parameter has to be lambda or else the command will trigger when the program launches
data_read_btn = Button(frame, textvariable=data.data_read_text, command=lambda: data_read_command())
data_read_btn.place(relx=.7275, rely=.8775, anchor='center')

camera_btn = Button(frame, textvariable=data.camera_text, command=lambda: camera_command())
camera_btn.place(relx=.86, rely=.8775, anchor='center')


update_data(root)
root.mainloop()
