


#purely combat test
label map0:
    #return

    #battle test

    python:
        LEVELCAP = 10
        yve = Unit_yve()
        yve.get_point().set_x(0)
        yve.get_point().set_y(3)

        friday = Unit_friday()
        friday.get_point().set_x(4)
        friday.get_point().set_y(3)


        party = [friday, yve]
        pl = [friday, yve]

        #baddie0 = Unit_groskel(0, "groskel", (1, 1), 1)
        baddie1 = Unit_jowler(0, "jowler", (0, 3), 1)
        baddie2 = Unit_jowler(0, "jowler 2", (3, 4), 1)
        baddie3 = Unit_jowler(0, "jowler", (2, 1), 1)
        el = [baddie1, baddie2, baddie3]

        inven = Inventory()

        battle0 = Battle(-1, party, pl, el, "battlefield0", inven)

        battle0.combat_round()

    return


































##eof
