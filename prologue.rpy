#prologue. divided by main story | side quests | dungeon | map jumps

#all vn events that can be triggered during the prologue should go in here.





#TODO
#as mc meets these new people, add their files to the glossary. they need to be character dossiers or something to give some background to the characters so i dont have to describe goddamn everything
## --------------------- Main Story: Prologue --------------------- ##
label p_ms_0:

    python:
        #ow.show_overworld(0)
        ow.show_overworld(1)
    #^^ testing stuff

    scene apartment_bedroom_dark

    "The first few notes of the song float through the air. From my unguarded state of mind, each note seems to last, and I only finish processing the first as the phrase finishes. The song continues as each note piles on, until the song is lost and its just the notes, removed and without pretense. Just the same notes, over and over."
    "It's an alarm, and I stop out of habit. I set the alarm early today, but I've been awake even earlier, so that it's not a signal of when to get up, but of a minimum required to sleep."
    "I throw off my blankets and get dressed in the darkness. In the room next door, Nai, my roommate will still be sleeping. And maybe his girlfriend too, if she's in there with him. She's been staying over more and more lately."
    "I stop thinking about it. Nai will be up soon in any case, so while I try to stay quiet, I don't try to be silent. He's a geologist, and they have to start early so as to get the drop on the rocks."
    "Times are changing. We're not kids anymore."
    "I grab my lunch from the fridge and put it in my bag. I don't normally pack a lunch, I just buy something, but I did it yesterday to calm my nerves. One less thing to worry about."

    scene apartment_living_room_dark
    with shortfade

    "I'm ready just a few minutes after I've gotten up, but it's still too early to leave. I sit in the living room in the dark with my bag by my feet and my coat stretched across my lap."
    "I always do this. I'll suffer for it later today, I'm sure."

    scene apartment_living_room_dark
    show nai at right
    with shortfade

    n "Is that you?"
    mc "Good morning, Nai."
    n "What are... good morning."
    "He shakes his head and heads back to his room. We've gotten used to each other."

    python:
        ow.show_overworld(0) #at this stage of the overworld, only the hq is unlocked. click on it to continue
