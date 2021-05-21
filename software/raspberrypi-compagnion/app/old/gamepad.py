"""Simple example showing how to get gamepad events."""

from __future__ import print_function
from inputs import get_gamepad
import numpy as np
import time
import threading
import logging
from queue import Queue, Empty
# https://www.troyfawkes.com/learn-python-multithreading-queues-basics/

class Gamepad:

    # =================================
    QUADCONT = {
        "ABS_Z": {"lb":0, "ub":255, "iv":0, "lbm":1150, "ubm":2000, "description":"throttle"},
        "ABS_X": {"lb":-32768, "ub":32767, "iv":0, "lbm":1000, "ubm":2000, "description":"roll"},
        "ABS_Y": {"lb":-32768, "ub":32767, "iv":0, "lbm":1000, "ubm":2000, "description":"pitch"},
        "ABS_RX": {"lb":-32768, "ub":32767, "iv":0, "lbm":1000, "ubm":2000, "description":"yaw"},
        "BTN_SOUTH": {"lb":0, "ub":1, "iv":0, "lbm":0, "ubm":1, "description":"arm"},
        "BTN_EAST": {"lb":0, "ub":1, "iv":0, "lbm":0, "ubm":1, "description":"disarm"},
    }

    # =================================
    def __init__(self):

        self.state = {
            "throttle":Gamepad.QUADCONT["ABS_Z"]["lbm"],
            "pitch":1500,
            "roll":1500,
            "yaw":1500,
            "armed": 0,
            "acc_cal": 0,
            "mag_cal": 0
        }
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.stopThread = False
        #self.queue = Queue()

    # =================================
    def _run(self):
        """Just print out some event infomation when the gamepad is used."""

        while not self.stopThread:

            self.state["acc_cal"] = 0
            self.state["mag_cal"] = 0
            events = get_gamepad()

            for event in events:

                if event.code in ["ABS_X", "ABS_Y", "ABS_Z", "ABS_RX"]:

                    val = int(np.interp(
                        event.state,
                        [Gamepad.QUADCONT[event.code]['lb'],
                         Gamepad.QUADCONT[event.code]['ub']],
                        [Gamepad.QUADCONT[event.code]['lbm'],
                        Gamepad.QUADCONT[event.code]['ubm']]
                    ))

                    self.state[Gamepad.QUADCONT[event.code]['description']] = val

                if event.code in ["BTN_SOUTH"] and self.state["armed"] == 0:
                    self.state["armed"] = 1
                    print("Drone armed")

                elif event.code in ["BTN_EAST"] and self.state["armed"] == 1:
                    self.state["armed"] = 0
                    print("Drone disarmed")

                elif event.code in ["BTN_NORTH"]:
                    self.state["acc_cal"] = 1
                    print("Calibrating ACC")

                elif event.code in ["BTN_WEST"]:
                    self.state["mag_cal"] = 1
                    print("Calibrating MAG")


    # =================================
    def start(self):
        self.thread.start()

    # =================================
    def stop(self):
        self.stopThread = True

    # =================================
    def getState(self):
        # Order according to multiwii python module
        return [self.state[k] for k in ["roll", "pitch", "yaw", "throttle", "armed", "acc_cal", "mag_cal"]]
        
        # Order in multiwii config.h
        #return ", ".join([str(val[k]) for k in ["throttle", "yaw", "roll", "pitch", "armed"]])

if __name__ == "__main__":
    cont = Gamepad()
    cont.start()

    while True:
        #print(threading.enumerate(), cont.thread.isAlive())
        print(cont.getState())
        time.sleep(0.01)

