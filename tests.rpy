label battle0:
    #this is a scripted event

    #do any deployment enabling/disabling
    python:
        allow_save = False
        enemylist = [baddie, baddie2]

        deployer = deployment(2)

        battle0 = battle(5, playerlist, enemylist, "battlefield0")


    scene image "combat/bg/deployfield0.jpg"
    call screen deploy_screen(deployer)

    "deployment finished. Fight!" #test

    #battle test
    python:
        battle0.combat_round()
        allow_save = True

    #afterwards:
    # -del playerlist[:] #deletes all contents. we'll fill it back up for the next fight
    # -fix display issues, if any.

    return
