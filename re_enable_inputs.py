import subprocess
import re
import os

TOUCHPAD_ID = "Touchpad"
KEYBOARD_ID = "AT Translated Set 2 keyboard"

POINTER_INPUT = 2
KEY_INPUT = 3

def main():
    xinput_proc = subprocess.Popen(['xinput', 'list'], stdout=subprocess.PIPE)

    input_devices = xinput_proc.communicate()[0]

    for input_device in input_devices.split("\n"):
        enable_cmd = "xinput reattach "
        ship_it = False
        if TOUCHPAD_ID in input_device:
            enable_cmd = enable_cmd + get_id(input_device) + " " + str(POINTER_INPUT)
            ship_it = True
        elif KEYBOARD_ID in input_device:
            enable_cmd = enable_cmd + get_id(input_device) + " " + str(KEY_INPUT)
            ship_it = True
            
        if (ship_it):
            os.system(enable_cmd)
        

def get_id(input_str):
    match = re.search(r".*id=([0-9]+).*", input_str)
    return match.group(1)


if __name__ == "__main__":
    main()