
#all the screens for the overworld map

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
                if gear[0].get_type() in equip_type:
                    textbutton gear[0].get_title() + " Q:" + str(gear[1]) action NullAction() hovered Function(ow.gear_browse, gear[0]) unhovered Hide("gear_browse")
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
                textbutton move.get_title() action NullAction() hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
screen party_view(party, i, ow):
    zorder 100

    #background
    add ow.get_party_bg()

    #character pose
    add party[i].get_pose() pos (380, 40)

    #close button
    textbutton "close" action Function(ow.close_party), Return pos (245, 10)

    #character's affinity inforrmation
    vbox:
        pos (680, 40)
        text "Aff: " + party[i].get_aff_name() + ","  + party[i].get_armour().get_aff_name()
        text "wpn aff: " + party[i].get_weapon().get_aff_name()

    #character's stat block
    vbox:
        pos (250, 390)
        text "HP = " + str(party[i].get_hp()) + "/" + str(party[i].get_hpmax_actual()) size 20
        text "Energy = " + str(party[i].get_energy()) + "/" + str(party[i].get_energymax()) size 20
        text "Able = " + str(party[i].get_ablemax_actual()) size 20
        text "Stamina = " + str(party[i].get_staminamax_actual()) size 20
        text "Phys atk = " + str(party[i].get_physa_actual()) size 20
        text "Phys def = " + str(party[i].get_physd_actual()) size 20
        text "Mag atk = " + str(party[i].get_maga_actual()) size 20
        text "Mag def = " + str(party[i].get_magd_actual()) size 20
        text "Hit = " + str(party[i].get_hit()) size 20
        text "Dodge = " + str(party[i].get_dodgemax_actual()) size 20


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

        textbutton party[i].get_acc().get_title() action Function(ow.swap_gear, party[i], 3) hovered Function(ow.gear_browse, party[i].get_acc()) unhovered Hide("gear_browse")

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
    text "Lvl " + str(party[i].get_lvl()) + " " + party[i].get_foc().get_title() pos (445, 20)

    #next unit button on midtop right: (i += 1 OR if i+1 > len(party), i = 0). dissolve.

    #eqipped moves. display depends on unit's pattern.
    vbox:
        yalign 0.25
        xalign 0.75
        spacing 8

        #patterns
        if party[i].get_pattern() == 1: #4/2
            text "front"
            for x in range(0, 4):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(4, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
        elif party[i].get_pattern() == 2: #3/3
            text "front"
            for x in range(0, 3):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(3, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
        elif party[i].get_pattern() == 3: #2/4
            text "front"
            for x in range(0, 2):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 1)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 1) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")
            text "back"
            for x in range(2, 6):
                if party[i].get_moves()[x] == None:
                    textbutton "None" action Function(ow.put_move, party[i], x, 2)
                else:
                    textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x, 2) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")

        #wild slot
        text "Wild"
        if party[i].get_moves()[6] == None:
            textbutton "None" action Function(ow.put_move, party[i], 6, 0)
        else:
            textbutton party[i].get_moves()[6].get_title() action Function(ow.swap_move, party[i], 6, 0) hovered Function(ow.move_browse, party[i].get_moves()[6]) unhovered Hide("move_browse")

        text "Intrinsic Passive"
        textbutton party[i].get_passive()[0].get_title() action Function(ow.swap_passive, party[i], 0) hovered Function(ow.passive_browse, party[i].get_passive()[0]) unhovered Hide("passive_browse")

        text "Gear Passive"
        textbutton party[i].get_passive()[1].get_title() action Function(ow.swap_passive, party[i], 1) hovered Function(ow.passive_browse, party[i].get_passive()[1]) unhovered Hide("passive_browse")



screen passive_swap(pl):
    modal True
    zorder 105
    textbutton "Cancel" action Return(0) pos (1220, 30)

    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20

            textbutton "Unequip" action Return(-1)

            for passive in pl:
                textbutton passive.get_title() action Return(passive) hovered Function(ow.passive_browse, passive) unhovered Hide("passive_browse")
screen passive_browse(passive):
    zorder 101
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(530, 200, 300, 400)
        ypadding 5
        xpadding 10

        vbox:
            text passive.get_title()
            text passive.get_flavour()
            #add: when the passive activates
