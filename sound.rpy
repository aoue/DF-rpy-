##for music and sounds
#using musescore3 for composing
#scores saved in C:\Users\aaja\Documents\MuseScore3\Scores
#using ogg

#https://www.renpy.org/doc/html/audio.html      for reference


#renpy.music.register_channel(sec)

#------------------------------
#channels:
init python:
    renpy.music.register_channel("sec", mixer="primixer", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    songname = ""

#-----------------------------------
#FAQ:
#$renpy.music.set_pause(1, channel="music")  <- pauses
#$renpy.music.set_pause(0, channel="music")  <- unpauses
#captures songname and then plays it in the second statement
#$songname = renpy.music.get_playing(channel="music")
#play music songname

#------------------------------
#planned tracks:
#define opening0 = "music/opening0.ogg"          #main menu track for the prologue only
#define roaring = "music/roaring.mp3"

#-------------------------------


#-------------------------------
#existing tracks:
define opening0 = "music/opening0.ogg"          #main menu track. temp
#define alarm0 = "music/alarm0.ogg"              #mc's alarm.


#-----------------------------------
#sounds:
#these must all be cleansed and re-crafted from scratch








































##eof













#h
