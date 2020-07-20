


#purely combat test
label map0:
    #return

    #battle test
    python:
        yve = Unit_yve()
        yve.get_point().set_x(2)
        yve.get_point().set_y(2)

        party = [yve]
        pl = [yve]

        #baddie0 = Unit_groskel(0, "groskel", (1, 1), 1)
        baddie1 = Unit_jowler(0, "jowler", (0, 3), 1)
        #baddie2 = Unit_jowler(0, "jowler 2", (3, 4), 1)
        el = [baddie1]#, baddie1, baddie2]

        inven = Inventory()

        battle0 = Battle(-1, party, pl, el, "battlefield0", inven)

        battle0.combat_round()

    return


































##eof
