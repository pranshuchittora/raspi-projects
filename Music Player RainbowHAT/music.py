import rainbowhat as rh
import os
import sys
import pygame
import time
from random import randint
import colorsys
# Open a file

pathToDIR = '/home/pi/MusicPlayer/'
dirs = os.listdir(pathToDIR)
fileArr = []

# This would store and print all the files and directories

for file in dirs:
    fileArr.append(file)
    print file

print len(fileArr)

flag = 0
loopName = False

songName = ''


def showOnDisplay(name):
    rh.display.print_str(name)
    rh.display.show()


i = 0
currentSong = pathToDIR+fileArr[i]
nextSong = pathToDIR+fileArr[i+1]


def music_core():
    global currentSong, nextSong, fileArr
    print 'Now Playing'+fileArr[i]
    print i
    nextSong = pathToDIR+fileArr[i+1]
   	
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(currentSong)
    pygame.mixer.music.queue(nextSong)
    pygame.mixer.music.play()

    
    showOnDisplay(' |> ')


def music_prev(key):
    rh.lights.rgb(1, 0, 0)
    showOnDisplay('<|<|')
    global i, fileArr, loopName, songName, currentSong
    if i > 0:
        i = i - 1
    else:
        i = 0

    fileNow = pathToDIR+fileArr[i]
    songName = fileNow
    currentSong = fileNow
    rh.lights.rgb(0, 0, 0)
    music_core()

   


def music_next(key):
    rh.lights.rgb(0, 0, 1)
    global i, fileArr, loopName, songName, currentSong

    if(i == len(fileArr)):
        i = 0
    showOnDisplay('|>|>')
    i = i + 1

    fileNow = pathToDIR+fileArr[i]
    songName = fileNow
    currentSong = fileNow
    rh.lights.rgb(0, 0, 0)
    music_core()

isPlaying = True


def music_pp(key):
    rh.lights.rgb(0, 1, 0)
    global isPlaying, nextSong, currentSong
    if(isPlaying == True):
        showOnDisplay(' || ')
        pygame.mixer.music.pause()
        isPlaying = False
    else:
        isPlaying = True
        showOnDisplay(' |> ')
        pygame.mixer.music.unpause()
    rh.lights.rgb(0, 0, 0)

rh.touch.A.press(music_prev)
rh.touch.B.press(music_pp)
rh.touch.C.press(music_next)

rh.rainbow.clear()

while True:
    for pixel in range(7):
        rh.rainbow.clear()
        rh.rainbow.set_pixel(pixel, randint(
            1, 255), randint(1, 255), randint(1, 255))
        rh.rainbow.show()
        time.sleep(0.2)
    for pixel in range(5, 0, -1):
        rh.rainbow.clear()
        rh.rainbow.set_pixel(pixel, randint(
            1, 255), randint(1, 255), randint(1, 255))
        rh.rainbow.show()
        time.sleep(0.2)