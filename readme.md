# remap.py

"Merry Christmas Damian."

This little script is a bit hacky, but it works nicely.

## What is this?

This is a macro keyboard for linux. It provides 21 completely configurable buttons. Each button can trigger a script that can run any action conceivable.

I use this to do things like open specific applications like python or vscode, or bring Microsoft Teams to the foreground immediately when you've lost it. Adjust your volume up and down. Mute/unmute. Have your computer say things. Switch scenes on OBS. It won't type garbage characters into your terminal, or cause you to lose your cursor focus unintentionally, or conflict with hotkey settings in the app you are using.

You can think of it as the dorky linux version of the Elgato Stream Deck MK.2

https://www.amazon.com/Elgato-Stream-Deck-MK-2-Controller/dp/B09738CV2G/

But with 40% more buttons and 10% of the price.

It's great. I have one button dedicated to pulling up python that I use as a calculator; one pulls up Teams (which is often lost under other windows); one pulls up the macro code so I can edit it on the fly without restarting; one pulls up obs; several switch camera views. You can also just map it to send keystrokes, or play audio, or whatever your imagination allows.


## Prerequisites:

You'll need the hardware:

https://www.amazon.com/Mechanical-Numeric-Backlit-Desktop-Computer/dp/B07FFLNF5C/

You'll need python3 installed.

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
./install
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

