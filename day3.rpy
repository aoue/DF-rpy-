label day3_scene0:
    #morning:
    #mc arrives at school alone. show flashback to nai saying he's going to run.
    #nai decides to train running. to be properly motivated, hes waiting to leave until he can just barely can make it to class running all the way. yve doesnt have this clas.
    #at school alone. mc sees dg in the field. go to her and she sees, leaves. mc will be late if he does. or dont.
    #    if he does, the embarassment level will rise againself.

    #scene day changing or whatever.

    centered "Twenty Fifth of Undim\nThirdday 07:30"

    scene apartment
    with longfade

    #play sound train_whistle

    "The whistle of the F-Train sounds off as it does twice each hour. Fittingly, there are two each day that have special meaning: this one in the morning when Anne departs and the second in the evening when she returns. Most days."
    "There's a minute before the time Nai and I usually leave. I take the time to review my agenda."

    #scene agenda_nov_25 #whatever
    #information:
    #class: 08:00 - noon ish
    #archives: 8:00 pm? - 2:00 am?. anyway, there isn't round the clock coverage. how knows how they decide what to cover.

    #the agenda remains on screen for the next few lines. it's treated as the scene.
    "Class, as always. And I'm working this evening down at the archives. Until quite late, actually. I wonder if I haven't taken the time down wrong."
    "I suppose I'll see when I get there."
    "I should probably go harass Nai or we'll be late."

    scene street
    with shortfade
    show nai
    with dissolve

    mc "That wasn't like you, Nai. You don't normally have trouble in the morning."
    n "I wasn't having trouble. I was just thinking."
    "He clears his throat."
    n "Yesterday when Yve said we should leave Citizenship, I opposed her pretty strongly."
    mc "Moderately."
    n "The point is maybe I was wrong. Maybe we should have left."
    mc "That's what you were thinking about?"
    n "Yeah. That and what it could mean for today."

    menu: #the different options presented here imply mc is making this up.
        "'Yve was joking.'":
            $de11 = 1
            $nai_yve += 1 #nai's impressed that she was clever enough he didn't notice.
            mc "Yve was joking?"
            "He blinks."
            n "She was?"
            mc "Yeah. Do you think Yve would have stayed if she had really wanted to leave? She was just trying to get a rise out of you."
            n "Huh. I suppose that's true."

            show nai grin

            extend "She got me, then. And got me thinking about it all morning too. Man, you can't let your guard down for a {i}second{/i} around that girl." #ruefully
            "I don't think she was joking, but who really cares."

        "'You were right.'":
            $de11 = 2
            $ nai_rel += 1 #nai likes positive reinforcement.
            mc "You were right. He did get back to the class and we heard something we wouldn't have otherwise. I mean, now we know about consdiction."
            n "That's con{i}scrip{/i}tion. I guess you're right."
            mc "Time has already vindicated you, don't waste any more time thinking about it."

    n "I feel a weight's been lifted."
    mc "That's good, but don't stop walking."
    "He shakes his head."
    n "Go on without me. I've got a lot of energy all of a sudden. I feel like training."
    "Training. Nai trains often, but never for the same thing twice. I can't decide whether to fault him for his lack of tenacity or admire him for continuing despite this. More likely he wouldn't care."
    mc "What for?"
    n "I thought just thought that maybe some general training was in order."
    mc "Makes sense."
    "He doesn't want to say, then."
    n "I'll see you in class. Watch, I'll beat you there."
    mc "I'm sure you will."
    "And so we part ways."

    scene campus_busy #it is
    with shortfade

    "It's another beautiful day on campus."
    "Busy for this time of day, but that can happen sometimes. People walk from building to building as they arrive to their classes."
    "I scan the crowd as it morphs from shape to shape for I recognize. Yve, I mean. I don't see her. Yve often doesn't head to school until a few minutes before the start of class." #who else besides yve? <- sarcasm
    "I continue on alone."

    scene uniclass
    show proff
    with shortfade

    #--- Geography Class ---#
    #first, show a map and whatnot. talk a bit about geography. some students keep asking about where different things mentioned from the war are. e.g. the sineb? the border? the capital? lablache?



    f "Everyone turn to page three hundred and twelve."

    "A few minutes have passed since class began, still with no sign of Nai."
    "This is geography, taught by Prof F. Other years, it's been dreaded and ignored by students, but this year it's one of the classes we await with the most interest."
    #why?
    #because of the war. everyone wants to know where everything was.

    $r1_name = "Eager Student"

    r1 "Professor?"
    "A student interrupts her."

    show proff tired

    f "Yes? I will not be derailed ten minutes after starting."
    r1 "Of course not Professor. I was just wondering if you had seen the KBA anniversary broadcast."
    f "Yes, I did. If you examine page three hundred and twelve of your textbooks, you'll see a breakdown of the unusual geographic features of the Greater Sarrenais Region."
    "I'm already familiar with the topological wonders found there, on account of growing up on top of them."
    r1 "--Professor, I was hoping you tell us about some of the places they mentioned in the broadcast. I've never traveled much, and neither has anyone I know, so you're like my last resort."
    f "I see. Did you have a particular concern?"
    r1 "Not really, they were dropping a lot of names that I'd never heard."
    f "In that case a general overview might be a good place to start."

    scene worldmap #she'll point to different places on the worldmap with a stick when she's talking about them.
    #show 'world map' <--- very important, since there's been name dropping before and after this.
    #things like:
    # -Donnlier and Larisse
    # -Sarranais
    # -the Sineb
    # -The F-Train and the whatever train. (add the train routes to the country map)

    fl "I hope you recognize this at least. The known world."

    scene worldmap_sarranais #stick at sarranis

    fl "The broadcast itself was distributed from Sarranais, like all government broadcasts."

    scene worldmap_sineb #stick on the sineb

    fl "And it was recorded on the other side of the Sineb River, here, in the Greather Southern Region. To add context--"

    scene worldmap_larisse

    extend "--We are here, right in the middle of the Greater Donnlier Region."

    scene worldmap_donnlier

    fl "And there is Donnlier proper. Though That's one I'm sure you knew."

    scene uniclass
    show proff
    with shortfade
    nvl clear

    f "Is that satisfactory."
    r1 "Yeah... It was a little fast, but I think I've got it."

    $r2_name = "Detail-Oriented Student" #TODO better name

    r2 "Professor, have they really gone to the other side of the Sineb?"
    f "Yes, they have and even beyond that."
    r2 "I don't understand why they would?"
    f "Out of duty and to protect those of us who remain here."
    r2 "Why wouldn't they just refuse? There's no way anything could get me to go to the {i}Wrongside{/i}."
    #glossary updated. wrongside = popular term for land beyond the sineb.
    f "Then you lack the a certain maturity, but that is neither here nor there. We are leaving the realm of geography."
    f "I will allow certain tangents in my class, but I will not entertain philosophy."
    "We move back to the topic of the various features of the Greater Sarranais Region."

    scene campus_class with longfade

    "About a third of class has passed by the time Nai comes in. Professor F. scowls in the direction of the noise he brings in with him."
    "He sits down, panting."

    show nai tired #class. nai comes in a few minutes late.

    n "i seem to have overestimated my abilities. I thought if I just wanted hard enough..."
    "Prof F. glares back, this time right at him."

    show nai mocksurprise

    "He widens his eyes in mock surprise and puts his hands out as if to steady himself. He shrugs helplessly."
    "We get back to the topic of geography."

    scene campus_hall
    with longfade

    "By the time the class had finished, we'd covered [[look up some geographic terms here] in all three regions and several other topics that arose besides. The fighting has gotten everyone more interested in geography, at least."
    "Nai and I are slowly walking our way out of the building."

    show nai

    n "What I was trying to say earlier:"
    mc "You overestimated yourself."
    n "Right, that. The thing with training is that it's not enough to just want, there are physical prerequisistes to this kind of exertion."
    n "I went back to the apartment and from there I ran all the way here. Well, I tried."
    mc "You didn't leave yourself much time."
    n "That's the point. By backing myself into a corner, I thought I could draw out all my strength. Sort of fight-or-flight myself. "

    show nai curious

    extend "It didn't work though."
    mc "Well, if it were me, I wouldn't be too bothered by the stakes. That's probably why. All you had to lose was being a few minutes late to class."
    n "You're saying if I want to up my game..."
    mc "... You need to up the stakes. It stands to reason." #mc is antagonizing nai, but nai is serious.
    n "It does."
    mc "How about humiliation?"
    n "hmmm-miliation? I don't like it."
    mc "That's perfect. The less you like it, the better it will work as motivation."

    show nai thoughtful

    "He nods thoughfully."
    n "That might work. Yeah, I can feel myself getting pumped-up. You're a real pal, thanks."
    mc "And for the method--"
    n "I've thought of the method already. I'll need someone's help to execute it, though, so if you don't mind..."
    mc "Happy to."
    "As if I'd miss it."

    scene campus_busy

    "We emerge out onto the campus. The weathe is much like it was this morning, but a little colder. A biting wind sweeps through the grounds and students scurry on their way, shielding their faces beneath hats or under hands."
    "There must be a wind coming down from the mountain. "

    scene pessevaine

    extend "{i}You know what I'm talking about, don't you.{/i}"
    "The mountain does its best to shrink guiltily into the background. It fails, of course, being a mountain."

    scene campus_busy
    show nai_cold #he's not wearing his winter gear. he left at home to train

    n "It's unreasonably cold."
    mc "It's not much different than yesterday, really."
    "He shivers."
    mc "Where's your coat, Nai?"
    n "I don't have it. There was this kitten in a box, starving, so I left it my coat."
    n "This was when after you were gone, by the way." #
    mc "You had your coat while I was there. So it would obviously have to be after I left. "
    n "That makes sense."
    mc "Very selfless."
    "He nods."
    mc "... I suppose I can lend you something."

    scene campus_busy
    show nai_borrowing #he's wearing partial snow stuff. one glove, scarf, no hat, etc. borrowed from mc.
    with shortfade

    "A minute and several articles of clothing later, I've shed what of my outer layer I'm willing to give up. Nai looks marginally less cold and much more embarrassed."
    n "... I'm still cold."
    "I am too. My winter clothes work as a perimeter to keep out the cold air. A single opening is the undoing of the entire system."
    n "Oh well, at least the library's heated."
    mc "You're going to the library?"
    n "I'm working all afternoon. Didn't I tell you?"
    n "You know where I'll be. Tell Yve hi if you run into her."

    hide nai_borrowing

    scene campus_edge
    with shortfade

    "I get to the edge of campus before I begin to regret my generosity in such harsh weather."
    "I need to remember to show up tonight at the archives, and I'll need to stop off at home before that. Until then, the rest of the day is there to waste."

    $explaining_gloves = 0
    #counter to mark the how many times mc's had to explain why he's wearing only half winter set. at one point, mc will realize that nai was about to go in to the library, so nai doesn't need the clothes anyway. in each jump here he explains it and increments the counter.
    #when talking to dg this night, dialog changes based on this var.

    python:
        map_unlocks[0] = True
        map_unlocks[1] = True
        map_unlocks[2] = True
        map_unlocks[3] = False
        map_unlocks[4] = True
        map_unlocks[5] = True

        map_jumps[0] = "day3_scene1"
        map_jumps[1] = "day3_scene0_j1"
        map_jumps[2] = "day3_scene0_j2"
        map_jumps[4] = "day3_scene0_j4"
        map_jumps[5] = "day3_scene0_j5"

    call screen map_nav_town(map_unlocks, map_jumps, map_descriptions)

