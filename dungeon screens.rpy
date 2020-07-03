

## -- OUT OF BATTLE SKILLS  -- ##
screen oob_unit_tab(dungeon):
    zorder 100
    modal True

    #adds the background
    #add dungeon.get_bg()
    vbox:
        xpos 800
        ypos 0

        textbutton "Close" action Hide("oob_unit_tab"), Hide("oob_move_select"), Hide("oob_target_select")

        #shows a column of all units in party. click a unit to see/select a move to use
        viewport:

            mousewheel True
            vbox:
                #xpos 500
                #ypos 400

                for unit in dungeon.get_party():
                    textbutton unit.get_name() action Hide("oob_move_select"), Hide("oob_target_select"), Function(dungeon.out_of_battle_skills, unit)
screen oob_move_select(dungeon, unit):
    zorder 101
    #modal True

    #all the unit's known moves with oob = 1.

    viewport:
        area (900, 100, 100, 300)
        vbox:
            spacing 10
            for move in unit.get_moves():
                if move != None:
                    if move.get_oob() == 1:
                        if unit.get_energy() >= move.get_energy_drain():
                            textbutton move.get_title() action Function(dungeon.out_of_battle_target, unit, move)
                        else:
                            textbutton move.get_title() action NullAction()

            for move in unit.get_movelist():
                if move != None:
                    if move.get_oob() == 1:
                        if unit.get_energy() >= move.get_energy_drain():
                            textbutton move.get_title() action Function(dungeon.out_of_battle_target, unit, move)
                        else:
                            textbutton move.get_title() action NullAction()
screen oob_target_select(dungeon, unit, move):
    zorder 102
    #modal True

    viewport:
        area (1000, 100, 100, 300)
        vbox:
            spacing 10
            for target in dungeon.get_party():
                imagebutton:
                    idle target.get_face()
                    hover target.get_face_h()
                    action Function(move.exert_oob, unit, target)



## -- DUNGEON SCREENS -- ##
screen dungeon_map(dungeon, map):
    #map: the connected net of rooms
    #spot: tuple of the party's position

    #room menu/skills menu
    vbox:
        yalign 0.05
        xalign 1.0
        spacing 10

        ## -- left side menu -- ##
        textbutton "skills" action Function(dungeon.out_of_battle_units) #out of battle skills menu

        # room specific stuff
        if dungeon.find_room().get_has_action() == 1:
            if dungeon.find_room().get_is_exit() == 1:
                textbutton dungeon.find_room().get_action_title() action Function(dungeon.exit_dungeon)
            elif dungeon.find_room().get_charges() != 0:
                textbutton dungeon.find_room().get_action_title() action Function(dungeon.find_room().room_action, dungeon)

        if dungeon.find_room().get_fight() == 1:
            textbutton "Find trouble" action Function(dungeon.find_trouble)

        if dungeon.find_room().get_poi() == 1:
            textbutton "Point of Interest" action Function(dungeon.find_room().poi_event(), dungeon)

    #party menu
    vbox:
        yalign 0.05
        xalign 0.0
        spacing 10
        #party button
        imagebutton:
            idle "party_b"
            hover "party_h"
            action Function(dungeon.get_master().show_party) #invoke in new context.

        #change deployment and change hold list. useful if ambush/we skip deployment. do we still want this??
        #imagebutton: #TODO

        #show party vital statistics of current deployed team. if no deployed team, show first (up to) 5 units in the party.
        if not dungeon.get_hold()[0]:
            for x in range(0, min(len(dungeon.get_party()), 5)):
                vbox:
                    text dungeon.get_party()[x].get_name() #change to portrait
                    text "Hp: "+str(dungeon.get_party()[x].get_hp())+"/"+str(dungeon.get_party()[x].get_hpmax_actual()) #change to bar. on hover, see actual numbers.
                    text "En: "+str(dungeon.get_party()[x].get_energy())+"/"+str(dungeon.get_party()[x].get_energymax_actual()) #change to bar. on hover, see actual numbers.
        else:
            for unit in dungeon.get_hold()[0]:
                vbox:
                    text unit.get_name() #change to portrait
                    text "Hp: "+str(unit.get_hp())+"/"+str(unit.get_hpmax_actual()) #change to bar. on hover, see actual numbers.
                    text "En: "+str(unit.get_energy())+"/"+str(unit.get_energymax_actual()) #change to bar. on hover, see actual numbers.

    #map
    text "Threat = " + str(dungeon.get_threat()) pos (610, 0)
    viewport:
        xpos 150 ypos 75 xysize (1000,625)
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

                        if (abs(dungeon.get_spot()[0] - room.get_x()) == 1 and dungeon.get_spot()[1] - room.get_y() == 0) or (dungeon.get_spot()[0] - room.get_x() == 0 and abs(dungeon.get_spot()[1] - room.get_y()) == 1):
                            if (dungeon.get_spot()[1] < room.get_y() and room.get_connect()[0] == 1) or (dungeon.get_spot()[0] > room.get_x() and room.get_connect()[1] == 1) or (dungeon.get_spot()[1] > room.get_y() and room.get_connect()[2] == 1) or (dungeon.get_spot()[0] < room.get_x() and room.get_connect()[3] == 1):

                                if room.get_locked() == 0:
                                    hover "room_hover"
                                    action Function(dungeon.move_spot, room.get_x(), room.get_y()) #play footsteps sound as the group walks
                                else:
                                    hover "room_lock"
                                    action Function(room.lock_event, dungeon)
                                    #action NullAction() #play lock clunking sound as the door is locked

                    if room.get_explored() == 1:
                        #add room icon
                        add room.get_icon() pos(room.get_dis_x() + 100, room.get_dis_y())

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
    #python:
    #    dungeon.show_dungeon()
    return

    #return
    #return

label test_dungeon_entrance:
    #"you enter the dungeon. bla blah can be anything."

    #in dungeon:
    #0: entering
    #1: inside
    #2: leaving

    python:
        if ow.get_in_dungeon() == 2:
            #renpy.hide_screen("dungeon_map")
            ow.show_overworld()
        else:
            ow.show_dungeon()

#eof
