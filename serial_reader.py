import serial
from tkinter import *
import time

# this class is used to read rocket data from an arduino and store it in arrays and tkinter values in order
# to be displayed in a gui. Used also to write rocket data to a txt file and to send commands to the arduino
#
# @author Ethan Visscher


class SerialReader:

    def __init__(self):
        self.ser = None                             # used to communicate with the arduino
        self.pings = 0                               # times the rocket has been pinged for data
        self.flight_time = 0.0

        self.reading_data = False
        self.camera_recording = False

        self.data_read_text = StringVar()   # text to be displayed on the data_read_btn
        self.camera_text = StringVar()      # text to be displayed on the camera_btn
        self.data_read_text.set('START')
        self.camera_text.set('START')

        # 0 = altitude
        # 1 = speed             # 2 = g-force       # 3 = battery Temp
        # 4 = cubesat temp      # 5 = motor Temp    # 6 = pressure
        # 7 = latitude          # 8 = longitude     # 9 pings
        self.instant_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]     # shows the instant values of the rocket
        self.max_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]         # shows the maximum values of the rocket

        # tkinter variables used so they can update real time in the gui
        self.alt = DoubleVar()
        self.speed = DoubleVar()
        self.gforce = DoubleVar()
        self.bat_temp = DoubleVar()
        self.cube_temp = DoubleVar()
        self.motor_temp = DoubleVar()
        self.pressure = DoubleVar()
        self.lat = DoubleVar()
        self.long = DoubleVar()

    # method used to get serial data from the Arduino,
    # decode the data, and put it into arrays and tkinter variables
    def get_data(self):
        try:                                                    # use try statement bc sometime she like to fail
            str_data = self.ser.readline().decode().rstrip()    # decode the serial data from the Arduino
            self.instant_data = str_data.split(';')             # put the decoded data in array
        except UnicodeDecodeError:
            print('Failed connecting')

        # update the maximum's array
        for i in range(0, len(self.instant_data)):
            if self.instant_data[i] > self.max_data[i]:
                self.max_data[i] = self.instant_data[i]

        self.pings = self.instant_data[9]

        # update the tkinter variables
        self.alt.set(self.instant_data[0])
        self.speed.set(self.instant_data[1])
        self.gforce.set(self.instant_data[2])
        self.bat_temp.set(self.instant_data[3])
        self.cube_temp.set(self.instant_data[4])
        self.motor_temp.set(self.instant_data[5])
        self.pressure.set(self.instant_data[6])
        self.lat.set(self.instant_data[7])
        self.long.set(self.instant_data[8])

    # method used to save the rocket's data to txt files
    def save_data(self):
        with open('end_data.txt', 'w') as f:
            f.write(f'Flight Time: {self.flight_time}\n'
                    f'Pings: {self.pings}\n\n'
                    f'Maximum Altitude: {self.max_data[0]}\n'
                    f'Maximum Speed: {self.max_data[1]}\n'
                    f'Maximum G-force: {self.max_data[2]}\n'
                    f'Maximum Battery Temperature: {self.max_data[3]}\n'
                    f'Maximum Cubesat Temperature: {self.max_data[4]}\n'
                    f'Maximum Motor Temperature: {self.max_data[5]}\n'
                    f'Maximum Pressure: {self.max_data[6]}\n\n'
                    f'Last Known Latitude Coord: {self.instant_data[7]}\n'
                    f'Last Known Longitude Coord: {self.instant_data[8]}')
            f.close()

    # starts reading the serial data
    def start_reading(self):
        if self.ser is None:
            self.ser = serial.Serial('COM4', 9600)  # Establish serial connection if not done so yet
        self.reading_data = True

    # stops reading the serial data
    def stop_reading(self):
        self.reading_data = False

    # starts the camera
    def start_camera(self):
        if self.ser is None:
            self.ser = serial.Serial('COM4', 9600)  # Establish serial connection if not done so yet
        self.camera_recording = True
        self.ser.write(1)
        time.sleep(.2)

    # stops the camera
    def stop_camera(self):
        self.camera_recording = False
        self.ser.write(0)
        time.sleep(.2)
