

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

































##eof
