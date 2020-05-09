

#collection of all the screens needed for the battle.

#------ally side positions------#
#px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

#------enemy side positions------#
#px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())

screen combatinfo(pl, el, pt, et, tl, rounds, ph):
    #display battle information: turns left for each, rounds, hp, positions, etc
    vbox:
        xalign 0.0
        yalign 0.02
        spacing 1
        text "rounds left : [rounds]"
        text "player turns left : [pt]"
        text "total turns left : [tl]"
        text "enemy turns left : [et]"
        text "phase: [ph]"
    vbox:
        xalign 0.0
        yalign 0.9
        spacing 2
        for i in range(0, len(pl)):
            text "{}'s hp = {} ({}) [[{}] stam={}".format(pl[i].get_name(), str(pl[i].get_hp()), str(pl[i].get_dodge()), pl[i].get_able(), pl[i].get_stamina())
    vbox:
        xalign 1.0
        yalign 0.9
        spacing 2
        for i in range(0, len(el)):
            text "{}'s hp = {} ({}) [[{}]".format(el[i].get_name(), str(el[i].get_hp()), str(el[i].get_dodge()), el[i].get_able())

screen show_units(pl, el):
    zorder 99
    for i in range(0, len(pl)):
        add pl[i].get_icon() pos(275 + 125*pl[i].get_point().get_x(), 385 + 65*pl[i].get_point().get_y())

    for i in range(0, len(el)):
        add el[i].get_icon() pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())
        text el[i].get_name() pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())

screen order_unit(pl):
    #select which unit to order from available units that have yet to act. returns rank of unit.
    zorder 100
    for i in range (0, len(pl)):
        if pl[i].get_able() > 0:
            button:
                pos(275 + 125*pl[i].get_point().get_x(), 385 + 65*pl[i].get_point().get_y())
                text pl[i].get_name()
                action Return(pl[i])


screen pick_move(unit, battle):
    #show moves. top left of box is 900, 175
    #TODO. show move descrition on hover. make it a long list thingy of symbols. we don't want it to be too large

    frame:
        xpadding 5
        ypadding 5
        yalign 0.4
        xalign 0.8
        vbox:
            text "Selected: " + unit.get_name()
            spacing 10
            for i in range(0, len(unit.get_moves())):
                if (unit.get_point().get_y() in range(0, 3)) and unit.get_moves()[i].get_rank() == 1:
                    if unit.get_stamina() >= unit.get_moves()[i].get_stamina_drain() and unit.get_moves()[i].check_clearance(unit, battle) == 1:
                        textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return
                    else:
                        text "{} (unable)".format(unit.get_moves()[i].get_title())#unselectable, but still shown

                elif (unit.get_point().get_y() in range(3, 5)) and unit.get_moves()[i].get_rank() == 2:
                    if unit.get_stamina() >= unit.get_moves()[i].get_stamina_drain() and unit.get_moves()[i].check_clearance(unit, battle) == 1:
                        textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return
                    else:
                        text "{} (unable)".format(unit.get_moves()[i].get_title())#unselectable, but still shown

            if unit.get_evo() == 1:
                if unit.get_stamina() >= unit.get_moves()[i].get_stamina_drain() and unit.get_moves()[i].check_clearance(unit, battle) == 1:
                    textbutton unit.get_moves()[7].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return
                else:
                    text "{} (unable)".format(unit.get_moves()[i].get_title())#unselectable, but still shown

            textbutton "Walk" action Function(unit.walk, battle), Return

            if unit.get_ablemax() == unit.get_able():
                textbutton "Defend" action Function(unit.defend), Return
            else:
                textbutton "Wait" action Function(unit.wait), Return

screen enemy_highlight(unit, cmove):
    zorder 101

    if cmove.get_type() == 26:
        for column in range(1, 4): #column
            for row in range(1, 4): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    hover "images/combat/fx/tile e hover.png"
                    pos(275 + row*125, 5 + column*65)
                    action Return((row, column)) hovered Function(enemy_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

    else:
        for column in range(0, 5): #column
            for row in range(0, 5): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    hover "images/combat/fx/tile e hover.png"
                    pos(275 + row*125, 5 + column*65)
                    action Return((row, column)) hovered Function(enemy_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

screen ally_highlight(unit, cmove):
    zorder 101

    if cmove.get_type() == 0: #for targeting self
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(275 + unit.get_point().get_x()*125, 385 + unit.get_point().get_y()*65)
            action Return() #return tuple
    else:
        for column in range(0, 5): #column
            for row in range(0, 5): #row
                imagebutton:
                    idle "images/combat/fx/tile.png"
                    hover "images/combat/fx/tile f hover.png"
                    pos(275 + row*125, 385 + column*65)
                    action Return((row, column)) hovered Function(ally_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple

screen walk_highlight(unit, battle):
    #move 1 square in any direction. respect borders, respect collision.
    #this means take account of the grid

    #grid checking positions:

    zorder 101
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
            pos(275 + max(dtuple[0]-1,0)*125, 385 + dtuple[1]*65)
            action Return((max(dtuple[0]-1,0), dtuple[1]))

    if target2 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(275 + min(dtuple[0]+1,4)*125, 385 + dtuple[1]*65)
            action Return((min(dtuple[0]+1,4), dtuple[1]))

    if target3 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(275 + dtuple[0]*125, 385 + max(dtuple[1]-1, 0)*65)
            action Return((dtuple[0], max(dtuple[1]-1, 0)))

    if target4 == None:
        imagebutton:
            idle "images/combat/fx/tile.png"
            hover "images/combat/fx/tile f hover.png"
            pos(275 + dtuple[0]*125, 385 + min(dtuple[1]+1, 4)*65)
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
#27: cross 5x5


screen enemy_highlight_extra(unit, cmove, row, column):
    zorder 102
    if cmove.get_type() == 2: # 1x2
        add "tile_e_hovered" at e_tile_hover(row, column-1)

    elif cmove.get_type() == 3: # 1x3
        pass

    elif cmove.get_type() == 15: # 4x1
        if column != 0:
            add "tile_e_hovered" at e_tile_hover(row, 0)
        if column != 1:
            add "tile_e_hovered" at e_tile_hover(row, 1)
        if column != 2:
            add "tile_e_hovered" at e_tile_hover(row, 2)
        if column != 3:
            add "tile_e_hovered" at e_tile_hover(row, 3)
        if column != 4:
            add "tile_e_hovered" at e_tile_hover(row, 4)

    elif cmove.get_type() == 26: #3x3 cross
        add "tile_e_hovered" at e_tile_hover(row, column-1)
        add "tile_e_hovered" at e_tile_hover(row, column+1)
        add "tile_e_hovered" at e_tile_hover(row-1, column)
        add "tile_e_hovered" at e_tile_hover(row+1, column)


screen ally_highlight_extra(unit, cmove, row, column):
    zorder 102

    if cmove.get_type() == 2: # 1x2
        add "tile_e_hovered" at a_tile_hover(row, column-1)

    elif cmove.get_type() == 3: # 1x3
        pass

    elif cmove.get_type() == 15: # 4x1
        if column != 0:
            add "tile_e_hovered" at a_tile_hover(row, 0)
        if column != 1:
            add "tile_e_hovered" at a_tile_hover(row, 1)
        if column != 2:
            add "tile_e_hovered" at a_tile_hover(row, 2)
        if column != 3:
            add "tile_e_hovered" at a_tile_hover(row, 3)
        if column != 4:
            add "tile_e_hovered" at a_tile_hover(row, 4)









##eof
