# Text Noises

init python:
    import random

    def typography(what):
        replacements = [
                ('. ','. {w=.2}'),
                ('? ','? {w=.25}'),
                ('! ','! {w=.25}'),
                (', ',', {w=.15}'),
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography

    # Continuous text sounds
    def text_sounds(event, interact=False, **kwargs):
        if event == "show":
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5

            for _ in range(sound_count):
                randosound = renpy.random.randint(1, 1)
                renpy.sound.queue(f"<volume 0.5>audio/popcat{randosound}.mp3", channel="sound", loop=False)

        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound")

init python:
    renpy.music.register_channel("scribble", "sfx", True, tight=True)

init python:
    renpy.music.register_channel("milk", "sfx", False)

init python:
    renpy.music.register_channel("shock", "sfx", False)

init python:
    import random, re

    renpy.music.register_channel("textsound", "sfx", False)

    _TAG = re.compile(r'{cps=(\d+)}')

    def adaptive_text_sounds(event, interact=True, **kw):
        if event == "show":
            renpy.sound.stop(channel="textsound")
            raw  = renpy.store._last_say_what or ""
            text = renpy.substitute(raw)
            cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

            for chunk in _TAG.split(text):
                if chunk.isdigit():
                    cps = int(chunk)
                    continue
                pause = 0 if cps <= 0 else 1.0 / cps

                for char in chunk:
                    if not char.isspace():
                        renpy.sound.queue(f"<volume 0.4>audio/popcat{random.randint(1, 1)}.mp3",channel="textsound")
                    if pause:
                        renpy.sound.queue(f"<silence {pause}>", channel="textsound")

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="textsound")

transform ending_box_appear:
    alpha 0.0
    linear 0.3 alpha 1.0

screen ending_text():
    frame:
        at ending_box_appear
        xpos 70
        yalign 0.72
        xpadding 30
        ypadding 20
        background Solid("#342559")

        text "YOU FAILED TO ANSWER THE DOOR":
            color "#ffffff"
            size 50
            slow_cps 15

screen act_one_text():
    text "ACT ONE: THE PARTY BEGINS":
        xalign 0.5
        yalign 0.5
        color "#ffffff"
        size 50
        slow_cps 15

screen act_two_text():
    text "ACT TWO: THE PARTY GROWS QUIET":
        xalign 0.5
        yalign 0.5
        color "#ffffff"
        size 50
        slow_cps 15

screen act_three_text():
    text "ACT THREE: THE PARTY GROWS QUIET":
        xalign 0.5
        yalign 0.5
        color "#ffffff"
        size 50
        slow_cps 15

# Characters
define o = Character(_("Otter"), color="#956dc9", what_slow_cps=35, callback=text_sounds)
define ch = Character(_("Charlie"), color="#6082d1", what_slow_cps=35, callback=text_sounds)
define c = Character(_("Cat"), color="#eb88cb", what_slow_cps=35, callback=text_sounds)
define d = Character(_("Danny"), color="#cc9189", what_slow_cps=35, callback=text_sounds)
define unknown = Character(_("{i}???{/i}"), color="#bdbdbd", what_slow_cps=35, callback=text_sounds)
define narrator = Character(None, what_italic=True, what_slow_cps=35, callback=text_sounds)
define replies = [
    ("It wasn't real."),
    ("I think I had a bad dream..."),
    ("Why can't I remember?"),
]
define replies2 = [
    ("Ugh, I look like shit."),
    ("Have I always been so pale?"),   
]
define alex_expressions = ["alex", "alex3",]
define config.layers = ['master', 'alexlayer', 'transient', 'say', 'screens',]
define config.top_layers = [ 'toplayer' ]
define config.say_layer = "say"
define flashbeat = Fade(0.4, 0.0, 0.05, color="#ffffff")

$ config.menu_include_disabled = True

# Variables
default betrayal = 0
default truth = 0
default violence = 0
default acceptance = 0

default charlie_bond = 0
default cat_bond = 0
default danny_bond = 0

default charlie_love = 0
default charlie_not_love = 0
default cat_love = 0
default danny_love = 0

default presents_opened = 0

default greyed_out = False

default annoying = 0

image white = Solid("#ffffff")

default char_menu = set()

# Inventory
default polaroid = 0
default has_photo = False
default has_charlie_album = False
default has_cat_gift = False
default has_danny_cassette = False
default music_choice = None

# Testing

default time_of_day = "2:30PM"

# Scaled Background Images
init python:
    BEDROOM_SCALE_X = 1.31
    BEDROOM_SCALE_Y = 1.31

    def scaled(name):
        return im.FactorScale(name, BEDROOM_SCALE_X, BEDROOM_SCALE_Y)

