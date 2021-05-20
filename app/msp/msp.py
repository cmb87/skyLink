from serial import Serial
from WiiProxy import MultiWii, Commands, Priority
from time   import sleep, time

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

        self.serial = Serial(serialPort, 115200)

        time.sleep(6)

        Commands.seed()
        self.fc = MultiWii(self.serial)
        self.fc.start()

        ident       = self.fc.data[Commands.IDENT]

        print("IDENT                                ")
        print("-------------------------------------")
        print(f"version       = {ident.version}     ")
        print( "multitype     = %s" % ident.multitype)
        print(f"capabilities  = {ident.capabilities}")
        print(f"navi_version  = {ident.navi_version}")


    # =================================
    def getAttitude(self):
        # Set state
        ident = self.fc.data[Commands.IDENT]
        status = self.fc.data[Commands.STATUS]
        rc = self.fc.data[Commands.RC]
        imu = self.fc.data[Commands.RAW_IMU]
        attitude = self.fc.data[Commands.ATTITUDE]

        return [attitude.angle, attitude.heading]