label day3_scene0_j1:
    $map_unlocks[1] = False
    $explaining_gloves += 1
    $yve_rel += 1
    # -cafe. yve_rel++, emery there too. you can get a chance to actually talk to him this time around.

    scene cafe_sparse
    with longfade

    "The cafe is mostly empty. The employees talk at the counter, one leaning on the side."
    "Oh, it's Yve. "

    show yve_uniform at left #to offset the normal
    show emery at right

    extend "And the same guy as before is hero too."
    "Yve looks up at the sound as I walk in."

    hide emery
    show yve_uniform at cen

    y "If it isn't one half of all the cute first years."
    mc "Hey Yve. Working again?"

    show yve_uniform_thumbsup at cen #she gives a thumbs up

    y "That I am. I don't do this for fun. As much as I might appear to be enjoying myself, know that it is a facade for the benefit of the patrons."

    show yve_uniform at cen

    mc "You look like you're enjoying yourself a little at least."
    y "Just a little. Where's the other one? Tell me."
    mc "He's working right now too."
    y "Huh. So he finally's got a job. Good on him..."
    mc "Nai's had a job long before you did Yve--"

    show yve_uniform_frown at cen

    y "Oh?"
    mc "--Before you had this job, at least. He's had it since the start of the semester. You know that."
    mc "You lead me into saying that. You're messing with me."

    show yve_uniform_smile at cen

    y "Maybe. Nai's easier, but you're not too hard yourself."
    mc "You're devious."
    "The door is pushed open again and Yve looks up."
    y "Ah, more customers. Pardon me while I do my job."
    "She goes to greet the group that just walked in."

    hide yve_uniform_smile

    "I watch her for a second before I start feeling someone looking at me."

    show emery_peering at farright #eyes narrowed, looking at mc

    menu:
        "[[Talk to him.]":
            $de12 = 1
            $express += 1
            "I decide to talk to him. There's no reason we should remain strangers."

            scene cafe_sparse
            show emery at cen
            with shortfade

            "The first thing I realize is that I'd been misjudging his height. He's quite tall. Not as tall as Yve, but still."

            show emery smile at cen

            extend "He smiles as I come up."
            "He's pretending I didn't catch him staring. Fine, nothing would ever get done if people acted on everything they saw."
            e "How can I help you?"

            scene flashback 4
            $renpy.pause()

            scene cafe_sparse
            show emery at cen
            with shortfade

            "I'm vaguely aware that I'm going to have to eat today. I was just hoping to do it in an affordable way."
            "I sigh and order something cheap."

            mc "By the way, do you know the girl who works here well?"
            e "Very well, in fact. Do you?"
            mc "Yeah. I was actually talking to her just a few minutes ago."
            e "Really? I hadn't noticed. "

            show emery smile at cen

            extend "Even if you're a friend of Yvette's I can't give you anything for free."
            mc "I wasn't trying for something like that."

            show emery at cen

            e "I see. Because a lot of people think like that. They think just because it's a small shop in a small town, everything will be free and when it's not it'll be half-off. We can't afford that. A big, proprietary, store could, but they'd burn it all rather than give it away."
            "He shakes his head."
            e "The more you have the less you give."

            "He tells me more about the finer points of corporate generosity while preparing the order."

            scene cafe_sparse
            show emery_smile at cen
            with shortfade

            e "I'm happy to help a friend of Yvette's to our complete selection of goods at a fair price, any time."
            "Plate in hand, I slink back to my table."
            "I wasn't even hungry."

        "[[...]":
            $de12 = 2
            $repress += 1
            "I don't know if he has something in mind, but it doesn't bother me. Not really."
            "... It would be fair to say I wish it didn't."

    #some time has passed. reconvene with yve.
    scene cafe_sparse
    with shortfade

    show yve_uniform_smile
    with dissolve

    "One group leads into the next and it's a quarter of an hour before Yve sits back down across from me."

    if de12 == 1:
        mc "You've got a strange guy working with you."

        show yve_unifrom eyebrow_raised at cen

        mc "He was looking at me a bit funny earlier."

        show yve_uniform at cen

        y "Cut him some slack, you're a bit funny looking."

        scene flashback5
        $renpy.pause()

        scene cafe_sparse
        with shortfade

        show yve_uniform_smile
        with dissolve

        mc "Am I really? You know Anne said something about that yesterday."
        y "Was she smiling when she said it?"
        mc "Not like you are now."

        show yve_uniform shrug

        y "Then I wouldn't worry about it."

    else:
        mc "Charming friend."

        show yve_uniform shocked #she's worried that emery spilled the beans about her past.

        y "What?"
        mc "Emery is. I'm sure you'll get along fine. I don't know how suited to this type of job he is, though."
        mc "He seems to hold you in high regard for some reason, too."

        show yve_uniform smile

        y "Oh. Well, naturally."

    "It's getting later. I feel like I've been here long enough."
    "I push my chair back and pull on my coat."
    mc "I should be going. There's still a few things I ought to do today."
    y "Sure. By the way... you dropped your other glove."

    show yve_uniform glove #she's holding out a strange glove. not mc's, but a different one.

    "She holds out a strange glove. Even without looking at it I know it doesn't belong to me, my other glove is with Nai."
    y "Don't just grin at it, take it. And don't drop your junk all over my cafe, at least not while I'm working."
    "I hold my hands out for her to see."
    mc "Thanks, but it's not my glove. I'm sure someone will be along looking for it, so you should probably hold onto it. It's cold out there."

    show yve_uniform narrowed_eyes #narrowed eyes + half smile

    "She just smiles."

    scene street
    with shortfade

    "It seems to have grown even colder in the time I was inside."
    mc "... I should have taken the glove."

    return


