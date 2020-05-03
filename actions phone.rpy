#keypad + directory

#https://lemmasoft.renai.us/forums/viewtopic.php?t=29320

#you should be able to call 911 at a certain part when mc is freaking out

#directory:
#area code?
# nai: 555 8922
# sis: 555 1790

#keypad

screen key_pad:
    imagemap:
        ground "phone/keypad.png"
        hover "phone/keypad.png"
        #add a text thing in the spot that shows the number typed

        #hitting hotspot appends to number
        #(top left x, top left y, width, height)
        hotspot (180, 410, 45, 65) action Return(1)
        hotspot (225, 410, 65, 65) action Return(2)
        hotspot (290, 410, 60, 65) action Return(3)
        #hotspot () action Return(4)
        #hotspot () action Return(5)
        #hotspot () action Return(6)
        #hotspot () action Return(7)
        #hotspot () action Return(8)
        #hotspot () action Return(9)
        #hotspot () action Return(0)
        hotspot (265, 590, 60, 50) action Function(renpy.call, label="make_call")
        #add a confirm
        #add a cancel
        hbox:
            xpos 185 ypos 150
            text n_dis

label phone_call:
    hide screen special_actions_overlay
    hide screen special_actions_screen
    $songname = renpy.music.get_playing(channel="music")
    stop music

    $ phone_counter = 0
    $ keys = []
    show screen key_pad
    $ phone_counter += 1

    python:
        while len(keys) < 10: #keep going until you have 7 digits

            result = ui.interact()

            if isinstance(result, int):
                keys.append(result) #add digit
                n_dis = n_dis + str(result) + " " #add digits to the displayable
    call make_call from _call_make_call
    show screen special_actions_overlay
    play music songname
    return

label make_call:
    hide screen key_pad
    if keys == [8, 6, 7, 5, 3, 0, 9]:
        hide screen key_pad with dissolve
        jump phone_jenny
    elif keys == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        hide screen key_pad with dissolve
        jump phone_nai
    else:
        hide screen key_pad with dissolve
        jump phone_nobody
    return


label phone_jenny:
    "jennyy~"
    return

label phone_nai:
    "this is nai's number (not really)."
    #if nai_available = true
    #   call nai_convo69#
    #else:
    #   "guess hes busy, he doesnt pick up."
    #   leave a message option?
    return

label phone_police:
    "you called the police"
    "I hope you had a real emergency"

    if real_emergency == 1:
        "you have a real emergency! cool!"
        #jump
    return

label phone_nobody:
    "I press buttons randomly like some kind of vapid idiot."
    return
























#