screen gear_swap(viewlist, equip_type):
    #inventory: overworld inventory object
    modal True
    zorder 105
    textbutton "Cancel" action Hide("gear_browse"), Return(0)

    viewport:
        xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. Just change the y value to len(viewlist)*whatever. Easy.
        mousewheel True

        vbox:
            spacing 20

            textbutton "Unequip" action Return(-1)

            for gear in viewlist:
                if gear[0].get_type() in equip_type:
                    textbutton gear[0].get_title() action Return(gear[0]) hovered Function(ow.gear_browse, gear[0]) unhovered Hide("gear_browse")
screen gear_browse(gear):
    zorder 101
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(530, 200, 300, 400)
        ypadding 5
        xpadding 10

        vbox:
            text "Hp = " + str(gear.get_hp()) size 20
            text "Able = " + str(gear.get_able()) size 20
            text "Stamina = " + str(gear.get_stamina()) size 20
            text "Phys atk = " + str(gear.get_physa()) size 20
            text "Phys def = " + str(gear.get_physd()) size 20
            text "Mag atk = " + str(gear.get_maga()) size 20
            text "Mag def = " + str(gear.get_magd()) size 20
            text "Hit = " + str(gear.get_hit()) size 20
            text "Dodge = " + str(gear.get_dodge()) size 20
            text "affinity = " + str(gear.get_aff_name()) size 20
            if gear.get_passive() != 0:
                text gear.get_passive().get_title() size 20
screen move_swap(movelist, rank):
    modal True
    zorder 105
    textbutton "Cancel" action Hide("move_browse"), Return(0) pos (1220, 30)

    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20

            textbutton "Unequip" action Return(-1)

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
            text "drain(a/s) = " + str(move.get_able_drain()) + "/" + str(move.get_stamina_drain()) size 20
            if move.get_rank() == 1:
                text "rank = Front" size 20
            elif move.get_rank() == 2:
                text "rank = Back" size 20
            else:
                text "rank = Wild" size 20
            if move.get_damage_type() == 0:
                text "power = " + str(move.get_power()) + " (Physical)" size 20
            else:
                text "power = " + str(move.get_power()) + " (Magical)" size 20
            if move.get_status_only() == 0:
                text "hit bonus = " + str(move.get_hit()) size 20
                text "affinity = " + str(move.get_element_name()) size 20 #<-- replace text with image.
screen party_step(overworld):
    #intermediary between clicking the party button and selecting a party unit.
    #allows player to click any party unit or to click the inventory.
    modal True

    frame:
        background "party_step_bg"
        xpos 305
        ypos 105

        textbutton "Close" action Hide("party_step"), Hide("overworld_helpers")

        hbox:
            ypos 40
            spacing 30

            imagebutton:
                idle "open_inventory"
                hover "open_inventory_h"
                action Function(overworld.show_inventory_step), Hide("overworld_helpers")

            for i in range(0, len(overworld.get_party())):
                #textbutton overworld.get_party()[i].get_name() action Function(overworld.show_party, i), Hide("overworld_helpers")#, Hide("party_step")
                imagebutton:
                    idle overworld.get_party()[i].get_face()
                    hover overworld.get_party()[i].get_face_h()
                    action Function(overworld.show_party, i), Hide("overworld_helpers")#, Hide("party_step")
screen inventory_view_proper(overworld):
    #this is the inventory view screen that gets brought up by the party_step screen
    modal True
    zorder 101

    #5 viewports for our 5 inventory subsections
    frame:
        xpos 10
        xmaximum 1150
        ypos 25
        ymaximum 700
        textbutton "close" pos (25, 25) action Hide("inventory_view_proper")
        viewport:
            xpos 10 ypos 60 xysize (210,625)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for gear in overworld.get_inventory().get_arm():
                    textbutton gear[0].get_title() + " Q:" + str(gear[1]) action NullAction() hovered Function(ow.gear_browse, gear[0]) unhovered Hide("gear_browse")
        viewport:
            xpos 230 ypos 60 xysize (210,625)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for gear in overworld.get_inventory().get_wea():
                    textbutton gear[0].get_title() + " Q:" + str(gear[1]) action NullAction() hovered Function(ow.gear_browse, gear[0]) unhovered Hide("gear_browse")
        viewport:
            xpos 450 ypos 60 xysize (210,625)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for gear in overworld.get_inventory().get_acc():
                    textbutton gear[0].get_title() + " Q:" + str(gear[1]) action NullAction() hovered Function(ow.gear_browse, gear[0]) unhovered Hide("gear_browse")
        viewport:
            xpos 670 ypos 60 xysize (210,625)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for ite in overworld.get_inventory().get_ite():
                    textbutton ite[0].get_title() + " Q:" + str(ite[1]) action NullAction()
        viewport:
            xpos 890 ypos 60 xysize (210,625)
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for mat in overworld.get_inventory().get_mat():
                    textbutton mat[0].get_title() + " Q:" + str(mat[1]) action NullAction()

