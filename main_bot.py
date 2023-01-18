import pywhatkit 
import keyboard
import time
from datetime import datetime

contato = ['+5567991799956']

while len(contato) >= 1:
    # Send a WhatsApp Message to a Contact 
    pywhatkit.sendwhats_image(contato[0],'1662693303800 (1).jpg', "um teste ae", datetime.now().hour, datetime.now().minute + 1)
    del contato[0]
    time.sleep(5)
    keyboard.press_and_release('ctrl + w')