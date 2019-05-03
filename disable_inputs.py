import subprocess
import re
import os

TOUCHPAD_ID = "Touchpad"
KEYBOARD_ID = "AT Translated Set 2 keyboard"

def main():
    xinput_proc = subprocess.Popen(['xinput', 'list'], stdout=subprocess.PIPE)

    input_devices = xinput_proc.communicate()[0]

    for input_device in input_devices.split("\n"):
        if TOUCHPAD_ID in input_device or KEYBOARD_ID in input_device:
            disable_cmd = "xinput float " + get_id(input_device)
            print(disable_cmd)
            os.system(disable_cmd)

#TODO move into common lib
def get_id(input_str):
    match = re.search(r".*id=([0-9]+).*", input_str)
    return match.group(1)


if __name__ == "__main__":
    main()