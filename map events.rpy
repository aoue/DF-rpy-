#three types of events:
#red: advance story line. required.
#blue: just talking and rel. skip if you really want to.
#green: you get moves/something out of this. skip at your own peril.


##----- Technical -----##

label music_save: #saves the music that was playing outside. starts playing it again afterwards.
    $songname = renpy.music.get_playing(channel="music")
    stop music
    "[[...]"
    play music songname #play the song that was playing before the call.

label fail:
    "map jump failed."
    return


##----- Prologue -----##








##----- Chapter I -----##
##----- Chapter II -----##
##----- Chapter III -----##
##----- Chapter IV -----##
##----- Chapter V -----##
##----- Chapter VI -----##
##----- Chapter VII -----##


































##eof
