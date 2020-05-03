

#collection of all the screens needed for the battle.

#------ally side positions------#
#px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

#------enemy side positions------#
#px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())


label battle0:
    #this is a scripted event

    #do any deployment enabling/disabling
    python:
        playerlist = []
        mc_d = unit_mc()
        yve_d = unit_yve()

        baddie = unit_grunt(0, "vile grunt", 1, 3)
        baddie2 = unit_grunt(1, "very vile grunt", 3, 3)
        enemylist = [baddie, baddie2]

        deployer = deployment(2)

    scene image "combat/bg/deployfield0.jpg"
    call screen deploy_screen(deployer)

    "deployment finished. Fight!" #test

    #new battle test
    python:
        battle0 = battle(5, playerlist, enemylist, "battlefield0")
        battle0.combat_round()

    return

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
    #TODO. show move descrition/image on hover.
    ##TODO clearance checks
    #stamina checks

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
                    textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return

                elif (unit.get_point().get_y() in range(3, 5)) and unit.get_moves()[i].get_rank() == 2:
                    textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return

            if unit.get_evo() == 1:
                textbutton unit.get_moves()[7].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y(), battle), Return

            textbutton "Walk" action Function(unit.walk, unit), Return

            textbutton "Pass" action Function(unit_pass, unit), Return



screen enemy_highlight(unit, cmove):
    zorder 101

    for column in range(0, 5): #column
        for row in range(0, 5): #row
            imagebutton:
                idle "images/combat/fx/tile.png"
                hover "images/combat/fx/tile e hover.png"
                pos(275 + row*125, 5 + column*65)
                action Return((row, column)) hovered Function(enemy_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple of top left corner

screen ally_highlight(unit, cmove):
    zorder 101
    for column in range(0, 5): #column
        for row in range(0, 5): #row
            imagebutton:
                idle "images/combat/fx/tile.png"
                hover "images/combat/fx/tile f hover.png"
                pos(275 + row*125, 385 + column*65)
                action Return((row, column)) hovered Function(ally_highlighter, unit, cmove, row, column) unhovered Function(hide_highlighter) #return tuple of top left corner



#------ally side positions------#
#px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

#------enemy side positions------#
#px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())

init python:
    #---- TARGETING LEGEND ----
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

    def enemy_highlighter(unit, cmove, row, column):
        if cmove.get_type() == 2:
            renpy.show("tile_e_hovered", at_list=[e_tile_hover(row, column-1)], zorder = 102)

        elif cmove.get_type() == 3:
            pass

    #highlighting allied grid
    def ally_highlighter(unit, cmove, row, column):
        if cmove.get_type == 2:
            renpy.show("tile_f_hovered", at_list=[a_tile_hover(row, column-1)], zorder = 102)

        elif cmove.get_type() == 3:
            pass


    def hide_highlighter():
        renpy.hide("tile_hovered")

    def unit_pass(unit):
        unit.set_able(unit.get_able()-1)
        unit.set_stamina(min(unit.get_stamina()+10, unit.get_staminamax()))















##eof