## -- HUB SCREENS -- ##
#TODO

## -- DIRECTION SCREENS -- ##
screen chapter_view(chapter, overworld):
    zorder 100

    #add a background frame. the journal can just overlay over wherever you are.
    add overworld.get_bg(chapter)
    add overworld.get_direction().get_bg() pos(302, 97) #background

    vbox: #shows a column of clickable chapter icons on the left of the questbook. click to change chapter.
        xpos 305
        ypos 105

        textbutton "Close" action Hide("quest_view"), Return

        for i in range(0, overworld.get_chapter()+1):
            if i == chapter:
                textbutton "chap [i]" action NullAction()
            else:
                textbutton "chap [i]" action Function(overworld.change_direction_view, i)

    #shows a column on clickable quest titles. click to change viewed quest. answers to chapter view.
    viewport:
        xpos 365
        ypos 125
        mousewheel True
        #xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. just multiply y by len of quest list.

        vbox:
            spacing 10
            for quest in overworld.get_direction().get_current():
                if (quest.get_chapter() - 1) == chapter:
                    textbutton quest.get_teaser() action Function(overworld.quest_view, quest)
screen quest_view(quest):
    zorder 101
    #for showing a particular quest. answers to chapter quests.

    #title
    if quest.get_progress() == -1:
        text quest.get_title() + " [[completed]" pos (550, 130)
    elif quest.get_progress() == -2:
        text quest.get_title() + "[[failed]" pos (550, 130)
    else:
        text quest.get_title() pos (550, 130)

    #expiry
    text "Expires: Chapter " + str(quest.get_chapter()) pos (850, 165)

    viewport:
        area (550, 200, 400, 600)
        vbox:
            spacing 10
            #title

            for i in range(0, quest.get_progress()):

                if quest.get_progress() - i == 1: #next objective
                    text quest.get_flavour()[i] + "[[next to do]" #highlighted
                    hbox:
                        text quest.get_requirement()[i]
                        add "quest_check_e"

                else: #already complete
                    text quest.get_flavour()[i] + "[[completed]" #greyed out
                    hbox:
                        text quest.get_requirement()[i]
                        add "quest_check_s"

## -- MAIN OVERWORLD SCREENS -- ##
screen overworld_helpers(overworld):
    #make these a mousearea thing:

    #if these guys get tooltips, they need some way to tell the screen where to show them
    vbox:
        yalign 0.4
        xalign 0.0
        spacing 20

        imagebutton: #party button
            idle "party_b"
            hover "party_h"
            #action Function(overworld.show_party) #invoke in new context
            action Function(overworld.show_party_step)
            #tooltip "Manage Party"

        imagebutton: #direction button
            idle "direction_b"
            hover "direction_h"
            action Function(overworld.show_direction)
            #tooltip "Directions"

        imagebutton: #hub button
            idle "hub_b"
            hover "hub_h"
            action Return #TODO later. after prologue. (the first hub will be nai's place.)
            #tooltip "Hub"
screen overworld_tooltip(descr, posl, images):
    #show spawn the frame window off to the right of the location icon in a little frame.
    #frame components:
    # -text title along the top of the frame

    frame:
        xpos posl[0]-20
        ypos posl[1]-112
        vbox:
            text descr color "#ffffff"
            hbox:
                for portrait in images:
                    add portrait
    timer 3.0 action Hide("overworld_tooltip", transition = dissolve)

screen overworld_map(overworld, chapter):

    #background bg
    add overworld.get_bg(chapter)

    #overworld helpers, party, quests, etc
    mousearea:
        area(0, 0.2, 0.1, 0.5) #dimensions
        hovered Function(overworld.show_ow_helpers)
        unhovered Hide("overworld_helpers", transition = dissolve)

    #events
    for route in overworld.get_routes()[chapter]:
        if route.get_lock() == 0:
            imagebutton:
                #pos (route.get_position()[0], route.get_position()[1])
                pos (route.get_position()[0]-54, route.get_position()[1]-72)
                idle "location_icon"
                hover "location_icon_h"
                action Function(renpy.invoke_in_new_context, route.call_event) hovered Function(overworld.show_tooltip, route.get_descr(), route.get_position(), route.get_images())




























##eof
