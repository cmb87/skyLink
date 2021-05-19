import os
import logging

_loggingLevels = {
    "INFO": logging.INFO, "DEBUG": logging.DEBUG,
    "CRITICAL": logging.CRITICAL, "ERROR": logging.ERROR,
}

drone = {
    "ppmgpio": int(os.getenv('PPMGPIO', '26')), # Pin 37 on PiZero
    "mspserialdev" : os.getenv('SERIALMSPDEV', "/dev/ttyS0"),
}


analytic = {
    "flip": os.getenv('INFERENCEFLIP', '0'),
    "send_width": int(os.getenv('SENDWIDTH', '150')),
    "send_height": int(os.getenv('SENDHEIGHT', '150')),
    "source": int(os.getenv('CAMERADEV', '2')),
    "sleeptime": float(os.getenv('INFERENCESLEEPTIME', '0.05')),
    "graysend": os.getenv('INFERENCEGRAY', '1'),
}

server = {
    "appname": os.getenv('ENV_APPNAME', 'joystick'),
    "logginglevel": _loggingLevels[os.getenv('LOGGING', 'INFO').upper()],
    "hostname": os.getenv('ENV_SOCKETIOSERVER', 'localhost'),
    "port": int(os.getenv('ENV_SOCKETIOPORT', 5000)),
    "namespace": os.getenv('ENV_NAMESPACE', "/control"),
}