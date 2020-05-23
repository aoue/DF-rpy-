
#all the screens for the overworld/dungeon map and some assisting images.
#to be reorganized later. grouper together for now for ease of development

## -- PARTY SCREENS -- ##
screen inventory_view(viewlist):
    zorder 101
    viewport:
        xpos 20 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20

            for gear in viewlist:
                textbutton gear.get_title() action NullAction() hovered Function(ow.gear_browse, gear) unhovered Hide("gear_browse")
screen party_view(party, i, ow):
    zorder 100

    #background
    add ow.get_party_bg()

    #close button
    textbutton "close" action Return pos (950, 10)

    #character pose
    add party[i].get_pose() pos(435, 55)

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
    text "Lvl " + str(party[i].get_lvl()) + " " +party[i].get_focus() pos (445, 20)

    #next unit button on midtop right: (i += 1 OR if i+1 > len(party), i = 0). dissolve.

    #eqipped moves
    vbox:
        yalign 0.55
        xalign 0.70
        spacing 40

        for x in range(0, len(party[i].get_moves())):
            if party[i].get_moves()[x] == None:
                textbutton "Nothing" action Function(ow.put_move, party[i], x)

            else:
                textbutton party[i].get_moves()[x].get_title() action Function(ow.swap_move, party[i], x) hovered Function(ow.move_browse, party[i].get_moves()[x]) unhovered Hide("move_browse")

    #move vp on the right
    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        #add whatever bg you want
        vbox:
            spacing 20
            for move in party[i].get_movelist():
                #if gear.get_type() == type:
                textbutton move.get_title() action NullAction() hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
screen gear_swap(viewlist, equip_type):
    #inventory: overworld inventory object

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
        area(245, 400, 300, 200)
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
screen move_swap(movelist):
    zorder 105

    textbutton "Cancel" action Return(0) pos (1220, 30)

    viewport:
        xpos 1080 ypos 60 xysize (160,625)
        #child_size(180, 670) #it may need to be bigger. that is no issue, just change the y value.
        mousewheel True

        vbox:
            spacing 20
            for move in movelist:
                textbutton move.get_title() action Return(move) hovered Function(ow.move_browse, move) unhovered Hide("move_browse")
screen move_browse(move):
    zorder 101
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(245, 400, 300, 200)
        ypadding 5
        xpadding 10

        vbox:
            text move.get_title()
            text move.get_flavour()
            text "drain(a/s) = " + str(move.get_able_drain()) + "/" + str(move.get_stamina_drain())
            if move.get_damage_type() == 0:
                text "power = " + str(move.get_power()) + " (Physical)"
            else:
                text "power = " + str(move.get_power()) + " (Magical)"
            if move.get_status_only() == 0:
                text "hit bonus = " + str(move.get_hit())
                text "affinity = " + str(move.get_element()) #<-- replace text with image. affinities will be conveyed this way.


## -- DIRECTION SCREENS -- ##
#TODO

## -- HUB SCREENS -- ##
#TODO

## -- OVERWORLD SCREENS -- ##
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

    #hotspot (170, 78, 343, 213) hovered Show(md[1]) unhovered Hide(md[0]) action Jump(map_jumps[0])

    vbox:
        yalign 0.20
        xalign 0.05
        spacing 20

        imagebutton: #party button
            idle "party_b"
            hover "party_h"
            action Function(overworld.show_party) #invoke in new context

        imagebutton: #direction button
            idle "direction_b"
            hover "direction_h"
            action Function(overworld.show_direction)

        imagebutton: #hub button
            idle "hub_b"
            hover "hub_h"
            action Return #TODO later. after prologue. (the first hub will be nai's place.)


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


## -- DUNGEON SCREENS -- ##
screen dungeon_map(dungeon, map, spot):
    #map: the connected net of rooms
    #spot: tuple of the party's position

    #manage party button
    vbox:
        yalign 0.05
        xalign 0.0
        spacing 10

        #party button
        imagebutton:
            idle "party_b"
            hover "party_h"
            action Function(dungeon.get_master().show_party) #invoke in new context.

        #change deployment and change hold list. useful if ambush/we skip deployment.
        #imagebutton: #TODO

        #show party vital statistics of current deployed team. if no deployed team, show first (up to) 5 units in the party.
        if not dungeon.get_hold():
            for x in range(0, min(len(dungeon.get_party()), 5)):
                vbox:
                    text dungeon.get_party()[x].get_name() #change to portrait
                    text "Hp: "+str(dungeon.get_party()[x].get_hp())+"/"+str(dungeon.get_party()[x].get_hpmax()) #change to bar. on hover, see actual numbers.
                    text "En: "+str(dungeon.get_party()[x].get_energy())+"/"+str(dungeon.get_party()[x].get_energymax()) #change to bar. on hover, see actual numbers.
        else:
            for unit in dungeon.get_hold()[0]:
                vbox:
                    text unit.get_name() #change to portrait
                    text "Hp: "+str(unit.get_hp())+"/"+str(unit.get_hpmax()) #change to bar. on hover, see actual numbers.
                    text "En: "+str(unit.get_energy())+"/"+str(unit.get_energymax()) #change to bar. on hover, see actual numbers.

    #make the map scrollable using the viewport
    viewport:
        xpos 100 ypos 75 xysize (1000,625)
        child_size (len(map)*128, 500) #xlength = len(dungeon.get_map()*(xroomspace+connector space)). ylength = len(longest list)*(yroomspace+connector space)
        draggable True
        #mousewheel True
        #arrowkeys True

        add dungeon.get_bg() #a dungeon's bg should be an aerial view of the area, with visual layout same as map

        for i in range (0, len(map)):
            for room in map[i]:
                if room != None:

                    #if room connected to the right, add horizontal hallway image. if top, add vertical, if left, if bottom, etc.
                    imagebutton:
                        pos (room.get_dis_x(), room.get_dis_y())

                        if room.get_explored() == 0:
                            idle "room"
                        else:
                            idle "room_ex"

                        if (abs(spot[0] - room.get_x()) == 1 and spot[1] - room.get_y() == 0) or (spot[0] - room.get_x() == 0 and abs(spot[1] - room.get_y()) == 1):
                            if (spot[1] < room.get_y() and room.get_connect()[0] == 1) or (spot[0] > room.get_x() and room.get_connect()[1] == 1) or (spot[1] > room.get_y() and room.get_connect()[2] == 1) or (spot[0] < room.get_x() and room.get_connect()[3] == 1):
                                hover "room_hover"
                                action Function(dungeon.move_spot, room.get_x(), room.get_y())

                    if room.get_explored() == 1:
                        #draw the connector hallways
                        if room.get_connect()[0] == 1:
                            add "hall_v" pos (room.get_dis_x() + 64, room.get_dis_y() - 18) #top

                        if room.get_connect()[1] == 1:
                            add "hall_h" pos (room.get_dis_x() + 128, room.get_dis_y() + 36) #right

                        if room.get_connect()[2] == 1:
                            add "hall_v" pos (room.get_dis_x() + 64, room.get_dis_y() + 72) #bottom

                        if room.get_connect()[3] == 1:
                            add "hall_h" pos (room.get_dis_x() - 22, room.get_dis_y() + 36) #left

        add "party_icon" pos (36 + dungeon.find_room().get_dis_x(), 3 + dungeon.find_room().get_dis_y())


label room(dungeon):
    "room: [dungeon.spot_x], [dungeon.spot_y] event"
    $dungeon.show_dungeon()


label test_dungeon_entrance:
    "you enter the dungeon. bla blah can be anything."
    python:
        ow.show_dungeon()

























##eof
