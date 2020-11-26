# Intro-skipper-for-vlc
A small intro skipping script.

Mostly inteded for VLC on Linux/Unix systems.
Makes it easy to skip intros on tv shows.
This idea came to mind when marathoning Star Trek TNG,
the easy install came about a little later.
In theory this works on YouTube, and maybe Netflix.

### Installing:

**For Linux Users:**

- Download or clone.
- Open a terminal in the downloaded folder.
- Run `pip install pyautogui`.
- Change the intro_duration value to the desired length in minutes.
- Run `python3 introskip.py add` 

You should now have a `skip` command which you can bind to a keyboard shortcut.

When triggered, it will fast forward in increments of 10 seconds, so you can skip your intro.


**For Windows users:**

- Run `pip install pyautogui`.

- You can change the extension in `introskip.py` to `pyw`, this will
avoid the annoying pop up command prompt. 

- Create a hotkey binding with AHK.



