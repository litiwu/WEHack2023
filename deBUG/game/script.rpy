# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#FF927A")
define spidey = Character("Spidey", color="#3426B1") 
define fade = Fade(0.5, 0, 0.5)
init:
    image roachie default = Image("roachie default.png")
    image laptop = Image("roachie laptop.png")
    image utdreddit = Image("bg utdreddit.png")
    image mapreddit = Image("bg mapreddit.png")
    image roachie delighted = Image("roachie delighted.png")
    image themap = Image("map.png")
    image roachie crying = Image("roachie crying.png")
    image roachie butterfly = Image("roachie butterfly.png")
    image roachie laptop = Image("roachie laptop.png")
    image bg black = Image("bg black.png")


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg black
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show roachie default
    # These display lines of dialogue.
    roachie "Hi! My name is Roachie, and I’m a cockroach studying Software Engineering at UTD."
    hide roachie default
    show roachie crying
    roachie "I was always picked on for being a software engineer who is a cockroach. Usually, only butterflies are software engineers . . ."
    hide roachie crying
    show roachie butterfly
    roachie "So I always really wanted to become a butterfly!"
    hide roachie butterfly
    show roachie laptop
    roachie "I searched online for a way to become a butterfly . . ."
    hide roachie laptop
    scene mapreddit
    roachie "and I came across this post on the UTD forum."
    scene bg black
    show themap
    roachie "What's this?"
    "A life filled with regret . . . can be solved by a magic comet. Follow the map to unlock . . . one wish to be granted by Temoc."
    hide themap
    show roachie default
    roachie "I really need this wish to finally be accepted as a normal software engineer, so I set out in search of Temoc, the comet."
    hide roachie default 
    hide themap
    with fade
    show spidey
    #show roachie default at right
    #roachie "this is us"
    # This ends the game.
    return