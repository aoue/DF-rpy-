##controls the display of character entries through the glossary

label glossary_call:
    $songname = renpy.music.get_playing(channel="music") #preserve outside music
    stop music

    hide screen special_actions_overlay
    hide screen special_actions_screen
    call screen glossary_vpgrid(last_entry)
    show screen special_actions_overlay

    play music songname #preserve outside track

    return

####features:
#independent soundtrack. return to previous song afterwards.
#tooltip that gives the Name + start of each entry
#show all letters right aways. darkened while locked, lightened and clickable when unlocked.
screen glossary_vpgrid(last_entry):
    modal True #if i've already set it to modal, then the 'showtransient' i do later is useless? is modal = True useless here?

    #currently the entry doesn't show up until you mouse over an imagebutton. No good. it needs to evaluate as soon as screen is called.
    if last_entry == "":
        pass
    else:
        $renpy.show_screen(last_entry)

    zorder 100
    vpgrid:
        cols 2
        xspacing 100
        yspacing 50
        draggable True
        mousewheel True
        scrollbars "vertical"
        #side_xalign 0.5

        #entries
        imagebutton:
            idle "glossary/placeholder.png"
            hover "glossary/placeholder hover.png"
            #hovered ShowTransient("glossary_entry0")
            action SetVariable("last_entry", "glossary_entry0"), ShowTransient("glossary_entry0")
            tooltip "{i}entry 0 ...{/i}"
        imagebutton:
            idle "glossary/placeholder.png"
            hover "glossary/placeholder hover.png"
            action Show("glossary_entry0")
            tooltip "{i}entry 1 ...{/i}"
        imagebutton:
            idle "glossary/placeholder.png"
            hover "glossary/placeholder hover.png"
            action Show("glossary_entry0")
            tooltip "{i}entry 2 ...{/i}"
        imagebutton: #TODO close button off on its own, not part of the vp grid, off in the right hand corner.
            idle "glossary/placeholder.png"
            hover "glossary/placeholder hover.png"
            action Hide(last_entry), Return()
            tooltip "{i}close{/i}"
        #TODO every character's silhouette should be present in the vpgrid. just uninteractable until unlocked.

        $ tooltip = GetTooltip()

    frame:
        area(915, 100, 300, 100) #reposition this so it doesn't block the entry

        vbox:
            if tooltip:
                text "{i}[tooltip]{/i}"
            else:
                text "Preview"

#Some notes for glossary entries:
#-if they get too long, then make them horizontally-scrollable. a viewport could work

screen glossary_entry0():
    #add("map/icon_hover.png") xalign 0.99 yalign 0.99
    #nai. also this will work as the example version.
    #if x == 0:
    # "blah blah 0"
    #elif x == 1:
    # "blah blah 1"
    # ^changes over story and as mc's feelings change.

    frame:
        area(600, 50, 500, 600)
        ypadding 5
        xpadding 10

        vbox:
            text "Nai is a cool guy"
            text "he's been my friend for a long time."

            if nai_rel > 5:
                text "We're still close."
            elif nai_rel < 5:
                text "We're growing apart."

            #^type of thing.
            #add a number line showing where nai_rel is relative to 0 ? i think no. it cheapens the relationship by making the player realize the result of their actions is just some in/decrementation of a variable.


screen glossary_entry1():
    pass


screen glossary_entry2():
    pass




##eof
