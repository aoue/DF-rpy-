### special actions function

#when the mouse enters specified area, special_actions_screen shows up
screen special_actions_overlay:
    zorder 99
    mousearea:
        area(0, 0, 0.5, 45)#dimensions
        hovered Show("special_actions_screen", transition = dissolve)
        unhovered Hide("special_actions_screen", transition = dissolve)

screen special_actions_screen:
    zorder 100
    window id "special_actions_window":
        at topright
        # place the window on the right of the screen
        hbox yalign 0.1:
            spacing 5

            if agenda_unlocked == True:
                imagebutton:
                    idle "agenda/icon.png"
                    hover "agenda/icon_hover.png"
                    action Function(renpy.call, label="open_agenda")
                    tooltip "Agenda"
            if phone_unlocked == True:
                imagebutton:
                    idle "phone/icon.png"
                    hover "phone/icon_hover.png"
                    action Function(renpy.call, label="phone_call")
                    tooltip "Phone"
            #if watch_unlocked == True: #TODO

            if glossary_unlocked == True:
                imagebutton:
                    idle "glossary/icon.png"
                    hover "glossary/icon_hover.png"
                    action Function(renpy.call, label="glossary_call")
                    tooltip "Glossary"

            $ tooltip = GetTooltip()
            if tooltip:
                text "[tooltip]"
#-------------------------------------------------------------


#-------------------------------------------------------------

init python:
    #whether an action is accessible or not
    ##NOTE ;all are true now for testing purposes
    glossary_unlocked = True #unlocked from the beginning, but empty. fills up as progress is made.
    watch_unlocked = True #important. check the tacit plan for symbolism.
    agenda_unlocked = True
    phone_unlocked = True


    #phone
    real_emergency = 0 #0 for not, 1 for is a real emergency. true lets mc call 911.
    phone_counter = 0
    result = 0
    keys = []
    n_dis = " "

    #agenda
    date = 0
    dis_date = 0 #dis_date = display date, used for agenda
    push_dir = 0 #1 = next, 2 = prev
    monthname = "Undim" #will be changed to the next month name on the appropriate date.
    dayname = "Seventhday" #changed each day

    #glossary
    last_entry = "" #loads glossary with the last viewed entry already shown. its a screen's name. starts empty to cause trigger pass









##eof
