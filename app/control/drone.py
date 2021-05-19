import time
from WiiProxy import MultiWii
from .ppm import PPM


class Drone:
    def __init__(self, ppmGPIO):
        self.ppm = PPM(gpio=ppmGPIO, frame_ms=20)

    def start(self):

        # Get control vector from sio

        x = [1000, 2000, 1000, 2000, 1000, 2000, 1000, 2000]

        self.ppm.update_channels(x)

        #
        time.sleep(0.001)

    def end(self):
        self.ppm.cancel()
