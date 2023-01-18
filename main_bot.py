import pywhatkit 
import keyboard
import time
from datetime import datetime

contato = ['+5567991799956']

while len(contato) >= 1:
    # Send a WhatsApp Message to a Contact at 1:30 PM
    pywhatkit.sendwhatmsg(contato[0], "um teste ae", datetime.now().hour, datetime.now().minute + 1)
    del contato[0]
    time.sleep(1)
    keyboard.press_and_release('ctrl + w')