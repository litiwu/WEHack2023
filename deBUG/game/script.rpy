# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define roachie = Character("Roachie", color="#FF927A")
define spidey = Character("Spidey", color="#3426B1") 


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

    roachie "meow"

    hide roachie default 
    show spidey default

    spidey "woof"

    show roachie default at right

    roachie "this is us"


    # This ends the game.

    return
