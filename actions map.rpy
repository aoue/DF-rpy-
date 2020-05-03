#method:
#show the image, there are character's icons on the map with two colours. white: no time passes, blue: advance time.

#three variants:
#act I: the town
#-university
#-anne's apt
#-dorms
#-icerink
#-azalea fields
#-streets
#-cafes: there are actually two cafes, but they look exactly the same inside. Mc hasn't noticed there are actually two. At the cafe: Emery talks. 'i'm my own person you know. yvette thinks she knows everything.'
#-

#act II: LaBlache
#act III: wherever on the road they happen to be.

#map nav for act I.
#here's how it works:
#-- when the screen is called, it is given arguments. These are:
#-first arg: list of booleans that determine whether a location is unlocked.
#-second arg: list of str label names that should be jumped to. paired one-to-one with first list.
#update the lists with each call.

#-----ACT I index-----#
#a certain item in the list always corresponds to the same physical location. It is as follows:
# [0] = apartment
# [1] = cafe(s)
# [2] = library
# [3] = dorms
# [4] = (azalea) field
# [5] = (no) street (in particular)
# [6] =
# [7] =
# etc

init python:
    #expand lists as needed
    map_unlocks = [False, False, False, False, False]
    #map_unlocks = [True, True, True, True] #<--- for testing purposes
    map_jumps = ["fail", "fail", "fail", "fail", "fail"]
    map_descriptions = ["example", "example", "example", "example", "example"]

    #^descriptions should stay the same. Everything else will change basically every jump. What a pain.
label fail:
    "map jump failed."
    return

screen example:
    add("map/icon_hover.png") #at mousepos??

    # ^doesnt display in the correct spot. fix this. maybe pass in coordinates or something?
    # OR display screen for each different position


screen map_nav_town(mu, mj, md):
    imagemap:
        ground "map/town map.jpg"
        hover

        #anne's apartment
        if mu[0] == True:
            hotspot (170, 78, 343, 213) hovered Show(md[1]) unhovered Hide(md[0]) action Jump(map_jumps[0])

        #cafe
        if mu[1] == True:
            hotspot (800, 205, 360, 220) action Jump(map_jumps[1])

        #library
        if mu[2] == True:
            pass

        if mu[3] == True:
            pass

        if mu[4] == True:
            pass

        #etc

# below: this label has nothing to do with the map, just don't want to lose it.
label music_save:
    $songname = renpy.music.get_playing(channel="music")
    stop music
    play music songname #play the song that was playing before the call.










##eof
