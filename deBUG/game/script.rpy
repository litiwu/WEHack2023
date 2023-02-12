# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#FF927A")
define spidey = Character("Spidey", color="#3426B1") 
define reddie = Character("Reddie", color="#ff5964")
define greenie = Character ("Greenie", color="#7bcd70")
define bluey = Character ("Bluey", color="#68afff")
define instruction = Character("Instructions", color="#232323")

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
    
    
label game: 


    instruction "Help the spider take the three ladybugs across the lake. The spider can only take one ladybug at a time, but Reddie and Greenie can’t be left alone together and Greenie and Bluey can’t be left alone together. Choose which ladybug the spider should take across the lake."

#label game_start:

    # booleans for logic 
    default spideyB = False
    default reddieB = False
    default greenieB = False
    default blueyB = False 
    
    scene bg 0000
    

label round1:

    scene bg 0000
    menu:

        "Take Reddie Across":
            $ spideyB = True
            $ reddieB = True
            scene bg 1100
            jump ending

        "Take Greenie Across":
            $ spideyB = True
            $ greenieB = True
            scene bg 1010
            jump round2

        "Take Bluey Across":
            $ spideyB = True
            $ blueyB = True
            scene bg 1001
            jump ending

        "Cross Alone":
            $ spideyB = True
            scene bg 1000
            jump round2 




label round2:

    if greenieB:
        scene bg 1010
        menu:
            "Take Greenie Back":
                $ greenieB = False
                $ spideyB = False
                scene bg 0000
                jump round1

            "Cross Back Alone":
                $ spideyB = False
                scene bg 1010
                jump round3 
    else:
        scene bg 1000
        menu:
            "Cross Back Alone":
                $ spideyB = False
                scene 0000
                jump round1



label round3:
    scene bg 0010 
    menu:
        "Take Reddie Across":
            $ spideyB = True
            $ reddieB = True
            scene bg 1110
            jump round4

        "Take Bluey Across":
            $ spideyB = True
            $ blueyB = True
            scene bg 1011
            jump round4

        "Cross Alone":
            $ spideyB = True
            scene bg 1010
            jump round2 

label round4: 
    if reddieB: 
        scene bg 1110 
        menu: 
            "Take Reddie Back":
                $ spideyB = False
                $ reddieB = False
                scene bg 0010
                jump round3
            "Take Greenie Back":
                $ spideyB = False
                $ greenieB = False
                scene bg 0100
                jump round5
            "Cross Back Alone": 
                $ spideyB = False
                scene bg 0110
                jump ending
    elif blueyB:
        scene bg 1011 
        menu: 
            "Take Greenie Back":
                $ spideyB = False
                $ greenieB = False
                scene bg 0100
                jump round5
            "Take Bluey Back":
                $ spideyB = False
                $ blueyB = False
                scene bg 0010
                jump round3
            "Cross Back Alone": 
                $ spideyB = False
                scene bg 0011
                jump ending
label round5:
    if reddieB:
        scene bg 0100
        menu: 
            "Take Greenie Across":
                $ spideyB = True
                $ greenieB = True
                scene bg 1110 
                jump round4
            "Take Bluey Across":
                $ spideyB = True
                $ blueyB = True 
                scene bg 1101
                jump round6
            "Cross Alone":
                $ spideyB = True
                scene bg 1100
                jump ending

    elif blueyB:
        scene bg 0001
        menu: 
            "Take Reddie Across":
                $ spideyB = True
                $ reddieB = True 
                scene bg 1101
                jump round6
            "Take Greenie Across":
                $ spideyB = True
                $ greenieB = True
                scene bg 1011 
                jump round4
            "Cross Alone":
                $ spideyB = True
                scene bg 1001
                jump ending

label round6:
    scene bg 1101 
    menu:
        "Take Reddie Back":
                $ spideyB = False
                $ reddieB = False
                scene bg 0001
                jump round5
        "Take Bluey Back":
                $ spideyB = False
                $ blueyB = False
                scene bg 0100
                jump round5
        "Cross Back Alone": 
                $ spideyB = False
                scene bg 0101
                jump round7

label round7:
    scene bg 0101
    menu:
        "Take Greenie Across":
            $ spideyB = True
            $ greenieB = True
            scene bg 1111
            jump ending
        "Cross Alone": 
            $ spideyB = True
            scene bg 1101
            jump round6 


label ending:

    scene bg lake

    if reddieB and greenieB and blueyB and spideyB:
        jump end_dialogue

    elif reddieB and blueyB:
        show spidey tired 
        spidey "Try again! Reddie, Greenie and Bluey can't all be together:( \nTap to try again!"
        jump game

    elif reddieB:
        show spidey tired 
        spidey "Try again! Reddie and Greenie can't be together:( \nTap to try again!"
        jump game

    elif blueyB:
        show spidey tired 
        spidey "Try again! Greenie and Bluey can't be together:( \nTap to try again!"
        jump game

label end_dialogue:
    spidey "this is a place holder for end of game"
    # This ends the game.
    return