label day3_scene0_j2:
    $map_unlocks[2] = False
    # -library. nai_rel++. talk to nai a bit. mc also checks his shift times, like he thought of doing this morning. they were correct.

    scene campus_library
    with longfade

    "The library is in full swing when I get inside though, being a library, you can't tell from the outside. It's quiet aside from the base frequency of hushed conversation."
    "Nai's not at the desk. I recognize the librarian's assistant there and we wave a little greeting to each other. I've met most of the people who work here. It's a small staff, just one librarian and a handful of student assistants, so it happened naturally."

    scene campus_library_2
    show nai_librarybasket #he's carrying a basket of library books and replacing them on the shelves.
    with shortfade

    "I find Nai among the shelves on the second floor."
    mc "Any of the other assistants working here looking to move out of the dorms?"
    "He stops what he was doing."
    n "Hey... that's not a bad idea. I'll see about it if I have time."
    n "There's a lot to do today."
    "He's apolegetic."
    mc "I'll help you."
    n "No, it's my job. I really do like you, so don't be alarmed, but please leave me alone for now."

    hide nai

    "He moves into the next aisle."

    return

label day3_scene0_j4:
    # -field. empty the first time, but it doesn't lock.
    $map_jumps[4] = "day3_scene0_j4b"

    scene field
    with longfade

    "I pass by that field as I walk through town."

    #panning shot.
    $renpy.pause(4.0) #too much pause? too little?

    "But it's empty."

    return

