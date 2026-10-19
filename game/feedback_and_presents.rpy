init python:

    def change_bond(who, amount, absolute=False):

        bond_variables = {
            "Cat": "cat_bond",
            "Charlie": "charlie_bond",
            "Danny": "danny_bond",
        }

        variable = bond_variables[who]
        old_value = getattr(renpy.store, variable)

        new_value = amount if absolute else old_value + amount

        setattr(renpy.store, variable, new_value)

        difference = new_value - old_value

        if difference == 0:
            return

        if difference > 0:
            message = "{} liked that".format(who)
            renpy.play("sfx/sfx/liked_that.mp3", channel="audio", relative_volume=0.2)
        else:
            message = "{} didn't like that".format(who)
            renpy.play("sfx/sfx/didnt_like_that.mp3", channel="audio", relative_volume=0.4)

        renpy.hide_screen("bond_notice", immediately=True)
        renpy.show_screen("bond_notice", message=message)


transform bond_notice_fade:

    on show:
        alpha 0.0
        linear 0.2 alpha 1.0

    on hide:
        linear 0.3 alpha 0.0


screen bond_notice(message):

    zorder 200

    text message:
        xpos 30
        ypos 30
        size 33
        italic True
        color "#eee8e1"
        outlines [(2.5, "#000000b0", 0, 0)]
        at bond_notice_fade

    timer 2.5 action Hide("bond_notice")

init python:

    def liked_notice(who):
        renpy.hide_screen("bond_notice", immediately=True)
        renpy.show_screen("bond_notice", message="{} liked that.".format(who))
        renpy.play(
            "sfx/sfx/liked_that.mp3",
            channel="audio",
            relative_volume=0.2
        )




# HOVERING PRESENTS #

define present_choices = (
    (
        "Charlie's present",
        "charlie_present_wrapped",
        "Charlie's is wrapped almost perfectly, every fold crisp enough that it feels wrong to tear it open.",
        0.23
    ),
    (
        "Danny's present",
        "danny_present_wrapped",
        "Danny's isn't wrapped at all, and is instead a cardboard box with HAPPY BIRTHDAY, OTTER scrawled across the side in black marker.",
        0.50
    ),
    (
        "Cat's present",
        "cat_present_wrapped",
        "Cat's has been wrapped in newspaper and held together with a thin string, tied into a bow at one end.",
        0.77
    ),
)


screen choose_present():

    modal True
    zorder 100

    add Solid("#000000aa")

    text "Which present will you open?":
        xalign 0.5
        ypos 0.14
        size 36
        color "#eee8e1"

    $ gift_size = int(min(config.screen_width * 0.20, config.screen_height * 0.36))

    $ remaining_presents = [gift for gift in present_choices if gift[0] not in char_menu]

    for i, gift index gift[0] in enumerate(remaining_presents):

        $ caption, artwork, description, old_slot = gift

        $ slot = 0.5 + (i - (len(remaining_presents) - 1) / 2.0) * 0.27

        imagebutton:

            idle Transform(
                artwork,
                xysize=(gift_size, gift_size),
                fit="contain"
            )

            hover Transform(
                artwork,
                xysize=(gift_size, gift_size),
                fit="contain",
                matrixcolor=BrightnessMatrix(0.18)
            )

            xpos slot
            xanchor 0.5
            ypos 0.45
            yanchor 0.5

            focus_mask True

            tooltip description
            activate_sound "sfx/sfx/click.mp3"
            action Return(caption)

        text caption:
            xpos slot
            xanchor 0.5
            ypos 0.67
            size 24
            color "#eee8e1"

    $ hovered_description = GetTooltip("choose_present")

    text (hovered_description or "Hover over a present, then click to open it."):
        xalign 0.5
        ypos 0.79
        xsize int(config.screen_width * 0.70)
        textalign 0.5
        size 24
        italic True
        color "#eee8e1"