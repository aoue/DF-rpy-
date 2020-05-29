
#map0 is run as a test


#purely combat
label map00:


    #battle test
    python:
        yve = unit_yve()
        yve.get_point().set_x(1)
        yve.get_point().set_y(1)

        fed = unit_federal()
        fed.get_point().set_x(3)
        fed.get_point().set_y(1)

        aide = unit_aide()
        aide.get_point().set_x(2)
        aide.get_point().set_y(2)


        #boy = unit_boy()
        #boy.get_point().set_x(4)
        #boy.get_point().set_y(4)


        pl = [yve, fed, aide]#, boy]

        baddie0 = unit_groskel(0, "groskel", (1, 1))
        #baddie1 = unit_jowler(0, "jowler", (0, 3), 1)
        #baddie2 = unit_jowler(0, "jowler 2", (3, 4), 1)
        el = [baddie0]#, baddie1, baddie2]

        battle0 = battle(-1, pl, el, "battlefield0")
        battle0.combat_round()

    return

#overworld screen
label map0:
    python:
        #overworld map test
        ow = overworld()

        yve = unit_yve()
        boy = unit_boy()
        ow.join_party(yve)
        ow.join_party(boy)

        #put some armours in the inventory
        piece1 = folding_armour()
        piece2 = bascule_armour()
        ow.get_inventory().add_gear(piece1)
        ow.get_inventory().add_gear(piece2)

        wep1 = folding_spear()
        ow.get_inventory().add_gear(wep1)

        ow.show_overworld()

    return

































##eof
