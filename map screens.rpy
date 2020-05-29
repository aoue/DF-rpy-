
#all the screens for the overworld/dungeon map and some assisting images.
#to be reorganized later. grouper together for now for ease of development

## -- PARTY SCREENS -- ##
screen inventory_view(viewlist, equip_type):
    #gear vp on the left
    zorder 101
    viewport:
        xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20
            for gear in viewlist:
                if gear.get_type() == equip_type:
                    textbutton gear.get_title() action NullAction() hovered Function(ow.gear_browse, gear) unhovered Hide("gear_browse")
screen move_view(viewlist):
    #move vp on the right.
    zorder 101
    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        #add whatever bg you want
        vbox:
            spacing 20
            for move in viewlist:
                #if gear.get_type() == type:
                textbutton move.get_title() action NullAction() hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
screen party_view(party, i, ow):
    zorder 100

    #background
    add ow.get_party_bg()

    #character pose
    add party[i].get_pose() pos (380, 40)

    #close button
    textbutton "close" action Return pos (950, 10)

    #character's affinity inforrmation
    vbox:
        pos (680, 40)
        text "Aff: " + str(party[i].get_aff_name()) + ","  + str(party[i].get_armour().get_aff_name())
        text "w aff: " + str(party[i].get_weapon().get_aff_name())

    #character's stat block
    vbox:
        pos (250, 390)
        text "HP = " + str(party[i].get_hp()) + "/" + str(party[i].get_hpmax())
        text "EN = " + str(party[i].get_energy()) + "/" + str(party[i].get_energymax())
        text "AB = " + str(party[i].get_able())
        text "ST = " + str(party[i].get_stamina())
        text "PA = " + str(party[i].get_physa()) + "+" + str(party[i].get_weapon().get_phys())
        text "PD = " + str(party[i].get_physd()) + "+" + str(party[i].get_armour().get_phys())
        text "MA = " + str(party[i].get_maga()) + "+" + str(party[i].get_weapon().get_mag())
        text "MD = " + str(party[i].get_magd()) + "+" + str(party[i].get_armour().get_mag())
        text "HI = " + str(party[i].get_hit()) + "+" + str(party[i].get_weapon().get_hit())
        text "DO = " + str(party[i].get_dodge()) + "+" + str(party[i].get_armour().get_dodge())


    #change the category of gear the player is looking at.
    hbox:
        xalign 0
        yalign 0.05
        spacing 5

        textbutton "Arm" action Function(ow.change_inventory_view, 0)
        textbutton "Wpn" action Function(ow.change_inventory_view, 1)
        textbutton "Acc" action Function(ow.change_inventory_view, 2)

    #equipped gear
    vbox:
        yalign 0.3
        xalign 0.25
        spacing 60

        textbutton party[i].get_armour().get_title() action Function(ow.swap_gear, party[i], 1) hovered Function(ow.gear_browse, party[i].get_armour()) unhovered Hide("gear_browse")

        textbutton party[i].get_weapon().get_title() action Function(ow.swap_gear, party[i], 2) hovered Function(ow.gear_browse, party[i].get_weapon()) unhovered Hide("gear_browse")

        textbutton party[i].get_weapon().get_title() action Return #replace with accessory

    #previous unit and next unit buttons:
    imagebutton:
        pos (355, 10)
        idle "party_prev"
        hover "party_prev_h"
        action Function(renpy.invoke_in_new_context, ow.next_party_unit, -1), Return
    imagebutton:
        pos (670, 10)
        idle "party_next"
        hover "party_next_h"
        action Function(renpy.invoke_in_new_context, ow.next_party_unit, 1), Return #does nothing though.


    #lvl and focus
    text "Lvl " + str(party[i].get_lvl()) + " " + party[i].get_focus().get_title() pos (445, 20)

    #next unit button on midtop right: (i += 1 OR if i+1 > len(party), i = 0). dissolve.

    #eqipped moves. display depends on unit's pattern.
    vbox:
        yalign 0.55
        xalign 0.75
        spacing 20

        if party[i].get_pattern() == 1: #4/2/1
            text "front"
            for x in range(0, 4):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(4, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
        elif party[i].get_pattern() == 2: #3/3/1
            text "front"
            for x in range(0, 3):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(3, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
        elif party[i].get_pattern() == 3: #2/4/1
            text "front"
            for x in range(0, 2):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(2, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "Nothing" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")

        #wild slot
        text "Wild"
        if party[i].get_moves()[6] == None:
            textbutton "Nothing" action Function(ow.put_move, party[i], 6, 0)
        else:
            textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], 6, 0) hovered Function(ow.move_browse, party[i].get_moves()[6]) unhovered Hide("move_browse")
screen gear_swap(viewlist, equip_type):
    #inventory: overworld inventory object
    modal True
    zorder 105
    textbutton "Cancel" action Return(0)

    viewport:
        xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. Just change the y value to len(viewlist)*whatever. Easy.
        mousewheel True

        vbox:
            spacing 20
            for gear in viewlist:
                if gear.get_type() == equip_type:
                    textbutton gear.get_title() action Return(gear) hovered Function(ow.gear_browse, gear) unhovered Hide("gear_browse")
screen gear_browse(gear):
    zorder 101
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(530, 200, 300, 225)
        ypadding 5
        xpadding 10

        vbox:
            text gear.get_title()
            text gear.get_flavour()
            text "physical power = " + str(gear.get_phys())
            text "magic power = " + str(gear.get_mag())
            if isinstance(gear, weapon) == True: #weapon
                text "hit bonus = " + str(gear.get_hit())
            else: #armour
                text "dodge bonus = " + str(gear.get_dodge())
            text "affinity = " + str(gear.get_aff()) #<-- replace text with image. affinities will be this way.
            if gear.get_passive() == 1:
                text "I have a passive"
screen move_swap(movelist, rank):
    modal True
    zorder 105
    textbutton "Cancel" action Return(0) pos (1220, 30)

    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20
            for move in movelist:
                if rank == 0:
                    textbutton move.get_title() action Return(move) hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
                elif move.get_rank() == rank or move.get_rank() == 0:
                    textbutton move.get_title() action Return(move) hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
screen move_browse(move):
    zorder 101
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(530, 200, 300, 225)
        ypadding 5
        xpadding 10

        vbox:
            text move.get_title()
            text move.get_flavour()
            text "drain(a/s) = " + str(move.get_able_drain()) + "/" + str(move.get_stamina_drain())
            text "rank = " + str(move.get_rank())
            if move.get_damage_type() == 0:
                text "power = " + str(move.get_power()) + " (Physical)"
            else:
                text "power = " + str(move.get_power()) + " (Magical)"
            if move.get_status_only() == 0:
                text "hit bonus = " + str(move.get_hit())
                text "affinity = " + str(move.get_element_name()) #<-- replace text with image.

## -- HUB SCREENS -- ##
#TODO

## -- DIRECTION SCREENS -- ##
screen chapter_view(chapter, state, overworld):
    zorder 100

    #add overworld.get_bg() #background
    #add a background frame. the journal can just overlay over wherever you are.

    hbox: #shows two buttons. click to switch between current and completed quests
        xalign 0.4
        yalign 0.1
        if state == 0:
            textbutton "View current" action NullAction()
            textbutton "View completed" action Function(overworld.change_direction_view, chapter, 1)
        else:
            textbutton "View current" action Function(overworld.change_direction_view, chapter, 0)
            textbutton "View completed" action NullAction()

    vbox: #shows a column of clickable chapter icons on the left of the questbook. click to change chapter.
        xalign 0.2
        yalign 0.2

        for i in range(0, overworld.get_chapter()+1):
            if i == chapter:
                textbutton "chapter [i]" action NullAction()
            else:
                textbutton "chapter [i]" action Function(overworld.change_direction_view, i, state)

    #shows a column on clickable quest titles. click to change viewed quest. answers to chapter view.
    viewport:
        xalign 0.5
        yalign 0.3
        mousewheel True
        #xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.

        vbox:
            spacing 10
            if state == 0: #view current quests
                for quest in overworld.get_direction().get_current():
                    if (quest.get_chapter() - 1) == chapter:
                        textbutton quest.get_title() action Function(overworld.quest_view, quest)

            else: #view completed quests
                for quest in overworld.get_direction().get_completed():
                    if (quest.get_chapter() - 1) == chapter:
                        textbutton quest.get_title() action Function(overworld.quest_view, quest)



screen quest_view(quest):
    zorder 101
    #for showing a particular quest. answers to chapter quests.
    frame:
        area(700, 300, 300, 400)
        ypadding 5
        xpadding 10
        vbox:
            text quest.get_title()
            text "Expires at the start of " + str(quest.get_chapter())

    #title at top
    #requirements (str) with tick boxes.
    #text "requirement one"
    #if fulfilled:
    #    add tick box checked
    #else:
    #    add tick box unchecked

    #for i in range(0, quest.get_progress()+1): #a list of flavou
        #if i == quest.get_progress():
            #text highlighted. #do this next
        #else:
            #text quest.get_flavour()[i] #greyed out. already been done.




## -- MAIN OVERWORLD SCREENS -- ##
screen overworld_helpers(overworld):
    #make these a mousearea thing:
    #need to be much smaller buttons. tooltip too.
    vbox:
        yalign 0.4
        xalign 0
        spacing 20

        imagebutton: #party button
            idle "party_b"
            hover "party_h"
            action Function(overworld.show_party) #invoke in new context
            tooltip "Manage Party"

        imagebutton: #direction button
            idle "direction_b"
            hover "direction_h"
            action Function(overworld.show_direction)
            tooltip "Directions"

        imagebutton: #hub button
            idle "hub_b"
            hover "hub_h"
            action Return #TODO later. after prologue. (the first hub will be nai's place.)
            tooltip "Hub"
    $ tooltip = GetTooltip()
    if tooltip:
        #text "[tooltip]" pos (posl[loc][0], posl[loc][1])
        text "[tooltip]"
screen overworld_map(ul, jl, dl, il, hl, posl, overworld):
    #bg: background image
    #ul: list of unlocked locations. 1: unlocked, 0: not
    #jl: jumps corresponding to unlocked locations.
    #dl: descriptions corresponding to unlocked locations
    #il: images corresponding to unlocked location.
    #hl: hover images corresponding to unlocked location
    #posl: position corresponding to unlocked location. tuples.

    #background bg
    add overworld.get_bg()[overworld.get_chapter()]

    mousearea:
        area(0, 0.2, 0.1, 0.6)#dimensions
        hovered Function(overworld.show_ow_helpers)
        unhovered Hide("overworld_helpers", transition = dissolve)

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
            #text "[tooltip]" pos (posl[loc][0], posl[loc][1])
            text "[tooltip]"



























##eof
