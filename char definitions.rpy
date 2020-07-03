#three letter names are preferred

#fonts
define names_font = "fonts/AmaticSC-Bold.ttf" #name font is defined in gui.rpy
define agenda_font = "fonts/DancingScriptRegular.ttf"
define tv_font = "fonts/CuteFont-Regular.ttf"

# Colours
#A character's name is one colour and their text is a different shade of that
define black = '#000000'
define white = '#FFFFFF'
define blue = '#6666FF'
define iceblue = '#93DCEB'
define paleyellow = '#c58e00'
define yellow = '#917223'
define purple = '#8e21d4'
define lightpurple = '#974de0'
define temp = '#eddff7'


#here's how to use a different textbox: ' window_background="gui/image.png" '  as one of the character's properties


####### CHARACTERS ########
#main cast
define b = Character("Me", color = blue, what_color=iceblue, what_prefix='"', what_suffix='"') #boy
define y = Character("Yvette", color = purple, what_color= lightpurple, what_prefix='"', what_suffix='"') #yve
define n = Character("Nai", color = yellow, what_color=paleyellow, what_prefix='"', what_suffix='"') #nai
define m = Character("Mechanical Girl", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #mechanical girl
define d = Character("Dg.", color = temp, what_color=temp, what_prefix='"', what_suffix='"', slow_cps_multiplier = 1.2,) #dg/dominique
define t = Character("Tori", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #tori/victoria
define o = Character("Osgood", color = temp, what_color=temp, what_prefix='"', what_suffix='"')
define a = Character("Artificer", color = purple, what_color= lightpurple, what_prefix='"', what_suffix='"') #the artificer

#secondary characters
define h = Character("Anima", color=purple, what_color= lightpurple, what_font= tv_font, what_prefix='<', what_suffix='>') #yve's handler.
