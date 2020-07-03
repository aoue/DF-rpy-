#collection of screens used in the battle.

#------ally side positions------#
#px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

#------enemy side positions------#
#px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())

init python:
    def show_status_screen(unit):
        renpy.show_screen("status_screen", unit)


screen status_screen(unit):
    #shows a screen with:
    # -all the stances the unit is currently under and their remaining durations
    # -unit's natural/armour affinity
    # -unit's passive

    zorder 100
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(910, 500, 300, 200)
        ypadding 5
        xpadding 10

        vbox:
            text unit.get_name()
            text "Aff: " + unit.get_aff_name() + ","  + unit.get_armour().get_aff_name()
            text "wpn aff: " + unit.get_weapon().get_aff_name()
            text "Passive: " + unit.get_passive().get_title()

            #dots
            if unit.get_stance().get_poison() > 0:
                text "Poison: " + str(unit.get_stance().get_poison())

            #stances
            if unit.get_stance().get_adrenaline() > 0:
                text "Adrenaline: " + str(unit.get_stance().get_adrenaline())

            if unit.get_stance().get_rally() > 0:
                text "Rally: " + str(unit.get_stance().get_rally())

            if unit.get_stance().get_howl() > 0:
                text "Howl: " + str(unit.get_stance().get_howl())

            if unit.get_stance().get_exhausted() > 0:
                text "Exhausted"

            if unit.get_stance().get_kindara() > 0:
                text "Kindara: " + str(unit.get_stance().get_kindara())

            if unit.get_stance().get_shatter() > 0:
                text "Shatter: " + str(unit.get_stance().get_shatter())

            if unit.get_stance().get_mtn() > 0:
                text "MTN: " + str(unit.get_stance().get_mtn())


screen combatinfo(pl, el, pt, et, rounds, ph):
    #display battle information: turns left for each, rounds, hp, positions, etc
    vbox: #round/turns info
        xalign 0.8
        yalign 0.02
        spacing 1
        if rounds > 0:
            text "rounds left : [rounds]"
        text "player turns left : [pt]"
        text "enemy turns left : [et]"
        text "phase: [ph]"


    vbox: #player stats/info
        xalign 0.0
        ypos (350)
        spacing 10

        for unit in pl:

            text "{}: hp={}/{} a={}\n dodge=[[{}/{}]% s={}/{} e={}/{}".format(unit.get_name(), unit.get_hp(), unit.get_hpmax_actual(), unit.get_able(), unit.get_dodge(), unit.get_dodgemax_actual(), unit.get_stamina(), unit.get_staminamax_actual(), unit.get_energy(), unit.get_energymax()) size 20

    vbox: #enemy stats/info
        xalign 0.0
        yalign 0.0
        spacing 2
        for unit in el:
            text "{}: hp={}/{} a={}\n dodge=[[{}/{}]% s={}/{}".format(unit.get_name(), unit.get_hp(), unit.get_hpmax_actual(), unit.get_able(), unit.get_dodge(), unit.get_dodgemax_actual(), unit.get_stamina(), unit.get_staminamax_actual()) size 20

screen show_units(pl, el):
    zorder 99
    for unit in pl:
        #add unit.get_icon() pos(265 + 124*unit.get_point().get_x(), 407 + 62*unit.get_point().get_y())
        imagebutton:
            pos(265 + 124*unit.get_point().get_x(), 407 + 62*unit.get_point().get_y())
            idle unit.get_icon()
            hover unit.get_icon()
            action NullAction() hovered Function(show_status_screen, unit) unhovered Hide("status_screen")

    for unit in el:
        #add unit.get_icon() pos(265 + 124*unit.get_point().get_x(), -2 + 62*unit.get_point().get_y())
        text unit.get_name() pos(265 + 124*unit.get_point().get_x(), -2 + 62*unit.get_point().get_y())

        imagebutton:
            pos(265 + 124*unit.get_point().get_x(), -2 + 62*unit.get_point().get_y())
            idle unit.get_icon()
            hover unit.get_icon()
            action NullAction() hovered Function(show_status_screen, unit) unhovered Hide("status_screen")

screen show_damage(showlist, title, unit):
    #showlist: list of four-tuples: (grid x, grid y, damage, iff)
    zorder 103

    if unit.get_iff() == 0:
        text title pos(265 + 124*unit.get_point().get_x(), 415 + 62*unit.get_point().get_y())
    else:
        text title pos(325 + 125*unit.get_point().get_x(), 5 + 65*unit.get_point().get_y())

    for tup in showlist:
        if tup[3] == 1:
            if tup[2] > 0:
                text "-{}".format(tup[2]) color "ff0000" pos(265 + 124*tup[0], 5 + 62*tup[1])
            add "tile_e_hovered" at e_tile_hover(tup[0], tup[1])
        else:
            if tup[2] > 0:
                text "-{}".format(tup[2]) color "ff0000" pos(265 + 124*tup[0], 415 + 62*tup[1])
            add "tile_e_hovered" at a_tile_hover(tup[0], tup[1])

    timer 1.0 action Hide("show_damage", transition = dissolve)