init python:
    SCALE_X = 0.38
    SCALE_Y = 0.38

    def scaled2(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init python:
    PORCH_SCALE_X = 0.55
    PORCH_SCALE_Y = 0.55

    def scaled3(name):
        return im.FactorScale(name, PORCH_SCALE_X, PORCH_SCALE_Y)

init python:
    LOUNGE_SCALE_X = 1.7
    LOUNGE_SCALE_Y = 1.7

    def scaled4(name):
        return im.FactorScale(name, LOUNGE_SCALE_X, LOUNGE_SCALE_Y)

init python:
    BATH_SCALE_X = 0.8
    BATH_SCALE_Y = 0.8

    def scaled5(name):
        return im.FactorScale(name, BATH_SCALE_X, BATH_SCALE_Y)

init python:
    KITCHEN_SCALE_X = 0.8
    KITCHEN_SCALE_Y = 0.8

    def scaled6(name):
        return im.FactorScale(name, KITCHEN_SCALE_X, KITCHEN_SCALE_Y)

init python:
    OVERLAY_SCALE_X = 0.5
    OVERLAY_SCALE_Y = 0.5

    def overlay(name):
        return im.FactorScale(name, OVERLAY_SCALE_X, OVERLAY_SCALE_Y)

init python:
    HALLWAY_SCALE_X = 0.78
    HALLWAY_SCALE_Y = 0.78

    def scaled7(name):
        return im.FactorScale(name, HALLWAY_SCALE_X, HALLWAY_SCALE_Y)

init python:
    PORCH_SCALE_X = 0.65
    PORCH_SCALE_Y = 0.65

    def scaled8(name):
        return im.FactorScale(name, PORCH_SCALE_X, PORCH_SCALE_Y)

init python:
    NEW_KITCHEN_SCALE_X = 1.1
    NEW_KITCHEN_SCALE_Y = 1.1

    def scaled9(name):
        return im.FactorScale(name, NEW_KITCHEN_SCALE_X, NEW_KITCHEN_SCALE_Y)

init python:
    DINING_TABLE_SCALE_X = 1.52
    DINING_TABLE_SCALE_Y = 1.52

    def scaled10(name):
        return im.FactorScale(name, DINING_TABLE_SCALE_X, DINING_TABLE_SCALE_Y)

init:
    image bedroom = scaled("bedroom.png")
    image doorway = scaled2("doorway.png")
    image porch = scaled3("porch.png")
    image lounge = scaled4("lounge.png")
    image lounge_test = scaled4("lounge_test.png")
    image lounge_two = scaled7("lounge_two.png")
    image bathroom = scaled5("bathroom.png")
    image kitchen = scaled9("kitchen.png")
    image outside = scaled6("outside.png")
    image house_exterior = scaled6("house_exterior.png")
    image house_exterior_two = scaled6("house_exterior_two.png")
    image hallway = scaled7("hallway.png")
    image back_porch = scaled8("back_porch.png")
    image balcony = ("balcony.png")
    image dining_table = scaled10("dining_table2.png")

    image noise_overlay = overlay ("texture.jpg")

# Endings

    image ending_one = ("ending_one.png")
    image ending_danny = ("ending_danny.png")
    image ending_charlie = ("ending_charlie.png")
    image ending_violent = ("ending_violent.png")

# Scaled Assets
init python:    
    ASSET_SCALE_X = 0.5
    ASSET_SCALE_Y = 0.5

    def scaledasset(name):
        return im.FactorScale(name, ASSET_SCALE_X, ASSET_SCALE_Y)

init python:    
    MIRROR_SCALE_X = 0.4
    MIRROR_SCALE_Y = 0.4

    def mirror(name):
        return im.FactorScale(name, MIRROR_SCALE_X, MIRROR_SCALE_Y)

image danny_present = scaledasset("danny_present.png")
image cat_present = scaledasset("cat_present.png")
image charlie_present = scaledasset("charlie_present.png")
image danny_present_wrapped = scaledasset("danny_present.png")
image cat_present_wrapped = scaledasset("cat_present.png")
image charlie_present_wrapped = scaledasset("charlie_gift.png")
image otter_mirror = mirror ("otter_mirror.png")
image otter_mirror_transparent = mirror ("otter_mirror_transparent.png")
image goldfish_photo = scaledasset("goldfish_photo.png")
image group_photo = scaledasset("group_photo.png")

# Scaled Sprites
init python:    
    SPRITE_SCALE_X = 0.5
    SPRITE_SCALE_Y = 0.5

    def scaledsprite(name):
        return im.FactorScale(name, SPRITE_SCALE_X, SPRITE_SCALE_Y)

init python:    
    RED_SCALE_X = 4
    RED_SCALE_Y = 4

    def redscale(name):
        return im.FactorScale(name, RED_SCALE_X, RED_SCALE_Y)


init:

    image cat_angry = scaledsprite("cat_angry.png")
    image cat_angry2 = scaledsprite("cat_angry2.png")
    image cat_angry3 = scaledsprite("cat_angry3.png")

    image cat_distraught = scaledsprite("cat_distraught.png")

    image cat_frustrated = scaledsprite("cat_frustrated.png")
    image cat_frustrated2 = scaledsprite("cat_frustrated2.png")
    image cat_frustrated3 = scaledsprite("cat_frustrated3.png")

    image cat_happy = scaledsprite("cat_happy.png")
    image cat_happy2 = scaledsprite("cat_happy2.png")
    image cat_happy3 = scaledsprite("cat_happy3.png")

    image cat_neutral = scaledsprite("cat_neutral.png")
    image cat_neutral2 = scaledsprite("cat_neutral2.png")

    image cat_sad = scaledsprite("cat_sad.png")
    image cat_sad2 = scaledsprite("cat_sad2.png")
    image cat_sad3 = scaledsprite("cat_sad3.png")

    image cat_shocked = scaledsprite("cat_shocked.png")
    image cat_shocked2 = scaledsprite("cat_shocked2.png")

    image cat_surprised = scaledsprite("cat_surprised.png")

    image cat_worried = scaledsprite("cat_worried.png")
    image cat_worried2 = scaledsprite("cat_worried2.png")

    image charlie_confused = scaledsprite("charlie_confused.png")
    image charlie_confused2 = scaledsprite("charlie_confused2.png")
    image charlie_confused3 = scaledsprite("charlie_confused3.png")

    image charlie_disgust = scaledsprite("charlie_disgust.png")
    image charlie_disgust2 = scaledsprite("charlie_disgust2.png")

    image charlie_happy = scaledsprite("charlie_happy.png")
    image charlie_happy2 = scaledsprite("charlie_happy2.png")
    image charlie_happy3 = scaledsprite("charlie_happy3.png")

    image charlie_neutral = scaledsprite("charlie_neutral.png")
    image charlie_neutral2 = scaledsprite("charlie_neutral2.png")

    image charlie_sad = scaledsprite("charlie_sad.png")
    image charlie_sad2 = scaledsprite("charlie_sad2.png")

    image charlie_shocked = scaledsprite("charlie_shocked.png")
    image charlie_shocked2 = scaledsprite("charlie_shocked2.png")

    image danny_angry = scaledsprite("danny_angry.png")
    image danny_angry2 = scaledsprite("danny_angry2.png")
    image danny_angry3 = scaledsprite("danny_angry3.png")

    image danny_disgust = scaledsprite("danny_disgust.png")
    image danny_disgust2 = scaledsprite("danny_disgust2.png")
    image danny_disgust3 = scaledsprite("danny_disgust3.png")

    image danny_happy = scaledsprite("danny_happy.png")
    image danny_happy2 = scaledsprite("danny_happy2.png")
    image danny_happy3 = scaledsprite("danny_happy3.png")

    image danny_neutral = scaledsprite("danny_neutral.png")
    image danny_neutral2 = scaledsprite("danny_neutral2.png")
    image danny_neutral3 = scaledsprite("danny_neutral3.png")

    image danny_sad = scaledsprite("danny_sad.png")
    image danny_sad2 = scaledsprite("danny_sad2.png")
    image danny_sad3 = scaledsprite("danny_sad3.png")

    image danny_surprise = scaledsprite("danny_surprise.png")
    image danny_surprise2 = scaledsprite("danny_surprise2.png")
    image danny_surprise3 = scaledsprite("danny_surprise3.png")

    image danny_disgust_smoking = scaledsprite("danny_disgust_smoking.png")
    image danny_disgust_smoking2 = scaledsprite("danny_disgust_smoking2.png")
    image danny_sad_smoking = scaledsprite("danny_sad_smoking.png")
    image danny_sad_smoking2 = scaledsprite("danny_sad_smoking2.png")
    image danny_happy_smoking = scaledsprite("danny_happy_smoking.png")
    image danny_happy_smoking2 = scaledsprite("danny_happy_smoking2.png")
    image danny_neutral_smoking2 = scaledsprite("danny_neutral_smoking.png")
    image danny_shocked_smoking = scaledsprite("danny_shocked_smoking.png")
    image danny_shocked_smoking2 = scaledsprite("danny_shocked_smoking2.png")
    image danny_concerned_smoking = scaledsprite("danny_concerned_smoking.png")
    image danny_concerned_smoking2 = scaledsprite("danny_concerned_smoking2.png")

    image cat_sitting_scared = ("cat_sitting_scared.png")
    image charlie_sitting_neutral = ("charlie_sitting_neutral.png")
    image danny_sitting_speaking = ("danny_sitting_speaking.png")
    image cake = ("cake.png")
    image plates = ("plates.png")
    image plates_food = ("plates_food.png")


    image red = ("red.jpg")
    
# Transforms for Sprites
transform right:
    anchor (0.5, 1.0)
    xalign 1.0
    yalign 1.0
 
transform rightish:
    anchor (0.5, 1.0)
    xalign 0.929
    yalign 1.0

transform left:
    anchor (0.5, 1.0)
    xalign 0
    yalign 1.0

transform slightleft:
    anchor (0.5, 1.0)
    xalign 0.43
    yalign -0.05

transform slightdown:
    anchor (0.5, 1.0)
    xalign 0.6
    yalign 0

transform swipe_left(duration=1.0):
    linear duration xalign -0.5  # move off-screen left

transform jolt:
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 0

transform center_to_right:
    xalign 0.5
    yalign 1.0    
    ease 1.0 xalign 1.0    

transform center_to_left:
    xalign 0.5
    yalign 1.0
    ease 1.0 xalign 0.0

transform right_to_center:
    xalign 1.0
    yalign 1.0
    ease 1.0 xalign 0.5

transform left_to_center:
    xalign 0.0
    yalign 1.0
    ease 1.0 xalign 0.5

transform left_to_right:
    xalign 0.0
    yalign 1.0
    ease 1.0 xalign 1.0

transform right_to_left:
    xalign 1.0
    yalign 1.0
    ease 1.0 xalign 0.0

transform text_shake:
    xoffset 0
    linear 0.02 xoffset -10
    linear 0.02 xoffset 10
    linear 0.02 xoffset -6
    linear 0.02 xoffset 6
    linear 0.02 xoffset 0

# The Game Starts Here
label start:

    scene black
    show screen noise_overlay
    with Fade(3,3,3)

    o "..." 
    
    o "AHHHHHHH!"

    o "Are they...?"

    o "Did I..."

    o "..."

    o "Guys?!"

    o "Oh god, what have I done?!"

    o "Guys! Please stop fucking playing around!"

    o "..."

    o "PLEEEEEEASEEE!!!!!!!!!"

    show black
    with Dissolve(1)


    show screen act_one_text
    pause 3.0
    hide screen act_one_text
    with Dissolve(1)

    ## ACT 1 BEGINS HERE !!! ##

    scene bedroom
    show screen noise_overlay
    show screen time_indicator
    with Dissolve(5)

    play sound "sfx/yawn.mp3" volume 0.5

    pause 1

    "You wake with a sharp breath."
    "Late afternoon light spills through the curtains, and as fast as the nightmare had started, it dissolves into dust..."

label wake_up_menu:

menu:

    "{i}Think about the dream{/i}":
        $ reply = renpy.random.choice(replies)

        o "[reply]"
        jump wake_up_menu

    "{i}Look in the mirror{/i}":
        scene black
        show otter_mirror:
            xalign 0.5
            yalign 0.2
        with Dissolve(1)
        $ reply = renpy.random.choice(replies2)

        o "[reply]"
        scene bedroom
        with Dissolve(1)
        jump wake_up_menu

    "{i}Get out of bed{/i}":
        jump leave_room

label leave_room:

    o "Shit. June 1st already? I'll be expecting them any minute now."

    "The calendar hanging across the room tells you it's June 1st, 2006. Your eighteenth birthday."
    "You've spent weeks imagining today. It has to go well. Your parents won't even be home anytime soon."

    scene black
    with Dissolve(1)

    pause 1

    show doorway
    with Dissolve(1)

    "{i}BRRRRRRRRRING{i}"

    "The doorbell rings through the house, and a familiar voice echoes from outside."

    ch "Otter!!! You up b-day boy? It's us! We're here!"

    "Another voice chimes in."

    c "Otter!" 

    "Then a third."

    d "Open up already, shithead!"

menu:

    "{i}Answer the door{/i}":
        jump answer_door

    "{i}Ignore the door{/i}":
        jump ending_one


label ending_one:

    $ annoying += 1

    with hpunch
    "{i} KNOCK KNOCK {/i}"

    with hpunch
    "{i} KNOCK KNOCK {/i}"
    with hpunch

    d "OTTER! OPEN UP!"

menu:

    "{i}Answer the door{/i}":
        jump answer_door

    "{i}Ignore the door... again{/i}":
        jump ending_one_final


label ending_one_final:

    scene black
    hide screen time_indicator
    with Dissolve(3)

    pause 2

    show ending_one
    show screen ending_text
    with Dissolve(1)

    pause 5

    scene black
    hide screen ending_text
    with Dissolve(5)

    pause 5

    return

label answer_door:

    "You rest your hand on the doorknob. Forcing a smile you don't entirely feel, you pull the door open."

    scene black
    with Dissolve(1)

    pause 1

    $ time_of_day = "2:45 PM"

    show porch
    with Dissolve(1)

    show charlie_happy2
    with Dissolve(0.5)

    if annoying == 1:

        ch "Finally! He emerges! Happy birthday, pal."
        jump skip_intro

    ch "Ahh... he emerges! Happy birthday, pal."

label skip_intro:

    hide charlie_happy2
    show charlie_neutral

    "Charlie has always been easy to read. He's loud and excitable, somehow managing to make everything feel like a bigger deal than it actually is."

    "He's the type to want to capture every little moment."

    hide charlie_neutral
    show cat_shocked
    with Dissolve(0.5)

    c "Jeez, you look terrible. Did you seriously just wake up?"

    hide cat_shocked
    show cat_neutral2

    "Cat's harder to figure out. She's blunt and observant, and has a habit of noticing things you'd rather she didn't."
    "You've never been sure whether she actually likes you or just finds you interesting."

menu:

    "Unfortunately":
        jump unfortunately

    "What's it to you?":
        jump whats_it_to_you

label whats_it_to_you:

    hide cat_neutral2
    show cat_neutral

    o "What's it to you?"

    jump scene_lounge

label unfortunately:

    hide cat_neutral2
    show cat_neutral

    o "Haha. Yeah, unfortunately."

    jump scene_lounge

label scene_lounge:

    hide cat_neutral
    hide cat_angry
    show cat_happy

    "Cat laughs under her breath, though there's a hint of concern. She casually brushes past you into the hallway."

    hide cat_happy
    show danny_neutral2
    with Dissolve(0.5)

    d "Or maybe he just forgot what sleep is."

    hide danny_neutral2
    show danny_happy

    "Danny gives you a playful shove with his shoulder."

    hide danny_happy
    show danny_happy2

    d "Happy birthday, little man."

    hide danny_happy2
    show danny_neutral2

    "Danny's different. You still remember when he used to make your life miserable. It makes it weird to think of him as one of your closest friends now."
    "Music is probably the thing you have most in common. You don't know if there's much else anymore."

    scene black
    with Dissolve(1)

    pause 1

    $ time_of_day = "3:00 PM"

    show lounge_test
    with Dissolve(1)

    "Charlie is already dropping his stuff off onto the dining table, making far more noise than necessary."
    "Somewhere in the kitchen, Cat is opening cupboards."
    "Danny plops himself down onto the couch."

menu:

    "Make yourselves at home":
        jump make_yourselves_at_home

    "{i}Say nothing{/i}":
        jump say_nothing

label say_nothing:

    o "..."

    jump lounge

label make_yourselves_at_home:

    o "Make yourselves at home, I guess."

    $ violence += 1
    $ betrayal += 1

    jump lounge

label lounge:

    show cat_shocked
    with Dissolve(0.5)

    c "Okay. Well we'd better get through these presents before Charlie explodes, man. He's been thinking about your big day for like... two weeks now."

    hide cat_shocked
    show cat_angry2 at center_to_left
    with None

    show charlie_confused3 at right
    with Dissolve(0.5)

    ch "Shut up, Catherine. You little rat."

    hide charlie_confused3
    hide cat_angry2
    with Dissolve(0.5)

    "Charlie is now kneeling on the carpet, trying to organize a pile of presents into something that vaguely resembles a neat stack."

    show charlie_happy2
    with Dissolve(0.5)

    ch "Okay, listen up."

    hide charlie_happy2
    show charlie_neutral

    ch "Some ground rules..."

    hide charlie_neutral
    show charlie_confused3 at center_to_right
    with None

    show cat_angry2 at left
    with Dissolve(0.5)

    c "There's... rules?"

    hide charlie_confused3
    show charlie_confused2 at right
    hide cat_angry2
    show cat_neutral at left

    ch "Yeah! There are now!"

    hide charlie_confused2
    show charlie_disgust at right
    with None

    hide cat_neutral
    show danny_angry3 at left
    with Dissolve(0.5)

    d "Christ."

    hide danny_angry3
    show danny_sad at left

    hide charlie_disgust
    show charlie_happy at right
    
    ch "Number one. Nobody opens presents until everyone's here."

    hide charlie_happy
    hide danny_sad

    show danny_disgust2 at left
    show charlie_confused3 at right

    d "...We are all here."

    hide danny_disgust2
    show danny_disgust at left

    hide charlie_confused3
    show charlie_happy2 at right

    ch "Exactly."

    hide danny_disgust
    hide charlie_happy2

    show charlie_confused3 at right
    show danny_angry3 at left

    d "So that's... that's not a rule."

    hide charlie_confused3
    show charlie_sad at right
    with None

    hide danny_angry3
    show cat_surprised at left
    with Dissolve(0.5)

    c "It's more of an observation, really..."

    hide cat_surprised
    show cat_neutral2 at left

    hide charlie_sad
    show charlie_disgust2 at right

    ch "Screw you guys!"

    hide charlie_disgust2
    show charlie_happy3 at right_to_center
    with None

    hide cat_neutral2
    with Dissolve(0.5)

    ch "Anyway, number two. Otter gets to decide everything we do today. Birthday privilege."

    hide charlie_happy3
    show charlie_neutral2

    ch "So, what'll it be first?"

    hide charlie_neutral2
    show charlie_neutral

menu:
    "{i}Take a photo{/i}":
        jump take_photo

    "{i}Listen to music{/i}":
        jump listen_music

    "{i}Play a game{/i}":
        jump play_game

label take_photo:

    $ charlie_bond +=1

    hide charlie_neutral
    show charlie_shocked

    o "Can we get a picture first?"

    hide charlie_shocked
    show charlie_happy2

    ch "Score! One for the scrapbook."

    hide charlie_happy2
    with Dissolve(0.5)

    "Everyone awkwardly squeezes together in the living room."

    show white
    with Dissolve(0.05)

    pause 0.15

    hide white
    show group_photo:
        xalign 0.5
        yalign 0.35
    with Dissolve(1)

    "The flash blinds you for a moment, burning white into your vision before it fades to reveal the photograph."

    "You can't remember the last time you all looked this happy."

    hide group_photo
    with Dissolve(1)

    show charlie_confused2
    with Dissolve(0.5)

    ch "Here, if I just shake it around it'll develop faster."

    hide charlie_confused2
    show charlie_confused3 at center_to_right

    show cat_angry3 at left
    with Dissolve(0.5)

    c "You know that's a myth, right? It doesn't do anything."

    hide cat_angry3
    show cat_shocked at left
    hide charlie_confused3
    show charlie_disgust2 at right

    ch "You're a total myth! You don't really do anything!"

    hide charlie_disgust2
    show charlie_confused at right
    hide cat_shocked
    show cat_angry at left

    "Cat rolls her eyes."

    hide charlie_confused
    show charlie_happy2 at right_to_center
    with None

    hide cat_angry
    with Dissolve(0.5)

    ch "Anyway, I'll just slip this in your pocket. Make sure to check back on it later."

    $ polaroid += 1

    hide charlie_happy2
    show charlie_happy3
    with None

    jump present_intro

label listen_music:

    hide charlie_neutral
    show charlie_shocked

    o "Let's play some music."

    $ danny_bond += 1

    hide charlie_happy2
    hide charlie_neutral
    hide charlie_shocked
    show danny_happy3
    with Dissolve(0.5)

    d "Now we are fuckin' talkin'!"

    hide danny_happy3
    with Dissolve(0.5)

    "You observe Danny as he kneels in front of the CD rack, an overflowing clutter packed with handwritten labels."

    show danny_neutral2
    with Dissolve(0.5)

    d "Wanna chuck on one of our mixes or listen to something a bit different?"

    hide danny_neutral2
    show danny_neutral

menu:
    "Danny's mix":
        jump dannys_mix

    "Charlie's mix":
        jump charlies_mix

    "Cat's mix":
        jump cats_mix

    "Something new":
        jump something_new

label dannys_mix:

    $ danny_bond += 1

    hide danny_neutral
    show danny_surprise2

    o "Let's put your one on."

    hide danny_surprise2
    show danny_happy3

    d "Correct answer."

    hide danny_happy3
    with Dissolve(0.5)

    "The room fills with old rock music. It's louder, rougher, and older than anything the rest of you usually listen to."

    "Danny drums his fingers to the beat absentmindedly, while Charlie complains that it's 'dad music'."

    show danny_disgust at left
    show charlie_confused3 at right
    with Dissolve(0.5)

    d "You just don't appreciate the classics."

    hide danny_disgust
    show danny_angry2 at left
    hide charlie_confused3
    show charlie_disgust2 at right

    ch "What, are you forty?"

    jump turn_the_music_off

label charlies_mix:

    $ charlie_bond += 1

    hide danny_neutral
    show danny_surprise2

    o "Let's put Charlie's one on."

    hide danny_surprise2
    show danny_disgust at center_to_left
    with None

    show charlie_happy3 at right
    with Dissolve(0.5)

    ch "...Seriously? Aw, thanks!"

    hide charlie_happy3
    show charlie_confused3 at right
    hide danny_disgust
    show danny_angry2 at left

    d "Really? Again?"

    hide danny_angry2
    hide charlie_confused3
    with Dissolve(0.5)

    "Everyone starts humming along to the comfortable tunes almost immediately."

    "Charlie laughs every time someone gets a line wrong, insisting they should know all this already, and for a little while, it feels impossible to imagine any of you anywhere else."
        
    jump turn_the_music_off

label cats_mix:

    hide danny_neutral
    show danny_surprise2

    $ cat_bond += 1

    o "Let's put Cat's one on."

    hide danny_surprise2
    show cat_shocked
    with Dissolve(0.5)

    c "You gotta hand it to him, he's got taste."

    hide cat_shocked
    with Dissolve(0.5)

    "The music that spills into the room is raw and emotional, unlike anything the others would've picked."

    "Charlie wrinkles his nose up while Danny quietly nods along to the rhythm."

    "Cat doesn't seem interested in whether anyone else likes it, and casually leans back, closes her eyes, and takes it all in."

    show cat_surprised
    with Dissolve(0.5)

    c "I like songs that really feel like they have something to say."

    hide cat_surprised
    show cat_happy

    c "...Gerard Way always has something important to say."

    jump turn_the_music_off

label something_new:

    $ acceptance += 1

    hide danny_neutral
    show danny_surprise2

    o "Let's put on something new."

    hide danny_surprise2
    show danny_surprise

    d "Wow. That's... surprising."

    hide danny_surprise
    show danny_disgust3

    d "Hmm... let's try this one."

    hide danny_disgust3
    with Dissolve(0.5)

    "A tune fills the space around you, and is clearly something that your parents listen to."

    "It's not unpleasant, and the four of you find yourselves getting lost in the gentle rhythm."

    "You swear you've heard this song somewhere before."

    jump turn_the_music_off

label turn_the_music_off:

    hide cat_happy
    hide danny_angry2
    hide charlie_disgust2
    with Dissolve(0.5)

    "Charlie turns the music off."

    show charlie_happy3
    with Dissolve(0.5)

    jump present_intro

label play_game:

    $ cat_bond += 1

    hide charlie_neutral
    show charlie_shocked

    o "Let's play a game, I suppose."

    hide charlie_shocked
    with Dissolve(0.5)

    "Cat leans back in her chair, looking between the three of you."

    show cat_neutral
    with Dissolve(0.5)

    c "Otter, truth or dare?"

menu: 
    "Truth":
        jump truth

    "Dare":
        jump dare

label truth:

    hide cat_neutral
    show cat_happy

    o "Truth, I guess."

    hide cat_happy
    show cat_surprised

    c "What do you actually think of us?"

    hide cat_surprised
    with Dissolve(0.5)

    "The question catches you off guard. You know what they're asking, but when you try to put it into words, your mind comes up strangely blank."
    "For some reason, that's a weirdly difficult question."

    show charlie_happy3
    with Dissolve(0.5)

    ch "That pause is brutal, dude!"

    hide charlie_happy3
    show danny_surprise3
    with Dissolve(0.5)

    d "Yeah, man. You hate us that much?"

    hide danny_surprise3
    show danny_surprise2

    o "Uhh..."
    o "You're cool."

    hide danny_surprise2
    show cat_shocked
    with Dissolve(0.5)

    c "Haha, reassuring..."

    hide cat_shocked
    show charlie_happy2
    with Dissolve(0.5)

    jump present_intro

label dare:

    hide cat_neutral
    show cat_happy

    o "Dare, I guess."

    hide cat_happy
    show cat_surprised

    c "I dare you to tell us something you've never told anyone else."
    
    hide cat_surprised
    show cat_angry2 at center_to_left
    with None

    show charlie_disgust2 at right
    with Dissolve(0.5)

    ch "Uhh... that's a truth, silly Cat. Not a dare."

    hide charlie_disgust2
    show charlie_happy3 at right_to_center
    with None

    hide cat_angry2
    with Dissolve(0.5)

    ch "I dare you to let me cut your hair!"

    hide charlie_happy3
    show charlie_sad

    o "Don't even think about it."

    hide charlie_sad
    show charlie_happy2

    ch "Just a little snip?"

    hide charlie_happy2
    show charlie_sad

    o "No."

    hide charlie_sad
    show charlie_confused3

    ch "A teeny tiny one? An inch?"

menu:

    "Not a chance":
        hide charlie_confused3
        show charlie_disgust
        o "Not a chance."
        jump dare_two

    "Only if I can cut yours":
        hide charlie_confused3
        show charlie_disgust
        o "Only if I can cut yours."
        jump dare_two

label dare_two:

    hide charlie_disgust
    show danny_disgust3
    with Dissolve(0.5)

    d "A shame. I think you're long overdue."

    hide danny_disgust3
    show cat_surprised
    with Dissolve(0.5)

    c "Yeah, how long has it been, years?"

    hide cat_surprised
    show cat_worried

    c "Probably for the best though, I don't think Charlie would do you much justice."

    hide cat_worried
    show cat_neutral at center_to_left
    with None

    show charlie_disgust2 at right
    with Dissolve(0.5)

    ch "Hey!!!"

    hide charlie_disgust2
    show charlie_happy3 at right_to_center
    with None

    hide cat_neutral
    show charlie_happy3
    with Dissolve(0.5)

    jump present_intro


label present_intro:

    ch "Okay, enough messing around. It's present time!"

    jump act_two


## ACT 2 BEGINS HERE !!! ##


label act_two:

    scene black
    hide charlie_happy3
    hide screen time_indicator
    with Dissolve(1)

    pause 1

    show screen act_two_text
    pause 3.0
    hide screen act_two_text
    with Dissolve(1)

    ## ACT 1 BEGINS HERE !!! ##

    $ time_of_day = "3:30 PM"
    show screen time_indicator
    scene lounge_two
    show screen noise_overlay
    with Dissolve(1)

    "Charlie rubs his hands together before hurrying everyone onto the carpet. The pile of presents sits proudly in the middle of the living room."

    show danny_disgust2 at left
    show charlie_neutral at right
    with Dissolve(0.5)

    d "Charlie, quit staring."

    hide danny_disgust2
    hide charlie_neutral
    show danny_sad2 at left
    show charlie_confused2 at right

    ch "I'm making sure they look nice."

    hide charlie_confused2
    hide danny_sad2
    show charlie_confused3 at right
    show danny_angry3 at left

    d "Oh my god, they're just presents."

    hide danny_angry3
    hide charlie_confused3
    show danny_sad at left
    show charlie_happy2 at right

    ch "Exactly."

    hide danny_sad
    show danny_surprise2 at left_to_right
    with None

    hide charlie_happy2

    pause 0.25

    show cat_surprised at left
    with Dissolve(0.5)

    c "He ironed the wrapping paper."

    hide cat_surprised
    show cat_neutral2 at left
    with None

    hide danny_surprise2
    show charlie_disgust2 at right
    with Dissolve(0.5)

    ch "...I did not!"

    hide cat_neutral2
    hide charlie_disgust2
    show cat_shocked at left
    show charlie_confused3 at right

    c "You totally thought about it."

    hide charlie_confused3
    hide cat_shocked
    with Dissolve(0.5)

    "Charlie rolls his eyes, though the corners of his mouth curl into a smile anyway."

    show charlie_happy2
    with Dissolve(0.5)

    ch "Alright, pick one."

    hide charlie_happy2
    with Dissolve(0.5)

    "Charlie's is wrapped almost perfectly, every fold crisp enough that it feels wrong to tear it open."

    "Cat's has been wrapped in newspaper and held together with a thin string, tied into a bow at one end. There's a doodle of a cat in the corner."

    "Danny's isn't wrapped at all, and is instead a cardboard box with HAPPY BIRTHDAY, OTTER scrawled across the side in black marker."

    show danny_surprise
    with Dissolve(0.5)

    d "What? I'm just saving money. You cannot blame me for that."

    hide danny_surprise
    show danny_angry2 at center_to_right
    with None

    show cat_frustrated3 at left
    with Dissolve(0.5)

    c "Or maybe you're just lazy?"

    hide cat_frustrated3
    show cat_angry at left
    with None

    hide danny_angry2
    show charlie_disgust at right
    with Dissolve(0.5)

    ch "Enough, you two."

    hide charlie_disgust
    show charlie_happy3 at right_to_center
    with None

    hide cat_angry
    with Dissolve(0.5)
    
    ch "Which is first, Otter?"

    jump present_menu

label present_menu_intro:

    if presents_opened == 3:
        jump post_presents

    hide cat_shocked
    hide charlie_confused3
    hide danny_disgust
    show charlie_happy3
    with Dissolve(0.5)

    ch "Ahem...  anyway. Whose is next?"

label present_menu:

menu:

    set char_menu

    "Charlie's present":
        jump charlie_present

    "Cat's present":
        jump cat_present

    "Danny's present": 
        jump danny_present


label charlie_present:

    if presents_opened ==0:
        $ charlie_bond += 2
    else:
        $ charlie_bond +=1
    
    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "Let's open yours."

    if presents_opened == 1:

        hide charlie_shocked
        show charlie_happy3

        ch "Otter. You flatter me, you really do."

        hide charlie_happy3
        show charlie_confused

        ch "I totally didn't persuade you to choose mine first or anything... did I?"

        hide charlie_confused
        show charlie_happy2

        ch "Ah, besides the point. Open it, open it!!!"

    if presents_opened > 1:
        
        hide charlie_shocked
        show charlie_neutral2

        ch "Open it, open it!!!"

    hide charlie_neutral2
    hide charlie_happy2
    with Dissolve(1)

    show charlie_present:
        xalign 0.5
        yalign 0.4
        zoom 0.8
    with Dissolve(2)

    "You carefully peel away the wrapping paper, revealing a thick photo album."

    "The first few pages are already filled with photographs from previous birthdays, school trips, and memories you'd long since forgotten."

    show charlie_neutral
    hide charlie_present
    with Dissolve(1)

    o "You... kept all these?"

    hide charlie_neutral
    show charlie_happy2

    ch "Somebody had to! Besides, eighteen is a HUGE deal!"

    hide charlie_happy2
    show charlie_confused3

    ch "I figured, after this, you'll need something to really remember us by."

    $ char_menu.add("Charlie's present")

menu:

    "How so?":
        o "How so?"
        $ betrayal += 1
        $ acceptance += 1
        jump present_menu_intro

    "Remember you by?":
        o "To remember you by? Where are you going?"
        $ betrayal += 1
        jump present_menu_intro

    "Where the fuck are you going?!":
        o "Where the fuck are you going?!"
        $ betrayal += 1
        $ violence += 1
        jump present_menu_intro

if presents_opened < 3:
    jump present_menu_intro

label cat_present:

    if presents_opened ==0:
        $ cat_bond += 2
    else:
        $ cat_bond +=1
    
    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "I'll open Cat's."

    hide charlie_shocked
    show cat_happy
    with Dissolve(0.5)

    c "Cool, man. I hope you like it."

    hide cat_happy
    with Dissolve(1)

    show cat_present:
        xalign 0.5
        yalign 0.35
        zoom 0.8
    with Dissolve(2)

    "Layers of newspaper slowly give way to a cassette player. A new tape already sits inside."

    show cat_surprised
    hide cat_present
    with Dissolve(1)

    c "It's nothing really... just some new music I thought you might like while we're apart."

    hide cat_surprised
    show cat_neutral

    $ char_menu.add("Cat's present")

menu:

    "While we're apart?":
        o "While we're apart?"
        $ acceptance += 1

        hide cat_neutral
        show cat_shocked

        c "Umm... well, yeah."
        jump present_menu_intro   

    "Are you leaving me?":
        o "Are you leaving me?"
        $ betrayal += 1

        hide cat_neutral
        show cat_shocked
        
        c "Umm... well, yeah."
        jump present_menu_intro

    "Where are you going?!":
        o "Where are you going?!"
        $ betrayal += 1
        $ violence += 1

        hide cat_neutral
        show cat_shocked
        
        c "Uhh... what?"
        jump present_menu_intro

label danny_present:

    if presents_opened ==0:
        $ danny_bond += 2
    else:
        $ danny_bond +=1

    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "Let's try Danny's."

    hide charlie_shocked
    show danny_disgust
    with Dissolve(0.5)

    d "Didn't wrap it. Sorry."

    hide danny_disgust
    show danny_angry2 at center_to_left
    with None

    show charlie_confused2 at right
    with Dissolve(0.5)

    ch "We can see that..."

    hide charlie_confused2
    hide danny_angry2
    with Dissolve(1)

    show danny_present:
        xalign 0.5
        yalign 0.4
        zoom 0.8
    with Dissolve(2)

    "Inside sits a vintage polaroid camera. A 600 series from what looks like the early 1980s. It's in excellent condition."

    hide danny_present
    with Dissolve(1)

    show danny_neutral2
    with Dissolve(1)

    o "Where did you even find this?"

    hide danny_neutral2
    show danny_disgust2

    d "Garage sale."

    hide danny_disgust2
    show danny_happy3

    d "Thought you could keep us updated while we're gone."

    hide danny_happy3
    show danny_neutral2

    $ char_menu.add("Danny's present")

menu:

    "Gone?":
        o "Gone?"
        $ acceptance += 1

        hide danny_neutral2
        show danny_disgust

        d "Uhh... well, yeah."
        jump present_menu_intro    

    "Update you on what?":

        hide danny_neutral2
        show danny_disgust

        o "Update you on what?"
        $ betrayal += 1

        jump present_menu_intro   

    "What the fuck?!":

        hide danny_neutral2
        show danny_disgust

        o "What the fuck? Where are you going?!"
        $ betrayal += 1
        $ violence += 1

        jump present_menu_intro   

label post_presents:

    $ time_of_day = "4:00 PM"

    hide cat_shocked
    hide charlie_confused3
    hide danny_disgust
    hide charlie_happy3
    show cat_worried
    with Dissolve(0.5)

    c "Otter, you're concerning us."

    hide cat_worried
    show charlie_sad2
    with Dissolve(0.5)

    ch "Yeah... I mean, I know you don't want to think about us leaving but..."

    hide charlie_sad2
    show charlie_confused3

    ch "It's like you've never even heard of these plans before?"

menu:
    "Plans?":
        jump post_presents_two

    "Leaving?":
        jump post_presents_two

label post_presents_two:

    hide charlie_confused3
    show charlie_shocked

    o "Plans? Leaving? What are you talking about?!"

    hide charlie_shocked
    with Dissolve(0.5)

    "The room falls silent. Charlie's voice wavers slightly as he speaks."

    show charlie_sad2
    with Dissolve(0.5)

    ch "Well... uhh... pretty much..."

    hide charlie_sad2
    show cat_surprised
    with Dissolve(0.5)

    c "We're moving away next week. We all got into Columbia."

    hide cat_surprised
    show charlie_happy3
    with Dissolve(0.5)

    ch "...But! It's nothing against you or anything!"

    hide charlie_happy3
    show charlie_confused2

    ch "We knew you didn't really care about college and we didn't want to make you feel..."

    hide charlie_confused2
    show danny_disgust
    with Dissolve(0.5)

    d "Like we were abandoning you."

    hide danny_disgust
    show danny_angry2 at center_to_left
    with None

    show charlie_disgust2 at right
    with Dissolve(0.5)

    ch "Stop interrupting me! I can speak for myself!"

    hide charlie_disgust2
    hide danny_angry2
    with Dissolve(0.5)

    "Charlie opens and closes his mouth like a gaping fish, desperately trying to find the right words to say. His shoulders slump."

    show charlie_confused3
    with Dissolve(0.5)

    ch "Yeah... We have been over this a few times now, though..."

    hide charlie_confused3
    with Dissolve(0.5)

    "There's no way they've told you this before, you would definitely remember something this important."

    "You look from Charlie to Cat... then Danny... waiting for someone to laugh, to say it's a joke, that they'd all decided to mess with you on your birthday."

    "No one laughs."
    "The day that was supposed to be special suddenly just feels suffocating."

    show cat_worried
    with Dissolve(0.5)

    c "Otter?"

    hide cat_worried
    with Dissolve(0.5)

    "The words seem to stretch out, becoming distant and muffled as the room begins to lose shape."
    "Columbia. You hear it again, but no one is speaking."
    "It's the same word from the dream, buried all the way underneath the screaming. You can see the table again. The cake. Your friends slumped over in their seats."
    "You're staring at the people you love, watching them disappear one by one, and somewhere in the back of your mind you can hear yourself saying the same thing over and over..."
    "...It wasn't my fault."

    "The room snaps back into focus and you realise you still haven't spoken."

    o "I... I don't know what to say."

    o "You're all leaving."

menu:

    "I'm happy for you" (disabled=violence >= 4) if violence < 4:
        jump happy_for_you

    "{color=#956dc9}I'm happy for you{/color}" (disabled=violence >=4) if violence >= 4:
        jump why_didnt_you_tell_me

    "Why didn't you tell me?!" (disabled=violence >= 4) if violence < 4:
        jump why_didnt_you_tell_me

    "{color=#956dc9}Why didn't you tell me?!{/color}" (disabled=violence >= 4) if violence >= 4:
        jump why_didnt_you_tell_me

    "Fuck all of you" (disabled=violence < 4) if violence >= 4:
        jump fuck_all_of_you   

    "{color=#956dc9}Fuck all of you{/color}" (disabled=violence < 4) if violence < 4:
        jump fuck_all_of_you   
        

label happy_for_you:

    $ acceptance += 2

    "You force a smile."

    o "I'm happy for you. You'll have a great time at Columbia."

    show danny_surprise
    show charlie_shocked at right
    show cat_shocked2 at left
    with Dissolve(0.5)

    "The others seem surprised, like they didn't expect that outcome."

    hide danny_surprise
    hide charlie_shocked
    show charlie_happy3 at right_to_center
    with None

    hide danny_surprise
    hide cat_shocked2
    with Dissolve(0.5)

    jump post_presents_outro

label why_didnt_you_tell_me:

    $ betrayal += 2

    o "So... You're all leaving me."

    show danny_surprise
    show charlie_shocked at right
    show cat_shocked2 at left
    with Dissolve(0.5)

    o "Why didn't you say anything? Why didn't you tell me?!"
    
    hide danny_surprise
    show danny_disgust2
    with None

    hide charlie_shocked
    hide cat_shocked2
    with Dissolve(0.5)

    d "Hey, man. It's not like that. We did-"

    hide danny_disgust2
    show danny_surprise

    o "Cut the shit! You've never told me anything!"

    hide danny_surprise
    show charlie_happy3
    with Dissolve(0.5)

    jump post_presents_outro

label fuck_all_of_you:

    $ betrayal += 2
    $ violence += 1

    show danny_surprise
    show charlie_shocked at right
    show cat_shocked2 at left
    with Dissolve(0.5)

    o "You're just gonna drop this on me now and expect me to be okay with it?! Fuck you guys."

    hide danny_surprise
    show danny_disgust2
    with None

    hide charlie_shocked
    hide cat_shocked2
    with Dissolve(0.5)

    d "Hey, man. It's not like that. We did-"

    hide danny_disgust2
    show danny_surprise

    o "Cut with the shit! You've never told me anything!"

    hide danny_surprise
    show cat_sad2
    with Dissolve(0.5)

    c "Charlie said he thought..."

    hide cat_sad2
    show cat_worried

    c "Something like this might happen..."

    hide cat_worried
    show cat_sad2

menu:  
    "What's that supposed to mean?":
        jump fuck_all_of_you_two

    "What the fuck?":
        jump fuck_all_of_you_two

    "{color=#956dc9}Like what?{/color}" (disabled=True):
        pass

label fuck_all_of_you_two:

    hide cat_sad2
    show cat_worried

    $ violence += 1

    o "What the fuck is that supposed to mean?"

    hide cat_worried
    show cat_frustrated at center_to_left
    with None

    show charlie_disgust2 at right
    with Dissolve(0.5)

    ch "Cat, why did you say that?!"

    hide charlie_disgust2
    show charlie_happy3 at right_to_center
    with None

    hide cat_frustrated
    with Dissolve(0.5)

    ch "Hey, it's just... You kinda do have a tendency to..."

    hide charlie_happy3
    show charlie_sad

    ch "Ah... never mind."

    jump post_presents_outro_two

label post_presents_outro:

    ch "Hey, we'll still keep in touch! See each other on breaks and such?"

    hide charlie_happy3
    show charlie_sad

    o "Yeah... I guess."

    jump post_presents_outro_two

label post_presents_outro_two:

    $ time_of_day = "4:15 PM"

    hide charlie_sad
    with Dissolve(0.5)

    "The conversation never recovers."

    "Charlie quietly excuses himself, muttering something about needing some air before disappearing through the sliding door into the backyard."

    "Danny pats his pockets and leaves out the balcony, clearly hinting at having a smoke."

    "Cat lingers for a moment before slipping down the hallway out of sight."

    "You remain alone in the living room, surrounded by birthday decorations."

label find_somebody_else:

menu:

    set char_menu

    "{i}Follow Charlie{/i}":
        $ time_of_day = "4:30 PM"
        jump follow_charlie

    "{i}Follow Cat{/i}":
        $ time_of_day = "4:30 PM"
        jump follow_cat

    "{i}Follow Danny{/i}":
        $ time_of_day = "4:30 PM"
        jump follow_danny

    "{i}Take a minute alone{/i}":
        jump stay_where_you_are

label follow_charlie:

    scene black
    with Dissolve(1)

    pause 1

    $ charlie_bond += 1

    show back_porch:
        xalign 0.5
        yalign 0.55
    
    with Dissolve(1)

    "You slide the back door open and the warm summer air immediately wraps around you. Charlie sits on the porch, looking at a picture in his wallet. He notices you almost immediately."

    show charlie_happy3
    with Dissolve(0.5)

    ch "Oh... hey!"

    hide charlie_happy3
    show charlie_confused3

    ch "Sorry about earlier, when we told you bef-"

    hide charlie_confused3
    show charlie_happy3

    ch "I mean, I really should've said something sooner. Sorry."

menu:

    "It's alright":
        hide charlie_happy3
        show charlie_neutral
        o "It's alright, Charlie."
        $ acceptance += 1
        jump charlie_path_two

    "You really should have":
        hide charlie_happy3
        show charlie_sad
        o "Yep. You really should have."
        $ betrayal += 1
        $ violence += 1
        jump charlie_path_two

label charlie_path_two:

    hide charlie_sad
    hide charlie_neutral
    with Dissolve(1)
    
    pause 0.5

    show goldfish_photo:
        rotate 0
        xalign 0.5
        ypos -150
    with Dissolve(1)

    "Charlie looks down, distractedly admiring the photograph of you two and the goldfish you were so attached to. You couldn't have been older than twelve."

    ch "Hey, remember this little guy? Bubbles... or... was it Goldie?"

    o "..."

    ch "You just scooped him out of the bag and ate him whole. It was crazy!"

    o "He was already dead..."

    ch "Ahh... I don't think he was."

    ch "...But I guess kids do weird stuff, right?"

    o "..."

    hide goldfish_photo
    with Dissolve(1)

    pause 0.5

    show charlie_happy3
    with Dissolve(1)

    ch "You know, I always thought we'd end up like this."

menu: 

    "Like what?":
        jump charlie_path_three

    "{color=#956dc9}Together?{/color}" (disabled=True) if charlie_bond < 3:
        pass

    "Together?" if charlie_bond >= 3:
        jump charlie_love

label charlie_love:

    hide charlie_happy3
    show charlie_shocked

    $ charlie_love +=1

    o "...Together?"

    hide charlie_shocked
    show charlie_happy3

    ch "Ahh... well, still together after graduation, looking back. It felt like it came way too soon..."

    jump charlie_menu

label charlie_path_three:

    hide charlie_happy3
    show charlie_neutral2

    ch "Still together after graduation, looking back. It felt like it came way too soon..."

    $ charlie_not_love += 1

    jump charlie_menu

label charlie_menu:

    hide charlie_neutral2
    hide charlie_happy3
    show charlie_neutral

menu:

    "Promise we'll stay friends?":
        o "Promise me we'll stay friends?"
        $ acceptance += 2
        jump charlie_path_four

    "Now you're leaving me" if charlie_love < 1:
        hide charlie_neutral
        show charlie_sad
        o "...Now you're leaving me."
        $ betrayal += 1
        jump charlie_path_five

    "{color=#956dc9}Could it be anything more?{/color}" (disabled=True) if charlie_love < 1:
        o "Could it be anything more?"
        pass

    "Could it be anything more?" if charlie_love > 0:
        hide charlie_neutral
        show charlie_shocked
        $ charlie_love +=1
        o "Could it be anything more?"
        jump charlie_path_five


label charlie_path_four:

    hide charlie_shocked
    hide charlie_sad
    hide charlie_neutral
    show charlie_happy

    "Charlie smiles, the warm glow in his eyes promising you that he wouldn't have it any other way."

    hide charlie_happy
    show charlie_neutral2

    ch "I promise."


label charlie_path_five:

    hide charlie_neutral2
    hide charlie_shocked
    hide charlie_sad
    hide charlie_neutral
    with Dissolve(0.5)

    "His smile seems to fade as soon as it came, and he lets out a quiet breath through his nose and closes his wallet with a soft thud."
    "His eyes stay fixed on the garden."

    show charlie_happy3
    with Dissolve(0.5)

    ch "Actually, there's something I wanted to tell you."

    hide charlie_happy3
    show charlie_sad

    ch "..."

    hide charlie_sad
    show charlie_sad2

    ch "It's stupid, but... well..."

    hide charlie_sad2
    show charlie_confused2

    ch "...I think I like Cat?"

    hide charlie_confused2
    show charlie_sad

    "For just a second, everything else fades into the background. Even Charlie, who's suddenly far more interested in his own shoes than your reaction."

    if charlie_love > 1:
        $ betrayal += 1
        "After what you'd just confessed, you feel a little humiliated."

    hide charlie_sad
    show charlie_confused3

    ch "Trust me, I know how ridiculous that sounds."

    hide charlie_confused3
    show charlie_shocked2

    ch "We've been friends forever, and I still can't tell whether she actually likes me or if she's just... Cat?"

    hide charlie_shocked2
    show charlie_confused2

    ch "Half the time I can't even tell what she's thinking."

    hide charlie_confused2
    show charlie_confused

menu:
    "Thanks for telling me" if charlie_love < 2:
        hide charlie_confused
        show charlie_neutral
        o "Wow... Thanks for confiding in me. I won't tell anyone."
        jump thanks_otter

    "That's not a good idea":
        $ betrayal += 1
        $ violence += 1
        hide charlie_confused
        show charlie_sad
        o "That's not a good idea. I know she doesn't like you."
        jump charlie_heartbreak

    "{i}Try to sound happy for him{/i}" if charlie_love == 2:
        o "Oh... er... good for you, man."
        $ betrayal += 1
        jump thanks_otter

label thanks_otter:

    hide charlie_neutral
    hide charlie_confused
    show charlie_neutral2

    ch "Thanks, Otter. I knew I could count on you."
    
    jump charlie_path_outro

label charlie_heartbreak:

    $ charlie_bond = -999
    hide charlie_sad
    show charlie_sad2

    ch "Oh... uh... okay." 

    hide charlie_sad2
    show charlie_sad

    ch "I see..."

    jump charlie_path_outro

label charlie_path_outro:

    hide charlie_neutral2
    hide charlie_sad
    show charlie_happy3

    ch "Anyway, let's go back inside, huh? I heard there's some cake just begging to be eaten!"

    jump act_three

label follow_cat:

    scene black
    with Dissolve(1)

    pause 1

    $ cat_bond +=1

    show bedroom
    with Dissolve(1)

    "You make your way down the hallway, noting that the door to your bedroom is already half open. Cat stands by the window, her back to you."
    "She notices your reflection in the glass before she hears your footsteps."

    show cat_sad
    with Dissolve(0.5)

    c "Look, Otter... I'm really sorry we're leaving."

menu:

    "It's alright":
        jump its_alright

    "You can't leave":
        jump you_cant_leave

    "Some notice would've been nice":
        jump some_notice

label its_alright:

    $ acceptance += 1

    hide cat_sad
    show cat_neutral

    o "Ah... it's alright."

    jump cat_route_two

label you_cant_leave:

    $ betrayal += 1
    $ violence += 1

    hide cat_sad
    show cat_worried

    o "You can't leave. You can't..."

    hide cat_worried
    show cat_sad3

    c "Otter, we really have to go."

    jump cat_route_two

label some_notice:

    $ betrayal += 1
    $ violence += 1

    hide cat_sad
    show cat_sad2

    o "Yeah, some notice would've been nice."

    hide cat_sad2
    show cat_worried

    c "Ah... yeah. Right."
    
    jump cat_route_two

label cat_route_two:

    hide cat_worried
    hide cat_sad3
    hide cat_neutral
    show cat_sad

    c "I'm really gonna miss you. You're one of the most interesting people I know."

    o "That's not true. You don't even know me."

    hide cat_sad
    show cat_angry

    c "Maybe I do, at least more than you think."

    hide cat_angry
    show cat_surprised

    c "I remember when we first met. You were always doing something weird. You'd say something completely insane and then just stare at everyone like you couldn't understand why they were laughing."

    hide cat_surprised
    show cat_worried

    c "I used to think that was just your humour... that was, until your dog died."

    hide cat_worried
    show cat_distraught

    c "You invited us over for some kind of impromptu gaming session and told us that your crying family was just 'being dramatic.'"

    hide cat_distraught
    show cat_sad2

    c "Did you even cry? Did you even care?"

menu:

    "Crying wouldn't change anything":
        o "It's not like crying would've changed anything."
        jump cat_route_three

    "That dog was annoying":
        o "So what? He was annoying."
        jump cat_route_three

label cat_route_three:

    hide cat_sad2
    show cat_worried2

    c "Uh..."

    hide cat_worried2
    show cat_surprised

    c "I just mean... most people are sad when they lose something they love."

    hide cat_surprised
    show cat_shocked2

    o "I was sad."

    hide cat_shocked2
    show cat_shocked

    c "Were you? You didn't act like it."

    hide cat_shocked
    show cat_worried

    o "What was I supposed to do?"

    hide cat_worried
    show cat_distraught

    c "I don't know... mourn him? Talk about it?"

    hide cat_distraught
    show cat_sad2

menu:

    "I didn't know how":
        jump didnt_know_how

    "I don't feel things like you":
        jump dont_feel_things

label didnt_know_how:

    hide cat_sad2
    show cat_shocked2

    o "I just... didn't know how. I've never known how."

    "The words feel heavy on your tongue and, for a moment, Cat doesn't say anything at all. The usual teasing expression on her face disappears, replaced by something closer to understanding. You hate looking weak."

    hide cat_shocked2
    show cat_shocked

    c "What do you mean?"

    hide cat_shocked
    show cat_sad

    o "Something has always been wrong with me."

    hide cat_sad
    show cat_sad2

    c "Otter..."

    hide cat_sad2
    show cat_sad3

    c "You should've told someone sooner."

    hide cat_sad3
    show cat_sad

    o "Who? Everyone calls me creepy. Even you."

    hide cat_sad
    show cat_surprised

    c "Yeah well... You are a little creepy."

    hide cat_surprised
    show cat_happy

    c "But you're my creepy friend."

menu:

    "Thanks, I guess":
        o "Thanks, I guess."
        jump cat_route_four

    "{color=#956dc9}Just friends?{/color}" (disabled=True) if cat_bond < 4:
        pass

    "Just friends?" if cat_bond >= 4:
        jump just_friends

label just_friends:
    $ cat_love += 1

    hide cat_happy
    show cat_shocked

    o "Are we just friends?"

    "The question comes out quieter than you intended. For once, Cat doesn't immediately make a joke."

    hide cat_shocked
    show cat_surprised

    c "Do you want us to be?"

    hide cat_surprised
    show cat_happy

    o "I don't know."

    hide cat_happy
    show cat_happy2

    c "That sounds a lot like you."

    hide cat_happy2
    show cat_happy3

    c "Maybe let's figure it out together."

    jump cat_route_four

label cat_route_four:

    hide cat_happy
    hide cat_happy3
    show cat_neutral

    c "Hmm... I'm gonna miss you, Otter."

    hide cat_neutral
    show cat_sad3

    c "I just wish we had more time."

    hide cat_sad3
    show cat_sad2

menu:

    "Me too":
        jump me_too

    "Then why are you leaving me?":
        jump leaving_me

label leaving_me:

    $ betrayal += 1

    o "Then why are you leaving me?"

    hide cat_sad2
    show cat_surprised

    c "I couldn't pass up an opportunity like Columbia, you know that."

    hide cat_surprised
    show cat_sad2

    c "I'm just sorry you... found out so late."

    jump cat_path_outro

label me_too:

    $ acceptance += 1

    o "Me too."

    hide cat_sad2
    hide cat_surprised
    show cat_happy2

    "Cat smiles warmly."

    jump cat_path_outro

label dont_feel_things:

    hide cat_sad2
    show cat_shocked

    o "Well, maybe I just don't feel things the way you do."

    "Cat goes quiet. She's trying to figure out if you're joking, but your face says otherwise."

    hide cat_shocked
    show cat_worried2

    c "Do you mean you know what you’re supposed to feel, but you don’t actually feel it?"

    hide cat_worried2
    show cat_sad3

    c "Does that bother you?"

    hide cat_sad3
    show cat_sad2

    o "Should it?"

    hide cat_sad2
    show cat_shocked

    c "Sometimes I forget you're joking."

    hide cat_shocked
    show cat_shocked2

    o "I'm not."

    hide cat_shocked2
    show cat_worried
    c "I see."

    $ violence += 1
    $ cat_bond = -999

label cat_path_outro:

    hide cat_sad2
    hide cat_happy2
    hide cat_worried
    show cat_surprised

    c "Anyway, we should probably head back before everyone starts wondering where we are."

    hide cat_surprised
    with Dissolve(0.5)

    jump act_three

label follow_danny:

    $ danny_bond += 2

    scene black
    with Dissolve(1)

    pause 1

    show balcony
    with Dissolve(1)

    "Danny leans against the wire gate on the balcony, admiring the neighborhood."
    "You close the front door and he turns to look at you."

    show danny_disgust_smoking
    with Dissolve(0.5)

    d "You know, every time I turn around you're just there. Staring."

    hide danny_disgust_smoking
    show danny_shocked_smoking2

    d "If I didn't know you I'd probably think you were a serial killer."

    hide danny_shocked_smoking2
    show danny_shocked_smoking

    o "And because you know me?"

    hide danny_shocked_smoking
    show danny_happy_smoking2

    d "I'm only like fifty percent sure."

    hide danny_happy_smoking2
    show danny_happy_smoking

    "He laughs, nudging your shoulder, then notices that you aren't laughing at all."
    
    hide danny_happy_smoking
    show danny_shocked_smoking

    "His smile fades too."

    hide danny_shocked_smoking
    show danny_concerned_smoking2

    d "Want a smoke?"

menu:

    "Sure":
        jump have_smoke

    "I'm okay":
        jump dont_smoke

label have_smoke:

    hide danny_concerned_smoking2
    show danny_happy_smoking2

    o "Yeah, okay. Sure."

    hide danny_happy_smoking2
    with Dissolve(0.5)

    "You inhale, coughing almost the second it hits the back of your throat."

    show danny_happy3
    with Dissolve(0.5)

    d "Hah. I'll have that back then."

    jump danny_route_two

label dont_smoke:

    o "No. I'm okay."

    hide danny_concerned_smoking2
    show danny_shocked_smoking

    d "Suit yourself."

    jump danny_route_two

label danny_route_two:

    hide danny_happy3
    hide danny_shocked_smoking
    show danny_sad_smoking

    d "..."

    hide danny_sad_smoking
    show danny_disgust_smoking
    
    d "Sorry. You know I don't actually think that. The serial killer thing."

    hide danny_disgust_smoking
    show danny_concerned_smoking

    d "I mean, I kinda did when we were kids."

    hide danny_concerned_smoking
    show danny_sad_smoking

    d "I was a dick."

    hide danny_sad_smoking
    show danny_concerned_smoking2

    d "I still think about the day we left you during hide-and-seek. We were just fucking around, but we took it way too far."

    hide danny_concerned_smoking2
    show danny_sad_smoking

    d "And now, I guess I'm still leaving you behind."

menu:

    "I don't want you to go":
        jump dont_want_you_to_go

    "Thanks for that":
        jump danny_says_sorry

label dont_want_you_to_go:

    $ betrayal +=1

    hide danny_sad_smoking
    show danny_shocked_smoking

    o "I don't want you to go."

    hide danny_shocked_smoking
    show danny_sad_smoking

    d "Yeah. I know."

    hide danny_sad_smoking
    show danny_shocked_smoking2

    d "I actually thought you'd be the first one to leave us."

    hide danny_shocked_smoking2
    show danny_concerned_smoking

    o "Why?"

    hide danny_concerned_smoking
    show danny_shocked_smoking2

    d "I dunno. You just always seemed like you were somewhere else."

    hide danny_shocked_smoking2
    show danny_concerned_smoking

    d "Like you didn't really need anyone."

menu:

    "I didn't know how to show I cared":
        jump show_i_cared

    "It's your fault":
        jump your_fault

    "You were the only one I cared about" if danny_bond >= 5:
        jump danny_love

    "{color=#956dc9}You were the only one I cared about{/color}" (disabled=True) if danny_bond < 5:
        pass

label show_i_cared:

    hide danny_concerned_smoking
    show danny_shocked_smoking

    o "I just didn't know how to show it. I thought it was obvious."

    hide danny_shocked_smoking
    show danny_concerned_smoking2

    d "Otter. You literally never say anything."

    hide danny_concerned_smoking2
    show danny_shocked_smoking2

    o "I know."

    hide danny_shocked_smoking2
    show danny_concerned_smoking

    d "Yeah. I suppose that is your whole thing."

    hide danny_concerned_smoking
    show danny_happy_smoking

    d "But I know now. Thanks for telling me."

    jump danny_path_outro

label danny_love:

    $ danny_love += 1

    hide danny_concerned_smoking
    show danny_shocked_smoking

    o "You were the only one I ever truly cared about."

    "Your voice cracks. You've never been so raw and vulnerable before. For once, it seems like Danny has truly been caught off guard."

    d "..."

    hide danny_shocked_smoking
    show danny_shocked_smoking2

    d "...Seriously?"

    hide danny_shocked_smoking2
    show danny_shocked_smoking

    d "Even after I was a jerk to you?"

    o "Yeah."

    hide danny_shocked_smoking
    show danny_concerned_smoking

    d "Man... you really are weird."

    jump danny_path_outro

label danny_says_sorry:

    $ betrayal += 1
    $ violence += 1

    o "Yep. Thanks for that one."

    jump danny_says_sorry_two

label your_fault:

    $ betrayal += 1
    $ violence += 1
    $ danny_bond = -999

    hide danny_concerned_smoking
    show danny_sad_smoking

    o "You treated me like shit."

    o "You made everyone look at me like some kind of freak."

    jump danny_says_sorry_two

label danny_says_sorry_two:

    hide danny_sad_smoking
    show danny_concerned_smoking2

    d "I know. I'm sorry."

    hide danny_concerned_smoking2
    show danny_sad_smoking

    d "..."

    jump danny_path_outro

label danny_path_outro:

    hide danny_sad_smoking
    hide danny_concerned_smoking
    hide danny_happy_smoking
    with Dissolve(0.5)

    "Danny stubs his cigarette out with his shoe."

    show danny_happy2
    with Dissolve(0.5)

    d "We should probably head back before everyone starts wondering if you finally killed me."

    hide danny_happy2
    with Dissolve(0.5)

    jump act_three

label stay_where_you_are:

    $ char_menu.add("Stay where you are")

    "You're better off without them. You must be. How could they ruin your special day? How could they make it all about themselves?"

    "Forget it. You just need your medication. Take it, calm down, and stop spiralling. The pills should be in the bathroom."

    scene black
    with Dissolve(1)

    pause 1

    $ time_of_day = "4:30 PM"

    show bathroom
    with Dissolve(1)

    o "..."

    "Huh. The bottle isn't in its usual spot. You glance toward the bin beside the sink and spot the empty bottle inside. Didn't you just get a new refill?"
    
menu:

    "{i}Look in the mirror{/i}":
        jump look_in_mirror

    "{i}Leave the bathroom{/i}":
        jump leave_bathroom

label look_in_mirror:

    "You lean closer to the mirror. The dark circles under your eyes look worse than usual. That's odd. You slept for hours. You should look better than this."

    o "Pull yourself together. Freak."

    o "There's nothing wrong with you."

    jump leave_bathroom

label leave_bathroom:

    scene black
    with Dissolve(1)

    pause 1

    show black
    with Dissolve(1)

    "You can still hear the others talking somewhere in the distance, their voices muffled by the walls. You could follow them, or you could find your pills. There might be more in the kitchen."

menu:

    "{i}Go to the kitchen{/i}":
        jump go_to_kitchen

    "{i}Find somebody else{/i}":
        jump find_somebody_else

label go_to_kitchen:

    scene black
    with Dissolve(1)

    pause 1

    show kitchen:
        xalign 0.5
        yalign 0.35
    with Dissolve(1)

    "Something pulls you toward the kitchen."

    "Arriving, you notice the cake. You can't shake the feeling that you've seen it somewhere before."

    "You step closer when suddenly- the kitchen is gone."

    "They sit around the table, motionless, with the cake sitting in the center. You can hear your own breath, loud and frantic in your ears."

    o "..."

    o "IT WASN'T MY FAULT!"

    "You come back to yourself, gripping the counter. Your heart is pounding, and your eyes are blown wide."

    o "What the fuck was that?"

    "Your eyes dart around the room frantically, searching for the pills you came for."

    "Your pills. The cake. You reel forward, clutching your head as a sudden, throbbing pain surges behind your eyes."

    "You remember noticing them pulling away. You remember how often they'd started talking about the future, about college, hushed and out of sight."
    "You remember the sinking feeling that something was being kept from you, and the anger that came with it. You remember being afraid that they were going to leave."

    "Columbia. They had mentioned it before. You can't believe you'd forgotten."

    $ truth += 1

    "A loud voice echoes throughout the house, pulling you out of your thoughts."

    ch "Otter! Let's finally get into that cake, huh?"

    jump act_three

label act_three:

    scene black
    hide screen time_indicator
    with Dissolve(1)

    pause 1

    show screen act_three_text
    pause 3.0
    hide screen act_three_text
    with Dissolve(1)

    $ time_of_day = "5:00 PM"
    show screen time_indicator
    show dining_table at truecenter
    show cat_sitting_scared
    show charlie_sitting_neutral
    show danny_sitting_speaking
    show plates
    show cake
    with Dissolve(1)

    "..."

    "The four of you sit around the dining table. You don't really remember getting here. It all happened so fast."

    "The room is dimmer than it was earlier, with birthday decorations still hanging from the walls, and everyone now sporting these colorful paper party hats. The cake sits in the center."

    "All three of them are sitting together in front of you, and it's clear that nobody wants to be the first one to talk."

    "They look nervous."

    "You can't help but think that this is exactly where they belong."

    "Finally, Charlie clears his throat."

    ch "Well... happy birthday, Otter."

    d "That's it?"

    ch "What do you want me to say? No one else was saying anything!"

    c "Please don't make him give a speech."

    "The room falls silent again."

    d "I guess you should make a wish then, Otter."

    "Eighteen tiny flames flicker before you. Most eighteen-year-olds would probably wish for something material: a nice car, endless wealth, that sort of thing. But all you really want is..."

menu:

    "{i}For them to stay here forever{/i}" if acceptance <= 4 and violence <= 4:
        o "{i}I wish they would stop talking about leaving. I wish nobody would go anywhere and everything could just stay like this. I don't want to lose anyone.{i}"

        jump act_three_part_two

    "{color=#956dc9}{i}For them to stay here forever{/i}{/color}" (disabled=True) if acceptance > 4 or violence > 4:
        pass

    "{i}For them to be happy{/i}" if acceptance > 4:
        o "{i}Weirdly enough, I think I just wish... that they were happy.{i}"

    "{color=#956dc9}{i}For them to be happy{/i}{/color}" (disabled=True) if acceptance <= 4:
        pass

        jump act_three_part_two

    "{i}For them to die{/i}" if violence > 4:
        o "{i}I wish that they would just die.{i}"
        "The thought arrives so suddenly that it catches you off guard. You don't mean it, do you?"
        "At least, you don't think you do."

    "{color=#956dc9}{i}For them to die{/i}{/color}" (disabled=True) if violence <= 4:
        pass

        jump act_three_part_two

label act_three_part_two:

    $ time_of_day = "6:15 PM"

    "Suddenly, the voices of your friends become distant and muffled as though somewhere far away. The table. Your friends, slumped over it. It's all you can see. The dream feels more real now than ever."
    
    "You can't take it anymore."

    o "IT WASN'T MY FAULT!!!"
    
    "The others recoil, visibly startled."

    if danny_bond > 4:
        jump danny_ending

    elif cat_bond > 3:
        jump cat_ending

    elif charlie_bond > 3:
        jump charlie_ending

    elif violence > 4:
        jump violent_ending

    else:
        jump betrayal_and_acceptance_endings


label danny_ending:

    d "Hey man... you good?"

    d "We could go on a drive if you want?"

    d "Might help to ease uh... whatever the fuck is going on here."

menu:

    "Okay":
        jump danny_real_ending

    "I want to stay":
        jump danny_fakeout_ending

label danny_fakeout_ending:

    o "No, no. I want to stay."

    d "You're sure?"

    "You nod."

    d "Cool, suit yourself."

    jump betrayal_and_acceptance_endings

label danny_real_ending:

    o "Okay, let's go."

    d "Sweet. Let's bounce."

    scene black
    hide screen time_indicator
    with Dissolve(1)

    pause 1

    show black
    $ time_of_day = "7:00 PM"
    show screen time_indicator
    with Dissolve(1)

    "Danny turns the radio up as he drives, drumming his fingers against the steering wheel. The smell of cigarettes clings to the seats."

    "The smell should bother you more than it does, but all you can think is that it smells like Danny."

    d "Hey."

    d "We're gonna be alright, you know. Me and you."

    "He smiles to himself, keeping his eyes on the road."

    d "I can't wait to see everyone at Columbia."

    d "Try not to miss me too much, serial killer."

    scene black
    hide screen time_indicator
    with Dissolve (1)

    pause 3

    show ending_danny
    with Dissolve(1)

    pause 5

    scene black
    with Dissolve(1)

    pause 3

    show ending_betrayal
    with Dissolve(1)

    pause 1

    scene black
    with Dissolve(1)

    pause 1


return

label cat_ending:

    "Cat focuses in on you."

    c "Hey... you okay?"

    c "We could go on a little walk if you'd like?"

    c "Get some fresh air?"

menu:

    "Okay":
        jump cat_real_ending

    "I want to stay":
        jump cat_fakeout_ending


label cat_fakeout_ending:

    o "No, no. I want to stay."

    c "You're sure?"

    "You nod."

    c "As you wish."

    jump betrayal_and_acceptance_endings

label cat_real_ending:

    o "Okay, let's go."

    c "Cool, let's head out."

    scene black
    hide screen time_indicator
    with Dissolve(1)

    pause 1

    show black
    $ time_of_day = "7:00 PM"
    show screen time_indicator
    with Dissolve(1)

    "The two of you walk for a while, neither of you really knowing where you're going. Eventually, Cat slows down, looking back toward the house in the distance."

    c "You know what?"

    c "Still creepy."

    o "Thanks."

    c "Anytime."

    "She laughs, nudging your shoulder with hers. For a second, it almost seems as if she's blushing. If you blinked you'd almost miss it."

    c "You know, I'm actually excited."

    c "For Columbia, that is."

    "She looks ahead, smiling."

    c "It's gonna be weird not having you around, but..."

    c "I can't wait to be with those guys over there."

    scene black
    hide screen time_indicator
    with Dissolve (1)

    pause 3

    show ending_cat
    with Dissolve(1)

    pause 5

    scene black
    with Dissolve(1)

    pause 3

    show ending_betrayal
    with Dissolve(1)

    pause 1

    scene black
    with Dissolve(1)

    pause 1

    return

label charlie_ending:

    "Charlie focuses in on you."

    ch "Hey Otter... you doing alright?"

    ch "Wanna get out of here for a bit?"

    ch "Might be good to de-stress a little?"

menu:

    "Okay":
        jump charlie_real_ending

    "I want to stay":
        jump charlie_fakeout_ending

label charlie_fakeout_ending:

    o "No, no. I want to stay."

    ch "You're sure?"

    "You nod."

    ch "Uh... alright!"

    jump betrayal_and_acceptance_endings

label charlie_real_ending:

    o "Okay, let's go."

    ch "Cool! Let's get outta here."

    scene black
    hide screen time_indicator
    with Dissolve(1)

    pause 1

    show black
    $ time_of_day = "7:00 PM"
    show screen time_indicator
    with Dissolve(1)

    "You and Charlie slip out of the house and make your way toward the football field, climbing up into the empty bleachers. The town is quiet from up here, and the party feels impossibly far away, like it happened hours ago."

    ch "I think that fish was called Goldie. I'm actually sure of it."

    o "It was Bubbles."

    ch "Yeah, whatever you say, fish murderer."

    "He looks out over the field, the empty rows of seats stretching out beneath you."

    ch "You know, I'm gonna miss you, little man. You're always gonna be my best pal."

    ch "But, I'm looking forward to seeing what's next."

    ch "I really can't wait for college with those guys..."

    scene black
    hide screen time_indicator
    with Dissolve (1)

    pause 3

    show ending_charlie
    with Dissolve(1)

    pause 5

    scene black
    with Dissolve(1)

    pause 3

    show ending_betrayal
    with Dissolve(1)

    pause 1

    scene black
    with Dissolve(1)

    pause 1

    return

label violent_ending:

    $ time_of_day = "8:30 PM"

    c "Otter-"

    o "SHUT THE FUCK UP!"

    "For a moment, nobody says anything. Your head is pounding so hard that you can barely hear anything else."

    o "You think I don't fucking know?"

    ch "Hey-"

    o "Don't. Just don't."

    "Looking around, the anger suddenly drains out of you. You look at their faces and realise how scared they are."

    if polaroid > 0:

        menu:

            "{i}Inspect photo in pocket{/i}":
                show group_photo:
                    xalign 0.5
                    yalign 0.35
                with Dissolve(1)
                
                "Who would've thought that the day would end like this? You all looked so happy just hours earlier."
                hide group_photo
                with Dissolve(1)

                jump violent_ending_closure

label violent_ending_closure:

    o "...I'm sorry."

    o "I just don't want you to go..."

    c "Otter, we're not leaving you!"

    o "Then don't go..."

    ch "We uh... we really do have to, though..."

    "For a moment, you almost accept it. Then Charlie speaks up again."

    ch "But we'll visit like all the time! You can visit us too!"

    o "..."

    o "It's not the same..."

    o "IT'S NOT THE SAME!"

    "The anger comes back all at once. You grab the knife beside the cake."

    d "Put it down."

    o "You said you weren't leaving me."

    d "Put it down! Please! We can talk!"

    scene red


    hide screen time_indicator
    with Dissolve (1)

    pause 3

    show ending_violent
    with Dissolve(1)

    pause 5

    scene black
    with Dissolve(1)

    pause 5

    return


label betrayal_and_acceptance_endings:

    $ time_of_day = "8:30 PM"

    "For a moment, nobody says anything. Your heart is pounding so hard that you can barely hear anything else."

    ch "Uhhh... Okay..."

    d "That was fucking weird."

    c "Yeah."

    "You look down at your hands, trying to slow your breathing. The feeling is already beginning to fade, leaving behind nothing but the uncomfortable certainty that you've done something wrong, even if you can't remember what."
    "Charlie clears his throat."

    ch "Can we just... have the cake?"

    d "Please. I'm starving."

    "Charlie shakes his head and starts cutting the cake, passing each slice around the table until everyone has a plate."
    "You stare down at the piece that's been placed in front of you. Your fork stays on the table. You can't make yourself pick it up, almost as if your body physically won't let you."

    d "Okay, this is good, and I'm always right."

    ch "It is. You're not."

    c "You're really not."

    "You watch them bicker and eat, and for a brief moment, the strange feeling in your chest disappears. Then Charlie stops. He puts his fork down."

    ch "...Does anyone else feel weird?"

    d "What do you mean?"

    ch "I don't know. Just... weird."

    "Cat's smile fades."

    c "Actually... Yeah."

    d "Probably just the cake. Wouldn't be the first time we ate something questionable."

    "He tries for a joke but nobody laughs, not even himself. Charlie grips the edge of the table."

    ch "Wait. Something's really wrong."

    "Your stomach drops. Charlie's face has gone pale and Cat doesn't look well either."

    c "I don't feel so good..."

    d "What the fuck?"

    "Your friends try to stand, try to steady themselves, but it all happens so fast. Groaning turns to mumbling, and mumbling finally turns into a painful, eerie silence."

    o "Guys...?"

    "Charlie pushes himself up one final time."

    ch "...O-tter...?"

    $ time_of_day = "10:45 PM"

    "You don't move. Horrifyingly, the room looks exactly the way it did in your dream."
    "You realise it was never a dream. It was never an irrational fear. Was it fate? Was it karma? Your brain feels like it could explode from the pressure."
    "You reel forward, clutching yourself, as you begin to scream."

    o "..." 
    
    o "AHHHHHHH!"

    o "Are they...?"

    o "Did I..."

    o "..."

    o "Guys?!"

    o "Oh god, what have I done?!"

    o "Guys! Please stop fucking playing around!"

    o "..."

    o "PLEEEEEEASEEE!!!!!!!!!"

    if truth > 0:

        "That's when it hits you."
        "That's when it REALLY hits you."
        "It comes to you so suddenly that you're forced to clutch your head as a sharp pain surges behind your eyes."
        "The day before the party. You remember standing over the cake mix. You remember opening the bottle and feeling the tablets in your hand. You remember the anger you'd felt when they told you they were leaving." 
        "They were going to leave you behind. You couldn't let them leave."
           
        o "Oh my god..."

        "You did this. Now they're dying in front of you."

        jump pre_ending

    "You know exactly what's happening. They're dying. Slowly and painfully."
    "Cat lifts her head up weakly."

label pre_ending:

    c "Please..."

    c "Do something..."

    "Your hands are shaking."
    "You could call someone. You could run for the phone. You could get them to a hospital."
    "Or... you could stay exactly where you are."
    "What will you do?"

menu:

    "{i}Call for help{/i}" if acceptance > 4:
        jump acceptance_ending

    "{color=#956dc9}{i}Call for help{/i}{/color}" (disabled=True) if acceptance <= 4:
        pass

    "{color=#956dc9}{i}Let them die{/i}{/color}" (disabled=True) if acceptance > 4:
        pass

    "{i}Let them die{/i}" if acceptance <= 4:
        jump betrayal_ending

label acceptance_ending:

    $ time_of_day = "11:30 PM"

    "There isn't time to think; you have to get help. You grab the home phone from the dock with shaking hands and nearly drop it before finally dialling 9-1-1."

    o "...Hello?!"

    o "Hello??!!"

    "You stumble through your address, barely able to get the words out. Your eyes keep moving back toward the table, terrified that one of them will stop breathing before anyone arrives."

    if truth > 0:

        o "I... I think I put something in the cake. I think I did this to them."

        "You feel sick to your stomach. You did this."

    o "Please... stay with me..."

    o "I'm so sorry..."

    if polaroid > 0:

        menu:

            "{i}Inspect photo in pocket{/i}":
                show group_photo:
                    xalign 0.5
                    yalign 0.35
                with Dissolve(1)

                "Who would've thought that the day would end like this? You all looked so happy just hours earlier."
                hide group_photo
                with Dissolve(1)

                jump acceptance_ending_closure


label acceptance_ending_closure:

    "Somewhere outside, you hear a siren. You close your eyes."
    "For the first time tonight, you don't care about Columbia. You don't care about what happens tomorrow. You just want them to live."
    "This is what's right, isn't it?"

    return


label betrayal_ending:

    $ time_of_day = "11:30 PM"

    "You grab the home phone from the dock with shaking hands and... you freeze."
    "Cat keeps looking at you, fear and uncertainty written all over her face. You stare at her."
    "She looks confused now. Almost... betrayed."
    "Your eyes drift toward the others, motionless, slumped over the table."
    
    if polaroid > 0:

        menu:

            "{i}Inspect photo in pocket{/i}":
                show group_photo:
                    xalign 0.5
                    yalign 0.35
                with Dissolve(1)

                "Who would've thought that the day would end like this? You all looked so happy just hours earlier."
                
                hide group_photo
                with Dissolve(1)

                jump betrayal_ending_closure

label betrayal_ending_closure:

    "You know you should help them. You know there is still time. But for once, they're all exactly where you want them to be. Still here, right in front of you. Not going anywhere."
    "Maybe this is just what they deserve."
    
    o "I'm sorry."

    o "You did this to yourselves, didn't you?"

    return



# THAT CONCLUDES DEATH OF A PARTY, FOLKS! #









































