label day3_scene0_j4b:
    # -field. second time. not empty this time around.
    $map_unlocks[4] = False

    scene field_dg
    with longfade

    "I pass by that field again."

    #same panning shot as before, but stop partway through.
    $renpy.pause(1.5)

    "..."

    menu:
        "[[Talk.]":
            $de13 = 1
            $express += 1
            $dg_emb += 1
            $explaining_gloves += 1
            "{w=0.2}I'll try to talk to her."

            scene infield_dg
            with shortfade

            "I take a few tentative steps closer."
            "Everything seems so much quieter. The world is waiting to see what happens and how it should react. My face feels warm despite the cold and where they meet, it burns."
            "Step. I've been holding my breath."
            "Step. This is something important. Step."
            "I know with a sudden certainty that the rest of my life has {i}been{/i} to get me here. It's been filler. It's been for this one moment."
            "{w=0.35}S{w=0.35} t{w=0.35} e{w=0.35} p{w=0.35} ."

            scene infield_dg_focus
            #with what? some kind of transition will be needed.

            $renpy.pause(3.0)

            "I freeze."

            scene infield
            show dg at dgright

            "What..."

            hide dg

            $renpy.pause()

            "She crosses to the other side of the field and is gone. And the field is empty once again."

        "[[...]":
            $de13 = 2
            $repress += 1
            "..."

    "I don't even like fields."

    return

