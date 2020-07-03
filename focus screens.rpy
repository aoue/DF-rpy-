
#-level up screen: shows stat increases and any moves learned. if it's a choose your focus level-up. then do a very dramatic picture (press a to grab destiny) with buttons, one for each focus. "unit name stands at a crossroads."
#    -when a focus is chosen, unlock a flashback for that character's backstory that can be viewed back at the hub next time you talk to that character. one flashback per focus per time chosen. the flashback has to do with the focus, obviously.
#    -it should be clear that a focus influences story, in the way that the character responds.


screen level_up(showlist, showlist2):
    #shown after a battle. shows all the exp gained for all units. if they leveled up, shows. if they learned a new move, shows that too.
    #format. showlist:
    # -[0]: unit. the unit. someone nice, I hope.
    # -[1]: unit's learned move, or -1 if no new move was learned.
    # -[2]: did unit level up? 1: yes, 0: no
    # -[3]: is it a level where the unit gets to change focus (and the unit leveled up)? 1: yes, 0: no
    # -[4]: old exp. the exp the unit had before the battle.

    #showlist 2:
    # -[0]: int. money gained.
    # else: new gear/item/mat object gained.

    zorder 100

    #modal True

    add "level_up_bg"

    text "Level cap = " + str(LEVELCAP) pos (1000, 25)
    text "Threat level increased." pos (1000, 50)

    for i in range(0, len(showlist)): #exp
        vbox:
            pos (200, 150 * i)

            text showlist[i][0].get_name()

            if showlist[i][2] == 1: #if the unit leveled up
                text "Level: " + str(showlist[i][0].get_lvl()-1) + " --> " + str(showlist[i][0].get_lvl()) + "(level up)"
            else:
                text str(showlist[i][0].get_lvl()) + " --> " + str(showlist[i][0].get_lvl())

            text "Exp: " + str(showlist[i][4]) + " --> " + str(showlist[i][0].get_exp()) + " / " + str(showlist[i][0].get_next_level_exp())


            if showlist[i][1] != -1:
                text "--learned: " + showlist[i][1].get_title()
            #else:
            #    text "--learned: no new moves"

    vbox:
        pos (800, 100)

        text "Gained [[" + str(showlist2[0]) + "] money."

        for i in range(1, len(showlist2)):
            text "Gained [[" + showlist2[i].get_title() + "]"
            #elif i == 10:
            #    text "And more"
            #else:
            #    pass





    #pick new focus
    #if unit.get_lvl() % 10 == 0:
    #    add "focus_up_bg"
    #    text unit.get_focus().get_title() + " =>" size 25 pos (600, 300)
    #    vbox:
    #        spacing 5
    #        for foc in unit.get_focuslist():
    #            textbutton foc.get_title() action Function(unit.set_focus, foc) #hovered, show screen focus_view
    #else:
    #    textbutton unit.get_focus().get_title() action Nullaction() #hovered, show screen focus_view
init python:
    def show_exp_view(exp, i):
        renpy.show_screen("exp_view", exp, i)

screen exp_view(exp, i):
    zorder 101
    text str(exp) pos (400, 200*i)


screen focus_view(foc):
    #indepth view of a focus. how it affects stats on the general, what moves will be unlocked before the unit has reachs the next focus branch. the player can see ahead, but not all the way ahead.
    pass





init:
    image level_up_bg:
        pass
    image focus_up_bg:
        pass



















##eof