label p_ms_1:
    #do some kind of transition to show mc traveled. he took transit.

    scene hq_outside
    with longfadefade

    "There's just a few people at the office at this time of day. Most people are working with operatives to the west of here, so they don't show up until they begin over there. Of course they stay late too."
    "That's why I'm here early today. I'll be in contact to the east. Us east-workers have to start early, but I can't bring myself to mind today."

    show mueler at left
    with dissolve

    m "Hey there, new guy."
    mc "Oh, hi Mueler."
    "Mueler - they put him in charge of training me."

    show mueler stretch at midleft

    m "You're not just gonna stand out here all day, right? You'll make me look bad. You mess up and it's a nightmare for both of us."
    m "We have the unshakeable bond of mentor and mentored-to now. Bring no shame upon this covenant."
    mc "I'm not intending to do anything wrong."
    m "Well that's a good start, but it's not the things you're ready for that get you. Make sure you remember that."

    show mueler at left

    extend " C'mon, let's go."

    scene hq
    show mueler at left
    with shortfade

    m "Looks different today, huh?"
    mc "It looks the same as always, doesn't it?"
    "He shakes his head."
    m "You're looking wrong, then. Didn't I teach you how to look properly? I must have. There is nothing more important for our kind of work than being able to see, to really see."

    show mueler shrug at left

    m "I guess you'll have to pick it up as you go."
    "We start walknig."
    mc "Mueler, I- I know I'm not the best student, but I really want to thank you for teaching me, well, everything. I really feel ready thanks to you."
    m "Really? Then I did it wrong."
    "He raises his hand as I start to protest."
    m "No, I know what you mean. And of course. You gotta look out for the new guys, so don't thank me."

    show mueler point at left

    extend " Especially before it's done you any good. You'd feel like a real idiot if you thank me right before what I've taught you puts you in the shit."
    mc "Oh. OK, I guess that makes sense."

    show mueler at left

    m "It does. So take it back."
    mc "Take it back? I don't-"
    m "Just do it."
    mc "Um, OK. Mueler, I am not thanking you for any of your training."
    m "You're absolutely not welcome. Chin up, now, you'll do fine."

    scene hq_station

    "We stop walking outside a pair of stations."
    m "You've just been following me this whole time, you know."
    mc "I... I guess I've gotten used to following you around..."
    m "Yeah, don't worry about it. Really I'm supposed to be keeping an eye on you today too. But Tori's given me some other stuff to do today."

    show mueler shrug at left

    extend " It's related to the stuff I was doing before you showed up."
    "Tori - That's Victoria. She's the floor manager. I saw her a few times during my training. No one calls her Tori though, at least to her face."
    m "Don't worry though, I got them to put you right next to me."
    mc "Thanks, that's a relief."

    show mueler narrowed at left

    m "Are you sassing me?"
    mc "What? No! I really mean it, I feel better knowing you're right next door."
    m "Right. OK, I guess you're welcome. It's no trouble, or something."

    show mueler at left

    m "Anyway, like I was saying, I won't be doing anything super important today, but I do need to be there. I can probably spare you a minute every so often, though. Just hit our shared wall if you need me."
    mc "I can hit the wall? Is that really OK?"
    m "Yeah, it's totally fine."
    "He moves to the front of his station. I notice there's a nameplate on the door."
    m "Oh, this? They'll get one for you too in a while."

    show mueler smile at left

    m "It's bad luck to go to too much trouble for a new guy, you know. The more you get ready for them to stay, the faster they get themselves killed. Sorry, we're a superstitious bunch. Don't hold it against us."
    m "And don't hold it against anyone who gives you the cold shoulder, either. They're just waiting to see if you'll make it. Give 'em a week."
    mc "I will, then. Thank you."
    m "Sure."

    show mueler exiting at right

    extend " I should go now, though. I'm sure everyone's been waiting for me."
    m "Remember - I'm only one knock away. If I don't come, just hit it again, harder."
    "He disappears into his station. The door closes behind him. A moment later, I can hear the muffled sound of his voice coming from inside."
    "I guess I should get to it."

    scene hq_station
    with shortfade

    "This is the one."
    "{w=1.0}I push it open."

    jump p_ms_2
label p_ms_2:
    scene hq_instation

    "This is my first time being inside a station by myself. During the training, Mueler or someone was always there. I've gone over how to use it at least ten times this since waking up, but that's all pushed into the recesses of my mind. It's got to, so there's room for everything else."
    "{w=1.0}... It's a lot more cramped than the training one. There's not much space between the station itself in the center and the systems along the walls. It's just wide enough for a single person to walk through."
    "I take a tentative step towards the chair, just close enough to touch it. I run my hand over the head. It's hard and smooth."
    "As I circle around the back, my foot catches on an errant cord stretched along the floor. I stumble and catch myself on the chair. It's really very firm."
    "I stand in front of the chair."
    "It's large-backed and planted firmly in the ground through metal beams. From every direction, a mess of wire and other intelligible shapes reach into the ceiling and the walls."
    "The whole room is the body for this machine. Everything about the room, its size and shape, its temperature, everything, are all build around the machine."
    "The interface. The most revolutionary invention of the last century, and its second best kept secret."
    "I sit down."

    scene hq_instation_seated

    "As I place my arms along the rests and then, slowly, lower my wrists into the straps, the machine hums itself to life. I keep my palms an inch off above their prints which have been imprinted into the metal."
    "Finally, I lower them down. The interface shudders and the hum slowly lowers in volume, until it's almost inaudible."

    #play sound interface0

    "The straps click shut along my arms."

    #play sound interface1

    "Along my legs."

    #play sound interface2

    "I close my eyes as the rest of the interface folds down from the ceiling around me."

    #play sound interface_start

    scene interface
    with longfade

    centered "WELCOME{w=1.0}, ANIMUS."

    #syncing. each time/ the interface is launched it takes a while to sync. in the meantime, people will brief mc or his teammates will talk to him.

    show mission cutin at right
    with dissolve

    #direction tutorial.
    c "This is mission control. We're going to brief you on a few things as the connection builds. Starting today, your interface has full functionality. There's a few ways its different than the training setups, so pay attention."

    show direction_tutorial

    c "This is your directional module. We set it up remotely from here in HQ. It will cover everything you'll need to know to with regards to your mission. Please review it now."
    "I look over the sheet."
    mc "I'm going to be working with another person? I mean obviously one person, but another pair?"
    c "Please do not ask any questions. and follow the instructions provided by your directional module. Your primary role takes presidence."
    c "Lastly, be sure to take complete and clear records of all events during your deployment. The importance of these records for both yourself and headquarters cannot be overstated."
    c "Control out."

    jump p_ms_3
