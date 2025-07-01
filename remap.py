#!/usr/bin/env python3
import asyncio
import time
#from evdev import InputDevice, categorize, ecodes
import evdev
import subprocess
import errno
import os
# https://python-evdev.readthedocs.io/en/latest/tutorial.html
DEV_1 = '/dev/input/by-id/usb-0c45_USB_Keyboard-event-kbd'
DEV_2 = '/dev/input/by-id/usb-0c45_USB_Keyboard-event-if01'

# needed to do this in python to prevent glitch characters in terminal when using
# input-remapper-gtk


def main():
    time.sleep(1) # to prevent remap.service: Start request repeated too quickly.
    try:
        asyncio.run(async_main())
    except OSError as e:
        if e.errno == errno.ENODEV:
            print("saw no device: sleeping so service doesn't give up")
            time.sleep(1)
        else:
            raise

async def async_main():
    try:
        dev =evdev.InputDevice(DEV_1)
        dev2 = evdev.InputDevice(DEV_2)
    except FileNotFoundError as e:
        print("Failed to open device: sleeping so service doesn't give up")
        time.sleep(1)
        return

    loop = asyncio.get_event_loop()
    with dev.grab_context():
        # to stop calculator functionality.
        
        with dev2.grab_context():
    
            async def print_events(device):
                async for event in device.async_read_loop():
                    #print(device.path, evdev.categorize(event), sep=': ')
                    #print(event)
    
                    if event.type == evdev.ecodes.EV_KEY:
                        key = evdev.categorize(event)
                        if key.keystate == key.key_down:
                            print(key.keycode)
                            subprocess.Popen(f'./hotkey-map {key.keycode}', shell=True)
    


            task = asyncio.ensure_future(print_events(dev))
            task2 = asyncio.ensure_future(print_events(dev2))
            await task
            await task2
            
            #loop.run_forever()

if __name__ == "__main__":
    main()

