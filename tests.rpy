label battle0:
    #this is a scripted event

    #do any deployment enabling/disabling
    python:
        mc_d = unit_mc()
        yve_d = unit_yve()
        playerlist = []

        baddie = unit_grunt(0, "vile grunt", 2, 1)
        baddie2 = unit_grunt(0, "very vile grunt", 2, 2)
        enemylist = [baddie, baddie2]

        deployer = deployment(2)

    scene image "combat/bg/deployfield0.jpg"
    call screen deploy_screen(deployer)

    "deployment finished. Fight!" #test

    #new battle test
    python:
        battle0 = battle(5, playerlist, enemylist, "battlefield0")
        battle0.combat_round()

    #afterwards:
    # -del playerlist[:] #deletes all contents. we'll fill it back up for the next fight
    # -fix display issues, if any.

    return
