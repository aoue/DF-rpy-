#event labels for the prologue. divided by main/location.

label prologue_0:
    "prologue starts"

    centered "{w=1.0}\n11.00 PM"

    scene sasaches_lobby with longfade
    play music track0

    "A tall uniformed man steps out from the street into the lobby. There are guards stationed in the hallways and one at the base of the stairs. All's the better, we don't want to be interrupted."
    "An aide by the door falls into step with him."
    fe "She's here?"
    ai "Yes, sir. On the fourth floor, room 412."
    "The downside of this type of uniform is recognizing who's inside. He had no trouble with this type of thing when he was younger and hadn't had as many heads under him."
    fe "That's how these old buildings work. You should know that."
    ai "Yes, sir."
    fe "Fourth floor, huh? Tell me, there's an elevator around here, isn't there?"
    ai "No sir."
    fe "... What kind of building doesn't have an elevator."
    "The two men walk across the lobby to the stairs."

    scene sasaches_lobby_2 with shortfade

    "The aide at the stairs salutes as they approach."
    fe "Good man, stand down."

    scene sasaches_lobby_3 with dissolve

    extend " Surely you're not going to follow me all the way up?"
    ai "I haven't handed off control of the site to you yet, sir."
    fe "Well, what are you waiting for?"
    ai "Sir! You transfer command of the site to you, sir."
    fe "Yes, yes. Now, I can find my way to the room just fine, thank you. Room 416, yeah?"
    "The aide coughs politely."
    ai "Room 412, sir."
    fe "Right."
    "He steps up onto the first step and rests his hand on the banister."
    fe "Are the owner and staff being kept busy?"
    ai "Yes, sir. We're questioning them in the office."
    fe "No, that won't do. Move them into one of the rooms and resume. I don't need to tell you how important it is we control the flow of information here."
    "The aide heads down the hallway to the office."
    fe "... That's one. Now, how do I lose you, huh?"
    "He grins at the aide standing at the stairs. He can't see the man's face through the mask, but he imagines the man grins back."

    scene sasaches_stairs with shortfade

    "There'll be someone at each door into the stairwell. At the first landing, the man stops for a moment to rest."
    fe "{size=15}Might as well level all these old buildings and start over...{/size}"
    "He's frustrated. He slams his clenched fist into the railing."
    "He's scared, too. Someone's dead because of his mistake. She's run away before, but never like this. Never off the estate."
    "And not for a decade. They'd thought she'd outgrown it. Once she'd gotten married, once she had the girl, they'd thought she'd have settled down. He shakes his head."
    "What had she been thinking?"

    scene sasaches_inside with shortfade
    #do a slow pan over the scene

    "There's one aide outside and another inside."
    fe "... God."
    ai "I'm sorry, sir. I've heard you were close with her."
    "He puts his hand on the other mans shoulder."
    fe "You ever lost someone?"
    ai "... Yes, sir."
    "He nods."
    fe "Of course. We all have, haven't we?"
    "The aide looks over at the door nervously."
    ai "I'm sure they could use another for patrol, sir."
    fe "No, no- stay a moment."

    scene sasaches_inside_close #with some kind of zoom in?
    #do a slow pan

    extend " They were like this?"
    ai "Yes, sir."
    fe "Who's seen?"
    ai "The two of us, sir. And the duty officer."
    fe "I'm sure we can count on your discretion."
    ai "Yes, sir. Like you said, sir, we've all lost someone."
    fe "Good lad. Off you go, now."

    scene sasaches_inside with shortfade




    #keep rewriting.
    #fp for yvette?


    f "I always thought the young miss would have more sense than this."
    "He reaches for a disc resting against the armour of his suit. When he pulls his hand away, the disc comes with it."
    f "Dispatch, this is Juliet-1."
    "He speaks into it."
    f "We've found her."

    show federal_aide at right

    fa "Sir, Medical is on their way."
    "He spins the disc against itself so they can't hear him on the other end."
    f "Alright. We'll stay until they get here."
    "The aide walks back outside and he spins the disc back."

    hide federal_aide

    "They're saying something on the line, but he can't make out the words. He wonders if he's connected to dispatch after all. But no, they don't talk to you like this other places. Anyone can be rude, dispatch has made an art of it."
    "And they're speaking english, but the words are all wrong. They sound all wrong."
    "He looks back towards the bedsheets."

    scene sasaches_inside_close

    f "{size=15}... What are you grinning for.{/size}"
    "He notices he's alone in here. They're never supposed to be alone in the field, but this team knows him."
    "They didn't know the young miss, though. Can't blame them, of course. They're just kids."
    "He crosses the tiny room and sits in the only chair. It rocks offensively."
    f "{size=15}Stupid girl...{/size}"

    stop music

    ##-- ^end of flashback
    scene title with longfade
    #if there's an opening movie, this is where to play it.
    #--

    centered "17 years later.{w=1.0}{nw}"

    show screen thought("Yvette. You need to get up now.")

    scene taxi with longfade
    play music track1

    t "Hey miss, you're awake now, huh? Good timing. We're almost there."
    "The driver looks into the back through the rearview mirror."
    t "You doing alright back there? It hasn't been too rough a ride, I hope."

    show screen thought("Yvette. How is your recollection?")
    y "I'm well."
    show screen thought("That's good. Stay relaxed for now, Yvette. We're expecting you'll be quite busy this morning.")
    "She can feel herself relaxing."
    show screen thought("I'll be in touch.")
    "A sudden shock of anxiety shoots through Yvette."
    show screen thought("Yvette... calm down. Try to relax for now, and we'll be back with you when you get out of the hotel.")
    "Yvette's lips tighten, She's heard this before. Without a basis for independent action, she wont't be able to act quickly when her life depends it. She knows, but she doesn't like to be alone."
    hide screen thought
    ta "Wow. This is a nice place, isn't it? Very expensive, yes?"
    "The car pulls into the lot of a huge building and the driver guides it in front of the building's glass doors. Despite the early hour, there's already people walking through the doors. Yvette watches them, but only for the reassurance it gives her."
    ta "Are you staying here, miss? 'Cause if you are I could tell you something about the area. Don't get me wrong, I don't live here, but I've driven the area for years."
    "Response 1."
    y "No, thank you. I'm staying with my elderly mother."
    "He smiles."
    ta "OK, sure. That's great. Young folks shouldn't forget about their elders the minute the don't need us."
    "Follow-up."
    y "She's sick."
    ta "Oh? What a great daughter. I wish my daughters were just one half as sweet as you."
    "He's still smiling. The car's still on."
    ta "One-hundred-eighty-eight, miss."
    "Yvttee's eyes flash to the meter at the front of the car."

    scene taxi_meter

    "He's lying, but Yvette knows better than to point it out. Instead, she pulls out the wallet she was given earlier and empties it into her hand. She passes the contents to the driver."

    scene taxi

    y "Have a nice day."
    ta "Sure, miss. You have a nice day too."
    "She steps out of the car."

    scene grandarms

    ta "Miss, your bag?"
    "Yve steps back and wordlessly picks up the bag from the floor of the back. The driver smiles again, and pulls away from the curb. In a moment the car's merged back onto the highway. Erased."
    "Though she has no recollection of the bag, she swings it across her back and starts up the walk to the doors of the hotel. "
    "They told her about this. It's happens sometimes, but it's nothing to be worried about."

    python:
        ow = Overworld()
        yve = Unit_yve()
        ow.join_party(yve)
        piece1 = Bascule_armour()
        ow.get_inventory().add_gear(piece1)

        ##now we want the player to open click on the hotel to start the hotel_0 event.


label hotel_0:
    scene grandarms_inside
    play music track2




















    "prologue ends."
