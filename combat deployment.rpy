# here is the junk for the deployment screen:

screen deploy_screen(deployer, party_list):

    if deployer.get_dc() > 0 and deployer.get_dc() <= deployer.get_dm():
        button:
            xalign 0.5 yalign 0.05
            text "Deploy Team ({}/{} selected)".format(deployer.get_dc(), deployer.get_dm())
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

        for unit in party_list:
            if unit.get_deployable() == 1:
                imagebutton:
                    idle unit.get_face()
                    hover unit.get_face_h()
                    action Function(deployer.deploy_unit, unit) hovered Function(deployer.browse, unit) unhovered Hide("deploy_browse")


screen choose_deploy_loc(player_list):
    #select which unit to order from available units that have yet to act. returns rank of unit.

    for y in range(0, 5): #column
        for x in range(0, 5): #row
            for j in range(0, len(player_list)): #make sure spot is empty
                if player_list[j].get_point().get_x() == x and player_list[j].get_point().get_y() == y:
                    pass
                else:
                    button:
                        pos(340 + x*120, 135 + y*65)
                        text "([x],[y])"
                        action Return(value = (x,y))
            if len(player_list) == 0:
                button:
                    pos(340 + x*120, 135 + y*65)
                    text "([x],[y])"
                    action Return(value = (x,y))

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
        def __init__(self, deploymax, party):
            self.deploycounter = 0
            self.deploymax = deploymax
            self.party = party #list of all units that can be sent into battle
            self.player = [] #list of units being sent into battle

            ##load up the last deployed crew

        #setters
        def set_dc(self, dc):
            self.deploycounter = dc
        def set_dm(self, dm):
            self.deploycounter = dm
        def set_player(self, hold):
            self.player = hold
        #getters
        def get_dc(self):
            return self.deploycounter
        def get_dm(self):
            return self.deploymax
        def get_party(self):
            return self.party
        def get_player(self):
            return self.player


        #actually handle deployment
        def browse(self, unit):
            renpy.show_screen("deploy_browse", unit)


        def remember_deployment(self, hold, xlist, ylist):
            if not hold:
                pass
            else:
                for x in range(0, len(hold)):
                    if x == self.get_dm():
                        break
                    if hold[x].get_ooa() == 0:
                        hold[x].set_deployable(0)
                        hold[x].get_point().set_x(xlist[x])
                        hold[x].get_point().set_y(ylist[x])

                        self.get_player().append(hold[x])
                        self.set_dc(self.get_dc()+1)

            self.deploy()

        def deploy(self):
            renpy.show("deployfield0")
            for unit in self.get_player():
                renpy.show(unit.icon, at_list=[deploypos(320 + unit.get_point().get_x() * 120, 135 + unit.get_point().get_y() * 65)])

            renpy.call_screen("deploy_screen", self, self.get_party())

        def deploy_unit(self, unit):
            if self.get_dc() < self.get_dm():
                unit.set_deployable(0)

                #call screen that places unit on the map, and set point.x, point.y accordingly
                dtuple = renpy.invoke_in_new_context(self.select_deploy_loc)
                unit.get_point().set_x(dtuple[0])
                unit.get_point().set_y(dtuple[1])

                self.get_player().append(unit)

                renpy.show(self.get_player()[self.get_dc()].icon, at_list=[deploypos(320 + unit.get_point().get_x() * 120, 135 + unit.get_point().get_y() * 65)])
            else:
                renpy.notify("You've already deployed the maximum number of units.")

            renpy.hide_screen("deploy_browse")
            self.set_dc(self.get_dc() + 1)
            return

        def reset_deployment(self):
            self.set_dc(0)
            for i in range(0, len(self.get_player())):
                self.get_player()[i].set_deployable(1)
                renpy.hide(self.get_player()[i].icon)
            del self.get_player()[:]


        def select_deploy_loc(self):
            dtuple = renpy.call_screen("choose_deploy_loc", self.get_player())
            return dtuple












































##eof
