import socket
import time
import serial, time, struct
from WiiProxy import MultiWii
from .agent import Agent

# ==================================
class QuadSocket:

    HEADERSIZE = 10

    # ==================================
    def __init__(self, host='192.168.2.107', port=2234, serialPort="/dev/ttyS0"):

        self.armed = False

        # Connect to Base
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.s.connect((host, port))
                break
            except:
                print(f"Couldnt connect to {host}")
                time.sleep(2)

        # Start serial and connect to FC
        self.agent = Agent(serialPort)
        self.agent.start()

    # ==================================
    def start(self):
        while True:

            try:

                full_msg, new_msg = '', True
                full_msg_complete = ""

                while True:

                    # ==============================================
                    # Send data
                    if new_msg:
                        msgOut = ", ".join(list(map(str,self.agent.state)))

                        print(msgOut)
                        msgOut = f"{len(msgOut):<{QuadSocket.HEADERSIZE}}"+msgOut
                        self.s.send(bytes(msgOut, "utf-8"))

                    # ==============================================
                    # Receive data from server
                    msg = self.s.recv(64)
                    full_msg += msg.decode("utf-8")

                    # Get length from header
                    if new_msg:
                        msglen = int(full_msg[:QuadSocket.HEADERSIZE])
                        new_msg = False

                    # True when message is complete
                    if len(full_msg)-QuadSocket.HEADERSIZE == msglen:
                        # Get full message
                        full_msg_complete = full_msg[QuadSocket.HEADERSIZE:].split(', ')

                        # arming controller
                        if full_msg_complete[4] == '1' and not self.armed:
                            self.agent.armed = True
                            self.armed = True
                            print("Controller armed!")

                        # Disarm controller
                        elif full_msg_complete[4] == '0' and self.armed:
                            self.agent.disarmed = True
                            self.armed = False
                            print("Controller disarmed!")

                        # Set channels
                        self.agent.cmds = list(map(int,full_msg_complete[:4]))

                        # Reset for next run
                        new_msg = True
                        full_msg = ""

        
                    # ==============================================

            finally:
                print('closing socket')
                self.s.close()
                self.agent.ser.close()