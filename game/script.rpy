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


# Characters
define o = Character(_("Otter"), color="#956dc9", what_slow_cps=35, callback=text_sounds)
define ch = Character(_("Charlie"), color="#6082d1", what_slow_cps=35, callback=text_sounds)
define c = Character(_("Cat"), color="#eb88cb", what_slow_cps=35, callback=text_sounds)
define d = Character(_("Danny"), color="#cc9189", what_slow_cps=35, callback=text_sounds)
define unknown = Character(_("{i}???{/i}"), color="#bdbdbd", what_slow_cps=35, callback=text_sounds)
define narrator = Character(None, what_slow_cps=35, callback=text_sounds)
define replies = [
    ("It wasn't real."),
    ("I think I had a bad dream...."),
    ("Why can't I remember?"),
]
define replies2 = [
    ("Ugh, I look like shit."),
    ("Have I always been so pale?"),   
]
define alex_expressions = ["alex", "alex3",]
define config.layers = ['master', 'alexlayer', 'transient', 'screens']
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

default char_menu = set()

# Inventory
default polaroid = 0
default has_photo = False
default has_charlie_album = False
default has_cat_gift = False
default has_danny_cassette = False
default music_choice = None

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

    
init:
    image bedroom = scaled("bedroom.png")
    image doorway = scaled2("doorway.png")
    image porch = scaled3("porch.png")
    image lounge = scaled4("lounge.png")
    image lounge_test = scaled4("lounge_test.png")
    image lounge_two = scaled4 ("lounge_two.png")
    image bathroom = scaled5 ("bathroom.png")








