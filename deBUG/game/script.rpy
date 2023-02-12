# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#e59d4f")
define susspidey = Character("Suspicious Spider", color="#ac26b1") 
define reddie = Character("Reddie", color="#d34949")
define greenie = Character("Greenie", color="#64af67")
define bluey = Character("Bluey", color="#559cc3")
define spidey = Character("Spidey", color="#ac26b1") 
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
    "{color=#b52b16}{i}A life filled with regret . . . can be solved by a magic comet. Follow the map to unlock . . . one wish to be granted by Temoc.{/i}{/color}"
    hide themap
    show roachie default
    roachie "I really need this wish to finally be accepted as a normal software engineer, so I set out in search of Temoc, the comet."
    hide roachie default 
    hide themap

    scene ch1
    "Chapter 1: Logic Lake"

    scene bg black

    roachie "The first location on the map was Logic Lake, just a few miles east."
    
    scene bg twohours
    roachie "{color=#0373fc}{i}After Two Hours{/i}{/color}"

    #scene bg lake
    show roachie default
    roachie "Finally here!"
    roachie "What's going on over there?"
    hide roachie default
    show susspidey at left
    #show three ladybugs at right
    roachie "{color=#0373fc}{i}At the lake, I saw a suspicious spider arguing with three young ladybugs.{/i}{/color}"
    roachie "{color=#0373fc}{i}I should go check if the ladybugs aren't being harassed.{/i}{/color}"

    susspidey "Hey guys, we don’t have much time. Can we please apologize to each other and go?"

    reddie "No way! Greenie won’t share their toys with me."

    greenie "You always take my toys and damage them! I don’t want to even be near Reddie right now."

    bluey  "Greenie hasn’t even returned my school notebook for a whole week! I don’t want to stay with him even for a second!"

    susspidey "So I can’t leave Reddie and Greenie together or Greenie and Bluey together, but I can only take one at a time across the lake . . . what should I do? ugh . . ."
    hide susspidey
    #hide three ladybugs

    show susspidey at right
    #show roachie ponder at left
    show roachie default at left
    roachie "Wait . . . I think I can help you."

    susspidey "{color=#0373fc}{i}A cockroach? How can a cockroach help me? Oh well, I am out of ideas, anyways. I’m just going to hear out what they have to say.{/i}{/color}"
    susspidey "Okay . . . tell me how to get us across the lake."

    hide susspidey
    hide roachie default

    #mini game here
    
    #scene bg lake
    show susspidey
    susspidey "Thank you so much, cockroach. My kids were being so difficult, but you were able to get them across safely."
    hide susspidey
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
    #scene bg lake
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
    #scene bg lake
    show spidey
    spidey "Oh my! You definitely have the brains to become a successful software engineer. Why are you traveling all the way out here?"
    hide spidey
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

    scene bg black

    "End of demo. Thanks for playing!"
    
    # This ends the game.
    return