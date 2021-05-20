
"""Simple example showing how to get gamepad events."""
import time
import logging
import socketio
import config
import pigpio

from camera.camera import Camera

# =============================================
# Set logging formats
logging.basicConfig(
    level=config.server["logginglevel"],
    format=("[%(filename)8s] [%(levelname)4s] :  %(funcName)s - %(message)s"),
)

# standard Python
sio = socketio.Client()

# Start pigpio
pi = pigpio.pi()

# Start camera
cam = Camera()

# =============================================
def getData():

    # Get camera frame
    try:
        frameBase64, _, _ = next(cam.processFrame())
    except:
        logging.error("Couldnt send frame")
        frameBase64 = ""
        pass

    return frameBase64, ""

# =============================================
@sio.on('sendNextData')
def sendData(msg):

    frameBase64, attitude = getData()

    print("message received")

    # Tansmit data
    sio.emit('inferenceresults', {
        'frame': frameBase64,
        'attitude': attitude,
        }, namespace=config.server["namespace"]
    )
    time.sleep(config.analytic["sleeptime"])


# =============================================
@sio.on('control')
def setControl(msg):
    pi.set_servo_pulsewidth(config.drone["pwmpin1"], int(msg[0]))
    pi.set_servo_pulsewidth(config.drone["pwmpin2"], int(msg[1]))
    pi.set_servo_pulsewidth(config.drone["pwmpin3"], int(msg[2]))
    pi.set_servo_pulsewidth(config.drone["pwmpin4"], int(msg[3]))
    pi.set_servo_pulsewidth(config.drone["pwmpin5"], int(msg[4]))
    pi.set_servo_pulsewidth(config.drone["pwmpin6"], int(msg[5]))
    pi.set_servo_pulsewidth(config.drone["pwmpin7"], int(msg[6]))
    pi.set_servo_pulsewidth(config.drone["pwmpin8"], int(msg[7]))

# =============================================
@sio.on('toggleled')
def setControl(msg):
    print("System armed")

# =============================================
@sio.event
def connect():
    logging.info('Successfully connected to server.')

# =============================================
@sio.event
def connect_error():
    logging.info('Failed to connect to server.')

# =============================================
@sio.event
def disconnect():
    logging.info('Disconnected from server.')


def main():
    while True:
        try:
            sio.connect(f"ws://{config.server['hostname']}:{config.server['port']}", namespaces=[config.server['namespace']])
            logging.info(f"Connected to ws://{config.server['hostname']}:{config.server['port']} under the namespace {config.server['namespace']}")
            break
        except:
            logging.warning(f"Could not connect to server ws://{config.server['hostname']}:{config.server['port']}")
            time.sleep(4)

    logging.info("Starting infinity loop")
    print("Server Online")

    # Start data Tansmission
    sio.emit('starttransmission', "start", namespace=config.server["namespace"])


if __name__ == "__main__":
    main()