label day3_scene0_j5:
    $map_unlocks[5] = False
    # -streets. mc sees something that reminds him of a past experience. flashback to ane and the birds, you remember. she throws until hits one, then upset.

    ##flashback sequence:
    scene fbpark

    "It's a warm day. The snow on the ground turned to slush overnight amid a humid rain. So humid. It's always wet in my hometown. Snow or rain, there's always one on the ground or falling from the sky."

    scene fbpark_birds

    "A flock of birds descends and lands at a distance. It's the vanguard of all the migratory birds coming back home after winter. If birds think like that."
    "Will each bird nest in the same tree as before? I doubt it. Nature seems far too pragmatic."

    "I remember this day. Well, no I don't, not really. But I do remember what's about to happen."
    "Anne's laughing. She's got a hold of me with one arm and with her other she's grabbing rocks "

    scene fbpark_rock

    extend "and throwing them at the birds. She'll never hit them, she's missing on purpose. She's not a violent girl."
    "But it's fun to throw."
    "And I'm laughing in her wake. I copy everything she does. When she stoops for a rock, so do I, but my throw is weak and the force is all wrong."
    "She's nine and I'm five and the birds, well, we didn't know how short a bird's live is. Maybe if we had..."

    scene fbpark_hit
    with longfade #some time has passed. timeskipping to once anne's hit a bird.

    "That's wishful thinking."
    "If you throw close to the birds for long enough, even the greatest reluctance may be overcome, little by little, and triumph soured into regret. And so the birds have flown, except for the one on the ground, and no, it won't be flying again."
    "And Anne is crying and I start crying too, once I notice, once I stop throwing stones at the afterimage. The bird is still on the ground."
    "I wonder if we're going to bury it like in picture books, but we leave it instead and whatever else we didn't do, the thing we didn't do the most was look at the body. Cadaver."
    ##end flashback.

    scene street
    with longfade

    "I had let my mind wander without realizing it. That was longer ago than is worth remembering."

    if express > repress:
        "A lot's changed since then."

    else:
        "Nothing's changed."

    return



