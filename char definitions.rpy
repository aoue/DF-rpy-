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

define paleyellow = '#c58e00' #TODO its too light
define yellow = '#917223'


define purple = '#8e21d4'
define lightpurple = '#974de0'

define temp = '#eddff7'

#template
#define templateCharacter = Character("Name", what_font = f.names, what_size = 26, what_prefix='"', what_suffix='"')

#here's how to use a different textbox (example):
# define e = Character("Eileen") define n = Character("Narrator", window_background="gui/textbox2.png")
init python:
    yve_name = "Yve" #can be yve or yvette. only in mc's thoughts, though he may let it slip.
    u_name = "?" #unknown name. change it to man's voice, or woman's voice, or ?, or whatever as the situation arises.
    r1_name = "rando"
    r2_name = "r2ndo"


####### CHARACTERS ########
define inarrator = Character(None, what_color=iceblue) #[i]cy narrator: displays non-dialogue text in '#79d4e7' it's an icy blue. for cold or snow.

define u = Character("u_name", dynamic=True, color = blue, what_color=iceblue, what_prefix='"', what_suffix='"') #unknown char.
define r1 = Character("r1_name", dynamic=True, color = blue, what_color=iceblue, what_prefix='"', what_suffix='"') #a rando
define r2 = Character("r2_name", dynamic=True, color = blue, what_color=iceblue, what_prefix='"', what_suffix='"') #another rando

define mc = Character("Me", color = blue, what_color=iceblue, what_prefix='"', what_suffix='"') #mc.

define n = Character("Nai", color = yellow, what_color=paleyellow, what_prefix='"', what_suffix='"') #nai, mc's oldest friend. nai = not, also osaNAIjimi

define y = Character("yve_name", dynamic=True, color = purple, what_color= lightpurple, what_prefix='"', what_suffix='"') #yve(tte), a friend to both mc and nai. dynamic because mc can choose to think of her as Yvette.

define d = Character(None, window_background="images/textboxes/textbox_test.png", color = temp, what_color=temp, what_prefix='"', what_suffix='"', slow_cps_multiplier = 1.2,) #dg #dee-gee, initials. first name dominique? fits the french theme at any rate.

define a = Character("Anne", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Anne, mc's older sister. ane = sister

define t = Character("Tori") #Tori, act II squad 2 captain. tori(kago) = birdcage. tori could be short for victoria

define e = Character("Emery", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Emery, works at the cafe. native to Larisse. Yve's known him from childhood.

define g = Character("Professor G.", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Hanna Gottschalk, professor of history.

define m = Character("Prof M.", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Professor M, professor of citizenship. Something of a revolutionary.

define f = Character("Professor F.", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Professor F, professor of geography.

define m2 = Character("Gladys", color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Gladys. Professor M's wife who is also in his class. name colour and text colour should be an inversion of prof m's.


####### NVL CHARACTERS ########
#--maybe it's better to have no names here, it should be obvious who's talking.

define gl = Character("Professor G.", type=nvl, color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Hanna Gottschalk, professor of history. lecture mode.

define ml = Character("Professor M.", type=nvl, color = temp, what_color=temp, what_prefix='"', what_suffix='"') #prof m, professor of citizenship. lecture mode.

define fl = Character("Professor F.", type=nvl, color = temp, what_color=temp, what_prefix='"', what_suffix='"') #Professor F, professor of geography. Lecture mode.

#agenda
define ag = Character(None, type=nvl, what_text_align=1.0, color=black, what_layout='subtitle', what_font = agenda_font)

####### TV ########
#their text size needs to be bigger
define tv = Character("TV Host", color = temp, what_color = temp, what_prefix = '"', what_suffix = '"', what_font = tv_font)
define lc = Character("Lord-Chairman", color = temp, what_color = temp, what_prefix = '"', what_suffix = '"', what_font = tv_font)
define as = Character("Advisor-Secretary", color = temp, what_color = temp, what_prefix = '"', what_suffix = '"', what_font = tv_font)
define hs = Character("Historian-General", color = temp, what_color = temp, what_prefix = '"', what_suffix = '"')

#----------------------------------------------#
#if you need to mess around with display, do it here.
#side images? I don't think so. mc should only be shown with blood on his hands.