label p_ms_3:

    scene mirror_dark
    with longfade

    "When I open my eyes again, I know that they are not my eyes."
    "I move my head from side to side, and it follows, half a second after. My movements feel insulated, like I'm moving from under a heavy blanket."
    "I force myself to remember: I'm attached to the interface right now. I am not here."
    "And that's just with the far connection."
    "Mueler said it would be like this. And not to scream. He said not to scream, no matter what."
    "I notice the mirror, but it can't be right. That's not my face."
    mc "It's Friday, right?"
    "I speak, but I don't hear my voice. Like walking without touching the ground."
    f "Yes."
    "It's a young woman's voice."
    mc "It's nice to meet you, Friday, I'm sorry for making you wait. I'm still on my first day."
    f "I understand. Thank you for your support."
    "She bows her head forward slightly."
    mc "You're holding a mirror."
    f "Yes. It's so you can see me. You see with my eyes?"
    mc "Uh, yes. Whatever you see, I can see."
    f "And hear, and also smell?"
    mc "Yes, both of those too. And there's more in the close connection."
    f "Yes. That is what they've told me."
    mc "I'm ready to look in the mirror."
    "Friday stands up and grabs hold of the sides of the mirror. It's not far, but the image it shows is hard to make out. I would imagine it's due in part to the angle, in part to the material. The mirror is shining like no glass mirror I've ever seen."
    "I remind myself of Mueler's warning once again. Don't scream. It's just a mirror, isn't it? I bite down on my tongue just in case."
    "Friday is holding the mirror at arm's length, but the image is still too distorted."
    "She brings the mirror closer."

    scene mirror_friday
    with brightfade

    "{w=1.0}.{w=1.0}.{w=1.0}."
    "There must be a instinctual response at seeing someone else's reflection where you expect to see your own. Without an identity, a human is matter floating around together. Without a face, there is no identity."
    "So I don't scream, but I would have. A second later I taste blood and let up."
    "Strange, I think, that there's no pain."
    mc "Please put the mirror down."

    scene cherespoir_room

    mc "... Thank you."
    "I'm feeling a bit nauseous. Friday asks a question as she sits back down."
    f "I'm sorry."
    mc "I'm... it's my own fault."
    "I've wasted enough time today. I grab back as much excitement as I can."
    mc "Friday, I'm glad to finally meet you. Let's do our best together."
    f "I'll support you as well as I am able."

    #play sound knock

    show yve

    "Friday turns to look at the woman who's just entered the room."
    f "Welcome back, Yve."
    "She's a tall young woman, looking a few years older than Friday."
    y "Hey again. Everything's set downstairs."

    show yve smile

    extend " I'm sorry, were you talking to someone?"
    "Friday nods."
    mc "This is our support, Friday? Have you been working with them?"
    f "Yes. Animus, this is Iris."
    "She gestures at the woman."
    f "And her eyes."
    y "More than just her eyes, thanks."

    show yve

    extend " I'm sorry. Apparently, I've been rude."
    "She steps forward to Friday and the two clasp hands."

    scene interface
    with longfade

    show payton cutin

    p "Hey there, I'm Payton."
    mc "It's nice to meet you, -"
    p "I know who you are, I've read your file."
    mc "Oh. Okay. What is this, exactly?"
    p "I'm just setting up a short-link between our interfaces so we can talk directly. Trust me, having to tell the girls to repeat after you everytime you want to talk is a real pain. And it's probably dangerous too, on account of it forming a kind of bottlenecking on communication."
    p "Also, there are times and things you don't want them to hear."


    menu:
        "What did you mean about not wanting them to hear?":
            $tick0 = 0
            mc "What did you mean about not wanting them to hear?"
            "There's a moment of silence."
            p "Sometimes...{w=1.0} things go wrong, you know. And strategical decisions need to be made for the good of the group."
            p "That kind of thing."
            p "Of course, there won't be anything like that happening today, right?"

        "Let's get back to it.":
            $tick0 = 1
            mc "Let's get back to it."
            p "Yeahh."

    p "It's finished syncing now, by the way."

    scene cherespoir_room
    show payton cutin
    with shortfade

    p "'Kay Yve, we're set."

    show yve

    "Yve nods and heads back to the door."
    y "We've got a few things still to do before we're ready to leave town."
    p "-Yve wrote a list-"
    y "-I've written a list for you guys. I don't mean to be rude, but we've already been here for the better part of a week. Some getting ready and some waiting for you guys, but... this is it. Now that {i}you're{i} here."
    f "She means you, animus."
    mc "Really? Why would you guys be waiting for me? I don't really have a clue what's going on..."
    p "Aww, he's cute. Hey Yve, d'you think we keep him?"
    y "I'll explain as we walk, come on."

    scene cherespoir_hotel
    show yve
    with shortfade

    y "You see, Payton and me, we're more like a reconnaissance pair."

    show payton cutin

    p "There used to be a lot more of us recon types, you know. But it's dangerous. So now there's only a few of us, but those that are left are really good."
    mc "Am I a recon type too? And you're here to show me the ropes?"
    "Yve laughs."
    p "First off, {i}you{/i} are nothing. You're a thousand miles away, there's nothing you could do here. With Friday, you're, well, tell him Friday."
    f "We're a combat pair, animus."
    mc "As in, not a reconnaissance pair?"
    f "Our exact role is to support Payton and her eyes."
    p "Since we're out a bit in the middle of nowhere, it's not too important what everyone's {i}quote{/i} role {i}unquote{/i} is. Mostly it's just important who's here."
    mc "Where are we anyway?"
    p "Where?"
    mc "Like on a map."
    p "A map? There's no maps here."
    mc "You're pulling my leg."
    p "You're not in Kansas anymore, new guy. Sure, there might be a map that's got this place on it, but there's no maps of it. That's partially what we've been doing here when we've got time. Can't leave a place unmapped, can we? Offends my delicated civilized sensibilities just thinking of it."
    p "The mapping is pretty easy though. We do tend to run out of white pencil, though, on account of there being so much damn snow. I daresay I'm supporting the coloured pencil industry here all on my own."
    mc "You use coloured pencils for mapping?"
    p "Why not? It's better than crayon."
    y "Payton, we're getting sidetracked."
    p "Ah, and so we are. Sorry about that. OK, sorry new guy, but no more questions 'til the end, yeah?"

    scene cherespoir_hill
    show payton cutin
    with brightfade

    "We finally make it outside. We're standing on a wide hill overlooking a valley"

    #play sound biting_wind

    p "Make sure you're not cold, Friday."

    scene cherespoir_hill_1
    show payton cutin

    p "You've got to make sure she isn't cold. Some of the girls, especially the newer ones can't really figure that stuff out for themselves."
    mc "Thanks for the advice, Payton. Friday, make sure to stay warm. It's... it looks like it's really cold."
    mc "And Payton... can we talk?"
    p "You mean private-like, huh. Sure."

    show mute

    extend " Right, they can't hear us now."
    mc "Is it alright to say that kind of thing around Friday?"
    p "Oh, sure. Out here in the countryside, at least, it's okay to let 'em off the leash a little. Someone like Friday, though, I don't think she really understands. Give it time."
    mc "I thought..."
    p "Yeah, well, a lot of people say a lot of things, don't they? Who can be bothered to keep track of it all. Out here, it's whatever works."
    mc "And... you said she's new?"
    p "Seems like it. I've never met her, and know one I know has ever met her either. Otherwise I'd know. She's probably about as new as you, I'd say. Nice when HQ can set it up like that."
    p "We should really get back."

    hide mute

    y "Here's the list."

    show list_0

    extend "We've got to do all these before we're ready to head out."
    "Yve points to the other side of town."
    y "See that shed? That there's the meeting spot, ergo we meet up there when we're done."
    p "Yvette and I will take care of {i}these.{/i}"

    show list_0_2

    extend " Since it's your first day, we'll take more. Just finish everything on that list, 'Kay?"

    scene cherespoir_hill_2

    "Yve starts walking down the hill into town."

    show payton cutin

    p "If you have any questions, ask each other. And remember- don't let the futility of your actions {i}ever{/i} impede your progress."

    show mute

    p "OK, but seriously, if you have any questions try asking Friday. She's been here for a few days already, and she's a fast learner. Aaaand I think she's been feeling a little shy. She hardly said a word the whole time we were walking."
    p "Payton out. I would say don't call me, but you can't."

    hide mute

    python:
        ow.show_overworld(2)

    #opens up the town.

