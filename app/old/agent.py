import socket
import time
import serial, time, struct
from WiiProxy import MultiWii
import threading

class Agent:
    # =================================
    def __init__(self, serialPort):

        self.armed = False
        self.disarmed = False

        self.cmds = [1000,1000,1000,1000]
        self.state = [1000,1000,1000,1000,0.0,0.0,0.0]

        self.ser = serial.Serial()
        self.ser.port= serialPort # Port depends on your OS and interface.
        self.ser.baudrate= 115200
        self.ser.bytesize= serial.EIGHTBITS
        self.ser.parity= serial.PARITY_NONE
        self.ser.stopbits= serial.STOPBITS_ONE
        self.ser.write_timeout= 3
        self.ser.xonxoff= False
        self.ser.rtscts= False
        self.ser.dsrdtr= False
        self.ser.open()
        self.multiwii = MultiWii(self.ser)

        ident = self.multiwii.get_ident()
        print(ident)

        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.stopThread = False

    # =================================
    def calibrateACC(self):
        print("Calibrating ACC")
        self.multiwii.calibrate_acc()
        
    # =================================
    def calibrateMAG(self):
        print("Calibrating MAG")
        self.multiwii.calibrate_mag()
        
    # =================================
    def _run(self):

        while not self.stopThread:
            # Set state
            motors = self.multiwii.get_motors()
            attitude = self.multiwii.get_attitude()
            self.state = list(map(str, motors[0:4])) + [str(attitude[k]) for k in ['angx', 'angy', 'heading']]
            #print("state", self.state)

            # Set controller
            #print("set channels:", self.cmds)
            self.multiwii.set_channels(self.cmds)

            if self.armed:
                self.multiwii.arm()
                self.armed = False
            elif self.disarmed:
                self.multiwii.disarm()
                self.disarmed = False

            time.sleep(0.05)

    # =================================
    def start(self):
        self.thread.start()

    # =================================
    def stop(self):
        self.stopThread = True