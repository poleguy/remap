# remap.py

"Merry Christmas Damian."

This little script is a bit hacky, but it works nicely.

## Prerequisites:

you'll need python3 installed.

To talk to the keyboard and do the obs magic:

https://pypi.org/project/obs-cli/

```
pip install evdev
pip install obs-cli
```

To hear your holiday greeting:

```
sudo apt install espeak
```


## To install:

Put the hotkey scripts in place.

Use these as examples to suit your needs. They generally run an app if it isn't running, or bring it in focus if it already is.

```
cp hotkey-* ~/.local/bin
```

Next, identify the correct usb device:

```
ls /dev/input/by-id/*USB_Keyboard-event*
```

Edit the script to call out the two correct device names for dev and dev2.

Edit the script to map each key to something fun.

Then run: 

```
sudo usermod -a -G input $USER
```

You'll probably have to log fully out and back in to get that to stick.

Then start the program to test:

```
python3 remap.py
```

Set it up to start at bootup. Edit the remap.desktop file to use the right path, then put it in place. (At least on xfce4)

```
cp remap.desktop ~/.config/autostart/
```

Finally print out some sticky labels with icons and affix to the stickers so you don't have to memorize all the mappings.

### Todo:

Figure out how to get this to run at boot. (On xfce4 you can run it from ~/.config/autostart/)

done: Figure out how to not require sudo permissions.

