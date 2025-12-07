# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

$ safety = 0
$ legal = 0
$ awareness_lvl = 0
$ mental = 0

image casual eileen:
    "casualEileen.png"
    zoom 0.65

image bedroom night:
    "bedNight.png"
    zoom 1.25

# The game starts here.

label start:

    "You are Eileen."

    "You are a 17 year old high school student."

    "You own a Tiktok account and frequently post under the name 'realeileensmith08'. "

    "You were doing it for fun, but you never expected your posts to blow up."
    
    "And one day... It did."

    "A cute, slightly uncanny video."

    "Within hours, it goes massively viral."
    
    scene bedroom night

    show casual eileen

    e "What is happening?"

    play sound "phonevibrate.mp3"

    e "My phone is going off!"

    e "Just who is contacting me!"

    menu:
        "Check your phone":
            $ awareness_lvl += 1
            jump phone_check
        "Go to sleep":
            $ mental += 1
            jump act_one

    label phone_check:

        show casual eileen at left with move

label act_one:

    return
