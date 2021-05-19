import logging
from datetime import datetime
import threading
import time 

from .database import Database


# ========================================
class DataLogger:
    # ========================================
    def __init__(self, loggingFrequency=50):

        # dd/mm/YY H:M:S
        #self.tablename = datetime.now().strftime("%d%m%Y%H%M%S")
        self.tablename = "mytable"
        self.columnsdict = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "time": "TEXT",
            "throttle": "INT",
            "pitch": "INT",
            "yaw": "INT",
            "roll": "INT",
            "armed": "INT",
            "engine1": "INT",
            "engine2": "INT",
            "engine3": "INT",
            "engine4": "INT",
            "angx": "FLOAT",
            "angy": "FLOAT",
            "head": "FLOAT",
        }

        #Database.delete_table(self.tablename)

        print(f"Creating table {self.tablename}")
        Database.create_table(self.tablename, self.columnsdict)

        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.stopThread = False

        self.cmds = [1000, 1000, 1000, 1000]
        self.motors = [1000, 1000, 1000, 1000]
        self.attitude = [0.0, 0.0, 0.0]
        self.armed = 0

        self.dt = (1.0/loggingFrequency)

    # ========================================
    def _run(self):

        while not self.stopThread:
            t = time.time()

            Database.insert(
                self.tablename, [{
                    "time": str(t), "throttle": self.cmds[3], "pitch": self.cmds[1],
                    "roll": self.cmds[0], "yaw": self.cmds[2], "armed": self.armed, 
                    "engine1": self.motors[0],"engine2": self.motors[1], "engine3": self.motors[2], 
                    "engine4": self.motors[3], "angx": self.attitude[0], 
                    "angy": self.attitude[1], "head": self.attitude[2]
                }])
            time.sleep(self.dt)

    # ========================================
    def start(self):
        self.thread.start()

    # ========================================
    def stop(self):
        self.stopThread = False
