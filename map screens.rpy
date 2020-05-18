
#all the screens for the overworld map.


screen overworld_map(ul, jl, dl, il, hl, posl):
    #bg: background image
    #ul: list of unlocked locations. 1: unlocked, 0: not
    #jl: jumps corresponding to unlocked locations.
    #dl: descriptions corresponding to unlocked locations
    #il: images corresponding to unlocked location.
    #hl: hover images corresponding to unlocked location
    #posl: position corresponding to unlocked location. tuples.

    #background bg

    #hotspot (170, 78, 343, 213) hovered Show(md[1]) unhovered Hide(md[0]) action Jump(map_jumps[0])

    for loc in range(0, len(ul)): #ul[chapter]

        imagebutton:
            pos (posl[loc][0], posl[loc][1])
            idle il[loc]
            hover hl[loc]

            if ul[loc] == 1:
                action Call(jl[loc]) #call? jump? idk.

            tooltip dl[loc]


        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" pos (posl[loc][0], posl[loc][1]) # (posl[loc][0], posl[loc][1])







init:
    #some images for the map

    image prologue_bg:
        "overworld/prologue.jpg"





































##eof
