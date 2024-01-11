#!/usr/bin/env python3
import asyncio
import time
#from evdev import InputDevice, categorize, ecodes
import evdev
import subprocess
# https://python-evdev.readthedocs.io/en/latest/tutorial.html

dev =evdev.InputDevice('/dev/input/by-id/usb-0c45_USB_Keyboard-event-kbd')
dev2 = evdev.InputDevice('/dev/input/by-id/usb-0c45_USB_Keyboard-event-if01')

# needed to do this in python to prevent glitch characters in terminal when using
# input-remapper-gtk

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
                        subprocess.Popen(f'hotkey-map {key.keycode}', shell=True)

        
        for device in dev, dev2:
            asyncio.ensure_future(print_events(device))
        
        loop = asyncio.get_event_loop()
        loop.run_forever()
