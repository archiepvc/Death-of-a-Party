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
define c = Character(_("Cat"), color="#c36fd6", what_slow_cps=35, callback=text_sounds)
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

# Variables
default betrayal = 0
default truth = 0
default violence = 0
default acceptance = 0

default charlie_bond = 0
default cat_bond = 0
default danny_bond = 0

default charlie_love = 0
default cat_love = 0
default danny_love = 0

default presents_opened = 0

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
    SCALE_X = 0.55
    SCALE_Y = 0.436

    def scaled(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init:
    image bedroom = ("bedroom.png")
    image bedroom_dark = scaled("bedroom_dark.png")
    image cafeteria = scaled ("cafeteria.png")
    image cafeteria_dark = scaled ("cafeteria_dark.png")
    image classroom = scaled ("classroom.png")
    image classroom_dark = scaled ("classroom_dark.png")
    image hallway = scaled ("hallway.png")
    image hallway_dark = scaled ("hallway_dark.png")
    image kitchen = scaled ("kitchen.png")
    image kitchen_dark = scaled ("kitchen_dark.png")
    image cafeteria_dark2 = scaled ("cafeteria_dark2.png")
    image hallway_dark2 = scaled ("hallway_dark2.png")
    image kitchen_dark2 = scaled ("kitchen_dark2.png")
    image bathroom = scaled ("bathroom.png")
    image bathroom_dark = scaled ("bathroom_dark.png")

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
    SCALE_X = 0.32
    SCALE_Y = 0.32

    def scaledsprite(name):
        return im.FactorScale(name, SCALE_X, SCALE_Y)

init:
    image alex_waking = scaledsprite ("alex_waking.png")
    image alex = scaledsprite ("alex.png")
    image alex_angry = scaledsprite ("alex_angry.png")
    image alex_angry2 = scaledsprite ("alex_angry2.png")
    image alex_flustered = scaledsprite ("alex_flustered.png")
    image alex_flustered2 = scaledsprite ("alex_flustered2.png")
    image alex_happy = scaledsprite ("alex_happy.png")
    image alex_happy2 = scaledsprite ("alex_happy2.png")
    image alex_happy3 = scaledsprite ("alex_happy3.png")
    image alex_happy4 = scaledsprite ("alex_happy4.png")
    image alex_happy5 = scaledsprite ("alex_happy5.png")
    image alex_happy6 = scaledsprite ("alex_happy6.png")
    image alex_happy7 = scaledsprite ("alex_happy7.png")
    image alex_hopeless = scaledsprite ("alex_hopeless.png")
    image alex_hurt = scaledsprite ("alex_hurt.png")
    image alex_phone = scaledsprite ("alex_phone.png")
    image alex_phone2 = scaledsprite ("alex_phone2.png")
    image alex_phone3 = scaledsprite ("alex_phone3.png")
    image alex_phone4 = scaledsprite ("alex_phone4.png")
    image alex_sad = scaledsprite ("alex_sad.png")
    image alex_sad2 = scaledsprite ("alex_sad2.png")
    image alex2 = scaledsprite ("alex2.png")
    image alex3 = scaledsprite ("alex3.png")
    image alex4 = scaledsprite ("alex4.png")
    image alex5 = scaledsprite ("alex5.png")
    image alex6 = scaledsprite ("alex6.png")
    image alex7 = scaledsprite ("alex7.png")
    image alex_looking = scaledsprite ("alex_looking.png")
    image alex_looking2 = scaledsprite ("alex_looking2.png")
    image alex_looking3 = scaledsprite ("alex_looking3.png")
    image alex_looking4 = scaledsprite ("alex_looking4.png")
    image alex_shocked = scaledsprite ("alex_shocked.png")
    image alex_shocked2 = scaledsprite ("alex_shocked2.png")
    image alex_shocked3 = scaledsprite ("alex_shocked3.png")
    image alex_shocked4 = scaledsprite ("alex_shocked4.png")
    image alex_shocked5 = scaledsprite ("alex_shocked5.png")

    image ash = scaledsprite ("ash.png")
    image ash2 = scaledsprite ("ash2.png")
    image ash3 = scaledsprite ("ash3.png")
    image ash4 = scaledsprite ("ash4.png")
    image ash5 = scaledsprite ("ash5.png")
    image ash6 = scaledsprite ("ash6.png")
    image ash_cringing = scaledsprite ("ash_cringing.png")
    image ash_sly = scaledsprite ("ash_sly.png")
    image ash_sly2 = scaledsprite ("ash_sly2.png")
    image ash_sly3 = scaledsprite ("ash_sly3.png")
    image ash_worried = scaledsprite ("ash_worried.png")
    image ash_happy = scaledsprite ("ash_happy.png")
    image ash_happy2 = scaledsprite ("ash_happy2.png")

    image hayley = scaledsprite ("hayley.png")
    image hayley2 = scaledsprite ("hayley2.png")
    image hayley3 = scaledsprite ("hayley3.png")
    image hayley_excited = scaledsprite ("hayley_excited.png")

    image tyler_angry = scaledsprite ("tyler_angry.png")
    image tyler_angry2 = scaledsprite ("tyler_angry2.png")
    image tyler_angry3 = scaledsprite ("tyler_angry3.png")
    image tyler_angry4 = scaledsprite ("tyler_angry4.png")
    image tyler_angry5 = scaledsprite ("tyler_angry5.png")
    image tyler_happy = scaledsprite ("tyler_happy.png")
    image tyler_happy2 = scaledsprite ("tyler_happy2.png")

    image mother = scaledsprite ("mother.png")
    image mother_two = scaledsprite ("mother_two.png")
    image mother_shocked = scaledsprite ("mother_shocked.png")
    image mother_shocked2 = scaledsprite ("mother_shocked2.png")
    image mother_blank = scaledsprite ("mother_blank.png")
    image mother_looking = scaledsprite ("mother_looking.png")
    image mother_looking2 = scaledsprite ("mother_looking2.png")
    image mother_looking3 = scaledsprite ("mother_looking3.png")
    image mother_klutz = scaledsprite ("mother_klutz.png")

    image teacher = scaledsprite ("teacher.png")
    image teacher2 = scaledsprite ("teacher2.png")

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


    ## ACT 1 BEGINS HERE !!! ##


    scene bedroom
    with Dissolve(0.5)

    play sound "sfx/yawn.mp3" volume 0.5

    pause 1

    "You wake with a sharp breath."
    "Morning light spills through the curtains, and as fast as the nightmare had started, it dissolves into dust..."

label wake_up_menu:

menu:
    "Inspect room":
        jump leave_room

    "Think about dream":
        $ reply = renpy.random.choice(replies)

        o "[reply]"
        jump wake_up_menu

    "Look in the mirror":
        $ reply = renpy.random.choice(replies2)

        o "[reply]"
        jump wake_up_menu

label leave_room:

    o "Shit. June 1st already? I'll be expecting them any minute now."

    "The calendar hanging across the room tells you it's June 1st, 2006. Your eighteenth birthday.
    You've been waiting for this day for weeks and absolutely nothing could ruin it."

    "{i}*BRRRRRRRRRING*{i}"

    "The doorbell rings through the house, and a familiar voice echoes from outside."

    ch "Otter!!! You up b-day boy? It's us! We're here!"

    "Another voice chimes in."

    c "Otter!" 

    "Then a third."

    d "Open up already, shithead!"

menu:
    "Ignore the door":
        jump ending_one

    "Answer the door":
        jump answer_door

label ending_one:

    "you failed to answer the door."

    return

label answer_door:

    "You rest your hand on the doorknob."
    "You force a smile you don't entirely feel and pull the door open.."

    ch "Ahh... he emerges! Happy birthday, pal."

    "Charlie beams. He's always been so cheery."

    c "Jeez, you look terrible. Did you seriously just wake up?"

menu:
    "What's it to you?":
        jump whats_it_to_you

    "Unfortunately":
        jump unfortunately

label whats_it_to_you:

    o "What's it to you?"

    jump scene_lounge

label unfortunately:

    o "Haha. Yeah, unfortunately."

    jump scene_lounge

label scene_lounge:

    "Cat laughs under her breath, though there's a hint of concern. She casually brushes past you into the hallway."

    d "Or maybe he just forgot what sleep is."

    "Danny gives you a playful shove with his shoulder."

    d "Happy birthday, little man."

    "Charlie is already dropping his stuff off onto the dining table, making far more noise than necessary."

    "Somewhere in the kitchen, Cat is opening cupboards."

    "Danny plops himself down onto the couch."

menu:
    "Say nothing":
        jump say_nothing

    "Make yourselves at home":
        jump make_yourselves_at_home

label say_nothing:

    o "..."

label make_yourselves_at_home:

    o "Make yourselves at home, I guess."

    $ violence += 1
    $ betrayal += 1

    jump lounge

label lounge:

    c "Okay. Well we'd better get through these presents before Charlie explodes, man. He's been thinking about your big day for like... two weeks now."

    ch "Shut up, Catherine. You little rat."

    "Charlie is now kneeling on the carpet, trying to organise a pile of presents into something that vaguely resembles a neat stack."

    ch "Okay, listen up."

    "He claps his hands together."

    ch "Some ground rules..."

    c "There's... rules?"

    ch "Yeah! There are now!"

    d "Christ."

    ch "Number one. Nobody opens presents until everyone's here."

    d "...We are all here."

    ch "Exactly."

    d "So that's... that's not a rule."

    c "It's more of an observation, really..."

    ch "Screw you guys!"

    ch "Anyway, number two. Otter gets to decide everything we do today. Birthday privilege."

    ch "So, what'll it be first?"

menu:
    "Take a photo":
        jump take_photo

    "Listen to music":
        jump listen_music

label take_photo:

    o "A picture first may be nice?"

    ch "Score! One for the scrapbook."

    "Everyone awkwardly squeezes together in the living room."

    "{i}*FLASH*{i}"

    "The camera spits out an undeveloped photograph."

    ch "Here, if I just shake it around it'll develop faster."

    c "You know that's a myth right? It doesn't do anything."

    ch "You're a total myth! You don't really do anything!"

    "Cat rolls her eyes."

    ch "Anyway, I'll just slip this in your pocket. Make sure to check back on it later."

    $ polaroid += 1

    jump present_intro

label listen_music:

    o "Let's play some music."

    $ danny_bond += 1

    d "Now we are fuckin' talkin'!"

    "You observe Danny as he kneels in front of the CD rack, an overflowing clutter packed with handwritten labels."

    d "Wanna chuck on one of our mixes or listen to something a bit different?"

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

    o "Let's put your one on."

    d "Correct answer."

    "The room fills with old rock music. It's louder, rougher, and older than anything the rest of you usually listen to."

    "Danny drums his fingers to the beat absentmindedly, while Charlie complains that it's 'dad music'."

    d "You just don't appreciate the classics."

    ch "What, are you forty?"

    jump turn_the_music_off

label charlies_mix:

    $ charlie_bond += 1

    "Let's put Charlie's one on."

    ch "...Seriously? Aw, thanks!"

    d "Really? Again?"

    "Everyone starts humming along to the comfortable tunes almost immediately."

    "Charlie laughs every time someone gets a line wrong, insisting they should know all this already, and for a little while, it feels impossible to imagine any of you anywhere else."

    jump turn_the_music_off

label cats_mix:

    $ cat_bond += 1

    "Let's put Cat's one on."

    c "You gotta hand it to him, he's got taste."

    "The music that spills into the room is raw and emotional; unlike anything the others would've picked."

    "Charlie wrinkles his nose up while Danny quietly nods along to the rhythm."

    "Cat doesn't seem interested in whether anyone else likes it, and casually leans back, closes her eyes, taking it all in."

    c "I like songs that really feel like they have something to say."

    c "...Gerard Way always has something important to say."

    jump turn_the_music_off

label something_new:

    $ acceptance += 1

    "Let's put on something new."

    d "Wow. That's... surprising."

    d "Hmm... let's try this one."

    "A tune fills the space around you, and is clearly something that one of your parents listen to."

    "It's not unpleasant, and the four of you find yourselves getting lost in the gentle rhythm."

    "You swear you've heard this song somewhere before."

    jump turn_the_music_off

label turn_the_music_off:

    "Charlie turns the music off."

    jump present_intro

label present_intro:

    ch "Okay, enough messing around. It's present time!"

    jump act_two


## ACT 2 BEGINS HERE !!! ##


label act_two:

    "Charlie rubs his hands together before hurrying everyone onto the carpet. The pile of presents sit proudly in the middle of the living room."

    d "Charlie, quit staring."

    ch "I'm making sure they look nice."

    d "Oh my god, they're just presents."

    ch "Exactly."

    c "He ironed the wrapping paper."

    ch "...I did not!"

    c "You totally thought about it."

    "Charlie rolls his eyes, though the corners of his mouth curl into a smile anyway."

    ch "Alright, pick one."

    "Charlie's is wrapped almost perfectly, every fold crisp enough that it feels wrong to tear it open."

    "Cat's has been wrapped in newspaper and held together with a thin string, tied into a bow at one end. There's a doodle of a cat in the corner."

    "Danny's isn't wrapped at all, and is instead a cardboard box with HAPPY BIRTHDAY, OTTER scrawled across the side in black marker."

    d "What? I'm just saving money. You cannot blame me for that."

    c "Or maybe you're just lazy?"

    ch "Enough, you two."
    
    ch "Which is first, Otter?"

menu:
    "Charlie's present":
        jump charlie_present

    "Cat's present":
        jump cat_present

    "Danny's present": 
        jump danny_present

















    















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

    a4 "This hallway is the food chain. You’ve got your typical archetypes: the jocks, band kids, goths, scene kids, nerds."

    hide alex3
    show alex at right

    a4 "Me? I feel like I'm the only normal person here. It feels like I'm looking behind the glass in a zoo."

    hide alex
    show alex2 at rightish

    a4 "If there’s a more depressing place to spend the supposed ‘best years of my life,' do me a favour and never take me there."

    hide alex2
    show alex3 at right

    a4 "Anyway, today’s the big finale. Spring Fling. Balloons. Bad punch. Everyone pretending they’re not about to scatter across the country and forget each other’s names."

    hide alex3
    show alex at right

    a4 "It’s supposed to be “magical.” You know what’s magical? Surviving four years in a building where someone {i}still{/i} thinks shoving kids into lockers is peak comedy."

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

    a "Eh... just figured I’d ruin someone else’s morning for a change. Congrats, you won the lottery."

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

    a4 "Right, Ms. Perkins. I’ll cherish the cafeteria mystery meat, the stuck up asshole who always took my money and all of my nonexistent friends. Memories forever."

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

    a4 "Mhm, very insightful. Maybe I’ll write 'life is unfair' instead."

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

    a4 "Hayley shoots me a look that says ‘you’re tolerated... for now.’ Perfect."

    hide alex7 onlayer alexlayer
    hide ash
    show alex_looking2 at right
    show ash2 at left

    ash "Alex, you know what I've been thinking about? Do you remember that time in Lincoln Park in ’02 with those dry-ice bottle rockets?"

    hide ash2
    hide alex_looking2
    show alex_happy3 at right
    show ash_happy at left

    ash "You said it was 'basically science class,’ then we completely blew out the neighbor’s windows."

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

    ash "Dude, you were the one who stole the lighter from your mom’s boyfriend! Pretty sure we were two seconds away from becoming a ‘local news cautionary tale.’"

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

    a "Yeah, well, the nerd table was full of people with futures. Thought I’d downgrade."

    hide tyler_angry4
    show tyler_happy at left
    hide alex6
    show alex4 at right

    t "Brave. What’s the occasion? Trying to get drafted?"

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
    
    a4 "Look at this. Every failure, every bad choice, memorialized. It’s like the Louvre of losers. Someday I’ll be a permanent exhibit."

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

    jump leave_bathroom

label leave_bathroom:

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

    a4 "Nope. Everyone else is too loud, too stupid, too obsessed with their hair or stats or whatever... I can’t deal with that. I’ll just sit here and enjoy my miserable cafeteria slop in peace."

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

    a4 "I’ll save the long dramatic monologues for someone else."

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

    a4 "Huh. Weird. Didn’t I...?"

    hide alex_shocked2
    show alex_shocked at right

    a4 "No. No, no, no. That’s impossible. I... I {i}definitely{/i} wasn’t supposed to wake up today. Unless heaven has a suspiciously accurate Cedar Hill zip code..."

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

    a4 "Leave it. Let him wonder if I’m dead."

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

    a4 "Two lockers down, Brent’s retelling his tragic fountain story."

    hide alex_shocked
    show alex_shocked4 at right

    a4 "Right on cue. Perfect comedic timing, if I wasn’t already internally screaming."

    hide alex_shocked4
    show alex6 at rightish

    a4 "{i}Fun psychological fact{/i}: this is where a person realizes they’re stuck in a time loop. {i}Fun Alex fact{/i}: I’m still pretending it’s a coincidence. Denial is cheaper than therapy."

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

    a4 "The universe is hitting play on a rerun I didn’t ask for."

    scene hallway_dark2
    show tyler_happy at left
    with Dissolve(0.5)

    hide alex5 onlayer alexlayer
    show alex_looking2 at right
    with Dissolve(0.5)

    t "See that? Around here, you don’t react. Reacting means you care, and caring is blood in the water. These halls run on humiliation. Lunch money? Gone. Dignity? Don’t even bother bringing it."

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

    a "Thing is, Kane, if you keep asking for my money every day, we’re basically dating. Should I get you a corsage for Spring Fling?"

    jump school_hallway_two

label taxes:

    hide tyler_angry2
    show tyler_happy2 at left
    hide alex
    show alex_looking at right

    a "Sure, Tyler, but if I’m funding your lunch every day, I’m claiming you as a dependent on my taxes."

    jump school_hallway_two

label school_hallway_two:

    hide alex_looking
    show alex_looking2 at right onlayer alexlayer
    hide tyler_happy2
    show tyler_angry5 at left

    t "You’re lucky I’m in a good mood, nerd. Don't let this get to your little head."

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

        a4 "Tyler said there’d be a Spring Fling ticket wedged above the lockers, right? Sure. And maybe Bigfoot’s up there handing out prom dates too."

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

    a4 "He’s even got the same crooked grin, like he knows something I don’t."

    if talked_to_ash == 0:

        hide alex
        show alex_looking at right

        a4 "Yesterday... my dream, hallucination, whatever, you walked right past me. I didn’t say a word."

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

        a "Thought you’d escaped this prison already."

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

    ash "Please. I’m not leaving until I get my diploma {i}and{/i} a tetanus shot."

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

    a "What can I say? Figured I’d face my fears before graduation, you know. Like 'gym class'."

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

    a4 "Oh, thanks for the reminder. I totally forgot that one of the universe’s rules is that prom is gated by a piece of paper."

    hide alex5
    show alex3 at right

    a4 "Honestly, it’s like the game just handed me a quest marker with a big glowing arrow saying, ‘Hey dummy, get this ticket or nothing happens.’ Thanks. Very subtle."

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

    a4 "Yesterday I’d have scoffed at that and then gone home to practice my dramatic exit. Dream or loop, this is a new variable."

    hide alex3
    show alex7 at right
    
    a4 "Yesterday I didn’t even get this far, and today, I can respond. Wow, I feel powerful."

    hide alex7
    show alex_happy7 at right

    a "Hah. Corner’s full. Had to take the scenic route through hell instead. You know... Axe body spray, screaming teenagers."

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

    a "Maybe a little of both. I mean, come on. Hayley’s sweet, but even she deserves a chance to panic about her life choices, right?"

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

    a4 "That’s all I need for now. Plant the seed, walk away, let chaos do the rest. One small nudge, a million possible outcomes."

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
    
    a4 "Hey Ash... uh, hey. I was gonna roast you for ghosting me, but... can’t think of anything clever now. Weird, right? I'm supposed to be smarter than I was yesterday."

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

    a4 "Mhm. Groundbreaking. Maybe I’ll just doodle ‘existence is rigged’..."

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

    a4 "There’s only one sensible choice. Either endure the jock table, or hide at a corner table and eavesdrop."

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

    a4 "Now it’s time for the social nightmare: sitting at the scene table with Ash and Hayley."

    hide alex
    show alex5 at rightish

    a4 "Yesterday, I would’ve obliterated Ash with sarcasm. Today... I can’t. I can’t think of anything truly mean. And that’s weird. That’s new. That’s... slightly dangerous."

    scene cafeteria_dark2
    with Fade (0.5,0.5,0.5)

    show alex4 at right
    with Dissolve(0.5)

    show ash_sly2 at left
    with Dissolve(0.5)

    ash "Hey. You made it. And here I thought you’d ghost us again like last year. What’s different today? Did the world finally bribe you to come?"

    hide ash_sly2
    show ash_sly3 at left
    hide alex4
    show alex_happy7 at right

    a "Oh, Ash... if only you knew I’m not making conscious decisions here. My brain’s just following yesterday’s cheat sheet."

    hide alex_happy7
    show alex5 at rightish

    a4 "Hah. If only he knew I was serious."

    hide alex5
    show alex_happy3 at right
    hide ash_sly3
    show ash4 at left

    ash "Huh. That’s... tame. Careful, Hayes, you might actually be growing up. Scary thought."

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

    a4 "I want to be snarky. I can’t. My chest does this weird little flutter thing, and I have no idea why. Worst bug in the system."

    hide hayley3
    show ash2 at left
    with Dissolve(0.5)
    hide alex_flustered2
    show alex_looking2 at right

    ash "Alex, you know what I've been thinking about? Do you remember that time in Lincoln Park in ’02 with those dry-ice bottle rockets?"

    hide ash2
    hide alex_looking2
    show alex_happy3 at right
    show ash_happy at left

    ash "You said it was 'basically science class,’ then we completely blew out the neighbor’s windows."

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

    ash "Dude, you were the one who stole the lighter from your mom’s boyfriend! Pretty sure we were two seconds away from becoming a ‘local news cautionary tale.’"

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

    a4 "And now, player, you’ve got the information you need to progress. Ticket: check. Life shit: messy. Feelings: convoluted."

    hide alex3
    show alex6 at rightish

    a4 "Let’s see if this edge lasts through the rest of the day... or if I’ll still screw it all up again."

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

        a4 "Alright, ticket: check. Survival: in progress. Now comes the part of the day I’m still figuring out... the hallway gauntlet."

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

    a4 "Or whatever cosmic rerun I’m trapped in."

    hide alex_shocked4
    show alex_looking4 at right

    a4 "But this time I’ve got the ticket. The so-called golden key to teen happiness."

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

    ash "Hayley told you already, huh? Yeah, she asked me. Guess I’ve got plans tonight."

    hide alex_flustered
    hide ash4
    show ash3 at left
    show alex_looking4 at right

    a4 "Plans. Right. Plans that apparently don’t care that I have the actual ticket in my pocket."

    hide alex_looking4
    show alex2 at rightish

    a4 "Having obtained the special quest item means you don't have to do all the talking, right? Isn’t that how this game works?"

    hide alex2
    show alex_happy2 at right

    a "Cool. That’s... cool. Big night. Balloons. Terrible music. Dream come true."

    hide ash3
    show ash5 at left
    hide alex_happy2
    show alex_looking3 at right onlayer alexlayer

    ash "I couldn't wait around forever for you to ask me, Alex. She got to me first, I'm sorry."
    
    hide ash5
    show ash4 at left

    ash "Anyway, if I don’t see you there... guess this is it. End of high school. End of... us being randomly in each other’s way."

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

    a4 "Yesterday, I thought this was just another reality check. Today? It’s worse."

    hide alex_looking4
    show alex_hopeless at right

    a4 "Today I know I could have been there."

    hide alex_hopeless
    show alex_looking4 at right

    a4 "I have the ticket. I have the timing. I have... feelings."

    hide alex_looking4
    show alex_flustered2 at right

    a4 "There it is. The final boss I didn’t know I was fighting."

    hide alex_flustered2
    show alex_shocked4 at right
    
    a4 "This isn’t about a dance. It’s about Ash."

    hide alex_shocked4
    show alex_hopeless at right

    a4 "The loop isn’t punishing me for missing a party, it’s punishing me for running from what I want."

    hide alex_hopeless
    show alex6 at rightish

    a4 "Great. So the universe isn’t just glitching, it’s shipping us. And it won’t stop the reruns until I stop being a coward. Fantastic. No pressure."

    jump evening_two

    label evening_two:

    scene bedroom
    with Fade(1,1,1)

    pause 2

    scene bedroom_dark
    with Dissolve(0.5)

    show alex_looking4 at right
    with Dissolve(0.5)

    a4 "Hayley’s probably picking out a dress right now. Ash is probably texting her. And I’m sitting here holding this piece of paper like it’s a map from hell."

    hide alex_looking4
    show alex_looking3 at right

    a4 "..."

    hide alex_looking3
    show alex_sad2 at right
    
    a4 "But I saw it this time. The way it felt when he said goodbye. That wasn’t nothing."

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

    a4 "Okay, no time for Tyler, no time for Hayley, no “gee Alex why the long face.” I’ve wasted two chances on fixing things and I'm not about to make it three."

    hide alex5
    show alex3 at right

    a4 "Get the ticket. Find Ash. Fix things for good. No detours, no sarcastic side quests, no NPC chatter. Everyone else can keep looping through May 19th forever; But I’ve got one shot to break the curse."

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

    a "Your mom’s in the principal's office. Something about your ‘borrowed’ skateboard."

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

    a "Listen. I can’t let today happen again. Yesterday, every yesterday, I fucked things up. I blew my last chance."

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

    a "Same. And it’s still the best week I’ve ever had."

    hide ash_happy
    show ash6 at left
    hide alex_happy5
    show alex_flustered2 at right

    a " Every time this day repeats... ...every time I think about what actually matters, that’s the memory that sticks. Just us, lost in the desert, laughing like idiots."

    hide alex_flustered2
    show alex_happy2 at right

    a "I don’t know if today’s gonna vanish, or if this is my last shot, but I can’t keep acting like you’re just some old inside joke I outgrew."

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

    a "Hey, I’m consistent. Late to everything except bad timing."

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

    a4 "Now? Somehow, I’m not dead. I’m... even kind of happy? Like I’m a character in some weird indie visual novel, and the player decided that a sad ending was just not good enough."

    hide alex7
    show alex_happy7 at right

    a4 "Maybe some days are worth repeating. Or maybe, finally, this one doesn’t have to."

    jump finale

label ending_two:

    hide ash5
    show ash6 at left
    hide alex_flustered
    show alex_happy2 at right

    a "Sturgeon Bay, 1999. That homemade flamethrower we almost burned my cousin’s shed down with."

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

    ash "Honestly, I wasn’t sure I’d ever hear you like this. But... damn, I’m glad I am."

    hide ash5
    show ash6 at left
    hide alex_happy3
    show alex_happy2 at right

    a "I don’t know if today’s gonna vanish, or if this is my last shot, but I can’t keep acting like you’re just some old inside joke I outgrew."

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

    ash "But some things just can’t be fixed in one day."

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
