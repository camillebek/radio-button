#!/usr/bin/python3
"""
Program to start and stop playing an internet radio
using a interuptor connected to GPIO
"""

__author__ = "Camille Le Mauff"
__copyright__ = "Copyright 2018, Camillebek"
__credits__ = ["Camille Le Mauff"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Camille Le Mauff"
__email__ = "camillebek@crans.org"
__status__ = "Production"

from gpiozero import Button
import time
import os
import subprocess
import signal
import re
from datetime import datetime

# Radio url
radioUrl = 'http://direct.franceinter.fr/live/franceinter-midfi.mp3'

# Music player
player = 'omxplayer'

# Button connected bteween GPIO 13 (pin 33) and GND
button = Button(13)


def play_radio(player, radioUrl):
    """
    To play an internet radio
    """
    cmd = [player, radioUrl]
    subprocess.Popen(cmd, stdin=subprocess.PIPE)


def kill_program(programName, sig=signal.SIGTERM):
    """
    To kill a program and its children by its name
    """
    cmd = ['ps', 'a', '--noheaders']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ps_output = proc.stdout.readlines()
    p = re.compile(r'%s' % programName)
    for i in ps_output:
        nbOcc = len(p.findall(str(i)))
        if nbOcc > 0:
            for j in str(i)[2:].split(' '):
                if (j != '') and (j != "b'"):
                    print("Ending process %s" % j)
                    pid = int(j)
                    os.kill(pid, sig)
                    break


def check_button_state():
    """
    To check the state of the button and launch an action
    """
    openState = True
    while True:
        if button.is_pressed:
            # Closed circuit
            if openState is True:
                date = datetime.now()
                os.system('echo %s' % str(date))
                play_radio(player, radioUrl)
                openState = False
        else:
            # Opened circuit
            if openState is False:
                date = datetime.now()
                kill_program(player)
                openState = True
        time.sleep(0.5)


if __name__ == "__main__":
    check_button_state()
