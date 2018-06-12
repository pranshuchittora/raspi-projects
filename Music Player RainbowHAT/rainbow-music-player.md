# Raspberry Pi + Rainbow HAT = :bomb:
## What we will build ??
>A raspberry pi music player which is controlled by RainbowHAT 

Its my vacations and having fun with my new raspberry pi model 3 b+. I also have an Android Things Kit which has NXP i.MX7D with a touch display and an awesome GPIO attachment Rainbow HAT.    

Unfortunately I am not able to boot up the board with official Google image :( 
So I took rainbow hat from that kit and tried to pair it up with the Pi and vola it attached successfully.
Now I have to pray that there is some python support for it and hopefully it exists.
[Getting Started with Rainbow HAT](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-rainbow-hat-in-python)

## Rainbowhat is an awesome library with easy to use functions

### Install it by:

```bash
curl https://get.pimoroni.com/rainbowhat | bash
```

I strongly recommend you to play with it a little bit to get familiar with it.

To play music and hadle event I went with [pygame](https://www.pygame.org/). Its one of the most popular library for the pi.
```bash
sudo apt-get install python3-pygame
```
------------------------------------
Basically we specify the path to the folder where the Music files exist. In my case its in the same directory. At the top of the program there is a variable named pathToDIR. Set it equal to the path of the music direcory

    pathToDIR = '/home/pi/MusicPlayer/'

After that using os and sys I looked through all the files and stored their name i.e file name in an array and then initialised a global var i which represents the index value or the fileArr index.

Ther are total 5 main functions
    Main music player : music_core()
    Display management : showOnDisplay()
    Next song : music_next()
    Previous song : music_prev()
    Play / Pause : music_pp()