## --------------------- Done --------------------- ##



label p_ms_4:
    #Scene 4: once that's done, call event from payton that says, sorry, they won't be able to make one of the stops on their list and need mc/friday to cover. just go check on the radar station. friday knows the way.
    #call overworld again, this time with radar station unlocked. (hill can still be unlocked too.)

    python:
        ow.get_routes[2][5].set_lock(0) #unlocks the radio.
        ow.get_routes[2][0].set_lock(1) #locks main story.







label p_ms_5:
    #scene 5: mc tells payton they were attacked. payton says no kidding, this is why we're here. mc asks if this is related to the pesticide. payton says yeah, it is, good job. let's get on the snowmobile and get moving. there's still lots to do today.

    #yvette starts slowing the snowmobile down. She kills the engine. Listen, she says. She hears monsters and so does friday. Mc can’t hear it though. He wants to know what’s going on though, so he glances up at the rest of the interface. He considers connecting. CHOICE. Either way, the monsters are coming this way, they must have smelled the two operatives. They might be able to escape, but the monsters would start chasing instead of stalking if the snowmobile was turned back on. We can take these guys, Yve says. Also, mc’s has to connect to the interface at this point if he hasn’t already.

    #Combat tutorial.

    #After fighting, mc is kind of shook. Friday is more or less acting herself and just waiting for confirmation from mc to act. Mc stammers out to follow yve’s lead. Yve starts tracking the beasts. They follow to the crest of a hill and see the tracks go quite a ways. Mc wonders if they should go back for the snowmobile. It’ll be more dangerous, but faster. They’re just doing reconnaissance today, so Yve says there’s no rush. Better to go in nice and quiet. They walk quickly through the snow all through the morning and most of the afternoon before they finally find the nest, what they were looking for. They wait awhile before heading in.

    #Dungeon tutorial. the player has to scout a way to the center of the dungeon. Bonus marks for finding other exits

