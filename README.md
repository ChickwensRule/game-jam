# CSHS 2022 Game Jam

This repository contains the submission for the CSHS 2022 Game Jam.

## Game Description

You have just been disqualified from the MATE Worlds Competition for "electrocuting the diver" or something. As Jefferson yells at you and your team, you notice a control panel near the pool's edge. Ignoring Jeff, you go investigate. You quickly realize that this is no ordinary control panel: a massive drain at the pool's bottom is somehow connected to the sewer. This panel allows you to regulate the flow of water from the pool into the sewers. You see a team doing its run as the competition continues. And as you look closer, you notice that their bright red ROV looks suspiciously similar to your least favorite team's ROV: because it is. Why are they your least favorite team? Because one of its members stole your favorite soldering iron for exactly 43.4 seconds.

It couldn’t be more perfect: to sabotage their run and get revenge for the trauma they caused to you, all you have to do is drain the massive swimming pool. But there’s a catch. In order to drain the pool, you must guess a series of words. Fail more than 5 times, and the alarm will go off and you will get shot.

Good luck!

## Playing the Game

You must have PyQt6 installed to run the game:

`pip3 install PyQt6` or `pip install PyQt6`

To run the game:

`python3 main.py` or `python main.py`

## Adding Words

Feel free to add new words to the `words.txt` list, but don't go over 10 characters per word or there will be some visual glitches. Words are separated by newlines (\n).

#### Valid characters:
- **A-Z** (caps only)
- Space