label day3_scene1:
    # -apartment. jump day3_scene1. mc drops his stuff off and gets what he needs for work. Also picks up nai's coat for him.
    #apartment. mc spends some time there and leaves again in the late afternoon.
    #there's a crowd at campus_edge. mc finds yve in the crowd.
    #special announcements. keep clear of roads and all transit will be closed while we wait for a military convoy to pass through. time unspecified for security reasons. they've closed off the main road so the convoy is undisturbed.
    #mc + nai + yve go to wait for it. wow! so cool! i saw some of those on the news! i saw some in the sky! the group can't see anything.
    #the group decides to head to a place where they can get a better look. the library roof? yve suggests. nai can get us a key. so can I, says mc. the library is empty, so in the end they don't even have to ask.
    #see the convoy and the mechs all wrapped up on flatbeds from the roof. they're headed south, presumably to where the action is.

    scene apartment
    with shortfade

    "It's still strictly afternoon when I get back to the apartment."
    "Nai's coat is hanging by the door. The cat must have returned it while we were out. I'll bring it to him for when his shift ends, he'll appreciate it on the way back."
    "Rather more importantly, I'll take back the rest of my winter clothes. I expect it to be deadly cold when I get off shift. And dark."
    "This will be the first time I've been out so late. In some ways I'm looking forward to it. There are some days I only feel awake in the middle of the night."
    "I take care of preparations for tonight."

    scene campus_edge
    with longfade

    #play sound crowd. it's the voices of people and stuff.

    "I make my way back to campus as evening approaches. There's an uncharacteristic crowd gathered at the point where the road diverges."

    show yve

    if de12 == 0: #mc didnt go to cafe
        mc "Yve? So this is where you were. What's happening?"
    else: #mc went to cafe
        mc "Yve? I thought you were working."
        y "We finished early."
        mc "What? Why?"

    y "That's what we're all here to see. Look."
    "She points over the crowd at the road heading into town. Whatever it is I can't out over or through the crowd."
    "... I need to hang out with shorter people."

    show yve smile

    y "They put a hurdle over the road. They've got all the roads that connect to the main street blocked off on this side all the way through the town. Well, that's what people are saying. For the other side of town, who knows? We can't get over there to see."

    y "It's just a sign, though. It won't stop anyone."
    mc "That's a sign backed up by all the authority of the government. You don't block off the main road all the way through an entire town for no reason."
    y "Someone will go and see what's happening."
    mc "You sound awfully sure."
    y "There's always someone."
    "More people are gathering. It was mostly students before, but now some of the professors have formed a small circle at the edge of the larger group."
    y "By the way... what's all this you have?"
    mc "Oh, right."
    "I've got all my stuff for tonight in my bag. I'm wearing Nai's coat overtop my own, a thick winter coat is far too awkward to carry all the way here from the apartment. It's hot, but I don't really care."
    "I briefly explain all this to Yve."

    show yve raisedeyebrow

    y "Go drop it off, then."
    mc "I'll miss what happens here."
    y "You don't want to be weighed down holding all that stuff {i}if{/i} something does happen. Just be quick."
    mc "Okay, but if I miss something historic I'm holding you responsible."
    y "Sure you are. Just go."

    scene campus
    with shortfade

    "I run the rest of the way to the library. Somehow everything doesn't feel as heavy as a moment ago."

    scene campus_library
    with shortfade

    show nai at left

    "Nai's at the front desk."
    n "Whoa! What's got you running so hard?"
    "I catch myself on the edge of the polished wood."
    mc "Here--"
    "I pass my bag and, once my hands are free, his coat."
    mc "--take these."
    n "What--"
    mc "Just put them back there. Something's happened. Happening."

    show nai confident

    "He nods knowingly."
    mc "What are you looking like that for?"
    n "Look around you. People came dashing in a few minutes ago and everyone got up and left with them."
    mc "But not you."

    show nai shrug

    n "I'm working."

    show nai

    mc "Nai... Put your coat on, let's go. I'm not going to let you miss a once in a life opportunity."
    n "It's not up to you. Look, if they find out I left the library unattended, I'm toast."
    "'They.' Take a different angle."
    mc "Nai, where is everyone else."
    n "I told you, everyone got up and left."
    mc "Not them. The staff. Where are the other assistant librarians?"

    show nai shrug

    n "They left with everyone else."
    mc "And they told you to mind the shop."
    n "I wouldn't put it that way."
    mc "Nai, you're a sucker. If everyone else's gone, no one'll blame you for leaving too. Besides, they love you here."

    show nai smile

    n "Well, I guess they kinda do."
    "The door flies open behind me and Nai smiles even wider."

    show yve at right

    mc "Yve, what are doing here? You're supposed to be watching the road for me."
    y "There's no point, it's like the entire town is there."
    mc "Just shove your way to the front, there."

    show yve frown at right

    y "Just hush. I've thought of something."
    "She points at Nai, who's been wearing a slightly bemused expression throughout this exchange."

    show yve at right

    y "You've got the keys to this place, yeah?"
    n "I do, but I don't think it would be a good idea to use them."
    mc "Yve, you're a genius. Give her the keys or I'll go get mine from downstairs."
    "There's a set of keys set aside downstairs for the use of the archives' staff, separate from the library."

    show nai distressed

    n "I don't know whatever terrible plan you guys have got, but I don't think I want to be part of it. Aren't you worried about being fired? Especially now, because of that {i}other thing{/i}." #that thing = new rent
    "At this rate it will be faster if I go get my keys."
    n "Guys... I don't want to do this..."
    y "There's a point in your life when you have to look at everything that's in front of you and sort out what's important from everything else."

    show yve wink

    y "It's probably not this point, but do it anyway, okay?"
    "Shaking his head, He gets to his feet."
    n "Fine. And where are we going?"

    show yve smile

    y "To the roof, of course."
    n "Are you kidding me?{nw}"

    scene campus_roof_glamour
    with brightfade

    "The wind is strong up here."
    "Among the edifices and trees along the streets of town, it's easy to forget how windy it is near the mountains."
    "Yve pulls her coat tighter."
    n "Woah..."
    y "We're in one of the highest places in the entire town."
    mc "You've been up here before?"
    y "A few times."

    scene campus_roof
    show yve at right
    show nai at left
    with dissolve

    "She walks to the barrier at the edge of the roof and leans over it, pointing down at an angle."
    y "There's the main road. "

    show yve smile at right

    extend "And there's everyone else."
    "She motions to the dense group along the barrier. I can see a bit more from here, and groups have formed at different intervals along the road. All pressing to the barrier, bothering to get a look of what's beyond."
    mc "I can't see anyone on the other side. No one's moving through and no one's crossed either."
    y "Fair enough. There's always been someone who crossed when I was around, but it was always me."
    n "Do you mean you've seen this before?"
    y "Sure I have. Plenty of times since the start of the war, but even before then. " #yve slips up a little here, implying she's lived here since before the start of the war. they don't notice though.

    show nai curious at left

    extend "We can expect some trucks coming through at some point today. They're ghastly with schedules, though, so they'll have the road walled off for hours before and after they pass through."
    n "... What are you talking about? You know what's happening?"

    show yve raisedeyebrow at right

    y "You do know where we are, right? The town might have come first, but the road through it is far more important. It's not the busiest road, but it {i}does{/i} lead to Donnlier."
    "We just stare at her."

    show yve smile at right

    y "Look, it's just transportation. They're moving stuff through here to Donnlier."
    n "Who's 'they?'"
    mc "And what stuff? And why are you talking like everybody already knows what you're talking about?"

    show yve at right

    y "The government. It could be military transportation, or it could just be transportation of goods to the refineries in Donnlier. A lot of production these days is done there."
    "She's facing us so she doesn't see the road, but watches our eyes widen. Yve turns back around."

    scene convoy_town #they're not being shipped dissasembled as in commonplace nowadays. no one's thought of doing that.

    n "Wha?"
    "I can't think of anything to say. A long line of flatbeds comes down the main road. On the back of each are blue tarpaulins with long ropes taut over each, joining together along the bottom of the vehicle's chassis."
    "Under the tarps are various shapes. I can see some of the edges of the form pressed again the tarpaulin from underneath, but along the sides the form is intelligible."
    n "What are these?"
    y "I don't know."
    "The next thing that strikes me is the size. The flatbeds proceed in single file and still take up most the road. I guess that's one reason for closing it off."
    y "But they're {i}huge{/i}."
    "I don't know exactly how far we are from there so it's hard to judge size, but the tarps are just as oversized as the trucks. Whatever's underneath fits to match. The area covered by the tarpaulin is probably five meters tall and half again as long."

    scene campus_roof
    show yve at right
    show nai at left
    with dissolve

    y "It's probably wood. Long trunks or something, all stacked together."

    scene convoy_town
    with brightfade

    n "You're just guessing, aren't you?"
    y "Yeah."

    #y "It's a good guess. It probably is wood." #TODO what to say here?

    $renpy.pause()

    #fade to black.

    jump day3_scene2

    #timeskip to archives