label p_ms_6:
    #Scene 6: Once finding the center, yve says this would be the best place for them to apply pesticide. They really need to be getting back, though. There’s a long walk back to the snowmobile. payton suggests she can take care of Friday from here. Mc says no, it's still dangerous. they need to get back. yve says its probably fine, mc says he doesnt want to take that chance. (this part is direct.)
    # they drive back and yve/payton congratulate the two of them. they're working well together, real faster, you've never met before, etc. the recipients clumsily accept.
    # a while of silence and friday falls asleep. payton contacts mc again, tells him that's enough, she'll take it from here and no arguing. he did fine for his first day. see you tomorrow, you'll need to be rested for that. mc exits the interface.
    #it's very late, so there's few people back at the hq. mueler left a note attached to mc's door. it says:
    #congratz on survivng ur first day!!!! you probably did a lot today, but don't feel overwhelmed. p.s. make sure you're not late tmrw -- you need to build success on top of success

    #mc gets back home and it’s very late. Nai has already gone to bed. Mc just barely makes it to his room before collapsing and falling asleep.

    #end of prologue day 1.

label p_ms_7:
    #day 2.



## --- SIDE QUESTS --- ##






## --- DUNGEON EVENTS --- ##





## --- MAP JUMPS --- ##

label hotel_jump:
    "hotel jumped to"

    return

label backstreets_jump:
    "backstreets jumped to"

    return







##eof
