import socket
import time
from .gamepad import Gamepad
from .horizont import Hud
from .datalogger import DataLogger

class BaseSocket:

    HEADERSIZE = 10

    def __init__(self, host="192.168.2.107", port=3000):

        # Create the socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)

        # Start the gamepad daemon
        self.gamepad = Gamepad()
        self.gamepad.start()

        # Horizont
        self.horizont = Hud()
        self.horizont.start()

        # DataLogger
        self.dataLogger = DataLogger()
        self.dataLogger.start()

    def start(self):

        while True:
            try:
                # ==============================================
                # now our endpoint knows about the OTHER endpoint.
                clientsocket, address = self.s.accept()
                print(f"Connection from {address} has been established.")

                # For messages from client
                full_msg, new_msg = '', True
                full_msg_complete = ""

                while True:

                    # ==============================================
                    # Receive data from client, receive the data on chunks of 16
                    msg = clientsocket.recv(64)
                    full_msg += msg.decode("utf-8")

                    # Get length from header
                    if new_msg:
                        msglen = int(full_msg[:BaseSocket.HEADERSIZE])
                        new_msg = False

                    # True when message is complete
                    if len(full_msg)-BaseSocket.HEADERSIZE >= msglen:
                        # Return full message
                        full_msg_complete = full_msg[BaseSocket.HEADERSIZE:msglen+BaseSocket.HEADERSIZE].split(', ')
                        state = list(map(int, full_msg_complete[0:4])) + list(map(float, full_msg_complete[4:]))
                        # Prepare everything for next data package
                        new_msg = True
                        full_msg = full_msg[msglen+BaseSocket.HEADERSIZE:]

                        #print("In:", full_msg_complete)

                        # Update artificial horizint
                        self.horizont.state = state
                        self.horizont.update()

                    # ==============================================
                    # Send data to client
                    cmds = self.gamepad.getState()

                    print(cmds)
                    msgOut = ", ".join(list(map(str, cmds)))
                    msgOut = f"{len(msgOut):<{BaseSocket.HEADERSIZE}}"+msgOut
                    clientsocket.send(bytes(msgOut,"utf-8"))

                    # ==============================================
                    # Store to DB
                    self.dataLogger.cmds = cmds[:4]
                    self.dataLogger.motors = state[:4]
                    self.dataLogger.attitude = state[4:]
                    self.dataLogger.armed = int(cmds[4])

                    # ==============================================
                    # Sleep
                    time.sleep(0.05)

            finally:
                # Clean up the connection
                print("Closing current connection")
                clientsocket.close()
                self.gamepad.stop()
                self.dataLogger.stop()
                self.horizont.stop()