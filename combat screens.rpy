

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

screen show_units(pl, el):
    for i in range(0, len(pl)):
        add pl[i].get_icon() pos(275 + 125*pl[i].get_point().get_x(), 385 + 65*pl[i].get_point().get_y())

    for i in range(0, len(el)):
        add el[i].get_icon() pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())
        text el[i].get_name() pos(275 + 125*el[i].get_point().get_x(), 5 + 65*el[i].get_point().get_y())

screen order_unit(pl):
    #select which unit to order from available units that have yet to act. returns rank of unit.
    for i in range (0, len(pl)):
        if pl[i].get_able() == 1:
            button:
                pos(275 + 125*pl[i].get_point().get_x(), 385 + 65*pl[i].get_point().get_y())
                text pl[i].get_name()
                action Return(pl[i])


screen pick_move(unit):
    #show moves. top left of box is 900, 175

    #TODO. show move descrition/image on hover.

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
                    textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y()), Return

                elif (unit.get_point().get_y() in range(3, 5)) and unit.get_moves()[i].get_rank() == 2:
                    textbutton unit.get_moves()[i].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y()), Return

            if unit.get_evo() == 1:
                textbutton unit.get_moves()[7].get_title() action Function(unit.use_move, unit.get_moves()[i], unit.get_point().get_x(), unit.get_point().get_y()), Return

            textbutton "Pass" action Return


screen enemy_highlight(unit):
    #highlight some squares on enemy board relative to mouse pos and borders of the grid.
    #when clicked, make a list of every affected square, and return it.
    #if unit.get_displayhelper() == 1: enum

    #$checkEvent()
    #text "{}".format(store.mousePosition) #TODO
    zorder 100 #for some reason, every unit is

    #x = unit.get_point().

    for column in range(0, 5): #column
        for row in range(0, 5): #row
            #if spot is empty, then:
            imagebutton:
                idle "images/combat/fx/tile.png"
                hover "images/combat/fx/tile hover.png"
                pos(275 + row*125, 5 + column*65)
                action Return((row, column)) hovered Function(enemy_highlighter, unit, row, column) #unhovered Function(hide_highlighter)

                #return tuple of top left corner


#------ally side positions------#
#px: 275 + 125*(point.get_x()), , 385 + 65*(point.get_y())

#------enemy side positions------#
#px: 275 + 125*(point.get_x()), , 5 + 65*(point.get_y())



init python:

    #stuff to fix. Should probably step through the programming necessary.
    # -shows some areas out of bounds.
    # -some other strange stuff.
    # -is not highlighting the multi target areas like i want it to.

    def enemy_highlighter(unit, row, column):
        renpy.hide("tile_hovered")
        #if unit.get_moves()[row].get_type() == 0:
            #renpy.show("tile_hovered", at_list=[tile_hover(row, column)])
        #    pass
        if unit.get_moves()[row].get_type() == 1:
            renpy.show("tile_hovered", at_list=[tile_hover(row, column-1)])

        #if 2:

        #etc

    def hide_highlighter():
        renpy.hide("tile_hovered")



    #(x,y) are the grid coordinates of the highlighted square. the type tells you what other squares should be highlighted as well, so long as they don't exceed the edges.

screen ally_highlight(unit):
    #highlight some squares on allied board relative to mouse pos and borders of the grid.
    #when clicked, make a list of every affected square, and return it.

    pass

screen pick_target_area(type):
    #type: the type of target area.
    # 1: single
    # 2: horizontal pair
    # 3: horizontal trio
    # 4: horizontal quartet
    # 5: horizontal line

    # 5: vertical pair
    # 6: vertical trio
    # 7: vertical quarter
    # 8: vertical line

    # 9: 2x2 box
    # 10: 3x3 box
    # 11: 2x3 box
    # 12: 3x2 box

    # 13: 5x5 cross

    #method:
    #wherever the mouse is part of the shape. the rest of the shape is highlighted on squares for the player's benefit.
    pass


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
            text "{}'s hp = {} ({}) [[{}]".format(pl[i].get_name(), str(pl[i].get_hp()), str(pl[i].get_dodge()), pl[i].get_able())
    vbox:
        xalign 1.0
        yalign 0.9
        spacing 2
        for i in range(0, len(el)):
            text "{}'s hp = {} ({}) [[{}]".format(el[i].get_name(), str(el[i].get_hp()), str(el[i].get_dodge()), el[i].get_able())








##eof