screen show_heal(showlist, title, unit):
    #showlist: list of four-tuples: (grid x, grid y, heal, iff)
    zorder 103

    if unit.get_iff() == 0:
        text title pos(265 + 124*unit.get_point().get_x(), 415 + 62*unit.get_point().get_y())
    else:
        text title pos(325 + 125*unit.get_point().get_x(), 5 + 65*unit.get_point().get_y())

    for tup in showlist:
        if tup[3] == 1:
            if tup[2] > 0:
                text "+{}".format(tup[2]) color "327345" pos(265 + 124*tup[0], 5 + 62*tup[1])
            else:
                text "+maxed" color "327345" pos(265 + 124*tup[0], 5 + 62*tup[1])

            add "tile_f_hovered" at a_tile_hover(tup[0], tup[1])

        else:
            if tup[2] > 0:
                text "+{}".format(tup[2]) color "327345" pos(265 + 124*tup[0], 415 + 62*tup[1])
            else:
                text "+maxed" color "327345" pos(265 + 124*tup[0], 415 + 62*tup[1])

            add "tile_f_hovered" at a_tile_hover(tup[0], tup[1])


    timer 1.0 action Hide("show_heal", transition = dissolve)

screen show_dot(showlist):
    #showlist: list of tuples: (unit, damage)
    zorder 103
    for tup in showlist:
        if tup[0].get_iff() == 1:
            if tup[1] < 0:
                text "{color=ff0000}[tup[1]]{/color}" pos(265 + 124*tup[0].get_point().get_x(), 5 + 62*tup[0].get_point().get_y())
            else:
                text "{color=327345}+[tup[1]]{/color}" pos(265 + 124*tup[0].get_point().get_x(), 5 + 62*tup[0].get_point().get_y())

        else:
            if tup[1] < 0:
                text "{color=ff0000}[tup[1]]{/color}" pos(265 + 124*tup[0].get_point().get_x(), 415 + 62*tup[0].get_point().get_y())
            else:
                text "{color=327345}+[tup[1]]{/color}" pos(265 + 124*tup[0].get_point().get_x(), 415 + 62*tup[0].get_point().get_y())

    timer 1.0 action Hide("show_dot", transition = dissolve)

screen order_unit(pl):
    #select which unit to order from available units that have yet to act. returns rank of unit.
    zorder 100
    for unit in pl:
        if unit.get_able() > 0:
            imagebutton:
                pos(265 + 124*unit.get_point().get_x(), 415 + 62*unit.get_point().get_y())
                idle "ready_icon"
                hover "ready_icon"
                action Return(unit) hovered Function(show_status_screen, unit) unhovered Hide("status_screen")

screen pick_move(unit, battle):

    frame:
        xpadding 5
        ypadding 5
        yalign 0.4
        xalign 0.8
        vbox:
            text "Selected: " + unit.get_name()
            spacing 10

            for move in unit.get_moves():
                if move == None:
                    pass
                #correct position
                elif (move.get_rank() == 0) or (unit.get_point().get_y() in range (0, 3) and move.get_rank() == 1 ) or (unit.get_point().get_y() in range (3, 5) and move.get_rank() == 2):
                    #able to use move
                    if unit.get_stamina() >= move.get_stamina_drain() and move.check_clearance(unit, battle) == 1 and unit.get_energy() >= move.get_energy_drain():
                        textbutton move.get_title() action Function(unit.use_move, move, battle), Return hovered Function(battle.move_browse_b, move) unhovered Hide("move_browse_b")

                    #unable to use move; tell the player why.
                    else:
                        if move.check_clearance(unit, battle) == 0:
                            text "{} (blocked)".format(move.get_title())

                        elif unit.get_energy() < move.get_energy_drain():
                            text "{} (need energy)".format(move.get_title())

                        elif unit.get_stamina() < move.get_stamina_drain():
                            text "{} (need stamina)".format(move.get_title())
                else:
                    text move.get_title() + " (rank)" #the list will get very long :( solution? is it fine?

            textbutton "Wait" action Function(unit.wait), Return

            textbutton "Cancel" action Return

screen move_browse_b(move):
    zorder 108
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(910, 500, 300, 200)
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
                text "affinity = " + str(move.get_element_name()) #<-- replace text with image.

