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
## -- main cast -- ##
define mc = Character("Me", color=purple, what_color= lightpurple, what_font= tv_font, what_prefix='"', what_suffix='"') #mc. handler
define f = Character("Friday", color = temp, what_color=temp, what_prefix='"', what_suffix='"', slow_cps_multiplier = 1.2,) #friday. op.

define y = Character("Yvette", color = purple, what_color= lightpurple, what_prefix='"', what_suffix='"') #yve. op.
define p = Character("Payton", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #payton. yve's handler.


define m = Character("Mueler", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #mueler. handler.
define t = Character("Tori", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #tori. floor direction/handler.

## -- other cast -- ##
define n = Character("Nai", color = temp, what_color=paleyellow, what_prefix='"', what_suffix='"') #nai. geologist.
define i = Character("Iris", color = purple, what_color= lightpurple, what_prefix='"', what_suffix='"') #iris. technician/crafting.

## -- interface voices -- ##
define c = Character("Control", color = temp, what_color=temp, what_prefix='--')#, what_suffix='--') #osgood. mission control.


#names?
#metz
#forest/barrett
#iri/iris
#kina/kinna










#eof