init python:
    SCALE_X = 0.5
    SCALE_Y = 0.5

    def ending(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init:
    image ball = ending ("ball.png")
    image ball2 = ending ("ball2.png")
    image ball3 = ending ("ball3.png")
    image car = ending ("car.png")

init python:
    SCALE_X = 0.435
    SCALE_Y = 0.435

    def scaledassault(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init:
    image assault = scaledassault ("assault.png")

# Scaled Sprites
init python:    
    SCALE_X = 0.5
    SCALE_Y = 0.5

    def scaledsprite(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

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
    
# Assets
init python:    
    SCALE_X = 0.25
    SCALE_Y = 0.25

    def scaledasset(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init:

    image text = scaledasset ("text.png")
    
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

# The Game Starts Here
label start:

    scene black
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

    pause 1

    "ACT 1: THE PARTY BEGINS."

    ## ACT 1 BEGINS HERE !!! ##

    scene bedroom
    with Dissolve(1)

    play sound "sfx/yawn.mp3" volume 0.5

    pause 1

    "You wake with a sharp breath."
    "Morning light spills through the curtains, and as fast as the nightmare had started, it dissolves into dust..."

label wake_up_menu:

menu:

    "Think about dream":
        $ reply = renpy.random.choice(replies)

        o "[reply]"
        jump wake_up_menu

    "Look in the mirror":
        $ reply = renpy.random.choice(replies2)

        o "[reply]"
        jump wake_up_menu

    "Inspect room":
        jump leave_room

label leave_room:

    o "Shit. June 1st already? I'll be expecting them any minute now."

    "The calendar hanging across the room tells you it's June 1st, 2006. Your eighteenth birthday."
    "You've been waiting for this day for weeks and absolutely nothing could ruin it."

    scene black
    with Dissolve(1)

    pause 1

    show doorway
    with Dissolve(1)

    "{i}*BRRRRRRRRRING*{i}"

    "The doorbell rings through the house, and a familiar voice echoes from outside."

    ch "Otter!!! You up b-day boy? It's us! We're here!"

    "Another voice chimes in."

    c "Otter!" 

    "Then a third."

    d "Open up already, shithead!"

menu:

    "Answer the door":
        jump answer_door

    "Ignore the door":
        jump ending_one


label ending_one:

    "You failed to answer the door."

    return

label answer_door:

    "You rest your hand on the doorknob."
    "You force a smile you don't entirely feel and pull the door open."

    scene black
    with Dissolve(1)

    pause 1

    show porch
    with Dissolve(1)

    show charlie_happy2
    with Dissolve(0.5)

    ch "Ahh... he emerges! Happy birthday, pal."

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

    show lounge_test
    with Dissolve(1)

    "Charlie is already dropping his stuff off onto the dining table, making far more noise than necessary."
    "Somewhere in the kitchen, Cat is opening cupboards."
    "Danny plops himself down onto the couch."

menu:

    "Make yourselves at home":
        jump make_yourselves_at_home

    "...":
        jump say_nothing

label say_nothing:

    o "..."

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

    "Charlie is now kneeling on the carpet, trying to organise a pile of presents into something that vaguely resembles a neat stack."

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
    "Take a photo":
        jump take_photo

    "Listen to music":
        jump listen_music

    "Play a game":
        jump play_game

label take_photo:

    $ charlie_bond +=1

    hide charlie_neutral
    show charlie_shocked

    o "A picture first may be nice?"

    hide charlie_shocked
    show charlie_happy2

    ch "Score! One for the scrapbook."

    hide charlie_happy2
    with Dissolve(0.5)

    "Everyone awkwardly squeezes together in the living room."

    "{i}*FLASH*{i}"

    "The camera spits out an undeveloped photograph."

    show charlie_confused2
    with Dissolve(0.5)

    ch "Here, if I just shake it around it'll develop faster."

    hide charlie_confused2
    show charlie_confused3 at center_to_right

    show cat_angry3 at left
    with Dissolve(0.5)

    c "You know that's a myth right? It doesn't do anything."

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

    "Let's put Charlie's one on."

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

    "Let's put Cat's one on."

    hide danny_surprise2
    show cat_shocked
    with Dissolve(0.5)

    c "You gotta hand it to him, he's got taste."

    hide cat_shocked
    with Dissolve(0.5)

    "The music that spills into the room is raw and emotional; unlike anything the others would've picked."

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

    "Let's put on something new."

    hide danny_surprise2
    show danny_surprise

    d "Wow. That's... surprising."

    hide danny_surprise
    show danny_disgust3

    d "Hmm... let's try this one."

    hide danny_disgust3
    with Dissolve(0.5)

    "A tune fills the space around you, and is clearly something that one of your parents listen to."

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

    hide charlie_confused3
    show charlie_disgust

    o "It's not happening."

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
    with Dissolve(1)

    pause 1

    "ACT 2: THE PARTY GROWS QUIET."

    show lounge_test
    with Dissolve(1)

    "Charlie rubs his hands together before hurrying everyone onto the carpet. The pile of presents sit proudly in the middle of the living room."

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

    ch "Ahem...  anyway. Who's is next?"

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

    $ charlie_bond += 2
    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "I suppose... Let's go with yours."

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
    with Dissolve(0.5)

    "You carefully peel away the wrapping paper, revealing a thick photo album."

    "The first few pages are already filled with photographs from previous birthdays, school trips, and memories you'd long since forgotten."

    show charlie_neutral
    with Dissolve(0.5)

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

    "Remember you by?!":
        o "Remember you by?!"
        $ betrayal += 1
        $ violence += 1
        jump present_menu_intro

if presents_opened < 3:
    jump present_menu_intro

label cat_present:

    $ cat_bond += 2
    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "I suppose... Let's go with Cat's."

    hide charlie_shocked
    show cat_happy
    with Dissolve(0.5)

    c "Cool, man. I hope you like it."

    hide cat_happy
    with Dissolve(0.5)

    "Layers of newspaper slowly give way to a cassette player. A new tape already sits inside."

    show cat_surprised
    with Dissolve(0.5)

    c "It's nothing really... just some new music I thought I could put you on while we're apart."

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
        $ violence += 1

        hide cat_neutral
        show cat_shocked
        
        c "Umm... well, yeah."
        jump present_menu_intro

label danny_present:

    $ danny_bond += 2
    $ presents_opened += 1

    hide charlie_happy3
    show charlie_shocked

    o "I suppose... Let's go with Danny's."

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
    with Dissolve(0.5)

    "Inside sits a vintage polaroid camera. A 600 series from what looks like the early 1980's. It's in excellent condition."

    show danny_neutral2
    with Dissolve(0.5)

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

    "Update you on what?!":

        hide danny_neutral2
        show danny_disgust

        o "Update you on what?!"
        $ betrayal += 1
        $ violence += 1

        jump present_menu_intro   

label post_presents:

    hide cat_shocked
    hide charlie_confused3
    hide danny_disgust
    hide charlie_happy3
    show cat_worried
    with Dissolve(0.5)

    c "Uh... Otter, you're concerning us."

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

    "You look from Charlie to Cat... then Danny... waiting for someone to laugh, to say its a joke, that they'd all decided to mess with you on your birthday."

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

    "{color=#956dc9}I'm happy for you{/color}" (disabled=violence >= 4) if violence >= 4:
        jump happy_for_you

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

    o "Cut with the shit! You've never told me anything!"

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

    hide charlie_sad
    with Dissolve(0.5)

    "The conversation never recovers."

    "Charlie quietly excuses himself, muttering something about needing some air before disappearing through the sliding door into the backyard."

    "Danny pats his pockets and leaves through the front door, clearly hinting at having a smoke."

    "Cat lingers for a moment before slipping down the hallway out of sight."

    "You remain alone in the living room, surrounded by birthday decorations."

    scene black

label find_somebody_else:

menu:

    set char_menu

    "Follow Charlie":
        jump follow_charlie

    "Follow Cat":
        jump follow_cat

    "Follow Danny":
        jump follow_danny

    "Stay where you are":
        jump stay_where_you_are

label follow_charlie:

    $ charlie_bond += 1

    "You slide the back door open and the warm summer air immediately wraps around you. Charlie sits on the porch, looking at a picture in his wallet. He notices you almost immediately."

    ch "Oh... hey!"

    ch "Sorry about earlier, when we told you bef-"
    ch "I mean, I really should've said something sooner. Sorry."

menu:

    "It's alright":
        o "It's alright, Charlie."
        $ acceptance += 1
        jump charlie_path_two

    "You really should have":
        o "Yep. You really should have."
        $ betrayal += 1
        $ violence += 1
        jump charlie_path_two

label charlie_path_two:

    "Charlie looks down, distractedly admiring the photograph of you two and the goldfish you were so attached to. You couldn't have been older than twelve."

    ch "Hey, remember this little guy? Bubbles... or... was it Goldie?"

    o "..."

    ch "You just scooped him out of the bag and ate him whole. It was crazy!"

    o "He was already dead..."

    ch "Ahh... I don't think he was."

    ch "...But I guess kids do weird stuff, right?"

    o "..."

    ch "You know, I always thought we'd end up like this."

menu: 

    "Like what?":
        jump charlie_path_three

    "{color=#956dc9}Together?{/color}" (disabled=True) if charlie_bond < 4:
        pass

    "Together?" if charlie_bond >= 4:
        jump charlie_love

label charlie_love:

    $ charlie_love +=1

    o "...Together?"

    ch "Ahh.. well, still together after graduation, looking back. It felt like it came way too soon..."

    jump charlie_menu

label charlie_path_three:

    ch "Still together after graduation, looking back. It felt like it came way too soon..."

    $ charlie_not_love

    jump charlie_menu

label charlie_menu:

menu:

    "Promise we'll stay friends?":
        o "Promise me we'll stay friends?"
        $ acceptance += 2
        jump charlie_path_four

    "Now you're leaving me" if charlie_love < 1:
        o "...Now you're leaving me."
        $ betrayal += 1
        jump charlie_path_five

    "{color=#956dc9}Could it be anything more?{/color}" (disabled=True) if charlie_love < 1:
        o "Could it be anything more?"
        pass

    "Could it be anything more?" if charlie_love > 0:
        $ charlie_love +=1
        o "Could it be anything more?"
        jump charlie_path_five


label charlie_path_four:

    "His smile seems to fade as soon as it came. He lets out a quiet breath through his nose and closes his wallet with a soft thud."
    "His eyes stay fixed on the garden."

    ch "I promise."


label charlie_path_five:

    "His smile seems to fade as soon as it came, and he lets out a quiet breath through his nose and closes his wallet with a soft thud."
    "His eyes stay fixed on the garden."

    ch "Actually, there's something I wanted to tell you."

    ch "..."

    ch "It's stupid, but... well..."

    ch "...I think I like Cat?"

    "For just a second, everything else fades into the background. Even Charlie, who's suddenly far more interested in his own shoes than your reaction."

    if charlie_love > 1:
        $ betrayal += 1
        "After what you'd just confessed, you feel a little humiliated."

    ch "Trust me, I know how ridiculous that sounds."

    ch "We've been friends forever, and I still can't tell whether she actually likes me or if she's just... Cat?"

    ch "Half the time I can't even tell what she's thinking."

menu:
    "Thanks for telling me" if charlie_love < 2:
        o "Wow... Thanks for confiding in me. I won't tell anyone."
        jump thanks_otter

    "That's not a good idea":
        $ betrayal += 1
        $ violence += 1
        o "That's not a good idea. I know she doesn't like you."
        jump charlie_heartbreak

    "Good for you..." if charlie_love == 2:
        o "Oh... er... good for you, man."
        $ betrayal += 1
        jump thanks_otter

label thanks_otter:

    ch "Thanks Otter. I knew I could count on you."
    
    jump charlie_path_outro

label charlie_heartbreak:

    $ charlie_bond -= 999

    ch "Oh... uh... okay." 

    ch " I see..."

    jump charlie_path_outro

label charlie_path_outro:

    ch "Anyway, let's go back inside huh? I heard there's some cake just begging to be eaten!"

    jump act_three

label follow_cat:

    $ cat_bond +=1

    "You make your way down the hallway, noting that the door to your bedroom is already half open. Cat stands by the window, her back to you."
    "She notices your reflection in the glass before she hears your footsteps."

    c "Look, Otto... I'm really sorry we're leaving."

menu:

    "It's alright":
        jump its_alright

    "You can't leave":
        jump you_cant_leave

    "Some notice would've been nice":
        jump some_notice

label its_alright:

    $ acceptance += 1

    o "Ah... it's alright."

    jump cat_route_two

label you_cant_leave:

    $ betrayal += 1
    $ violence += 1

    o "You can't leave. You can't..."

    c "Otter, we really have to go."

    jump cat_route_two


label some_notice:

    $ betrayal += 1
    $ violence += 1

    o "Yeah, some notice would've been nice."

    c "Ah... yeah. Right."
    
    jump cat_route_two

label cat_route_two:

    c "I'm really gonna miss you. You're one of the most interesting people I know."

    o "That's not true. You don't even know me."

    c "Maybe I do, at least more than you think."

    c "I remember when we first met. You were always doing something weird. You'd say something completely insane and then just stare at everyone like you couldn't understand why they were laughing."

    c "I used to think that was just your humour... that was, until your dog died."

    c "You invited us over for some kind of impromptu gaming session and told us that your crying family was just 'being dramatic'"

    c "Did you even cry? Did you even care?"

menu:

    "Crying wouldn't change anything.":
        o "It's not like crying would've changed anything."
        jump cat_route_three

    "That dog was annoying.":
        o "So what? He was annoying."
        jump cat_route_three

label cat_route_three:

    c "Uh..."

    c "I just mean... most people are sad when they lose something they love."

    o "I was sad."

    c "Were you? You didn't act like it."

    o "What was I supposed to do?"

    c "I don't know... mourn him? Talk about it?"

menu:

    "I didn't know how":
        jump didnt_know_how

    "I don't feel things like you.":
        jump dont_feel_things

label didnt_know_how:

    "The words feel heavy on your tongue and, for a moment, Cat doesn't say anything at all. The usual teasing expression on her face disappears, replaced by something closer to understanding. You hate looking weak."

    c "What do you mean?"

    o "Something has always been wrong with me."

    c "Otter..."

    c "You should've told someone sooner."

    o "Who? Everyone calls me creepy. Even you."

    c "Yeah well... You are a little creepy."

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

    o "Are we just friends?"

    "The question comes out quieter than you intended. For once, Cat doesn't immediately make a joke."

    c "Do you want us to be?"

    o "I don't know."

    c "That sounds a lot like you."

    c "Maybe let's figure it out together."

    jump cat_route_four

label cat_route_four:

    c "Hmm... I'm gonna miss you, Otter."

    c "I just wish we had more time."

menu:

    "Me too.":
        jump me_too

    "Then why are you leaving me?":
        jump leaving_me

label leaving_me:

    $ betrayal += 1

    o "Then why are you leaving me?"

    c "I couldn't pass up an opportunity like Columbia, you know that."

    c "I'm just sorry we told you so late."

    jump cat_path_outro

label me_too:

    $ acceptance += 1

    o "Me too."

    "Cat smiles warmly."

    jump cat_path_outro

label dont_feel_things:

    o "Well, maybe I just don't feel things the way you do."

    "Cat's smile fades. She's trying to figure out if you're joking, but your face says otherwise."

    c "Do you mean you know what you’re supposed to feel, but you don’t actually feel it?"

    c "Does that bother you?"

    o "Should it?"

    c "Sometimes I forget you're joking."

    o "I'm not."

    c "I see."

    $ violence += 1
    $ cat_bond -= 9999

label cat_path_outro:

    c "Anyway, we should probably head back before everyone starts wondering where we are."

    jump act_three

label follow_danny:

    $ danny_bond += 2

    "Danny leans against the front of the house, admiring the neighbourhood."
    "You close the front door and turns to look at you."

    d "You know, every time I turn around you're just there. Staring."

    d "If I didn't know you I'd probably think you were a serial killer."

    o "And because you know me?"

    d "I'm only like fifty percent sure."

    "He laughs, nudging your shoulder, but shortly notices that you aren't laughing at all. His smile fades too."

    d "Want a smoke?"

menu:

    "Sure.":
        jump have_smoke

    "I'm okay":
        jump dont_smoke

label have_smoke:

    o "Yeah, okay. Sure."

    "You inhale, coughing almost the second it hits the back of your throat."

    d "Hah. I'll have that back then."

    jump danny_route_two

label dont_smoke:

    o "No. I'm okay."

    d "Suit yourself."

label danny_route_two:

    d "..."
    
    d "Sorry. You know I don't actually think that. The serial killer thing."

    d "I mean, I kinda did when we were kids."

    d "I was a dick."

    d "I still think about the day we left you  during hide-and-seek. We were just fucking around, but we took it way too far."

    d "And now, I guess I'm still leaving you behind."

menu:

    "I don't want you to go":
        jump dont_want_you_to_go

    "Thanks for that":
        jump danny_says_sorry

label dont_want_you_to_go:

    $ betrayal +=1

    o "I don't want you to go."

    d "Yeah. I know."

    d "I actually thought you'd be the first one to leave us."

    o "Why?"

    d "I dunno. You just always seemed like you were somewhere else."

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

    o "I just didn't know how to show it. I thought it was obvious."

    d "Otter. You literally never say anything."

    o "I know."

    d "Yeah. I suppose that is your whole thing."

    d "But I know now. Thanks for telling me."

    jump danny_path_outro

label danny_love:

    $ danny_love += 1

    o "You were the only one I ever truly cared about."

    "Your voice cracks. You've never been so raw and vulnerable before. For once, it seems like Danny has truly been caught off guard."

    d "..."

    d "...Seriously?"

    d "Even after I was a jerk to you?"

    o "Yeah."

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
    $ danny_bond -= 999

    o "You treated me like shit."

    o "You made everyone look at me like some kind of freak."

    jump danny_says_sorry_two

label danny_says_sorry_two:

    d "I know. I'm sorry."

    d "..."

    jump danny_path_outro

label danny_path_outro:

    "Danny stubs his cigarette out with his shoe."

    d "We should probably head back before everyone starts wondering if you finally killed me."

    jump act_three


label stay_where_you_are:

    $ char_menu.add("Stay where you are")

    "You're better off without them. You must be. How could they ruin your special day? How could they make it all about themselves?"

    "Forget it. You just need your medication. Take it, calm down, and stop spiralling. The pills should be in the bathroom."

    o "..."

    "Huh. The bottle isn't in its usual spot. You glance toward the bin beside the sink and spot the empty capsule inside. Didn't you just get a new refill?"
    
menu:

    "Look in the mirror":
        jump look_in_mirror

    "Leave the bathroom":
        jump leave_bathroom

label look_in_mirror:

    "You lean closer to the mirror. The dark circles under your eyes look worse than usual. That's odd. You could've sworn you got a good night's sleep."

    o "Pull yourself together. Freak."

    o "There's nothing wrong with you."

    jump leave_bathroom

label leave_bathroom:

    "You can still hear the others talking somewhere in the distance, their voices muffled by the walls. You could follow them, or you could find your pills. There might be more in the kitchen."

menu:

    "Go to the kitchen":
        jump go_to_kitchen

    "Find somebody else":
        jump find_somebody_else

label go_to_kitchen:

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

    "Columbia. They had mentioned it before. You can't believe you'd forgot."

    $ truth += 1

    "A loud voice echoes throughout the house, seperating you from your thoughts."

    ch "Otter! Let's finally get into that cake, huh?"

    jump act_three

label act_three:

    "..."

    "The four of you sit around the dining table. You don't really remember getting here, it happened all so fast."

    "The room is dimmer than it was earlier, with birthday decorations still hanging from the walls, and everyone now sporting these colourful, pointy, party hats. The cake sits in the center."

    "All three of them are sitting together in front of you, and its clear that nobody wants to be the first one to talk."

    "They look nervous."

    "You can't help but think that this is exactly where they belong."

    "Finally, Charlie clears his throat."

    ch "Well... happy birthday, Otter"

    d "That's it?"

    ch "What do you want me to say? No one else was saying anything!"

    c "Please don't make a him do a speech."

    "The room falls silent again."

    d "I guess you should make a wish then, Otter."

    "Eighteen tiny flames flicker before you. Most eighteen-year-olds would probably wish for something material: A nice car, endless wealth, that sort of thing. But all you really want is..."

menu:

    "For them to stay here forever" if acceptance <= 4 and violence <= 4:
        o "{i}I wish they would stop talking about leaving. I wish nobody would go anywhere and everything could just stay like this. I don't want to lose anyone.{i}"

        jump act_three_part_two

    "{color=#956dc9}For them to stay here forever{/color}" (disabled=True) if acceptance > 4 or violence > 4:
        pass

    "For them to be happy" if acceptance > 4:
        o "{i}Weirdly enough, I think I just wish... that they were happy.{i}"

    "{color=#956dc9}For them to be happy{/color}" (disabled=True) if acceptance <= 4:
        pass

        jump act_three_part_two

    "For them to die" if violence > 4:
        o "{i} I wish that they would just die. {i}"
        "The thought arrives so suddenly that it catches you off guard. You don't mean it, do you?"
        "At least, you don't think you do."

    "{color=#956dc9}For them to die{/color}" (disabled=True) if violence <= 4:
        pass

        jump act_three_part_two

label act_three_part_two:

    "Suddenly, the voices of your friends become distant and muffled as though somewhere far away. The table. Your friends, slumped over it. It's all you can see. The dream feels more real now than ever."
    
    "You can't take it anymore."

    o "IT WASN'T MY FAULT!!!"
    
    "The others recoil, visibly startled."

    if danny_bond > 4:
        jump danny_ending

    elif cat_bond > 4:
        jump cat_ending

    elif charlie_bond > 4:
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

"Danny turns the radio up as you drive, drumming his fingers against the steering wheel. The smell of cigarettes clings to the seats."

"The smell should bother you more than it does, but all you can think is that it smells like Danny."

d "Hey."

d "We're gonna be alright, you know. Me and you."

"He smiles to himself, keeping his eyes on the road."

d "I can't wait to see everyone at Columbia."

d "Try not to miss me too much, serial killer."

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

label cat_real_ending:

    o "Okay, let's go."

    c "Cool, let's head out."

    "The two of you walk for a while, neither of you really knowing where you're going. Eventually, Cat slows down, looking back toward the house in the distance."

    c "You know what?"

    c "Still creepy."

    o "Thanks."

    c "Anytime."

    "She laughs, nudging your shoulder with hers. For a second, it almost seems as if she's blushing. If you blinked you'd have missed it."

    c "You know, I'm actually excited."

    c "For Columbia, that is."

    "She looks ahead smiling to herself."

    c "It's gonna be weird not having you around, but..."

    c "I can't wait to be with those guys over there."

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

    ch "Uh... alright! As you wish"

    jump betrayal_and_acceptance_endings

label charlie_real_ending:

    o "Okay, let's go."

    ch "Cool! Let's get outta here."

    "You and Charlie slip out of the house and make your way toward the football field, climbing up into the empty bleachers. The town is quiet from up here, and the party feels impossibly far away, like it happened hours ago."

    ch "I think that fish was called Goldie. I'm actually sure of it."

    o "It was Bubbles."

    ch "Yeah whatever you say, fish murderer."

    "He looks out over the field, the empty rows of seats stretching out beneath you."

    ch "You know, I'm gonna miss you little man, you're always gonna be my best pal."

    ch "But, I'm looking forward to see what's next."

    ch "I really can't wait for college with those guys..."

    return

label violent_ending:

    c "Otter-"

    o "SHUT THE FUCK UP!"

    "For a moment, nobody says anything. Your head is pounding so hard that you can barely hear anything else."

    o "You think I don't fucking know?"

    ch "Hey-"

    o "Don't. Just don't."

    "Looking around, the anger suddenly drains out of you. You look at their faces and realise how scared they are."

    menu:

        "Inspect photo in pocket" if polaroid == 1:
            "Who would've thought that the day would end like this? You all looked so happy just hours earlier."
            jump violent_ending_closure

label violent_ending_closure:

    o "...I'm sorry"

    o "I just dont want you to go..."

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

    return


label betrayal_and_acceptance_endings:

    "For a moment, nobody says anything. Your heart is pounding so hard that you can barely hear anything else."

    ch "Uhhh... Okay..."

    d "That was fucking weird."

    c "Yeah."

    "You look down at your hands, trying to slow your breathing. The feeling is already beginning to fade, leaving behind nothing but the uncomfortable certainty that you've done something wrong, even if you can't remember what."
    "Charlie clears his throat."

    ch "Can we just... have the cake?"

    d "Please. I'm starving."

    "Charlie shakes his head and starts cutting the cake, passing each slice around the table until everyone has a plate."
    "You stare down at the piece that's been placed in front of you. You feel resistance in reaching over to eat any, almost as if your body physically won't let you."

    d "Okay, this is good, and I'm always right."

    ch "It is but... you're not though."

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

    "Your stomach drops. Charlie's face has gone pale and Cat's not starting to look well either."

    c "I don't feel so good.."

    d "What the fuck?"

    "Your friends try to stand, try to steady themselves, but it all happens so fast. Groaning turns to mumbling, and mumbling finally, turns into a painful, eerie silence."

    o "Guys...?"

    "Charlie pushes himself up one final time."

    ch "...O-tter...?"

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

    if truth == 1:

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

    "Save them" if acceptance > 4:
        jump acceptance_ending

    "{color=#956dc9}Save them{/color}" (disabled=True) if acceptance < 4:
        pass

    "Let them die" if betrayal >= 4:
        jump betrayal_ending

    "{color=#956dc9}Let them die{/color}" (disabled=True) if betrayal < 4:
        pass

label acceptance_ending:

    "There isn't time to think; you have to get help. You grab the home phone from the dock with shaking hands and nearly drop it before finally dialling 9-1-1."

    o "...Hello?!"

    o "Hello??!!"

    "You stumble through your address, barely able to get the words out. Your eyes keep moving back toward the table, terrified that one of them will stop breathing before anyone arrives."

    o "Please... stay with me..."

    o "I'm so sorry..."

    menu:

        "Inspect photo in pocket" if polaroid == 1:
            "Who would've thought that the day would end like this? You all looked so happy just hours earlier."
            jump acceptance_ending_closure


label acceptance_ending_closure:

    "Somewhere outside, you hear a siren. You close your eyes."
    "For the first time tonight, you don't care about Columbia. You don't care about what happens tomorrow. You just want them to live."
    "This is what's right, isn't it?"

    return


label betrayal_ending:

    "You grab the home phone from the dock with shaking hands and... you freeze."
    "Cat stays looking toward you, fear and uncertainty written all over her face. You stare at her."
    "She looks confused now. Almost... betrayed."
    "Your eyes drift toward the others, motionless, slumped over the table."
    
menu:

    "Inspect photo in pocket" if polaroid == 1:
        "Who would've thought that the day would end like this? You all looked so happy just hours earlier. What a shame."
        jump betrayal_ending_closure

label betrayal_ending_closure:

    "You know you should help them. You know there is still time. But for once... They're all exactly where you want them to be. Still here, right in front of you. Not going anywhere."
    "Maybe this is just what they deserve."
    
    o "I'm sorry."

    o "You did this to yourselves though, didn't you?"

    return



# THAT CONCLUDES DEATH OF A PARTY, FOLKS! #









































































# SEPERATE GAME #


label school_intro:

    stop music fadeout 3
    play music "sfx/Far Away.mp3" fadein 3

    scene hallway_dark
    with Fade (1, 1, 1)
    pause 0.5

    show alex2 at rightish
    with Dissolve(2.0)

    a4 "Welcome to Cedar Hill High. Land of the free, home of brainless morons."

    hide alex2
    show alex3 at right

    a4 "This hallway is the food chain. You've got your typical archetypes: the jocks, band kids, goths, scene kids, nerds."

    hide alex3
    show alex at right

    a4 "Me? I feel like I'm the only normal person here. It feels like I'm looking behind the glass in a zoo."

    hide alex
    show alex2 at rightish

    a4 "If there's a more depressing place to spend the supposed ‘best years of my life,' do me a favour and never take me there."

    hide alex2
    show alex3 at right

    a4 "Anyway, today's the big finale. Spring Fling. Balloons. Bad punch. Everyone pretending they're not about to scatter across the country and forget each other's names."

    hide alex3
    show alex at right

    a4 "It's supposed to be “magical.” You know what's magical? Surviving four years in a building where someone {i}still{/i} thinks shoving kids into lockers is peak comedy."

    hide alex
    show alex5 at rightish

    a4 "The worst part of all of this though? I swear I've done this already. Like... this exact hallway, these exact idiots, this exact morning. Deja vu on steroids."

    hide alex5
    show alex3 at right

    a4 "But hey, maybe senior year is just one long nightmare that you have to keep waking up from."

    hide alex3
    show alex_shocked2 at right

    play sound "sfx/lockerslam.mp3"

    "{i}*locker slams*{i}"

    stop sound

    scene hallway_dark2
    
    show tyler_angry3 at left
    show alex at right
    with Dissolve(0.5)

    unknown "Well, well, well. Look who the cat dragged in. Lunch money now, nerd! Don't even bother fighting back, it's not worth it."

    hide alex
    hide tyler_angry3
    show alex5 at rightish
    show tyler_angry4 at left

    a4 "Right on cue. Tyler Kane, human embodiment of puberty with fists. A classic, raging archetype of a man."

    hide alex5
    show alex_looking2 at right

menu:
    "Hand it over.":
        jump hand_it_over

    "Refuse.":
        jump refuse

    "Run.":
        jump run

label hand_it_over:

    hide alex_looking2
    hide tyler_angry4
    show alex_looking at right
    show tyler_happy2 at left

    a "Fine, take it. Just leave me alone."

    hide tyler_happy2
    hide alex3
    show alex_looking2 at right onlayer alexlayer
    show tyler_happy at left

    t "See, isn't that so easy? Pleasure doing business."

    hide tyler_happy
    with Dissolve(0.5)

    scene hallway_dark
    with Dissolve(0.5)
    pause 0.75

    hide alex_looking2 onlayer alexlayer
    with None
    show alex5 at rightish

    a4 "Ugh. Human vermin..."

    jump hallway_two

label refuse:

    hide alex_looking2
    show alex_angry at right
    hide tyler_angry4
    show tyler_happy2 at left

    a "No. Not today, Tyler."

    hide alex_angry
    show alex_angry2 at right
    hide tyler_angry4
    show tyler_angry5 at left

    t "Wrong answer."

    jump head_slam

label run:

    hide alex_looking2
    with Dissolve(0.5)

    hide tyler_angry4
    show tyler_angry5 at left

    t "Not so fast, nerd!"

    jump head_slam

label head_slam:

    scene assault at slightdown
    play sound "sfx/lockerslam.mp3" 
    with flashbeat
    with hpunch

    scene hallway_dark
    with flashbeat
    show alex_hurt at right
    with Dissolve(0.5)

    pause 0.5

    a "Fuck, ouch."

    hide alex_hurt
    show alex_hopeless at right

    a4 "I can't believe this day already sucks. It's only 8:00AM. I swear the universe fucking hates me."

    $ has_bruise += 1

    jump hallway_two

label hallway_two:

    scene hallway_dark
    with Fade (1, 1, 1)

    show alex3 at right
    with Dissolve(0.5)

    a4 "Ahh... the last piece of my endlessly messy puzzle. Ash Vaughn."   

    hide alex3
    show alex5 at rightish

    a4 "We used to be good friends, now he's just a MySpace cryptid who hangs out with all the other scene losers."

    hide alex5
    show alex_looking at right

    a4 "He probably thinks he's too cool to be seen with me nowadays."

    hide alex_looking
    show alex6 at rightish

    a4 "It's funny how people drift... or maybe they just swim away before you sink."

    hide alex6
    show alex4 at right onlayer alexlayer

menu:

    "Call out to Ash.":
        jump ash_convo

    "Ignore him.":
        jump ignore_ash

label ash_convo:
    $ talked_to_ash += 1

    scene hallway_dark2
    with Dissolve(1)

    hide alex4 onlayer alexlayer
    show alex at right
    show ash_sly2 at left
    with Dissolve(1)

    ash "Well well, if it isn't the ghost of homeroom past. Survived the morning apocalypse?"

    hide ash_sly2
    show ash_sly3 at left

menu:
    "Still haunting these halls?":
        jump ash_convo2

    "Did Hot Topic spit you out?":
        jump ash_convo2
    
label ash_convo2:

    hide alex
    show alex6 at rightish

    a "Ash. Still haunting these halls, or did Hot Topic just spit you back out?"

    hide ash_sly3
    show ash_cringing at left
    hide alex6
    show alex_angry2 at right

    ash "Ouch. Someone woke up bitter."

    hide alex_angry2
    show alex_looking2 at right
    hide ash_cringing
    show ash_sly at left

    ash "So what's the occasion? What did I do to deserve your presence? You usually avoid me like gym class."

    hide ash_sly
    show ash at left
    hide alex_looking2
    show alex5 at rightish

    a4 "There it is- that half-teasing, half-knifing tone that used to be our whole language back when we were... whatever we were."

    hide ash
    show ash3 at left
    hide alex5
    show alex_looking at right

    a "Eh... just figured I'd ruin someone else's morning for a change. Congrats, you won the lottery."

    hide alex_looking
    show alex_looking2 at right
    hide ash3
    show ash4 at left

    ash "Very funny. Anyway, you coming to the Spring Fling tonight? Or are you planning to sulk in a corner like a tragic indie film protagonist?"

    hide ash4
    show ash3 at left

menu:
    "Depends.":
        jump ash_convo3

    "I won't make it.":
        jump ash_convo3

label ash_convo3:

    hide alex_looking2
    show alex_looking at right

    a "Depends on if I make it that far."

    hide alex_looking
    show alex_looking2 at right
    hide ash3
    show ash5 at left

    ash "Wow, dark much? You're even edgier than me these days, and I'm literally a scene kid." 

    play sound "sfx/schoolbell.mp3"

    jump homeroom

label ignore_ash:

    hide alex4 onlayer alexlayer
    show alex_looking at right

    a4 "Nope. I don't trust whatever I might say to him. I can't have my last words to Ash being some stupid bullshit."

    jump homeroom

label homeroom:

    scene classroom_dark
    with Fade (1, 1, 1)

    show alex5 at rightish
    with Dissolve(1)

    a4 "Homeroom. Forty-five minutes of useless babble and motivational posters staring into my soul."

    hide alex5
    show alex3 at right

    a4 "Today in particular, they'll say some bullshit about friendship, memories, and future. Great."

    hide alex3
    with Dissolve(0.5)

    show teacher at right
    with Dissolve(0.5)

    teach "Good morning, seniors! Today is a special day, it being the last day of your little school lives, so let's all remember to cherish our friends and celebrate the end of high school with a spectacular bang!"

    hide teacher
    with Dissolve(0.5)

    show alex2 at rightish
    with Dissolve(0.5)

    a4 "Right, Ms. Perkins. I'll cherish the cafeteria mystery meat, the stuck up asshole who always took my money and all of my nonexistent friends. Memories forever."

    hide alex2
    show alex_looking at right 

    a4 "What? I mean, I don't have any friends because everyone is too annoying to be friends with, it's not like I'm some kind of loser."


label homeroom_menu:

    hide alex6
    hide alex
    hide alex3
    hide alex_looking
    show alex_looking2 at right

menu:
    set char_menu
    "Write sarcastic note.":
        jump sarcastic_note

    "Look around.":
        jump look_around

    "Pretend to take notes.":
        jump takes_notes

jump cafeteria

label sarcastic_note:

    play scribble "sfx/scribble.mp3" volume 0.5

    hide alex_looking2
    show alex6 at rightish
    
    a4 "Hey Ash, thanks for ghosting me for the past two years. Really appreciated."

    stop scribble

    $ char_menu.add("Write sarcastic note.")

    jump homeroom_menu

label look_around:

    hide alex_looking2
    show alex at right

    a4 "Everyone pretending this matters. Smiling like idiots about to graduate into misery."

    $ char_menu.add("Look around.")

    jump homeroom_menu

label takes_notes:

    hide alex_looking2
    show alex3 at right

    a4 "Mhm, very insightful. Maybe I'll write 'life is unfair' instead."

    $ char_menu.add("Pretend to take notes.")

    jump homeroom_menu

label cafeteria:

    scene cafeteria_dark
    with Fade(1,1,1)

    pause 1

    show alex5 at rightish
    with Dissolve(0.5)

    a4 "Cafeteria. Where everyone pretends survival matters more than getting to the bottom of whatever this mystery slop is."

    hide alex5
    show alex at right

    a4 "Table one: the jocks. Tyler Kane, overly loud and proud as usual, like testosterone will solve algebra."

    hide alex
    show alex3 at right

    a4 "Table two: the nerds. Arguing over D&D stats and Magic cards."

    hide alex3
    show alex6 at rightish

    a4 "Table three: the goths and scene kids. Dark clothes, thick eyeliner, all covering a singular eye with their razor sharp hair."

    hide alex6
    show alex_looking at right

    a4 "Table four: the preps. Perfect hair, matching polos, plotting social ruin."

    hide alex_looking
    show alex_happy at right

    a4 "Ah. A place to observe, endure, and imagine what would happen if a light fixture fell from the ceiling."

    hide alex_happy
    show alex3 at right

    a4 "Now... where do I sit?"

    hide alex3
    show alex_looking2 at right

    jump where_to_sit_menu

label where_to_sit_menu:
menu:
    "The scene table with Ash." if not ash_table_seen:
        $ ash_table_seen = True
        jump scene_table

    "The jock table with Tyler.":
        jump jocks_table

    "Alone.":
        jump sit_alone

label scene_table:

    scene cafeteria_dark
    with Fade(1, 1, 1)

    show alex at right onlayer alexlayer
    with Dissolve(0.5)

    a "Uh, hey. Can I sit here?"

    scene cafeteria_dark2
    with Dissolve(0.5)

    hide alex
    show ash2 at left
    with Dissolve (0.5)
    show alex_flustered at right onlayer alexlayer
    with Dissolve(0.5)

    ash "Sure man, don't need to ask."

    hide alex_flustered onlayer alexlayer
    hide alex onlayer alexlayer
    hide ash2
    with Dissolve(0.2)

    scene cafeteria_dark
    with Dissolve(0.2)

    show hayley2 at right
    with Dissolve(0.5)

    h "..."

    scene cafeteria_dark2
    with Dissolve(0.2)

    show ash at left
    show alex7 at right onlayer alexlayer
    with Dissolve(0.5)

    a4 "Hayley shoots me a look that says ‘you're tolerated... for now.' Perfect."

    hide alex7 onlayer alexlayer
    hide ash
    show alex_looking2 at right
    show ash2 at left

    ash "Alex, you know what I've been thinking about? Do you remember that time in Lincoln Park in '02 with those dry-ice bottle rockets?"

    hide ash2
    hide alex_looking2
    show alex_happy3 at right
    show ash_happy at left

    ash "You said it was 'basically science class,' then we completely blew out the neighbor's windows."

    hide alex_happy3
    show alex_happy at right
    hide ash_happy
    show ash_happy2 at left

    a "Hahaha! Dude, the look on their faces before we started running made it totally worth it!"

    hide alex_happy
    show alex_happy4 at right
    hide ash_happy2
    show ash_happy at left

    ash "Oh, oh, and that time in '99 when we went up to Sturgeon Bay and you made a flamethrower out of a WD-40 can!"

    hide ash_happy
    show ash_happy2 at left
    hide alex_happy4
    show alex_happy6 at right

    a "You were a total maniac with that thing! We must have burned down at least a hundred feet of bush!"

    hide alex_happy6
    show alex_happy4 at right
    hide ash_happy2
    show ash_happy at left

    ash "Dude, you were the one who stole the lighter from your mom's boyfriend! Pretty sure we were two seconds away from becoming a ‘local news cautionary tale.'"

    hide ash_happy
    show ash_happy2 at left
    hide alex_happy4
    show alex_happy5 at right

    a4 "There's this uncontrollable spasm in my face, am I smiling? Just hearing Ash laugh makes it hard not to. It's kinda contagious?"

    hide alex_happy2
    show alex7 at right

    a4 "This is the one moment today that hasn't felt like absolute garbage. Odd."

    jump hallway_three

label jocks_table:

    $ jock_table += 1

    scene cafeteria_dark
    with Fade(1, 1, 1)

    show alex3 at right onlayer alexlayer
    with Dissolve(0.5)

    a4 "This might be funny, but it'll most likely just end up with me as the punchline. It's funny how I don't even care anymore."

    scene cafeteria_dark2
    with Dissolve(0.5)
    
    show tyler_angry3 at left
    hide alex3 onlayer alexlayer
    hide alex7
    show alex_looking2 at right onlayer alexlayer
    with Dissolve(0.5)

    t "What the-? Since when did losers start getting a lunch invite with us?"

    hide alex_looking2 onlayer alexlayer
    hide tyler_angry3
    show tyler_angry4 at left
    show alex6 at rightish

    a "Yeah, well, the nerd table was full of people with futures. Thought I'd downgrade."

    hide tyler_angry4
    show tyler_happy at left
    hide alex6
    show alex4 at right

    t "Brave. What's the occasion? Trying to get drafted?"

    hide alex4
    show alex_looking at right
    hide tyler_happy
    show tyler_happy2 at left

    a "I just felt like completely throwing away all sense of reason and leaving my life to fate."

    hide alex_looking
    hide tyler_happy 
    show tyler_angry5 at left
    show alex_looking2 at right

    t "You do know what you're in for now right? It'll be worse than what I did to Stevie Kenarban yesterday. Poor fella's prom ticket is on the lockers now."

    hide tyler_angry5
    show tyler_angry4 at left

    if loops_done == 1:
    
        hide alex_looking2
        show alex7 at right

        a4 "Hey, not bad. I just found myself a ticket."

    hide alex7
    hide alex_looking2
    show alex at right

    $ ticket_found += 1

    a "Ahh... just get it over with."

    jump bathroom

label bathroom:

    play sound "sfx/toiletflush.mp3"

    scene bathroom
    with Fade (2,2,2)

    pause 2

    scene bathroom_dark
    with Dissolve(0.5)

    show alex5 at rightish
    with Dissolve(0.5)

    stop sound fadeout 2

    a4 "Jeez, he really did a number on me, I look like shit."

    hide alex5
    show alex_looking at right

    a4 "Ah yeah, the bathroom. Great confessional hall of Cedar Hill High."

    hide alex_looking
    show alex5 at rightish
    
    a4 "Look at this. Every failure, every bad choice, memorialized. It's like the Louvre of losers. Someday I'll be a permanent exhibit."

    hide alex5
    show alex4 at right

menu:
    "Reflect.":
        jump reflect

    "Inspect wall carvings.":
        jump wall_carvings

    "Leave.":
        jump leave_bathroom

label reflect:

    hide alex4
    show alex at right

    a4 "Just what I needed... my own pathetic face staring back at me..."

    hide alex
    show alex4 at right

menu:
    "Inspect mirror carving":
        jump mirror_carving

label mirror_carving:

    hide alex4
    show alex3 at right
    
    a4 "{i}'Spring Fling, '06'{i}"

    hide alex3
    show alex6 at rightish

    a4 "Ugh, the troubles of today... the Spring Fling, Ash, Tyler's constant torture. If I could've figured out how to arrange them just right... maybe I wouldn't have sucked at this day. Or life."

    hide alex6
    show alex at right

    a4 "Probably not, but hey, optimism is overrated anyway."

    jump leave_bathroom

label wall_carvings:

    hide alex4
    show alex5 at rightish

    a4 "Huh... this one stands out."

    hide alex5
    show alex3 at right

    a4 "{i}'Burning man, 2003'.{i}"

    hide alex3
    play sound "sfx/shock.mp3"
    show alex_shocked2 at right

    a4 "Holy shit, I remember that."

    hide alex_shocked2
    show alex_shocked at right

    a4 "Ash and I decided it would be a good idea to convince some seniors to take us to this crazy festival all the way out in Black Rock desert. We were alone together in the desert for an entire week."

    hide alex_shocked
    show alex7 at right

    a4 "I've never gotten so high in my life."

    $ burning_man += 1

    jump leave_bathroomm

label leave_bathroomm:

    hide alex7
    hide alex
    hide alex4
    show alex5 at rightish

    a4 "Okay, I'm out of here. This place reeks of Axe body spray and a whole lot of regret."

    hide alex5
    with Dissolve(0.5)

if loops_done == 0:

    jump hallway_three

else:

    jump hallway_day_two_two

label sit_alone:
    
    hide alex_looking2
    show alex6 at rightish

    a4 "Nope. Everyone else is too loud, too stupid, too obsessed with their hair or stats or whatever... I can't deal with that. I'll just sit here and enjoy my miserable cafeteria slop in peace."

    hide alex6

label observe_menu:

    hide alex6
    hide alex_shocked2
    show alex4 at right

    menu:
        set char_menu
        "Observe the scene table.":
            jump observe_scene

        "Observe the jock table.":
            jump observe_jock

if loops_done == 0:
    jump hallway_three

else:
    jump observe_two_outro

label observe_scene:

    hide alex4
    show alex6 at rightish

    a4 "Ugh... watching Ash and his best friend Hayley banter over there is just torture. I hadn't thought of him in years until today. Why is life such a cruel joke?"

    $ char_menu.add("Observe the scene table.")

    jump observe_menu

label observe_jock:

    hide alex4
    show alex6 at rightish

    a4 "Classic. Tyler is flexing his muscles on someone much smaller than him. His masculinity is so fragile that I reckon I could shatter it with a pin."

    hide alex6
    show alex3 at right

    a4 "I wonder what he thinks about... Is the most interesting part of his day really shaking helpless students by their ankles and shoving them into lockers?"

    hide alex3
    with Dissolve(0.5)
    with Fade (0.5,0.5,0.5)
    show tyler_happy at right
    with Dissolve(0.5)

    t "Dude, I totally swiped Stevie's prom ticket and hid it on top of the lockers. Gave that loser a huge wedgie while I was at it, could have never seen it coming."

    hide tyler_happy
    with Dissolve(0.5)
    with Fade (0.5,0.5,0.5)
    show alex_shocked4 at right
    with Dissolve(0.5)

    a4 "Huh, a prom ticket on the lockers. Poor Stevie, don't know what he did to deserve that. Knowing Tyler, he probably just breathed in his general direction."

    $ ticket_found += 1

    $ char_menu.add("Observe the jock table.")

    jump observe_menu

label hallway_three:

    scene hallway_dark
    with Fade (1, 1, 1)

    pause 2

    show hayley_excited at right
    with Dissolve(0.5)

    h "{i}*overheard*{/i} I can't believe I did it! I asked Ash to the Spring Fling and he said yes!"

    hide hayley_excited
    with Dissolve(0.5)
    show alex_looking at right
    with Dissolve(0.5)

    a4 "Huh, good for him."

    hide alex_looking
    show alex at right onlayer alexlayer

    a4 "Well, I feel like I should be happy for him, but I'm not. I honestly feel worse."

    scene hallway_dark2
    with Dissolve(0.5)
    hide alex onlayer alexlayer
    show alex4 at right
    show ash5 at left
    with Dissolve(0.5)

    ash "Alex! Sorry, just had to escape from Hayley for a sec to talk one last time."

    hide ash5
    show ash at left
    hide alex4
    show alex_looking at right

    a "Oh... hey. What's up?"

    hide alex_looking
    show alex_looking2 at right
    hide ash
    show ash2 at left

    ash "Well, you know, we probably won't talk for a while after this, maybe ever. You know, since you're ditching the prom and all."

    hide ash2
    show ash5 at left
    hide alex_looking2
    show alex_looking3 at right onlayer alexlayer

    ash "I guess I just wanted to say goodbye. Thanks for everything. You meant a lot to me."

    hide ash5
    with Dissolve(0.5)
    scene hallway_dark
    with Dissolve(0.5)

    a4 "..."

    hide alex_looking3
    hide alex_looking3 onlayer alexlayer
    show alex_hopeless at right

    stop music fadeout 3

    a4 "I didn't even say goodbye."

    jump evening

label evening:

    play music "sfx/Silent Voices.mp3" fadein 3

    scene bedroom
    with Fade(1,1,1)

    pause 2

    scene bedroom_dark
    with Dissolve(0.5)

    show alex_sad at right
    with Dissolve(0.5)

    a4 "..."

    a4 "..."

    hide alex_sad
    show alex_sad2 at right

    a4 "God, silence is so heavy, isn't it?"

    hide alex_sad2
    show alex6 at rightish

    a4 "I finally have to face all of the horrible choices I made today."
    
    hide alex6
    show alex_looking3 at right

    a4 "I didn't tie any loose ends, I got humiliated, and I came home even more pathetic than I already was."

    hide alex_looking3
    show alex_looking at right

    a4 "Maybe this is the part where everything ends cleanly. Like a fade-out."

    hide alex_looking
    show alex5 at rightish

    a4 "But no one asked me before writing this script, did they?"

    hide alex5
    show alex at right

    a4 "Do I make it quick and painless, or powerful and poetic?"

    hide alex
    show alex3 at right

    a4 "I'll save the long dramatic monologues for someone else."

    hide alex3
    show alex_looking at right

    a4 "Tonight... tonight everything will finally be quiet."

    hide alex_looking
    show alex_looking3 at right

    a4 "One perfect, final act of control."

    hide alex_looking3
    show alex_sad at right

    "..."

    stop music fadeout 5

    jump second_intro

label second_intro:

    scene bedroom
    with Fade(3,3,3)

    pause 1

    $ loops_done += 1

    play sound "sfx/alarmclock.mp3"

    "{i}*Alarm buzzes*{i}"
    
    "{i}7:00AM, May 19th, 2006.{i}"

menu:
    "Wake up.":
        jump wake_up_two

    "Snooze alarm.":
        jump snooze_alarm_two

label snooze_alarm_two:

    stop sound

    a "Just five more minutes..."

    m "{i}*Yelling from the kitchen{/i}* Alex! If you don't wake up right now, young man!"

    jump wake_up_two

label wake_up_two:

    stop sound

    play music "sfx/Sealed.mp3" fadein 2

    scene bedroom_dark
    with Dissolve(0.5)

    play sound "sfx/yawn.mp3" volume 0.5

    show alex_waking at right
    with Dissolve (2.0)

    hide alex_waking
    with Dissolve (1.0)

    show alex at right
    with Dissolve (1.0)
    pause 1

    hide alex
    play sound "sfx/shock.mp3"
    show alex_shocked2 at right

    a4 "Huh. Weird. Didn't I...?"

    hide alex_shocked2
    show alex_shocked at right

    a4 "No. No, no, no. That's impossible. I... I {i}definitely{/i} wasn't supposed to wake up today. Unless heaven has a suspiciously accurate Cedar Hill zip code..."

    hide alex_shocked
    show alex5 at rightish

    a4 "Okay. Its simple. I just dreamed out my entire day, start to finish. Right?"

    hide alex5
    show alex6 at rightish

    a4 "It was the weirdest dream too,"

    hide alex6
    show alex3 at right

    if jock_table == 1:
        a4 "Ash tried to reach out to me again, and I got a swirly from Tyler Kane."
    else:
        a4 "Tyler took my lunch money, and Ash and I briefly reconnected before he vanished away from me again without a trace."

    hide alex3
    show alex_waking at right

    a4 "The worst part about everything though, is that I have to delay the inevitable for another long day."

    hide alex_waking
    show alex at right

    a4 "Ugh, fine."

    hide alex
    show alex4 at right

menu:
    "Leave room.":
        jump leave_room_two

label leave_room_two:

    scene kitchen
    with Fade (1, 1, 1)
    pause 0.5

    scene kitchen_dark
    with Dissolve(0.5)

    show alex5 at rightish onlayer alexlayer
    with Dissolve(1.0)
    pause 0.5

    a4 "Huh. that same smell of syrup and burnt toast from my dream..."

    scene kitchen_dark2
    hide alex5 onlayer alexlayer
    show alex4 at right onlayer alexlayer
    show mother_two at left
    with Dissolve (0.5)

    m "Morning, honey! Big day!"

    hide alex4 onlayer alexlayer
    hide mother_two
    show alex_looking at right
    show mother_looking2 at left

    a "Ugh, yeah. Last day of school, the Spring Fling, I get it. I don't need to be reminded, thanks."

    hide mother_two
    hide alex_looking
    show mother_looking at left
    show alex_looking2 at right

    m "I made waffles, your favorite. Eat up!"

label shocked:

    hide mother_looking2
    hide mother_two
    hide mother_klutz 
    hide alex_shocked
    hide alex_flustered
    with Dissolve(0.5)

    scene kitchen_dark
    with Dissolve(0.5)

    hide alex_shocked3 onlayer alexlayer
    show alex_shocked2 at right
    with Dissolve(0.5)

    a4 "Huh?! There's no way. What's going on??"

    hide alex_shocked2
    show alex3 at right

    a4 "This is the part where a normal person would start screaming. I, however, am a professional in the art of ignoring red flags. Top of my class, thank you."

label ash_text_two:

    hide alex3
    show alex_shocked4 at right

    play sound "sfx/buzz.ogg"

    "{i}*phone buzzes*{i}"

    a4 "Ash?"

    hide alex_shocked4
    show alex_phone at rightish
    show text at slightleft
    with Dissolve(0.5)

    ash "{i}yo, still alive? last day 2day. better see u there.{i}"

    hide text
    with Dissolve(0.3)
    pause 0.5
    hide alex_phone
    show alex_phone2 at rightish
    
    a4 "Huh? I am... still alive."

    hide alex_phone2
    show alex_phone at rightish

menu:
    "Text back sarcastically.":
        jump sarcastic_two

    "Leave it on read.":
        jump read_two

label sarcastic_two:

    hide alex_phone
    show alex_phone at rightish

    a4 "I type: {i}'unfortunately. see u @ skl'{i}"

    jump school_intro_two

label read_two:

    hide alex_phone
    show alex_phone3 at rightish

    a4 "Leave it. Let him wonder if I'm dead."

    stop music fadeout 3

    jump school_intro_two

label school_intro_two:

    play music "sfx/Far Away.mp3" fadein 3

    scene hallway
    with Fade (1, 1, 1)
    pause 0.5

    scene hallway_dark
    with Dissolve(0.5)

    show alex5 at rightish
    with Dissolve(1.0)
    pause 0.5

    a4 "Ah. the delightful smell of Eau de Public School: An enchanting mix of Axe body spray, sweaty teenagers, and crushed dreams."

    hide alex5
    show alex_shocked at right

    a4 "Two lockers down, Brent's retelling his tragic fountain story."

    hide alex_shocked
    show alex_shocked4 at right

    a4 "Right on cue. Perfect comedic timing, if I wasn't already internally screaming."

    hide alex_shocked4
    show alex6 at rightish

    a4 "{i}Fun psychological fact{/i}: this is where a person realizes they're stuck in a time loop. {i}Fun Alex fact{/i}: I'm still pretending it's a coincidence. Denial is cheaper than therapy."

    hide alex6
    show alex3 at right

    a4 "The Spring Fling poster? Still peeling at the corner. Tyler? Thinks he's sneaking up on me, but I know he's there. Locker slam? Right as I turn my head."

    hide alex3
    show alex4 at right

    play sound "sfx/lockerslam.mp3"

    "{i}*locker slams*{i}"

    stop sound

    hide alex4
    show alex5 at rightish onlayer alexlayer

    a4 "The universe is hitting play on a rerun I didn't ask for."

    scene hallway_dark2
    show tyler_happy at left
    with Dissolve(0.5)

    hide alex5 onlayer alexlayer
    show alex_looking2 at right
    with Dissolve(0.5)

    t "See that? Around here, you don't react. Reacting means you care, and caring is blood in the water. These halls run on humiliation. Lunch money? Gone. Dignity? Don't even bother bringing it."

    hide tyler_happy
    show tyler_happy2 at left
    hide alex_looking2
    show alex5 at rightish onlayer alexlayer

    a4 "Right on time. Tyler Kane. I think he only picks these petty fights because he hates himself."

    hide tyler_happy
    show tyler_angry3 at left
    hide alex5 onlayer alexlayer
    show alex_angry2 at right

    t "Anyway, lunch money now, Hayes. Those hot churros aren't gonna pay for themselves."

    hide tyler_angry3
    show tyler_angry4 at left
    hide alex_angry2
    show alex3 at right

    if has_bruise == 0:

        a4 "Yesterday... dream yesterday... I folded like a wet paper towel. Dug through my pockets, gave him everything, mumbled something about “just take it.”"

    else:

        a4 "Yesterday... dream yesterday... Tyler forced me to kiss cold locker metal."

    hide alex3
    show alex5 at rightish
    
    a4 "Today? Different script. I've had time to think about what I should've done differently."

    hide alex5
    show alex at right

menu:

    "Are we dating?":
        jump dating

    "I'm claiming you as a dependent on my taxes.":
        jump taxes

label dating:

    hide tyler_angry2
    show tyler_happy2 at left
    hide alex
    show alex_looking at right

    a "Thing is, Kane, if you keep asking for my money every day, we're basically dating. Should I get you a corsage for Spring Fling?"

    jump school_hallway_two

label taxes:

    hide tyler_angry2
    show tyler_happy2 at left
    hide alex
    show alex_looking at right

    a "Sure, Tyler, but if I'm funding your lunch every day, I'm claiming you as a dependent on my taxes."

    jump school_hallway_two

label school_hallway_two:

    hide alex_looking
    show alex_looking2 at right onlayer alexlayer
    hide tyler_happy2
    show tyler_angry5 at left

    t "You're lucky I'm in a good mood, nerd. Don't let this get to your little head."

    scene hallway_dark
    with Dissolve(0.5)

    pause 0.5

    hide alex_looking2 onlayer alexlayer
    show alex_shocked4 at right
    with Dissolve(0.5)

    a4 "Yesterday I paid the toll. Today I keep the cash. Same hallway, same bully, different outcome."

    hide alex_shocked4
    show alex3 at right
    
    a4 "Feels like cheating at life... or whatever this is."

    if ticket_found == 1:

        hide alex3
        show alex6 at rightish

        a4 "Okay... just humor the crazy dream kid for a sec."

        hide alex6
        show alex2 at rightish

        a4 "Tyler said there'd be a Spring Fling ticket wedged above the lockers, right? Sure. And maybe Bigfoot's up there handing out prom dates too."

        hide alex2
        show alex_shocked2 at right

        play sound "sfx/shock.mp3"

        "{i}*Picks up ticket*{i}"

        $ ticket_collected += 1

        hide alex_shocked2
        show alex_happy5 at right

        a4 "...Okay. Nope. No. This is fine. Totally normal for reality to start taking notes from my subconscious."

        hide alex_happy5
        show alex6 at rightish

        a4 "Next up, maybe the janitor tells me my horoscope."

        jump hallway_day_two
    else:
        jump hallway_day_two

label hallway_day_two:
    
    scene hallway_dark
    with Fade (0.5,0.5,0.5)

    show alex_looking3 at right
    with Dissolve(0.5)

    a4 "And there he is. Ash. Same slouch against the lockers, same chipped black nail polish tapping out some My Chemical Romance song."

    hide alex_looking3
    show alex at right

    a4 "He's even got the same crooked grin, like he knows something I don't."

    if talked_to_ash == 0:

        hide alex
        show alex_looking at right

        a4 "Yesterday... my dream, hallucination, whatever, you walked right past me. I didn't say a word."

        hide alex_looking 
        show alex3 at right

        a4 "And then... yeah, we all know how that night ended."

        hide alex3
        show alex6 at rightish onlayer alexlayer

        a4 "So what happens if I actually open my mouth this time? Science experiment, kids. Place your bets."

        jump ash_encounter
    else:

        hide alex
        show alex6 at rightish onlayer alexlayer

        a4 "I feel like I can do better than I did yesterday."

        jump ash_encounter

label ash_encounter:

    scene hallway_dark2
    with Dissolve(0.5)

    show ash_sly2 at left
    with Dissolve(0.5)

    hide alex6 at rightish onlayer alexlayer
    show alex at right
    with Dissolve(0.5)

    ash "Well well, if it isn't the ghost of homeroom past. Survived the morning apocalypse?"

    hide ash_sly2
    show ash_sly3 at left

menu:
    "Thought you'd escaped.":

        hide alex
        show alex_looking at right

        a "Thought you'd escaped this prison already."

        jump ash_encounter2

    "Not at Hot Topic?":

        hide alex
        show alex_looking at right

        a "Haven't crawled off to work full time at Hot Topic yet?"

        jump ash_encounter2

label ash_encounter2:

    hide alex_looking
    show alex_looking2 at right
    hide ash_sly3
    show ash_sly at left

    ash "Please. I'm not leaving until I get my diploma {i}and{/i} a tetanus shot."

    hide ash_sly
    show ash at left
    hide alex_looking2
    show alex_happy7 at right

    a "Classic Cedar Hill starter pack."

    hide alex_happy7
    show alex4 at right
    hide ash
    show ash4 at left

    ash "So what's the occasion? What did I do to deserve your presence?"

    hide ash4
    show ash5 at left
    
    ash "You usually avoid me like gym class."

    hide ash5
    hide alex4
    show ash3 at left
    show alex_shocked at right

    a "What can I say? Figured I'd face my fears before graduation, you know. Like 'gym class'."

    hide alex_shocked
    show alex5 at rightish

    a4 "Look at that. I think I did pretty well there."

    hide alex5
    show alex4 at right
    hide ash3
    show ash4 at left

    ash "Anyway, you coming to the Spring Fling tonight? Or are you planning to sulk in a corner like a tragic indie film protagonist?"

    hide ash4
    show ash3 at left

    if ticket_found == 0:
        menu: 
            "Depends.":
                jump ash_no_ticket

            "I won't make it.":
                jump ash_no_ticket

    else:
        menu:
            "Got it handled.":
                jump ash_ticket

label ash_no_ticket:

    hide alex_looking2
    hide alex4
    show alex_looking at right

    a "Depends on if I make it that far."

    hide alex_looking
    show alex_looking2 at right
    hide ash3
    show ash5 at left

    ash "Wow, dark much? You're even edgier than me these days, and I'm literally a scene kid."

    hide ash5
    show ash at left
    hide alex_looking2
    show alex_looking at right

    a "Well, I would... but I don't have a ticket."

    hide alex_looking
    show alex at right onlayer alexlayer
    hide ash
    show ash5 at left

    ash "Well, come back to me with more prom 'logistics' when you do."

    hide ash5
    scene hallway_dark
    with Dissolve(0.5)

    pause 1

    hide alex onlayer alexlayer
    show alex5 at rightish

    a4 "Oh, thanks for the reminder. I totally forgot that one of the universe's rules is that prom is gated by a piece of paper."

    hide alex5
    show alex3 at right

    a4 "Honestly, it's like the game just handed me a quest marker with a big glowing arrow saying, ‘Hey dummy, get this ticket or nothing happens.' Thanks. Very subtle."

    play sound "sfx/schoolbell.mp3"
    
    jump homeroom_two

label ash_ticket:

    hide alex4
    show alex_happy7 at right

    a "Yep... got it handled, no worries."

    hide ash3 
    show ash_happy at left
    hide alex_happy7
    show alex at right

    ash "Wow, Look at you! Who even are you? I thought you'd think the prom was a 'tragic waste of time', and you'd be off hiding in a corner somewhere instead, wallowing in existential dread."

    hide ash_happy
    show ash at left
    hide alex
    show alex3 at right

    a4 "Yesterday I'd have scoffed at that and then gone home to practice my dramatic exit. Dream or loop, this is a new variable."

    hide alex3
    show alex7 at right
    
    a4 "Yesterday I didn't even get this far, and today, I can respond. Wow, I feel powerful."

    hide alex7
    show alex_happy7 at right

    a "Hah. Corner's full. Had to take the scenic route through hell instead. You know... Axe body spray, screaming teenagers."

    hide alex_happy7
    show alex_looking at right

    a "So... you planning on asking Hayley?"

    hide alex_looking
    show alex_looking2 at right
    hide ash
    show ash_sly2 at left

    ash "Depends. Are you trying to be helpful, or just judging me?"

    hide ash_sly2
    show ash_sly3 at left
    hide alex_looking2
    show alex6 at rightish

    a "Maybe a little of both. I mean, come on. Hayley's sweet, but even she deserves a chance to panic about her life choices, right?"

    hide alex6
    show alex_flustered at right
    hide ash_sly3
    show ash_sly at left

    ash "Hah. Whatever, Hayes. You implying anything?"

    hide ash_sly
    show ash at left

menu:

    "Maybe.":

        hide alex_flustered
        show alex6 at rightish

        a "I dont know, am I?"

        jump ash_encounter_end

    "No...":

        hide alex_flustered
        show alex6 at rightish

        a "I'm just saying, don't leave her hanging too long!"

        jump ash_encounter_end

label ash_encounter_end:

    hide ash
    with Dissolve(0.5)

    pause 1
    
    hide alex6
    show alex7 at right

    a4 "That's all I need for now. Plant the seed, walk away, let chaos do the rest. One small nudge, a million possible outcomes."

    hide alex7
    show alex at right

    a4 "Heart rate check: slightly faster. Probably the mold."

    play sound "sfx/schoolbell.mp3"

    jump homeroom_two

label homeroom_two:

    scene classroom
    with Fade(1,1,1)

    pause 2

    scene classroom_dark
    with Dissolve(0.5)

    show alex5 at rightish
    with Dissolve(0.5)

    a4 "Homeroom. Someone coughs across the room, a dramatic, “look at me, I might die any second,” and the motivational posters glare right back at me. Everything looks... exactly the same."

    hide alex5
    show alex_looking at right

    a4 "Ash is leaning back with that expression that says, 'I am unimpressed and possibly plotting domination'."

    hide alex_looking
    show alex3 at right

    a4 "Hayley snickers at something he wrote,"

    hide alex3
    show alex6 at rightish

    a4 "Tyler flexes like a guy in a superhero audition,"

    hide alex6
    show alex_shocked4 at right

    a4 "and me? Trying not to hyperventilate."

    hide alex_shocked4
    show alex5 at rightish

    a4 "Great. Here comes the speech. Right on cue."

    hide alex5
    with Dissolve(0.5)
    show teacher2 at right
    with Dissolve(0.5)

    teach "Good morning, seniors! Today is a special day, it being the last day of your little school lives, so let's all remember to cherish our friends and celebrate the end of high school with a spectacular bang!"

    hide teacher2
    with Dissolve(0.5)
    show alex at right
    with Dissolve(0.5)

    a4 "Ah. Yep. Exactly the same speech. Word for word. Yesterday she said it, I nodded and pretended to care while mentally composing my suicide note, today, somehow, it lands even worse."

    hide alex
    show alex4 at right

    jump homeroom_menu_two

label homeroom_menu_two:

    hide alex_looking
    hide alex
    hide alex6
    show alex4 at right

menu:
    set char_menu
    "Write a sarcastic note.":
        jump sarcastic_note_two

    "Look around you.":
        jump look_around_two

    "Pretend to write notes.":
        jump take_notes_two

jump cafeteria_two

label sarcastic_note_two:

    play scribble "sfx/scribble.mp3" volume 0.5

    hide alex4
    show alex_looking at right
    
    a4 "Hey Ash... uh, hey. I was gonna roast you for ghosting me, but... can't think of anything clever now. Weird, right? I'm supposed to be smarter than I was yesterday."

    stop scribble

    $ char_menu.add("Write a sarcastic note.")

    jump homeroom_menu_two

label look_around_two:

    hide alex4
    show alex6 at rightish

    a4 "Look at them all, grinning like fools. They're totally clueless."

    hide alex6
    show alex at right
    
    a4 "They don't know that they're programmed to do all of these things exactly the way they happened yesterday, like a load of video game NPCs..."

    $ char_menu.add("Look around you.")

    jump homeroom_menu_two

label take_notes_two:

    hide alex4
    show alex6 at rightish

    a4 "Mhm. Groundbreaking. Maybe I'll just doodle ‘existence is rigged'..."

    $ char_menu.add("Pretend to write notes.")

    jump homeroom_menu_two

label cafeteria_two:

    scene cafeteria
    with Fade(1,1,1)

    pause 2

    scene cafeteria_dark
    with Dissolve(0.5)

    show alex3 at right
    with Dissolve(0.5)

    a4 "The cafeteria smells like mystery slop and a toasted sense of ambition."

    hide alex3 
    show alex2 at rightish

    a4 "Students are clustered at the same cliques as yesterday: jocks flexing at the big table, scene kids whispering over MySpace layouts, a few loners trying not to make eye contact with anyone, including me."

    if ticket_found == 0:
        jump no_ticket

    else:
        jump has_ticket

label no_ticket:

    hide alex2
    show alex at right

    a4 "Okay, the universe has made it very clear to me that I need a ticket for this stupid prom. I have to sit somewhere to figure it out."

    hide alex
    show alex5 at rightish

    a4 "There's only one sensible choice. Either endure the jock table, or hide at a corner table and eavesdrop."

    hide alex5
    show alex4 at right

    jump where_to_sit_menu

label has_ticket:

    hide alex2
    show alex5 at rightish

    a4 "Same chaos, same smells, same existential dread."

    hide alex5
    show alex3 at right

    a4 "Yesterday, I figured out a few secrets, like the location of the Spring Fling ticket, and now it feels like I have a tiny edge. A cheat code for survival, if you will."

    hide alex3
    show alex at right

    a4 "Now it's time for the social nightmare: sitting at the scene table with Ash and Hayley."

    hide alex
    show alex5 at rightish

    a4 "Yesterday, I would've obliterated Ash with sarcasm. Today... I can't. I can't think of anything truly mean. And that's weird. That's new. That's... slightly dangerous."

    scene cafeteria_dark2
    with Fade (0.5,0.5,0.5)

    show alex4 at right
    with Dissolve(0.5)

    show ash_sly2 at left
    with Dissolve(0.5)

    ash "Hey. You made it. And here I thought you'd ghost us again like last year. What's different today? Did the world finally bribe you to come?"

    hide ash_sly2
    show ash_sly3 at left
    hide alex4
    show alex_happy7 at right

    a "Oh, Ash... if only you knew I'm not making conscious decisions here. My brain's just following yesterday's cheat sheet."

    hide alex_happy7
    show alex5 at rightish

    a4 "Hah. If only he knew I was serious."

    hide alex5
    show alex_happy3 at right
    hide ash_sly3
    show ash4 at left

    ash "Huh. That's... tame. Careful, Hayes, you might actually be growing up. Scary thought."

    hide ash4
    show hayley at left
    with Dissolve(0.5)

    hide alex_happy3
    show alex_looking2 at right

    h "Someone swapped your brain for a slightly less miserable one?"

    hide hayley
    show hayley3 at left

    hide alex_looking2
    show alex_flustered2 at right

    a4 "I want to be snarky. I can't. My chest does this weird little flutter thing, and I have no idea why. Worst bug in the system."

    hide hayley3
    show ash2 at left
    with Dissolve(0.5)
    hide alex_flustered2
    show alex_looking2 at right

    ash "Alex, you know what I've been thinking about? Do you remember that time in Lincoln Park in '02 with those dry-ice bottle rockets?"

    hide ash2
    hide alex_looking2
    show alex_happy3 at right
    show ash_happy at left

    ash "You said it was 'basically science class,' then we completely blew out the neighbor's windows."

    hide alex_happy3
    show alex_happy at right
    hide ash_happy
    show ash_happy2 at left

    a "Hahaha! Dude, the look on their faces before we started running made it totally worth it!"

    hide alex_happy
    show alex_happy4 at right
    hide ash_happy2
    show ash_happy at left

    ash "Oh, oh, and that time in '99 when we went up to Sturgeon Bay and you made a flamethrower out of a WD-40 can!"

    hide ash_happy
    show ash_happy2 at left
    hide alex_happy4
    show alex_happy6 at right

    a "You were a total maniac with that thing! We must have burned down at least a hundred feet of bush!"

    hide alex_happy6
    show alex_happy4 at right
    hide ash_happy2
    show ash_happy at left

    ash "Dude, you were the one who stole the lighter from your mom's boyfriend! Pretty sure we were two seconds away from becoming a ‘local news cautionary tale.'"

    hide ash_happy
    show ash_happy2 at left
    hide alex_happy4
    show alex_happy5 at right

    a4 "There's this uncontrollable spasm in my face, am I smiling? Just hearing Ash laugh makes it hard not to. It's kinda contagious?"

    hide alex_happy2
    show alex7 at right

    a4 "This is the one moment today that hasn't felt like absolute garbage. Odd."

    jump hallway_day_two_two

label observe_two_outro:

    hide alex4
    show alex3 at right

    a4 "And now, player, you've got the information you need to progress. Ticket: check. Life shit: messy. Feelings: convoluted."

    hide alex3
    show alex6 at rightish

    a4 "Let's see if this edge lasts through the rest of the day... or if I'll still screw it all up again."

    jump hallway_day_two_two

label hallway_day_two_two:

    scene hallway
    with Fade (1, 1, 1)
    pause 0.5

    scene hallway_dark
    with Dissolve(0.5)

    if ticket_collected == 0:

        show alex_happy3 at right
        with Dissolve(0.5)

        "{i}Using your newfound knowledge, you collect the ticket from on top of the lockers{i}"

        $ ticket_collected += 1

        hide alex_happy3
        show alex_happy7 at right

        a4 "Alright, ticket: check. Survival: in progress. Now comes the part of the day I'm still figuring out... the hallway gauntlet."

        hide alex_happy7
        hide alex5
        show alex_looking at right

    else:
        show alex5 at rightish
        with Dissolve(1.0)
        pause 0.5

    a4 "Yesterday, I fumbled through here and Hayley spilled the beans about the dance. I looked like a complete moron. Today, though? Today I get to try again."

    hide alex_looking
    hide alex5
    show hayley_excited at right
    with Dissolve(1)

    h "{i}*overheard*{/i} I can't believe I did it! I asked Ash to the Spring Fling and he said yes!"

    hide hayley_excited
    show alex_shocked5 at right
    with Dissolve(1)

    stop music fadeout 3

    a4 "..."

    play music "sfx/Value.mp3" fadein 3

    hide alex_shocked5
    show alex_shocked4 at right

    a4 "No..."

    hide alex_shocked4
    show alex2 at rightish

    a4 "That line, word for word, was from yesterday."

    hide alex2
    show alex3 at right

    a4 "Or the dream."

    hide alex3
    show alex_shocked4 at right

    a4 "Or whatever cosmic rerun I'm trapped in."

    hide alex_shocked4
    show alex_looking4 at right

    a4 "But this time I've got the ticket. The so-called golden key to teen happiness."

    hide alex_looking4
    show alex_hopeless at right onlayer alexlayer

    a4 "So how the hell is the same scene playing again?"

    scene hallway_dark2
    show ash_happy at left
    with Dissolve(0.5)
    hide alex_hopeless onlayer alexlayer
    show alex at right
    with Dissolve(0.5)

    ash "Alex! Sorry, just had to escape from Hayley for a sec to talk one last time."

    hide ash_happy
    show ash_happy2 at left
    hide alex
    show alex_looking4 at right

    a4 "And here comes the encore. Same entrance. Same smile. Except now it hits different."

    hide alex_looking4
    hide ash_happy2
    show ash at left
    show alex_flustered2 at right

    a "Uh... yeah. Just... leaving. Congrats on, uh, the... thing."

    hide ash
    show ash4 at left
    hide alex_flustered2
    show alex_flustered at right

    ash "Hayley told you already, huh? Yeah, she asked me. Guess I've got plans tonight."

    hide alex_flustered
    hide ash4
    show ash3 at left
    show alex_looking4 at right

    a4 "Plans. Right. Plans that apparently don't care that I have the actual ticket in my pocket."

    hide alex_looking4
    show alex2 at rightish

    a4 "Having obtained the special quest item means you don't have to do all the talking, right? Isn't that how this game works?"

    hide alex2
    show alex_happy2 at right

    a "Cool. That's... cool. Big night. Balloons. Terrible music. Dream come true."

    hide ash3
    show ash5 at left
    hide alex_happy2
    show alex_looking3 at right onlayer alexlayer

    ash "I couldn't wait around forever for you to ask me, Alex. She got to me first, I'm sorry."
    
    hide ash5
    show ash4 at left

    ash "Anyway, if I don't see you there... guess this is it. End of high school. End of... us being randomly in each other's way."

    hide ash4
    show ash6 at left

    ash "..."

    hide ash6
    hide ash_happy2
    show ash5 at left

    ash "Take care, alright?"

    hide ash5
    with Dissolve(1)
    show alex_looking3 at right onlayer alexlayer
    scene hallway_dark
    with Dissolve(0.5)

    pause 1.5

    hide alex_looking3 onlayer alexlayer
    show alex_hopeless at right
    with Dissolve(0.5)

    a4 "No. No. This can't be happening."

    hide alex_hopeless
    show alex_sad2 at right

    a4 "I need to shout out, stop him from leaving. I can't lose him again."

    hide alex_sad2
    show alex_looking4 at right

    a4 "Why aren't my feet moving?"

    hide alex_looking4
    show alex_sad2 at right

    a4 "Why can't I scream?"

    hide alex_sad2
    show alex_looking3 at right

    a4 "Why have I wasted my second chance?"

    hide alex_looking3
    show alex_looking4 at right

    a4 "Yesterday, I thought this was just another reality check. Today? It's worse."

    hide alex_looking4
    show alex_hopeless at right

    a4 "Today I know I could have been there."

    hide alex_hopeless
    show alex_looking4 at right

    a4 "I have the ticket. I have the timing. I have... feelings."

    hide alex_looking4
    show alex_flustered2 at right

    a4 "There it is. The final boss I didn't know I was fighting."

    hide alex_flustered2
    show alex_shocked4 at right
    
    a4 "This isn't about a dance. It's about Ash."

    hide alex_shocked4
    show alex_hopeless at right

    a4 "The loop isn't punishing me for missing a party, it's punishing me for running from what I want."

    hide alex_hopeless
    show alex6 at rightish

    a4 "Great. So the universe isn't just glitching, it's shipping us. And it won't stop the reruns until I stop being a coward. Fantastic. No pressure."

    jump evening_two

    label evening_two:

    scene bedroom
    with Fade(1,1,1)

    pause 2

    scene bedroom_dark
    with Dissolve(0.5)

    show alex_looking4 at right
    with Dissolve(0.5)

    a4 "Hayley's probably picking out a dress right now. Ash is probably texting her. And I'm sitting here holding this piece of paper like it's a map from hell."

    hide alex_looking4
    show alex_looking3 at right

    a4 "..."

    hide alex_looking3
    show alex_sad2 at right
    
    a4 "But I saw it this time. The way it felt when he said goodbye. That wasn't nothing."

    hide alex_sad2
    show alex_looking4 at right

    a4 "Maybe the loop isn't a punishment, it's one more shot to get it right."
    
    hide alex_looking4
    show alex_looking at right

    a4 "Please, you sick and twisted god, give me one more chance."

    hide alex_looking
    show alex_hopeless at right

    a4 "I hope it's still May 19th tomorrow."

    stop music fadeout 3

    jump loop_three_intro

label loop_three_intro:

    scene bedroom
    with Fade(3,3,3)

    pause 1

    $ loops_done += 1

    play sound "sfx/alarmclock.mp3"

    "{i}*Alarm buzzes*{i}"
    
    "{i}7:00AM, May 19th, 2006.{i}"

menu:
    "Wake up.":
        jump wake_up_three

    "Snooze alarm.":
        jump snooze_alarm_three

label snooze_alarm_three:

    stop sound

    a "Just five more minutes..."

    m "{i}*Yelling from the kitchen{/i}* Alex! If you don't wake up right now, young man!"

    jump wake_up_three

label wake_up_three:

    play music "sfx/Sealed.mp3" fadein 3

    stop sound

    scene bedroom_dark
    with Dissolve(0.5)

    play sound "sfx/yawn.mp3" volume 0.5

    show alex_waking at right
    with Dissolve (2.0)

    hide alex_waking
    with Dissolve (1.0)

    show alex at right
    with Dissolve (1.0)
    pause 1

    hide alex
    show alex_shocked5 at right

    a4 "!!!"

    play sound "sfx/shock.mp3"

    hide alex_shocked5
    show alex_shocked2 at right

    a4 "Ah!! It's still May 19th!!"

    hide alex_shocked2
    show alex_shocked4 at right
   
    a4 "There's no time to waste."

    jump leave_room_three

label leave_room_three:

    scene kitchen
    with Fade (1, 1, 1)
    pause 0.5

    scene kitchen_dark2
    with Dissolve(0.5)

    show alex_shocked5 at right
    show mother_two at left
    with Dissolve(1.0)
    pause 0.5

    m "Morning, honey! Big day!"

    hide alex_shocked5
    show alex_shocked at right
    hide mother_two
    show mother_looking3 at left

    a "Watch out for the milk!"

    hide mother_looking3
    play sound "sfx/shock.mp3"
    show mother_shocked at left
    hide alex_shocked
    show alex_happy4 at right

    m "How did you-?"

    hide alex_happy4
    show alex_happy2 at right
    hide mother_shocked
    show mother_shocked2 at left

    a "Lucky guess. Love you, bye!"

    stop music fadeout 3

    scene black
    with Dissolve(1)

    a4 "{i}'ash. I know u were abt to txt me. just meet me @ skl. talk soon.'{i}"

    jump school_intro_three

label school_intro_three:

    play music "sfx/Empty Hope.mp3" fadein 3

    scene hallway
    with Fade (1, 1, 1)
    pause 0.5

    scene hallway_dark
    with Dissolve(0.5)

    show alex5 at rightish
    with Dissolve(1.0)
    pause 0.5

    a4 "Okay, no time for Tyler, no time for Hayley, no “gee Alex why the long face.” I've wasted two chances on fixing things and I'm not about to make it three."

    hide alex5
    show alex3 at right

    a4 "Get the ticket. Find Ash. Fix things for good. No detours, no sarcastic side quests, no NPC chatter. Everyone else can keep looping through May 19th forever; But I've got one shot to break the curse."

    hide alex3
    show alex_angry at right onlayer alexlayer

    a4 "Move it, Hayes. This shit ends now."

    scene hallway_dark2
    show tyler_angry3 at left
    with Dissolve(0.5)

    hide alex_angry onlayer alexlayer
    show alex_angry2 at right
    with Dissolve(0.5)

    t "Well, well, well, Look who the cat dragged in. Lunch mon-"

    hide tyler_angry3
    show tyler_happy2 at left
    hide alex_angry2
    show alex_angry at right

    a4 "There's no time for you, Tyler."

    hide alex_angry
    show alex6 at rightish onlayer alexlayer

    a "Your mom's in the principal's office. Something about your ‘borrowed' skateboard."

    scene hallway_dark
    with Dissolve(0.5)
    hide tyler_happy2
    with Dissolve(0.5)

    hide alex6 onlayer alexlayer
    show alex_happy4 at right
    with Dissolve(0.5)

    "{i}*He runs off*{i}"

    a4 "Hah. Predictable."

    hide alex_happy4
    show alex_shocked4 at right

    a4 "Oh my god, Ash. Finally."

    hide alex_shocked4
    show alex_hurt at right onlayer alexlayer

    a "Ash!!"

    scene hallway_dark2
    with Dissolve(0.5)

    show ash5 at left
    with Dissolve(0.5)
    hide alex_hurt onlayer alexlayer
    show alex at right
    with Dissolve(0.5)

    ash "Uh... hey? How did you-"

    hide ash5
    show ash6 at left
    hide alex
    show alex_flustered2 at right

    a "Listen. I can't let today happen again. Yesterday, every yesterday, I fucked things up. I blew my last chance."

    hide alex_flustered2
    show alex_flustered at right
    hide ash6
    show ash5 at left

    ash "Alex, what are you-"

    if burning_man == 1:
        jump ending_one2

    else:
        jump ending_two

label ending_one2:

    hide ash5
    show ash6 at left
    hide alex_flustered
    show alex_happy2 at right

    a "You remember Burning Man. 2003. When those idiot seniors drove us all the way out to Nevada, and we spent a week getting stoned out of our minds in the middle of the desert?"

    hide alex_happy2
    show alex_happy4 at right
    hide ash6
    show ash_happy at left

    ash "God, yeah. Hard to think we were only fifteen. I thought we were gonna die or end up on a missing poster."

    hide ash_happy
    show ash_happy2 at left
    hide alex_happy4
    show alex_happy5 at right

    a "Same. And it's still the best week I've ever had."

    hide ash_happy
    show ash6 at left
    hide alex_happy5
    show alex_flustered2 at right

    a " Every time this day repeats... ...every time I think about what actually matters, that's the memory that sticks. Just us, lost in the desert, laughing like idiots."

    hide alex_flustered2
    show alex_happy2 at right

    a "I don't know if today's gonna vanish, or if this is my last shot, but I can't keep acting like you're just some old inside joke I outgrew."

    hide alex_happy2
    show alex_happy7 at right

    a "I can't keep ignoring you, wallowing in my own little misery."

    hide alex_happy7
    show alex3 at right

    a4 "There's no turning back now."

    hide alex3
    show alex_flustered2 at right

    a "I like you, Ash. A lot."

    hide alex_flustered2
    show alex_happy7 at right

    a "And if tomorrow never comes, I want you to know that."

    hide alex_happy7
    show alex_looking3 at right

    ash "..."

    hide ash6
    show ash4 at left
    hide alex_looking3
    show alex_flustered at right

    ash "You waited three years to tell me this, and you picked the morning of our last day?"

    hide ash4
    show ash_happy2 at left
    hide alex_flustered
    show alex_happy2 at right

    a "Hey, I'm consistent. Late to everything except bad timing."

    hide alex_happy2
    show alex_happy3 at right
    hide ash_happy2
    show ash_sly2 at left

    ash "You know what? screw the dance. It's a 'tragic waste of time' anyways. Let's just disappear after school."

    hide alex_happy3
    show alex_happy4 at right
    hide ash_sly2
    show ash_sly at left

    ash "Another road trip. ...Maybe not Nevada this time."

    hide ash_sly
    show ash_happy at left
    hide alex_happy4
    show alex_happy6 at right onlayer alexlayer

    a "Yeah. I'd like that."

    scene hallway_dark
    hide alex_happy6 onlayer alexlayer
    with Fade(2,2,2)

    show alex3 at right
    with Dissolve(0.5)

    a4 "Today, I killed myself. The spectacular tragedy of May 19th. A 17 year-old mopey, suicidal mess with nothing to live for."

    hide alex3
    show alex7 at right

    a4 "Now? Somehow, I'm not dead. I'm... even kind of happy? Like I'm a character in some weird indie visual novel, and the player decided that a sad ending was just not good enough."

    hide alex7
    show alex_happy7 at right

    a4 "Maybe some days are worth repeating. Or maybe, finally, this one doesn't have to."

    jump finale

label ending_two:

    hide ash5
    show ash6 at left
    hide alex_flustered
    show alex_happy2 at right

    a "Sturgeon Bay, 1999. That homemade flamethrower we almost burned my cousin's shed down with."

    hide alex_happy2
    show alex_flustered2 at right

    a "I think that was when I realised how much you meant to me. And maybe... I dunno... you mattered more than I let myself admit."

    hide alex_flustered2
    show alex_flustered at right

    ash "..."

    hide ash6
    show ash5 at left
    hide alex_flustered
    show alex_happy3 at right

    ash "Honestly, I wasn't sure I'd ever hear you like this. But... damn, I'm glad I am."

    hide ash5
    show ash6 at left
    hide alex_happy3
    show alex_happy2 at right

    a "I don't know if today's gonna vanish, or if this is my last shot, but I can't keep acting like you're just some old inside joke I outgrew."

    hide alex_happy2
    show alex_happy7 at right

    a "I can't keep ignoring you, wallowing in my own little misery."

    hide alex_happy7
    show alex3 at right

    a4 "There's no turning back now."

    hide alex3
    show alex_flustered2 at right

    a "I like you, Ash. A lot."

    hide alex_flustered2
    show alex_happy7 at right

    a "And if tomorrow never comes, I want you to know that."

    hide alex_happy7
    show alex_looking3 at right

    ash "..."

    hide ash6
    show ash5 at left

    ash "Alex, I like you too."

    hide ash5
    show ash4 at left

    ash "But some things just can't be fixed in one day."

    hide ash4
    show ash6 at left

    ash "..."

    hide ash6
    show ash_happy at left
    hide alex_looking3
    show alex_happy3 at right

    ash "How about we start with you taking me to the prom tonight?"

    hide alex_happy3
    show alex_happy7 at right onlayer alexlayer
    hide ash_happy
    show ash_happy2 at left

    a "Yeah. I'd like that."

    scene hallway_dark
    hide alex_happy7 onlayer alexlayer
    with Fade(2,2,2)

    show alex3 at right
    with Dissolve(0.5)

    a4 "Somehow I went from wanting to kill myself to standing here, alive, talking to the one person who actually makes me care about anything, all on the same day."

    hide alex3
    show alex6 at rightish

    a4 "Yeah, I know this is technically a game mechanic, but fuck that. This feels real."

    hide alex6 
    show alex_happy3 at right

    pause 2

    hide alex_happy3
    show alex_happy at right

    a4 "This is a good ending."

    jump finale2

label finale:

    scene car

    with Fade(3,3,3)

    pause 3

    scene black
    with Fade (3,3,3)
    
    # This ends the game.

    return

label finale2:

    scene ball3

    with Fade(3,3,3)

    pause 3

    scene black
    with Fade (3,3,3)


    # This ends the game.

    return
