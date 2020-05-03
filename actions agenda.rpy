#agenda labels are all in here
#all you can do with these is look at what's coming up. update the agenda based on mc's choices or plans he made.
#
#mc's school schedule:
#mon           tues               wed               thurs             fri
#phil: 1-3.30  comp: 7.30-8.30    comp: 7.30-8.30   comp: 7.30-8.30   comp: 7.30-8.30
#              ethics: 9-11.30    phil: 10-12.30    ethics: 9-11.30
#
###add other people's schedules. nai, yve, and dg all need school schedules. i guess profg does too
#ane needs work schedule



####add an event that calls up the agenda of the current day and that of the next at the end of a day.

#don't forget the passenger could leave notes in the agenda?
#any label with _s afterwards refers to a special label that is called for an event and is not callable by the player.

#NOTE
#𝒯𝒽𝒾𝓈 𝒾𝓈 𝒶 𝓃𝑜𝓉𝑒
#^neat handwriting font. find it at https://coolsymbol.com/cool-fancy-text-generator.html

#NOTE

#upon opening agenda: opens to current date.
#-buttons:
#-next day, prev day, monthly view
#from monthly view: close button.
#player can go all the way to the end of the year.


screen agenda_month_nav:
    zorder 100
    imagemap:
        ground "agenda/month.png"
        hover "agenda/month.png"

        #1 hotspot, close agenda
        #hotspot (45, 90, 140, 105) action Hide("agenda_month_nav", transition=fade)
        hotspot (45, 90, 140, 105) action Call("agenda_close")

        #9 hotspots, 22nd through 30th
        hotspot (190, 400, 140, 105) action Call("nov22")
        hotspot (335, 400, 140, 105) action Call("nov23")
        hotspot (480, 400, 140, 105) action Call("nov24")
        hotspot (625, 400, 140, 105) action Call("nov25")
        hotspot (770, 400, 140, 105) action Call("nov26")
        hotspot (915, 400, 140, 105) action Call("nov27")
        hotspot (045, 505, 140, 105) action Call("nov28")
        hotspot (190, 505, 140, 105) action Call("nov29")
        hotspot (335, 505, 140, 105) action Call("nov30")

screen agenda_box:
    imagemap:
        ground "agenda/agenda box.png"
        hover "agenda/agenda box.png"
        hotspot (325, 0, 320, 160) action Call("agenda_next")
        hotspot (325, 165, 320, 165) action Call("agenda_prev")
        hotspot (325, 320, 320, 155) action Call("agenda_back")

label agenda_close:
    nvl clear
    hide screen agenda_month_nav with fade
    return
#opens first
label open_agenda:
    hide screen special_actions_overlay
    $ dis_date = date
    $ checkedagenda = True
    show screen agenda_month_nav
    $ ui.interact()
    nvl clear
    show screen special_actions_overlay
    return

label agenda_next:
    nvl clear
    $ dis_date += 1
    #switch to jump to the label for the new dis_date
    if dis_date == 22:
        call nov22 from _call_nov22
    elif dis_date == 23:
        call nov23 from _call_nov23
    elif dis_date == 24:
        call nov24 from _call_nov24
    elif dis_date == 25:
        call nov25 from _call_nov25
    elif dis_date == 26:
        call nov26 from _call_nov26
    elif dis_date == 27:
        call nov27 from _call_nov27
    elif dis_date == 28:
        call nov28 from _call_nov28
    elif dis_date == 29:
        call nov29 from _call_nov29
    elif dis_date == 30:
        call nov30 from _call_nov30
    else:
        "out of bounds"
    hide screen agenda_box
    hide screen agenda_month_nav
    return

label agenda_prev:
    nvl clear
    $ dis_date -= 1
    #switch to jump to the label for the new dis_date
    if dis_date == 22:
        call nov22 from _call_nov22_1
    elif dis_date == 23:
        call nov23 from _call_nov23_1
    elif dis_date == 24:
        call nov24 from _call_nov24_1
    elif dis_date == 25:
        call nov25 from _call_nov25_1
    elif dis_date == 26:
        call nov26 from _call_nov26_1
    elif dis_date == 27:
        call nov27 from _call_nov27_1
    elif dis_date == 28:
        call nov28 from _call_nov28_1
    elif dis_date == 29:
        call nov29 from _call_nov29_1
    elif dis_date == 30:
        call nov30 from _call_nov30_1
    else:
        "Error, out of bounds"
    hide screen agenda_box
    hide screen agenda_month_nav
    return

label agenda_back:
    nvl clear
    hide screen agenda_box
    $ ui.interact()
    return

#labels for all the days below
label nov22:
    $ dis_date = 22
    show screen agenda_box
    call ag_mon from _call_ag_mon
    # "work from 23.00 - 07.-00" #TODO #strikethrough
    $ ui.interact()
    return

label nov23:
    $ dis_date = 23
    show screen agenda_box
    call ag_tue from _call_ag_tue

    #ag "{color=000000}Head to the cafe after school{/color}{fast}{nw}}"

    $ ui.interact()
    return

label nov24:
    $ dis_date = 24
    show screen agenda_box
    call ag_wed from _call_ag_wed
    $ ui.interact()
    return

label nov25:
    $ dis_date = 25
    show screen agenda_box
    call ag_thu from _call_ag_thu
    $ ui.interact()
    return

label nov26:
    $ dis_date = 26
    show screen agenda_box
    call ag_fri from _call_ag_fri
    $ ui.interact()
    return

label nov27:
    $ dis_date = 27
    show screen agenda_box
    call ag_sat from _call_ag_sat
    $ ui.interact()
    return

label nov28:
    $ dis_date = 28
    show screen agenda_box
    call ag_sun from _call_ag_sun
    $ ui.interact()
    return

label nov29:
    $ dis_date = 29
    show screen agenda_box
    call ag_mon from _call_ag_mon_1
    $ ui.interact()
    return

label nov30:
    $ dis_date = 30
    show screen agenda_box
    call ag_tue from _call_ag_tue_1
    $ ui.interact()
    return
#and so on. eventually there should be some if statements in there depending on the plans mc made.







#these labels are called very often, on the corresponding day, and ag_date displays the date.
label ag_date:
    ag "{color=000000}[dayname] [monthname] [dis_date], 1999{/color}{fast}{nw}"
    return
label ag_mon:
    call ag_date from _call_ag_date
    ag "{color=000000}philosophy: 1-3.30{/color}{fast}{nw}"

    return
label ag_tue:
    call ag_date from _call_ag_date_1
    ag "{color=000000}composition: 7.30-8.30{/color}{fast}{nw}"
    ag "{color=000000}ethics: 9-11.30{/color}{fast}{nw}"

    return
label ag_wed:
    call ag_date from _call_ag_date_2
    ag "{color=000000}composition: 7.30-8.30{/color}{fast}{nw}"
    ag "{color=000000}philosophy: 1-3.30{/color}{fast}{nw}"
    return
label ag_thu:
    call ag_date from _call_ag_date_3
    ag "{color=000000}composition: 7.30-8.30{/color}{fast}{nw}"
    ag "{color=000000}ethics: 9-11.30{/color}{fast}{nw}"
    return
label ag_fri:
    call ag_date from _call_ag_date_4
    ag "{color=000000}composition: 7.30-8.30{/color}{fast}{nw}"
    return
label ag_sat:
    call ag_date from _call_ag_date_5
    ag "{color=000000}laurem ipsum{/color}{fast}{nw}"
    return
label ag_sun:
    call ag_date from _call_ag_date_6
    ag "{color=000000}laurem ipsum{/color}{fast}{nw}"
    return





#
