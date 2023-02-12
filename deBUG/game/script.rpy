# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#e59d4f")
define susspidey = Character("Suspicious Spider", color="#ac26b1") 
define reddie = Character("Reddie", color="#d34949")
define greenie = Character("Greenie", color="#64af67")
define bluey = Character("Bluey", color="#559cc3")
define spidey = Character("Spidey", color="#ac26b1") 
define instruction = Character("Instructions", color="#232323")
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
    image susspidey = Image("spidey default.png")
    image spidey = Image("spidey default.png")
    image ch1 = Image("ch1.png")
    image bg twohours = Image("bg twohours.jpeg")
    image bg utd = Image("bg utd.png")
    image bg lake = Image("bg lake.png")
    image spidey doubt = Image("spidey doubt.png")
    image spidey happy = Image("spidey happy.png")
    image spidey surprised = Image("spidey surprised.png")
    image spidey tired = Image("spidey tired.png")
    image ladybugs crying = Image("ladybugs crying.png")
    image bg path = Image("bg path.png")
    image bg 0000 = Image("bg mg0000.png")
    image bg 0001 = Image("bg mg0001.png")
    image bg 0010 = Image("bg mg0010.png")
    image bg 0011 = Image("bg mg0011.png")
    image bg 0100 = Image("bg mg0100.png")
    image bg 0101 = Image("bg mg0101.png")
    image bg 0110 = Image("bg mg0110.png")
    image bg 1001 = Image("bg mg1001.png")
    image bg 1010 = Image("bg mg1010.png")
    image bg 1100 = Image("bg mg1100.png")
    image bg 1101 = Image("bg mg1101.png")
    image bg 1110 = Image("bg mg1110.png")
    image bg 1111 = Image("bg mg1111.png")
    image bg 1000 = Image("bg mg1000.png")
    image bg 1011 = Image("bg mg1011.png")
    


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg utd
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
    scene bg black
    show roachie laptop
    roachie "I searched online for a way to become a butterfly . . ."
    hide roachie laptop
    scene mapreddit
    roachie "and I came across this post on the UTD forum."
    scene bg black
    show themap
    roachie "What's this?"
    "{color=#b52b16}{i}A life filled with regret . . . can be solved by a magic comet. Follow the map to unlock . . . one wish to be granted by Temoc.{/i}{/color}"
    hide themap
    scene bg utd
    show roachie default
    roachie "I really need this wish to finally be accepted as a normal software engineer, so I set out in search of Temoc, the comet."
    hide roachie default 
    hide themap

    scene ch1
    "Chapter 1: Logic Lake"

    scene bg black
    show themap

    roachie "The first location on the map was Logic Lake, just a few miles east."

    hide themap
    
    scene bg twohours
    roachie "{color=#0373fc}{i}After Two Hours{/i}{/color}"

    scene bg lake
    show roachie default
    roachie "Finally here!"
    roachie "What's going on over there?"
    hide roachie default
    show spidey tired at left
    show ladybugs crying at right
    roachie "{color=#0373fc}{i}At the lake, I saw a suspicious spider arguing with three young ladybugs.{/i}{/color}"
    roachie "{color=#0373fc}{i}I should go check whether the ladybugs are being harassed or not.{/i}{/color}"

    susspidey "Hey guys, we don’t have much time. Can we please apologize to each other and go?"

    reddie "No way! Greenie won’t share their toys with me."

    greenie "You always take my toys and damage them! I don’t want to even be near Reddie right now."

    bluey  "Greenie hasn’t even returned my school notebook for a whole week! I don’t want to stay with him even for a second!"

    susspidey "So I can’t leave Reddie and Greenie together or Greenie and Bluey together, but I can only take one at a time across the lake . . . what should I do? ugh . . ."
    hide spidey tired
    hide ladybugs crying

    show spidey tired at right
    show roachie default at left
    roachie "Wait . . . I think I can help you."

    hide spidey tired
    show spidey doubt at right
    susspidey "{color=#0373fc}{i}A cockroach? How can a cockroach help me? Oh well, I am out of ideas, anyways. I’m just going to hear out what they have to say.{/i}{/color}"
    susspidey "Okay . . . tell me how to get us across the lake."

    hide spidey doubt
    hide roachie default

    #mini game here
    label game: 

        instruction "Help the spider take the three ladybugs across the lake. The spider can only take one ladybug at a time, but Reddie and Greenie can’t be left alone together and Greenie and Bluey can’t be left alone together."

        # booleans for logic 
        default spideyB = False
        default reddieB = False
        default greenieB = False
        default blueyB = False 
        
        scene bg 0000

    label round1:

        scene bg 0000
        menu:
            instruction "Choose which ladybug the spider should take across the lake."
            "Take Reddie Across":
                $ spideyB = True
                $ reddieB = True
                scene bg 1100
                pause 1
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
                pause 1
                jump ending

            "Cross Alone":
                $ spideyB = True
                scene bg 1000
                pause 1
                jump ending 

    label round2:

        if greenieB:
            scene bg 1010
            menu:
                instruction "Choose which ladybug the spider should take across the lake."
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
            instruction "Choose which ladybug the spider should take across the lake."
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
                instruction "Choose which ladybug the spider should take across the lake."
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
                    pause 1
                    jump ending
        elif blueyB:
            scene bg 1011 
            menu: 
                instruction "Choose which ladybug the spider should take across the lake."
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
                    pause 1
                    jump ending
    label round5:
        if reddieB:
            scene bg 0100
            menu: 
                instruction "Choose which ladybug the spider should take across the lake."
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
                    pause 1
                    jump ending

        elif blueyB:
            scene bg 0001
            menu: 
                instruction "Choose which ladybug the spider should take across the lake."
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
                    pause 1
                    jump ending

    label round6:
        scene bg 1101 
        menu:
            instruction "Choose which ladybug the spider should take across the lake."
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
            instruction "Choose which ladybug the spider should take across the lake."
            "Take Greenie Across":
                $ spideyB = True
                $ greenieB = True
                scene bg 1111
                pause 1
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
            spidey "Try again! Reddie, Greenie and Bluey can't all be together. \nTap to try again!"
            jump game

        elif reddieB:
            show spidey tired 
            spidey "Try again! Reddie and Greenie can't be together. \nTap to try again!"
            jump game

        elif blueyB:
            show spidey tired 
            spidey "Try again! Greenie and Bluey can't be together. \nTap to try again!"
            jump game
        elif spideyB:
            show spidey tired 
            spidey "Try again! Reddie, Greenie and Bluey can't all be together. \nTap to try again!"
            jump game
        

    label end_dialogue:
    
    scene bg lake
    show spidey happy

    susspidey "Thank you so much, cockroach. My kids were being so difficult, but you were able to get them across safely."
    
    hide spidey happy
    show roachie default

    roachie "Your kids?"

    hide roachie default
    show spidey

    spidey "Yes! I am their adoptive parent, and I was dropping them off at the daycare. My name is Spidey."

    hide spidey
    scene bg black
    show spidey

    roachie "{color=#0373fc}{i}Wow, I thought spiders were cold and uncaring, but I was making assumptions.{/i}{/color}"

    hide spidey
    scene bg lake
    show spidey

    spidey "What's your name?"

    hide spidey
    show roachie default

    roachie "I'm Roachie, and I'm a software engineering student."

    hide roachie default
    scene bg black
    show roachie default

    spidey "{color=#0373fc}{i}I never thought cockroaches could ever become software engineers, but I changed my mind. I didn’t know cockroaches could be so smart!{/i}{/color}"
    
    hide roachie default
    scene bg lake
    show spidey surprised

    spidey "Oh my! You definitely have the brains to become a successful software engineer. Why are you traveling all the way out here?"
    
    hide spidey surprised
    show roachie default

    roachie "{color=#0373fc}{i}Spidey believes I can become a software engineer as a cockroach?{/i}{/color}"
    roachie "Oh . . . I'm trying to find the magic Temoc to grant my wish."

    hide roachie default
    show roachie default at left 
    show spidey at right

    spidey "Let me come and help you. I’m indebted to you for helping us cross the lake."
    roachie "{color=#0373fc}{i}Hmmm. I am still pretty scared of spiders, but maybe I’m wrong about them . . .{/i}{/color}"
    roachie "Thanks for helping! Next, we have to go to Python Pit."

    hide roachie default
    hide spidey 
    scene bg path
    "To be continued . . ."

    scene bg black

    "End of demo. Thanks for playing!"
    
    # This ends the game.
    return