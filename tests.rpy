label battle0:
    #this is a scripted event

    #do any deployment enabling/disabling
    python:
        #initialize all the units and helperss


        boy_d = unit_boy()
        yve_d = unit_yve()
        party_list = [boy_d, yve_d] #all units that are part of the party


        baddie = unit_grunt(0, "vile grunt", 2, 0)
        baddie2 = unit_grunt(0, "horrid grunt", 2, 2)

        allow_save = False
        enemy_list = [baddie, baddie2]
        player_list = [] #list of units being sent into battle

        deployer = deployment(5)

        battle0 = battle(5, playerlist, enemy_list, "battlefield0")


    scene image "combat/bg/deployfield0.jpg"
    call screen deploy_screen(deployer)

    "deployment finished. Fight!" #test

    #battle test
    python:
        battle0.combat_round()
        allow_save = True

    # -del playerlist[:] #deletes all contents. we'll fill it back up for the next fight
    # -adjust displaying things

    return