label day3_scene2:
    #-evening:
    #mc working at the archives.#8:00 pm? - 2:00 am?
    #read something? (about the construction/design of the mechs.)
    #surprised at how these important documents are just laying around.
    #dg is out past curfew or something; comes to the archives and asks to borrow the keys to unlock the dorms, sees it's mc and leaves. she doesn't feel like she can ask him for anything, given that's she's decided to play the bad guy. mc gets to the bottom of this. embarrassment level between 1,2,3.
    #normally he wouldn't let someone in, but this is a delicate moment, a like peace negotiations. he decides to.
    #sure, someone would let dg back in if she knocked, but then she'd owe them one. she returns them by dropping them from the window.

    scene campus_archives
    with longfade

    "Yve was proved right in the end: It was hours after the trucks had passed before the road was open again."
    "People faded back to whatever it is people do, and the three of us came back down to the roof to our own callings."
    "It's late evening, but there are still people in the library. It never really empties until the staff kicks everyone out, about an hour before the university's curfew."

    show nai at cen

    mc "All done?"

    show nai sheepish at cen

    "He nods. It was a long shift for him today, though it was split by the afternoon's excitement. As neither of us say anything for a moment, I can tell he's thinking back to it."
    n "Do you think they've made it to... to Donnlier yet?"
    mc "Probably, it's not too far. Yve said they might just be passing through Donnlier though, just like here."
    n "Where are they going? I don't feel like I should care, but I do."
    mc "I know what you mean."
    mc "You should go home, shouldn't you? You must be starving."
    n "How could I care about that right now?"
    mc "I bet Anne would know if they went through Donnlier."

    show nai excited at cen

    n "I wonder if they blocked off the roads there. She might be late again. Wait a second... Do you think it was something like this that made her late last time?"
    mc "She said they were all working late."
    n "--Because they couldn't get home and the roads were blocked off. I'll get her to tell me."

    show nai at cen

    "This is quite the turn from earlier when we had to drag him to the roof."
    mc "... And Nai."


    mc "Don't talk to Anne about finding a new roommate. It affects me too. when it comes to this, we'll have to face her together."
    mc "She'll walk all over you on your own."

    show nai stretching

    n "Or you."
    "I shrug."

    show nai smile

    n "We'll have to plan out what we're going to do about this going forward. One of these days before too long. If Anne has her way we'll just be switching out guardians."

    menu:
        "'You avoided mentioning this to Yve earlier.'":
            $de15 = 1
            mc "You avoided mentioning this to Yve earlier."
            n "I guess I did. I didn't want to get her hopes up in case this doesn't work out."
            mc "Get her hopes up? You think Yve would even want to live with us?"

            show nai frown

            n "She's our friend."

        "'Do you really think it was wood under there?'":
            $de15 = 2
            mc "Do you really think it was wood under there?"
            n "No way."

            show nai grin

            extend "Yve talks nonsense all the time. I can recognize it a mile away. And the shapes under the tarp..."
            n "It would have to be some kind of crazy tree."

    n "Anyway, time's getting on."
    mc "Be careful on the way back."

    show nai laugh

    if de == 2 pr de == 3:
        n "won't i be fine?" #referencing mc's responses #TODO

    $renpy.pause(0.5)

    hide nai laugh

    scene campus_archives_room
    with longfade

    "An hour later and it's finally empty. I've been hiding in here the whole time, and while I will spend most of my shift in here, I feel obligated to walk around every now and then."
    "But it's dark."

    scene campus_archives
    with shortfade

    "My first shift here I thought it would be a good idea to turn the lights on. It's easier to see. Isn't it good to see? One of the professors happened to see the lights on and came to see what was going on."
    "I've been much more cautious since then."
    "It's still dark, though."

    #start panning or something.

    "I don't go up to the library either. There's probably some rule about it: 'archive staff must never take stairs except backwards,' or something."
    "... Maybe I should look for a new job."
    "..."
    "I walk through the halls for a while longer."

    scene campus_archives_room
    with longfade

    #play sound chains or someting
    "..."
    #play sound similar
    "..."
    centered "Twenty Fifth of Undim\nThirdday 21:00"
    "The sounds from outside finally stop as the last of the staff leave for the night. The gate is dragged shut at the front of campus and the dormitories are locked."
    "The library doors don't get anything like that though."

    scene campus_archives_room
    with longfade

    centered "Twenty Fifth of Undim\nThirdday 22:00"
    "I'm tired. Even though I knew I was working tonight, I didn't change anything in my schedule to prepare for it."
    "Regreting that now."

    scene campus_archives_room
    with longfade
    centered "Twenty Fifth of Undim\nThirdday 23:00"
    "It's deadly cold. The late November weather is unrelenting in its intensity and the chill seeps through every imperfection in the buidling's aging foundation. It's sharp and cuts across the skin."

    "It's an old building and is wooden in part, bringing along all the structural problems of aged wood."
    "Decades of contraction and expansion in turn have taken a toll and though the walls are occasionally reinforced or painted over, it's a hopeless battle that will only end once the building is gone."
    "As an archive holding most government, bank, and other legal documents for local companies, it once had a very important role to play. Now it's little more than a fire hazard."
    "Time marches onward and records pile up. This place was probably holding ancient history by the time I was born. I check the label on one of the boxes absentmindedly."

    show image popup_imagedate #not full screen image of the labels date. it's year 32 or something.

    "A hundred years ago someone felt something was important enough to write down and preserve. And here it is now, forgotten in a listless place wandered only by insomniacs. A treasure trove for a certain type of person."
    "But for now, nothing. A quiet peace circulates among the shelves. Folders, undisturbed for decades, disintegrate slowly into dust."
    "I should do another round."

    scene campus_archives
    with shortfade

    "It's just as cold in the hallways, but I work myself back up to a comfortable temperature before too long."
    "I find myself wondering at the time. I'm not in the habit of ever wearing a watch, I just rely on whatever clock I can find nearby. There's one in the employee's room here, but I think it ticks too slow. It feels like I've been here for ages."

    #play sound knocking_far

    "What's that?"

    #play sound knocking_far

    "This is why the lights should stay on. I'm not scared of the dark, that's ridiculous. I'm very reasonably scared of the things that might be in the dark sitting just beyond the reach of my maladjusted eyes."
    "It came from the other side of the building."

    #play sound knocking_light (it's closer though)

    ""






    #out of context
    d "Do you forgive me?"
    "As far as I'm concerned there's nothing to forgive."
    mc "As far as I'm concerned there's nothing to forgive."
    d "... So you do not? Because you say there is nothing to forgive. You say I have not wronged you."
    mc "Of course you haven't {i}wronged{/i} me."
    d "I disagree. I fear I have wronged you twice now by being so difficult."
    mc "Not at all. I'm the one who went up and bothered you for no reason."

    show dg tired

    d "Would you humour me, then, and say you've forgiven me."
    mc "Sure. Consider yourself forgiven."
    d "You forgive too easily."
    mc "What, I was just saying...{w=0.3} Maybe I do.."
    d "It's alright. It's quite common here, especially among the male students. Yes, they are much readier to forgive than the places I lived when I was younger." #joke. it's because she's pretty. when she was younger, they weren't acting upon it.

    scene dg_glamour #a glamourous shot of dg. drawn to make her beautiful. it's for humourous purpose. takes up full screen? part?
    with brightfade

    $renpy.pause()

    scene archives
    show dg at cen
    with dissolve

    "I think I might know why."


    #reference if mc pursued her in the fields. if he did: dg is curious about the winter clothes. lame excuse.



















































    #eof
