


#purely combat test
label map00:
    #return

    #battle test
    python:
        yve = Unit_yve()
        yve.get_point().set_x(0)
        yve.get_point().set_y(3)

        fed = Unit_federal()
        fed.get_point().set_x(4)
        fed.get_point().set_y(2)

        aide = Unit_aide()
        aide.get_point().set_x(4)
        aide.get_point().set_y(3)


        boy = Unit_boy()
        boy.get_point().set_x(4)
        boy.get_point().set_y(4)

        party = [yve, boy, fed, aide]
        pl = [yve, fed, aide]#, boy]

        baddie0 = Unit_groskel(0, "groskel", (1, 1), 1)
        #baddie1 = Unit_jowler(0, "jowler", (0, 3), 1)
        #baddie2 = Unit_jowler(0, "jowler 2", (3, 4), 1)
        el = [baddie0]#, baddie1, baddie2]


        battle0 = Battle(-1, party, pl, el, "battlefield0")

        battle0.combat_round()

    return

#overworld screen
label map0:

    #return
    python:
        #overworld map test
        ow = Overworld()

        yve = Unit_yve()
        ow.join_party(yve)

        boy = Unit_boy()
        ow.join_party(boy)

        #put some armours in the inventory
        piece1 = Folding_armour()
        ow.get_inventory().add_gear(piece1)

        piece2 = Bascule_armour()
        ow.get_inventory().add_gear(piece2)

        wep1 = Folding_spear()
        ow.get_inventory().add_gear(wep1)

        ow.show_overworld()

    return

































##eof
