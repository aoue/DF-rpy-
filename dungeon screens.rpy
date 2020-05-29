

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