screen enemy_highlight(unit, cmove):
    zorder 101

    if cmove.get_type() == 26 or cmove.get_type() == 27:
        for column in range(1, 4): #column
            for row in range(1, 4): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    if cmove.get_type() == 27:
                        idle "images/combat/fx/tile.png"
                    else:
                        hover "images/combat/fx/tile e hover.png"
                    pos(265 + (124*row), -2 + (62*column))
                    action Return((row, column)) hovered Function(enemy_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

    else:
        for column in range(0, 5): #column
            for row in range(0, 5): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    hover "images/combat/fx/tile e hover.png"
                    pos(265 + 124*row, -2 + 62*column)
                    action Return((row, column)) hovered Function(enemy_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

    frame:
        area (530, 340, 100, 40)
        textbutton "Cancel" action Return(-1)

screen ally_highlight(unit, cmove):
    zorder 101

    if cmove.get_type() == 0: #for targeting self
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(265 + 124*unit.get_point().get_x(), 407 + 62*unit.get_point().get_y())
            action Return() #return tuple

    else:
        for column in range(0, 5): #column
            for row in range(0, 5): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    hover "images/combat/fx/tile f hover.png"
                    pos(265 + (124*row), 407 + (62*column))
                    action Return((row, column)) hovered Function(ally_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

    frame:
        area (530, 340, 100, 40)
        textbutton "Cancel" action Return(-1)

screen walk_highlight(unit, battle):
    #move 1 square in any direction. respect borders, respect collision.
    #this means take account of the grid

    zorder 101
    #cancel button:
    frame:
        area (530, 340, 100, 40)
        textbutton "Cancel" action Return(-1)

    python:
        dtuple = (unit.get_point().get_x(), unit.get_point().get_y())

        target = battle.get_allymap().search_map((max(dtuple[0]-1,0), dtuple[1]))#left tile
        target2 = battle.get_allymap().search_map((min(dtuple[0]+1,4), dtuple[1])) #right tile
        target3 = battle.get_allymap().search_map((dtuple[0], max(dtuple[1]-1, 0))) #below tile
        target4 = battle.get_allymap().search_map((dtuple[0], min(dtuple[1]+1, 4))) #above tile

    if target == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(265 + max(dtuple[0]-1,0)*124, 415 + dtuple[1]*62)
            action Return((max(dtuple[0]-1,0), dtuple[1]))

    if target2 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(265 + min(dtuple[0]+1,4)*124, 415 + dtuple[1]*62)
            action Return((min(dtuple[0]+1,4), dtuple[1]))

    if target3 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(265 + dtuple[0]*124, 415 + max(dtuple[1]-1, 0)*62)
            action Return((dtuple[0], max(dtuple[1]-1, 0)))

    if target4 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(265 + dtuple[0]*124, 415 + min(dtuple[1]+1, 4)*62)
            action Return((dtuple[0], min(dtuple[1]+1, 4)))


#---- TARGETING LEGEND ----
# 0: self
# 1: 1x1
# 2: 1x2
# 3: 1x3
# 4: 1x4
# 5: 1x5
# 6: 2x1
# 7: 2x2
# 8: 2x3
# 9: 2x4
#10: 2x5
#11: 3x1
#12: 3x2
#13: 3x3
#14: 3x4
#14: 3x5
#15: 4x1
#16: 4x2
#17: 4x3
#18: 4x4
#19: 4x5
#20: 5x1
#21: 5x2
#22: 5x3
#23: 5x4
#24: 5x5
#26: cross 3x3
#27: cross 3x3 w/ no center
#28: cross 5x5


screen enemy_highlight_extra(unit, cmove, row, column):
    zorder 102
    if cmove.get_type() == 2: # 1x2
        $column = min(column, 1)
        for c in range(column, column+2):
            for r in range(row, row+1):
                add "tile_e_hovered" at e_tile_hover(r, c)

    elif cmove.get_type() == 3: # 1x3
        $column = min(column, 2)
        for c in range(column, column+3):
            for r in range(row, row+1):
                add "tile_e_hovered" at e_tile_hover(r, c)

    elif cmove.get_type() == 7: # 2x2
        $column = min(column, 3)
        $row = min(row, 3)
        for c in range(column, column+2):
            for r in range(row, row+2):
                add "tile_e_hovered" at e_tile_hover(r, c)

    elif cmove.get_type() == 27: #3x3 cross w/ no center
        add "tile_e_hovered" at e_tile_hover(row, column-1)
        add "tile_e_hovered" at e_tile_hover(row, column+1)
        add "tile_e_hovered" at e_tile_hover(row-1, column)
        add "tile_e_hovered" at e_tile_hover(row+1, column)

screen ally_highlight_extra(unit, cmove, row, column):
    zorder 102

    if cmove.get_type() == 3: # 1x3
        add "tile_f_hovered" at a_tile_hover(row, column-1)
        add "tile_f_hovered" at a_tile_hover(row, column-2)

    elif cmove.get_type() == 13: #3x3
        $row = min(row, 2)
        $column = min(column, 2)
        for c in range(column, column+3):
            for r in range(row, row+3):
                add "tile_f_hovered" at a_tile_hover(r, c)
