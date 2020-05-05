# here is the junk for the deployment screen:

screen deploy_screen(deployer):
    if deployer.get_dc() > 0 and deployer.get_dc() <= deployer.get_dm():
        button:
            xalign 0.5 yalign 0.05
            text "Deploy Team ({} selected)".format(deployer.get_dc())
            action Return()
        button:
            xalign 0.5
            yalign 0.1
            text "Reset"
            action Function(deployer.reset_deployment)

    vpgrid:
        rows 1
        draggable True
        mousewheel True
        scrollbars "horizontal"
        xalign 0
        yalign 1.0
        spacing 15

        if mc_d.get_deployable() == 1: #mc
            imagebutton:
                idle "combat/face/deploy mc.png"
                hover "combat/face/deploy mc hover.png"
                action Function(deployer.deploy_unit, mc_d) hovered Function(deployer.browse, mc_d) unhovered Hide("deploy_browse")
        if yve_d.get_deployable() == 1: #yve
            imagebutton:
                idle "combat/face/deploy yve.png"
                hover "combat/face/deploy yve hover.png"
                action Function(deployer.deploy_unit, yve_d) hovered Function(deployer.browse, yve_d) unhovered Hide("deploy_browse")

screen choose_deploy_loc():
    #select which unit to order from available units that have yet to act. returns rank of unit.

    for x in range(0, 5): #column
        for i in range(0, 5): #row
            for j in range(0, len(playerlist)): #make sure spot is empty
                if playerlist[j].get_point().get_x() != x or playerlist[j].get_point().get_y() != i:
                    button:
                        pos(340 + i*120, 135 + x*65)
                        text "([i],[x])"
                        action Return(value = (i,x))
            if len(playerlist) == 0:
                button:
                    pos(340 + i*120, 135 + x*65)
                    text "([i],[x])"
                    action Return(value = (i,x))

#unit overview. one screen fits all.
screen deploy_browse(unit):
    frame: #obviously all the positioning aspects will have to be perfected.
        background Solid("#0000007F") # for transparency. colour = rrggbbaa where red green blue alpha
        area(600, 50, 500, 600)
        ypadding 5
        xpadding 10

        vbox:
            text unit.get_name()
            text "HP = " + str(unit.get_hp())
            text "EXP = " + str(unit.get_exp())
            text "moves, focus, whatever, etc{p}what the character has to say about the upcoming battle?"

            #text "Moves:"
            #for i in range(0, 6):
            #    text " -" + unit.get_flavour(i)
            #if unit.get_evo() == 1:
            #    text " -" + unit.get_flavour(6)


init python:
    #each pilot's unlock status initialization:
    class deployment():
        def __init__(self, deploymax):
            self.deploycounter = 0
            self.deploymax = deploymax
        #setters
        def set_dc(self, dc):
            self.deploycounter = dc
        def set_dm(self, dm):
            self.deploycounter = dm

        #getters
        def get_dc(self):
            return self.deploycounter
        def get_dm(self):
            return self.deploymax

        #actually handle deployment
        def browse(self, unit):
            renpy.show_screen("deploy_browse", unit)

        def deploy_unit(self, unit):
            if self.get_dc() < self.get_dm():
                unit.set_deployable(0)

                #call screen that places unit on the map, and set point.x, point.y accordingly
                dtuple = renpy.invoke_in_new_context(self.select_deploy_loc)
                #dtuple = renpy.invoke_in_new_context("choose_deploy_loc") #TODO unicode object is not callable, which means you're treating a string as if it were a function.
                unit.point.set_x(dtuple[0])
                unit.point.set_y(dtuple[1])

                playerlist.append(unit)
                renpy.show(playerlist[self.get_dc()].icon, at_list=[deploypos(320 + unit.get_point().get_x() * 120, 135 + unit.get_point().get_y() * 65)])
            else:
                renpy.notify("You've already deployed the maximum number of units.")

            renpy.hide_screen("deploy_browse")
            self.set_dc(self.get_dc() + 1)
            return

        def reset_deployment(self):
            self.set_dc(0)
            for i in range(0, len(playerlist)):
                playerlist[i].set_deployable(1)
                renpy.hide(playerlist[i].icon)
            del playerlist[:]


        def select_deploy_loc(self):
            dtuple = renpy.call_screen("choose_deploy_loc")
            return dtuple












































##eof
