import pygame
from pygame import mixer
from colorama import init, Fore
import time
import random
import re
import os


# ---------------- SETUP ---------------- #

init(autoreset=True)

pygame.init()


try:
    mixer.init()

except pygame.error as e:

    print(Fore.RED + f"Audio error: {e}")
    exit()



# ---------------- MUSIC ---------------- #

MUSIC_FOLDER = "Music"



def find_song():

    if not os.path.exists(MUSIC_FOLDER):

        os.makedirs(MUSIC_FOLDER)

        print(Fore.YELLOW)
        print("Created Music folder.")
        print("Put your MP3 here:")
        print(os.path.abspath(MUSIC_FOLDER))

        return None



    songs = [

        f for f in os.listdir(MUSIC_FOLDER)

        if f.lower().endswith(".mp3")

    ]



    if not songs:

        print(Fore.YELLOW)
        print("No MP3 file found.")

        print(
            "Add your song here:",
            os.path.abspath(MUSIC_FOLDER)
        )

        return None



    return os.path.join(
        MUSIC_FOLDER,
        songs[0]
    )



# ---------------- LYRICS ---------------- #

LRC_TEXT = """

[00:00.00]Ishq junoon jab hadh se badh jaaye
[00:04.25]Ishq junoon jab hadh se badh jaaye
[00:08.50]Haste haste aashiq sooli chadh jaaye
[00:13.16]Ishq ka jaadu sar chadha kara bole
[00:17.15]Ishq ka jaadu sar chadha kara bole
[00:21.66]Khoob laga lo pehre raste rab khole
[00:26.16]Yahi ishq di marzi hain
[00:28.41]Yahi rab di marzi hain
[00:34.65]Yahi ishq di marzi hain
[00:37.66]Yahi rab di marzi hain
[00:39.66]Tere bin jeena kaisa
[00:42.15]Haan khudgarzi hain
[00:44.65]Tune kya kar dala
[00:46.90]Marr gayi main mitt gayi main
[00:48.90]Ho ji haan ji hogayi main
[00:53.41]Teri deewani.. deewani
[00:57.66]Teri deewani.. deewani
[01:02.41]Teri deewani.. deewani

"""



colors = [

    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.CYAN,
    Fore.MAGENTA,
    Fore.BLUE,
    Fore.WHITE

]



# ---------------- FUNCTIONS ---------------- #


def clear():

    os.system(
        "cls" if os.name == "nt"
        else "clear"
    )




def parse_lrc(text):

    lyrics = []

    pattern = r"\[(\d+):(\d+\.\d+)\](.*)"



    for line in text.strip().split("\n"):


        match = re.match(pattern, line)


        if match:

            minutes = int(match.group(1))

            seconds = float(match.group(2))


            lyrics.append(

                (
                    minutes * 60 + seconds,
                    match.group(3).strip()
                )

            )


    return lyrics




def type_writer(text, duration):

    color = random.choice(colors)



    if len(text) > 0:

        delay = duration / len(text)

    else:

        delay = 0



    for char in text:

        print(
            color + char,
            end="",
            flush=True
        )

        time.sleep(delay)



    print()



# ---------------- MAIN ---------------- #

clear()



print(
    Fore.CYAN +
    "=" * 60
)

print(
    Fore.YELLOW +
    "              PYTHON KARAOKE PLAYER"
)

print(
    Fore.CYAN +
    "=" * 60
)

print()



SONG_FILE = find_song()



if SONG_FILE is None:

    pygame.quit()
    exit()



try:

    mixer.music.load(SONG_FILE)


except pygame.error as e:

    print(
        Fore.RED +
        f"Song loading failed: {e}"
    )

    pygame.quit()
    exit()



lyrics = parse_lrc(LRC_TEXT)



print(
    Fore.GREEN +
    "Playing:"
)

print(
    Fore.CYAN +
    os.path.basename(SONG_FILE)
)

print()



# Start music

mixer.music.play()



# Synchronize lyrics

song_start = time.time()



for index, (timestamp, lyric) in enumerate(lyrics):


    # Wait until lyric timestamp

    while time.time() - song_start < timestamp:

        time.sleep(0.01)



    # Calculate typing duration

    if index + 1 < len(lyrics):

        next_timestamp = lyrics[index + 1][0]

        typing_time = (
            next_timestamp - timestamp
        )


    else:

        typing_time = 4



    type_writer(
        lyric,
        typing_time
    )



# Wait for music end

while mixer.music.get_busy():

    time.sleep(1)



print()

print(
    Fore.GREEN +
    "Song Finished!"
)



pygame.quit()
