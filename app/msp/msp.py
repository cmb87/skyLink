import serial, time, struct
from WiiProxy import MultiWii


class MSPDummy:
    def __init__(self, serialPort="/dev/ttyS0"):
        pass
    def getAttitude(self):
        return None
    def setCmds(self, cmds):
        pass

class MSP:
    # =================================
    def __init__(self, serialPort="/dev/ttyS0"):
        self.armed = False
        self.disarmed = False

        self.ser = serial.Serial()
        self.ser.port= serialPort # Port depends on your OS and interface.
        self.ser.baudrate=115200
        self.ser.bytesize=serial.EIGHTBITS
        self.ser.parity=serial.PARITY_NONE
        self.ser.stopbits=serial.STOPBITS_ONE
        self.ser.write_timeout= 3
        self.ser.xonxoff=False
        self.ser.rtscts=False
        self.ser.dsrdtr=False
        self.ser.open()
        self.multiwii = MultiWii(self.ser)

        ident = self.multiwii.get_ident()
        print(ident)
        time.sleep(5)

    # =================================
    def getAttitude(self):
        # Set state
        motors = self.multiwii.get_motors()
        attitude = self.multiwii.get_attitude()

        # [1000,1000,1000,1000,0.0,0.0,0.0]
        return list(map(str, motors[0:4])) + [str(attitude[k]) for k in ['angx', 'angy', 'heading']]

    # =================================
    def setCmds(self, cmds):
        # Set controller
        # cmds = [1000, 1000, 1000, 1000]
        self.multiwii.set_channels(cmds)

        if self.armed:
            self.multiwii.arm()
            self.armed = False

        elif self.disarmed:
            self.multiwii.disarm()
            self.disarmed = False

        time.sleep(0.05)


    # =================================
    def calibrateACC(self):
        print("Calibrating ACC")
        self.multiwii.calibrate_acc()

    # =================================
    def calibrateMAG(self):
        print("Calibrating MAG")
        self.multiwii.calibrate_mag()

