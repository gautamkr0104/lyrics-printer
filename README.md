# Python Karaoke Player

A simple terminal-based karaoke player written in Python. It plays an MP3 from the `Music/` folder using `pygame` and displays the song's lyrics line-by-line in sync with the music, with a colorful typewriter effect powered by `colorama`.

## Features

- 🎵 Plays the first MP3 found in the `Music/` folder
- 🎤 Lyrics displayed in sync with the song using timestamps
- ⌨️ Typewriter-style text animation
- 🌈 Random color for each lyric line
- 📁 Automatically creates the `Music/` folder if it doesn't exist
- 🛑 Clean exit if no MP3 is found or audio fails to initialize

## Requirements

- Python 3.x
- [pygame](https://www.pygame.org/) (for audio playback)
- [colorama](https://pypi.org/project/colorama/) (for colored terminal output)

## Installation

1. Clone or download this repository.
2. Install the dependencies:

```bash
pip install pygame colorama
```

## Usage

1. Put an MP3 file inside the `Music/` folder:

```
Music/
└── your-song.mp3
```

2. Run the player:

```bash
python main.py
```

The script will play the first `.mp3` file it finds in `Music/` and print the lyrics in sync with the song.

## Customizing the Lyrics

Lyrics are defined as LRC-format text inside `main.py` (the `LRC_TEXT` variable). Each line uses a timestamp in `[minutes:seconds.centiseconds]` format followed by the lyric text:

```
[00:04.25]Ishq junoon jab hadh se badh jaaye
[00:08.50]Haste haste aashiq sooli chadh jaaye
```

To use different lyrics, replace the contents of `LRC_TEXT` with the LRC data for your song (many lyric sites let you download LRC files). Make sure timestamps match your MP3's timing.

## Project Structure

```
.
├── main.py       # Karaoke player script
├── Music/        # Folder containing MP3 files (auto-created if missing)
└── README.md
```

## Notes

- Only MP3 files are detected (case-insensitive). If multiple MP3s exist, the first one found is played.
- The bundled lyrics in `main.py` are for the song *Teri Deewani* by Kailash Kher. Song and lyrics are the property of their respective copyright holders.
