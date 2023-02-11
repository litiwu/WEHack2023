﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#e46e53")
define spidey = Character("Spidey", color="#3426B1") 
define fade = Fade(0.5, 0, 0.5)
init:
    image roachie default = Image("roachie default.png")
    image laptop = Image("roachie laptop.png")
    image utdreddit = Image("bg utdreddit.png")
    image mapreddit = Image("bg mapreddit.png")
    image roachie delighted = Image("roachie delighted.png")
    image themap = Image("themap.png")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show roachie default

    # These display lines of dialogue.

    roachie "Hi! My name is Roachie, and I’m a cockroach studying Software Engineering at UTD."

    # SHOULD SWICH TO SAD ROACHIE

    roachie "I was always picked on for being a software engineer who is a cockroach. Usually, only butterflies are software engineers . . ."

    hide roachie default

    #SCENE CHANGE TO THOUGHT BUBBLE AS BUTTERFLY

    roachie "so I always really wanted to become a butterfly!"

    scene laptop

    roachie "I searched online for a way to become a butterfly when I came across this post on the UTD forum."

    scene mapreddit

    "A life filled with regret . . . can be solved by a magic comet. Follow the map to unlock . . . one wish to be granted by Temoc."
    
    scene themap

    show roachie delighted

    roachie "I really need this wish to finally be accepted as a normal software engineer, so I set out in search of Temoc, the comet."

    hide roachie delighted
    with fade

    #show roachie default at right

    #roachie "this is us"


    # This ends the game.

    return
