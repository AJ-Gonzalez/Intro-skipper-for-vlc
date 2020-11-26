# Intro-skipper-for-vlc
A small intro skipping script.

Mostly inteded for VLC on Linux/Unix systems.
Makes it easy to skip intros on tv shows.
This idea came to mind when marathoning Star Trek TNG,
the easy install came about a little later.
In theory this works on YouTube, and maybe Netflix.

To install as regular Python:
- Download or clone.
- Open a terminal in the downloaded folder.
- Change the intro_duration value to the desired length in minutes.
- Run `python3 introskip.py add` 

To install as binary:
- Download or clone.
- Open a terminal in the downloaded folder.
- Change the intro_duration value to the desired length in minutes.
- Run `chmod u+x introskip && ./introskip.py add` 


You should now have a `skip` command which you can bind to a keyboard shortcut.

When triggered, it will fast forward in increments of 10 seconds, so you can skip your intro.

For Windows users, you can change the extension in `introskip.py` to `pyw`, this will
avoid the annoying pop up command prompt. 



