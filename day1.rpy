label day1_scene0:
#day 1: firstday
#-morning:
#mc+nai go to school. pass the dormitories/archives/library, explain mc and nai arent living there. they bunked together because old friends.
#dg at the door. mc can double down to later both their extra embarrassment later.
#meet up with yve who was already waiting.
#class. prof g. [history] use this chance to describe more about current events and the town's position in events. don't say theyre totally safe, but say

    $date = 23

    #black screen with longfade. a day passes.

    centered "Twenty third of Undim\nFirstday, 07:00"


    scene street #a street near the campus. used to indicate proximity to the campus.
    #play music unconcerned     #a chill track, reminiscient of happier times.

    "It's rained during the night. If it were just a bit colder there'd be a thin layer of snow on the ground. As it is, there's trickles flowing through cracks in the pavement."
    "I watch the dew-wet grass and concentrate on the details by my feet. Nai mumbles to himself while we step around worms stranded on the sidewalk."

    show nai

    n "Okay, how's this: "

    show nai puzzled

    extend "That was a very interesting lecture, Professor. I was actually thinkng of changing my major to history."
    mc "Nobody wants to hear 'interesting.' It's the limp handshake of compliments."
    n "Anne told me people like to be called interesting."
    mc "Anne is a lot more charming than you. It doesn't matter what she says so long as the meaning is understood."
    "Nai frowns."
    n "That's not really a nice thing to say about your sister."
    "I say nothing. Nai starts up again after a moment."
    n "I really enjoyed today's lecture Professor. Maybe I should change my major to history next semester."
    mc "Fail: you didn't leave a spot for an answer."
    n "I really love your lectures, Professor. Say, are you looking for research assistants this summer? Maybe for some fieldwork?"
    mc "We're trying to suck up, not harrass her."

    show nai strange    #a kind of creepy-on-purpose face.

    n "This sucks alright. Just like your lectures, Professor. Are you looking to become a hermit by any chance? I know a great secluded mountain not too far from here."

    show nai #normal. he breaks character.

    n "I can't do it. There's nothing I like about this class. There's nothing to like. And Professor G? She's damn scary and scary smart. What are we thinking?"
    "I sigh and shake my head. We're walking to university right now, and engaged in one of our less noble pursuits. Namely, buttering up our teachers."
    "It's simple. The halo effect: cognitive bias, the more you like a person, the more willing you are to dismiss their faults and accept their merits. As a student, or really anytime you're subordinate, it's one of the more useful tools you've got."
    "It's also nice to be liked."

    scene pessevaine    #mc is looking at the mountain. the screen is panning on it as he thinks.

    "It's looking to be another beautiful day. The weather is the best you get all year. Not too hot or cold or wet or dry, the winds blows by like a stranger on a busy street."   #unconcerned with you. quick to ignore/forget you.
    "Despite the hour, daylight is just beginning to push into the town. The sun has to make it over the mountain before any light shines in here, so it's like the sun rises a little bit later."
    "I don't mind. It reminds me I'm somewhere different."
    mc "It doesn't matter. She probably wouldn't believe it anyway."
    "I can't be upsed with anything on a day like this."

    "We're walking to school for our morning classes. Since we don't live in the dormitories on campus, we have to get up early and walk in with the sunrise."
    "Neither of us really mind, but I sometimes wish I could live with everyone else in one of the dormitories. As it stands, it's an economic matter and beyond either of our control."
    "Way back when Anne started at the university here our parents rented the place for her to stay. It's way too big for her though, so they told her to find some people to share it with and split the cost. She did. Always been a bit of a social butterfly."
    "I haven't got any idea what happened there during the years since I rarely saw my sister, but when they finished school, all her roommates scattered, either going home or moving to the city or whatever, with Anne close to follow. That was this spring."
    "In the intervening time, Nai and myself were ready to start, so we moved into the empty rooms with our families splitting the cost. For me, it was the natural move and for Nai, well we've been friends forever. Anne is practically sister to us both. And I think my parents were glad to have her here to look out for us, even if just for a while."
    "With her moving out though, it opens a whole new set of possibilities. It's accepted that we'll find a third roommate ourselves, but Anne holds the right to veto any candidate we present."

    scene campus

    "We arrive on campus in good time, just as the first crowds are beginning to form. Here and there, students sit on the grass talking or reading books while the latecomers rush down the street from the dormitory. It's not a big university, but it's a big small university."
    "Along the tiled path, the buildings of instruction are lined, separated by department. At the end of the row stands the library."

    scene campus_library

    "The building is three-storied, with main floor and the second being open to students from early to late at night, everyday. The bottom floor is used as a kind of storehouse for old books, records, and machinery. I come here often despite the distance."
    "At the start of the school year, Anne set me up with a job as an archival assistant in the basement, easy and late hours, which though less than ideal, don't interfere with my classes. Apparently, she worked the job for several years while she was a student and when she quit, she offered me as a replacement. It might have been nice if she'd asked me first."
    "Two weeks after I started, Nai somehow wormed his way into the library's staff. Even though we work in the same building, we're rarely scheduled at the same time and even if we are, we're stranded on different floors."
    "Nai heads to the front desk and I go downstairs. At the beginning of each week, we have to go sign up for next week's shifts."

    scene campus_archives

    "The door to the basement is locked, of course, so I unlock it. It's a job where you often work alone, so there's a degree of trust they're forced to accord to employees. One of these is a key."
    "I check the sheet along the wall and sign up for a few shifts. Just above is the previous week's signings. I copy down it down."
    "I see Nai's still busy at the front desk. The main library has more staff and a more complicated schedule, being open nearly all the time. I'll head to class first then."

    $renpy.notify("agenda updated")
    $agenda_unlocked = True
    #the agenda is now availbale.
    #cool agenda notes. Have it go until the end of the year. it shoud be partially filled out with important dates. example: nai's birthday. there'll never be a mention and you can stumble upon an event later by chance, but if the player sees this they'll be able to expect something. reward ppl who look for secrets.
    #holidays, etc. kba day.

    scene campusdoor    #outside a classroom. can be used everywhere on campus.

    "I walk throught the Humanities building's halls up to the second floor. A few people are already there, waiting outside. The lecture hall has two entrances, heavy wooden doors which feel as thick as they are wide, at either end along its inside wall and while they're both closed, they're probably not locked-they rarely are. A few people stand chatting at the far entrance with the door open wide into the hallhway."
    "As I close in on the nearer of the two, I notice someone standing in front."

    show dg

    "Standing rirght in front. She's standing just so, neatly in the middle of the frame, doors shut behind her. If someone were to open the doors from inside, they'd hit her square in the back. But she stands there, apparently unconcerned."
    #did you think of that dg? since its jammed it wont open -> so it wont hit her in the back. ofc she thought of it.

    mc "Excuse me." #pause half a second to show dg isnt answering.

    $renpy.pause(0.5)

    "She doesn't react. I wonder if my voice was caught in my throat."
    mc "Sorry, but would you mind letting me through? I've got class in this room."

    $renpy.pause(0.5)
    show dg eyesclosed

    "She slowly closes her eyes. A gentle look passes over her otherwise sharp face."
    "Ah, she's ignoring me then."

    menu:
        "[[Go in through the other door.]":
            $de0 = 1
            $repress += 1
            "I stand there thinking for a moment before turning back. This girl is pissing me off. I'm not about to shove past her, so I turn away, only hoping no one was around to see."


        "[[Get her attention.]":
            $de0 = 2
            $express += 1
            $dg_emb += 1
            mc "I said please move. I don't know what you're doing or what your problem is, but-"
            "She opens her eyes suddenly, still looking at the same place as before as if she'd been blinking incredibly slowly."

            show dg_bag_unslung  #unslings her bag
            show dg_palmbook    #starts reading from her palmbook

            "Oh.{w=0.3} Read your damn book then."
            "Confused and embarassed, I feel the urge to run. I don't understand why she's so cruel. Is it so hard to muster a 'drop dead.'"
            "I've changed my mind after all. I have no problem being upset on a day like this."

    scene campus_class with shortfade #can be used for all the classrooms on campus
    show nai    # at midleft

    "We take our usual seats. In the end, I slunk in through the other door and found Nai here waiting for me."
    n "Are you surprised that I'm here already?"
    mc "No, not really. This class is in your schedule same as it's in mine."
    n "But, you left first. But I got here first. Seems weird, right?"
    mc "I wasn't really paying attention."
    n "You are such a liar. Just admit you're surprised that I got here first. I beat you handicapped."
    mc "I'm surprised you went to all this trouble just to feel mildy superior."
    n "You're kind of ruining it."

    hide nai

    "Most seats are already full. There are no desks, but rather the back of each row has a long table curving along the backs of the seats its entire length. This is one of the biggest halls on campus, so many of the general and interdisciplinary classes are held here."
    "Right now - History, though with the war on everyone is more interested in talking about current events. Not that that matters."
    "At the front of the room, facing the tiers and off to the side is the professor's desk, though it's treated more like a coat rack."
    "The professor is there already. She always is."
    "Seated at the teacher's desk, she's one of the only ones to actually use it. We'll see her making her way through obscenely tall stacks of documents, pen in hand, frown on face. Small university it may be, but they work their staff hard."

    scene campus_class_profg    #shows profg at the front sitting at her desk with the provocative book.
    "Today she's not marking anything. The book she's reading from is flattened against the table."
    mc "I can't believe they would hire someone who treats books like that."
    "Nai had been looking someone else. He squints down at the professor. Finally, he shrugs."
    n "I guess they wouldn't have known. Words are meant to serve people, not be served by them. Put a bunch together and they start to get ideas, she's just reminding them of that."
    "She turns a page."
    mc "Wow, she finished the page."
    mc "I said, she already flipped the page."
    "Nai looks back over. He'd been looking somewhere else again."
    n "Wow... fast..."
    "He looks down and rummages in his bag."
    #description of professor g.
    "Professor G, that's her name, is a tall woman. She has a bit of an accent, something very slight, and if you listened to her long enough you'd begin to notice that she pauses more than natural when she speaks."
    "She dresses sharply and even looking down, her chin is raised. I imagine she's accustomed to holding power and using it in equal measure."
    "From a distance, she's intimidating. From nearer, she's unapproachable. We're not sure how old she is, but Anne was her student. So she's young, it's just a question of how exactly."
    #end description
    "Nai rises back up in his seat holding something up his hand."

    show nai_pencilcase at left

    n "Pencil case."
    "And so it is."

    scene uniclass
    show profg
    with dissolve
    #-------History-------#
    #talk history. not on the war. students continue to try to derail it.



    g "welcome back to history class. I hope you've all seen the anniversary report over the weekend?"
    r1 "that's right! I was wondering about a few things, professor."
    g "I will answer any questions you have on the previous chapter, [[that is]."
    r1 "I was wondering more about the KBA."
    g "Don't say K-B-A. Some things are worth taking the time to say properly. You can be forgiven for now on account of your youth. The Kurt-Blaney Act was a very important moment for our nation."
    g "But it's not covered in this class. There are to be no more interruptions, we've wasted enough time."

    gl "now we start nvl stuff."

    ##--?
    "she starts broadly. finally some background on the history of the nation and the KBA."
    "questions from students try to get her talking about the war: something like : what can the past tell us about the war"
    g "History repeats itself. Such a damning phrase and so often used. This is the reason many people act so indifferently towards our history. Anyone can tell at a glance it's ridiculous."
    g "If I were to rephrase it, I'd say that trends exert themselves in history, or that history is a circle. Obviously a man can die but once, a time can pass but once. Each of us is unique and the time we live in is unique and the way we experience this is unique to ourselves."
    g "This is not a good thing or a bad thing, but a lonely truth. To be different is not the same as to be rare."
    g "The point is, though patterns may emerge throughout history, we are a people who have discarded our own. Some things are perhaps not worth remembering. Even if we could predict what would happen through this, I suspect we are better without."
    g "to love your country is to know its beginning."
    nvl clear

    #-------End Social Studies-------#

    scene campus_class with longfade #class ends

    "We hover around our seats as class ends and Professor G slumps down at her desk. She tends to go on until she wears herself out."
    "Students leave in a great crowd, and the manic rush that we had avoided this morning is now in full swing. The hallway lets in the noise from the hallway: people talking and yelling and the stamp of hundreds of feet all around."
    "In a minute the front of the class is deserted. The field is open and the game can start."
    "I start down the steps towards the front of the class when I hear something that stops me in my tracks. There's just the one set of feet going down the stairs: Mine."

    show nai worried

    extend " And I remember this morning."
    mc "What, too scared to move?"
    n "No. It's just pointless. It's worse than that, really, since she won't be fooled for a second. This is no way to be treating a teacher you admire."
    mc "We don't admire her."
    n "Maybe I do. Maybe I can't think of the right thing to say because I'm worried what she'll think of me."
    mc "Really?"
    n "Not really."
    "I walk back up the steps to stand next to him."
    mc "Nai, Professor G seems fair, right?"
    n "She seems totally impartial and not at all understanding."
    mc "Don't even go that far, just focus on whether or not she's fair. She is, right?"
    n "Sure, she's fair."
    "Nai, you simple child." #mc is not very kind. at least not to nai.
    mc "If she's fair, then even if she isn't fooled, we won't lose anything. She isn't going to take any marks off our assignments. We have nothing to lose."
    n "I mean, I see what you're saying, but no one is capable of totally removing themselves from the situation like that."
    "I gesture behind myself at the Professor."
    mc "If you're that worried, just look at her. She's just reading. She won't even remember us tomorrow. Anyway, there's no reason we have to tell her our names."
    n "Well maybe, but-"
    mc "Nai, don't worry. She has a hundred students in every class. She doesn't have time to carry out a vendetta."

    show nai smile  #despite himself

    n "Have it your way, just don't expect any magniloquence from me."
    mc "Do I ever? Now let's go brighten up her day."
    "Turning around, I see something rare."

    scene campus_class_front with shortfade #prof g's desk.

    extend "There's a student talking to Professor G. I suppose it must happen from time to time when they're driven to desparation. We can hear them talking."

    show profg
    show dg_back #she's facing the other way
    with dissolve

    g "Is that right? {w=0.4}Thank you for letting me know."
    "The Professor's harsh voice."
    d "Thank you."
    "And another one. Ordinary."

    show dg #with slowdissolve #she turns around

    "My legs stop moving."
    n "Hmm?"
    "I suddenly want to run."
    n "Something wrong? {w=1.0}Dude?"
    "She walks past us on the steps. Eyes straight ahead, not even looking to the side for a moment."

    hide dg

    n "Are you alright?"
    "He's all serious now. I realize I can still breathe again, and do."
    mc "Do you know, I suddenly feel sick."
    "My voice is hoarse. I'm overreacting, I know. But I feel like a fool."
    n "Let's leave this for another day, then. Probably nothing was going to happen anyway."
    "I follow him to the top of the stairs. There's a bit of congestion around the one door, but it's much closer than the other so we head there anyway."

    scene doorjam with shortfade

    "Once we're closer I can see it's not congestion, but a crowd. Maybe ten students standing around the closed door and despite the efforts of the students at the front, it refuses to budge."
    n "Is the door locked or something?"
    "No one answers. Nai grabs the shoulder of a girl near the back."
    n "What's happening?"
    "She shrugs him off without looking back and steps deeper into the crowd. Nai looks at me, half-grinning."
    n "What's... ?"
    "I see someone at the front trying to turn the doorknob. Suddenly becoming animated, he throws his hand off. He pushes through the crowd."
    "What is it with doors that make them so attractive, I wonder." #pushing player towards trying the door. this is indicative of mc's temperment.
    "The rest of the crowd begins to dissipate and some try the door for themselves. In half a minute we're alone again and I realize I feel the same compulsion."

    menu:
        "[[Try the Door]":
            $de1 = 1
            $express +=1
            show nai grin
            "Nai grins as I try the door for myself. The handle catches partway through the turn."
            n "We just saw like five people try that exact thing."
            mc "I was feeling left out."
            "Still gripping the handle, I try to turn it again."
            "It's stuck. Well and truly stuck."
            "I nod in satisfaction."
            "He rolls his eyes."
            n "So?"
            mc "Stuck."


        "[[Don't]":
            $de1 = 2
            $repress -=1
            "I sigh."
            mc "Let's get going."

    "We're the last ones out."

    jump day1_scene1


label day1_scene1:
#-afternoon:
#meet yve. head back to dorms for her to drop stuff off. she has a different class in the morning.
#heads back to the mc+nai's apartment. play into the fake who will be the new roommate thing.' Yve is interested. why: the ppl who know her and know how she messed up all live in the dorms and she sees them on the daily.

    scene campus_hall #hallway outside class
    show nai at midleft
    with longfade

    "Someone's waiting for us outside."

    show yve imperious at midright
    with dissolve

    y "You guys are slow."
    n "Captain!"
    mc "Commandant!"

    $renpy.notify("Glossary entry \'Yve\' updated.")
    #the third musketeer. use our nice description paragraph.

    y "Yes, yes, greetings idiots. Aren't you worried people are going to think you're idiots if you talk like that?"
    mc "They'd be right!"
    n "That's what makes it so devastating."
    "No one standing next to Yve can look like an idiot."
    y "Okay okay, good work. Now,"

    show yve #normal now

    extend " there is good news."
    "As a vampire, good news for Yve inevitably means bad news for someone else."
    y "I've decided to make something of my life. I thought to myself: Enough is enough. I- {w=0.2}Are you listening?"
    "She's looking at me."
    y "Come on, fool."
    mc "I'm a fool?"
    y "Just now you looked like you were thinking about something else. Kind of rude, really. "
    mc "I wasn't."
    y "Nai."
    n "He seemed distracted when he came to sit before class. I dismissed it at the time since I thought he was upset that I beat him there even though he left first, but... "
    "He shrugs."
    n "It could be something else."
    y "I would say it almost certainly is. "

    show yve thinking

    extend "{w=0.4} Are you feeling distracted?"
    mc "You're distracting me right now."
    y "Is that right? There's nothing besides this?"

    menu:
        "'There's nothing.'":
            $de2 = 1
            $repress += 1
            mc "There's nothing."
            "Yve looks into my eyes."
            y "O-kay."
        "'There's something.'":
            $de2 = 2
            $express += 1
            mc "There's something. {w=0.5}But it's nothing, really."
            n "Oh thanks, that's really clear. Make some sense."
            mc "It's honestly too boring to share."
            y "Suit yourself."
            "She shrugs."
            y "I wish you had this attitude more often, though. Like when you're talking about rocks, or trees, or the squirrel you saw that one morning."
            y "I don't care that it was slightly orange or that you named it."

    show yve grin

    y "You know something that's hilarious? Sometimes people lie to try to make their stories interesting, but they still aren't. That's the actual most hilarious thing." #she's talking about herself.
    "She smiles to herself, but doesn't say anything else."

    scene campus

    "We leave the building. There's nothing else I have to do on campus today. My plan is to head back to the apartment and finish my schoolwork early since Anne will be wanting my help with packing in the evening. She comes back so tired, after all."
    "It's the least I can do."
    "The same goes for Nai. Yve, well, who knows what she's got going on."

    scene campus_edge with shortfade

    "We walk to the edge of campus together. To the right are the school dormitories, left is the rest of the town."
    y "Need to get something."
    "Yve adjusts her backpack and heads down the path to the dormitories. A few steps and she turns back to face us."
    y "Come on."

    scene campus_dorm with shortfade

    "The dorms are new buildings, much newer than the rest of this town, and they look it. From the outside, their walls are a bright white, and from the inside a soft gray. No expense was spared in their construction; it was tortured before facing the firing squad."
    "It has four floors and its layout is a bit confusing. I'm never sure whether a hallway will lead to the lobby or to a dead end, surrounded by rooms on every side. Between this and the staircases, I try not to come here much."
    "It must have been designed to fit as many as possible, because the passageways are just short of cramped. It's all I can do to follow Yve. When we pass a group coming down the stairs we have to turn sideways."
    "We follow Yve up to her room."

    scene campus_dorm_yve with shortfade #its a very normal room. normal mess, etc

    "The first time I went into her room, I was expecting a mess. Barring that, I was expecting something incredibly organized. "
    "But not this."
    "She acts on such extremes, a room like this feels too ordinary."

    show yve at midright
    show nai at midleft
    with dissolve

    y "Just a minute, you guys."
    "She takes a few things out of her bag and puts them on the desk. She sighs."
    y "It's such a pain to live in the dorms, you guys don't know how lucky you are."
    mc "I have an idea."

    show yve_smirk at midright #she smirking because hes playing into her hands

    y "Oh? And what's your idea?"
    mc "Ah, wait. I mean I have an idea of how lucky I am."

    show yve at midright #what a hilarious misunderstanding

    "She laughs and zips her bag shut."
    "She makes eyes at the door and shooes us along ahead of her."

    scene campus_dorm
    show yve at midright
    show nai at midleft
    with shortfade

    "A minute later we're standing back in the dormitory lobby. Far from the earlier press, it's now deserted, the students having gone to class or back to their rooms. It flows along the schedule of classes, but in the meantime, it's almost a ghosttown."
    n "We've got a bunch of schoolwork to do still. Are you coming, Yve?"
    y "Hmm, why not. I can help you with the tricky ones."
    "We step out into the sun."

    ##----------map tutorial---------##
    #map. unlocked locations: home, libraries, cafe.

    #home: jump day1_scene2
    #library: jump scene of yve saying lets not go to the library, it will be [[excuse].
    #cafe: jump scene of yve saying lets not go to the cafe, it will be too crowded.
    python:
        map_unlocks[0] = True
        map_jumps[0] = "day1_scene2"
        map_unlocks[1] = True
        map_jumps[1] = "day1_scene1_j1"
        map_unlocks[2] = True
        map_jumps[2] = "day1_scene1_j2"

    call screen map_nav_town(map_unlocks, map_jumps, map_descriptions)

#these two labels are the gang deciding to go somewhere, then yve saying let's not.
label day1_scene1_j1:
    #player clicked on cafe
    $map_unlocks[1] = False #so you can't click it again
    n "Why don't we head to the cafe?"

    show yve frown at midright2

    "We sometimes go to one of the nearby cafes to do our schoolwork. It's fine by me."
    y "I'd rather not, there would hardly be space to breathe at this time of day."
    n "No, lunch hour has come and come. This is when it'd be at its emptiest."
    y "Seriously, just think for a minute. You still have the stragglers from lunch, the early birds for supper, and whatever opportunists that thought the same as you. I guarantee it will be full." #she's lying, of course.
    "Some things aren't worth arguing about."
    return #if this doesnt work, then: call screen again? necessary?

label day1_scene1_j2:
    #player clicked on library
    $map_unlocks[2] = False #so you can't click it again
    mc "How about the library?"

    show yve frown at midright2

    extend "And that way you won't have to carry your bag halfway across the city, Yve."
    "She doesn't seem impressed by my quick thinking. Of course, I never could persuade her."
    y "I don't think so. The library kind of pisses me off."
    n "Yeah, it's too close to work for me. Can't relax."
    mc "Oh. You never said anything."
    "He shrugs."
    return #if this doesnt work, then: call screen again? necessary?


label day1_scene2:
#-late afternoon:
#help Anne move her stuff. tomorrow when she heads back into the city she'll bring the stuff to her new place. no car or anything, so she has to take it a few bags at a time on transit.

    #play sound keyinlock #like theyre turning a key or something? idk? can be a recurring sound.
    scene apartment_hall with longfade #whatever punk

    "In the end, we decided to head back to the apartment. It's still afternoon when we get there, so we'll have the place to ourselves for a few hours more."
    "Yve goes down the hall straightaway."
    y "Ah... It's so spacious here. If this were the dorms it'd fit twice as many people."

    show yve frown

    extend "Give me one good reason a person could need this much space."
    mc "To flaunt their wealth."
    n "That {i}is{/i} a good reason."
    y "Well, it's wasted on you, two of the worst flaunters I've ever seen. The fact is you've got too much space."
    mc "Sorry."
    "That satisfies her, for some reason. She moves to the end of the hall."
    mc "You can't go in there."
    y "Your sister's room? I wasn't going to. I already know what a dazzling woman's room looks like." #TODO weak. think up a better punchline.
    "She drifts back down the hall into the living room."

    scene apartment with shortfade

    "I don't know how Anne feels about people in her room, but she'd banned me from it at some point when we were kids. It's never felt right after."
    n "Did you just come here to spy on our real estate, or... ?"
    y "Of course not. Now, the hardest question, just leave it to me."

    scene apartment with shortfade

    #add value to yve (below)
    "We finish in no time at all, in part thanks to Yve's ministrations."

    y "So your sister is all set to leave, then?"
    mc "That's right. Next week."
    y "And when is the farewell?"
    mc "What, you mean like a goingaway party?"

    show yve smile

    y "What else would I mean? And you are inviting me, right? Don't think you can get away with hiding it from me. Don't think I won't ask, I'm not like you guys that have to ask for permission to breathe."
    "Nai and I exchange a look. I often find it awkward to talk family with strangers. He reads my silent question." #nai has mc's back
    n "There's not going to be a party-"
    y "That's no good. If someone's leaving then you have to throw a party."
    n "-because she said she didn't want one."
    #nai leaves

    show yve stern

    y "Children, why can't you ever think? Look, a party is not about the person it's being held for, there's only one of them after all. The other people are many and are so much more important."
    y "She probably said she didn't want one because she didn't want you to go to any trouble-"
    "Hmmm..."
    y "-or she was too shy to ask-"
    "Hmmmmm..."
    y "Or she didn't think it was worth the effort."
    n "That's the first reason again."
    y "Wait, I've got it. There is a party but you two aren't invited. She just didn't want to hurt your feelings. Well, whatever. People come and peole go. Just remember them and you'll be fine."

    show yve smile

    y "That goes for me too."

    "Just then the shrill whistle of the F-Train sounds out and fills the neighbourhood. It permeates through every imperfection in the building and asserts its presence sharply before fading just as quickly."
    "Yve raises her eyebrows. I shake my head."

    mc "Not her's, it's still too early."
    y "Your sister takes the F-Train to work everyday?"
    mc "Yeah, as far as Donnlier."
    "Yve grimaces."
    y "That's a long way. To save the money, I assume?"
    "I nod."
    mc "She didn't think she could survive the irony of having to pay to go to work."
    y "How's she moving, then? Not a hired truck, surely."
    mc "Right, not a chance. No, she's just been taking a bit at a time with her each day on the F-Train and stopping by the new place to drop it off."

    show yve shocked

    y "That's awful, she's working herself to death."
    mc "She seems fine."
    "But Yve's words strike a chord within me. I do worry that Anne has been stretching herself thin since Nai and myself came here. It's just too many things for a person to handle, piled up and up. Being on her own will be good for her."
    #nai returns
    y "she's been taking care of you guys, what does she think will happen once she's gone. replacement, fending, etc?"
    n "She says we'll have to look out for ourselves."
    y "What about the empty room? is she keeping it for herself?"
    mc "No, she was really clear about that. She's dropping the whole place on us."

    show yve smile

    extend "She's just being dramatic, really."

    jump day1_scene3

label day1_scene3:
#-evening:
#anne late coming home. everyone just waits around until yve says she has to go home.

#offer yve escort. she's fine. insist:
# -nai goes. mc has scene with anne when she calls on the relay. they talk somewhat awkwardly and mc wonders how things can change so fast.
# -mc goes. mc has scene with yve while they walk. then mc sees planes flying or something, just ambient-like. get home. at home, nai passes on anne's message.
# -no one goes. mc has scene with nai at home.
#anne's message: she's so late that there's no point coming home today. she'll be back tomorrow evening.

    scene apartment_evening with longfade #blinds pulled, pretty dark inside; only shapes, etc. no lights on inside

    "The sun sets early this time of year. We close the windows and blinds. Evening comes and we hear the sounds of the F-Train passing. And then the next."
    "Anne still hasn't returned."
    "There's nothing to be concerned about, this has happened many times since she started work. They work hard and late."
    "We decide to eat. We once waited for her and was she ever angry."
    "At some point even the faint light leaking through the blinds seems to fade completely, until you can't see anything except silhouettes."
    mc "We could try to reach her on the relay." #tech note
    n "No."
    "I can't see him, but I recognize his voice."
    "He doens't bother to explain, he knows I know why. There's little chance the relays would be available. Ever since the start of the war, essential communication has outstripped the available relays. They could always build more, but it's difficult to plan for the future when there's already more immediate danger than you know what to do with."
    "We have no guarantee Anne's even at her new apartment, she might just as well be on the F-Train. Factor in the service cost and the whole enterprise becomes more than just a waste of time. I don't particularly mind wasting money for a reason like this, but, well, Anne wouldn't want me to."

    scene apartment_evening with shortfade #same as previous.

    "After a time Yve stands."
    y "It's been fun, but curfew approaches fast."
    "Curfew. It springs back up from the recesses of my mind. There's no gate or anything on campus, but they lock all the doors. A student out too late may end up having to beg entry to the dorms or spend the night elsewhere."
    "I'd never given it a moment's thought since it doesn't apply to those of us off-campus, though it's fair to say Ane imposes a kind of curfew of her own."
    n "Wow Yve, I never thought you'd be one to care about something like curfew."
    y "There are many things I care about. {w=0.2}I'm sorry, I can't see a thing in here."
    "She flicks the light switch by the door"

    scene apartment #same scene, now bright.
    show yve at right
    show nai at left
    with brightfade

    extend "And pulls her coat on by its light."
    y "Thanks for having me over, guys."
    mc "Thanks for being an unobtrusive guest."
    n "You're leaving?"
    y "I thought that was obvious. I do hope your sister gets back soon, though. Say hi for me."
    n "Let one of us go with you then, it's dark."

    show yve grin

    y "What, think I might get lost?"
    n "It could happen."
    y "Fine, but I'm not waiting."
    "He looks to me."
    n "You should stay here in case Anne calls."

    menu:
        "'Thanks.'":
            $de3 = 1
            $nai_yve += 1
            mc "Thanks."
            n "For sure. Don't fall asleep before I get back."
            jump day1_scene3_j1


        "'Actually, I'd rather go.'":
            $de3 = 2
            $yve_rel += 1 #they spend more time together and grow closer as a result
            mc "Actually, I'd rather go. The waiting is getting a little old. I'd like to work off some of this nervous energy."
            n "Ah, I see. {w=0.1}Of course. I'll keep an ear to the relays for you, then."
            jump day1_scene3_j2

        "'Won't she be fine on her own?'":
            $de3 = 3
            $nai_yve += 1
            mc "Won't she be fine on her own?"
            y "Of Course I will."
            n "Then I'll go with you for company."
            jump day1_scene3_j1



label day1_scene3_j1:
# -nai goes. mc has scene with anne when she calls on the relay. she wont be back tonight. take care.

    scene apartment #lights on

    "The door clicks shut behind them. It's quiet again."
    "I suddenly feel it's too quiet and walk across the room to turn the TV on."

    scene apartment_tv #now the tv is on, but still normal sized. dont make it discernable.

    "It's just like always. On one channel a reporter interviews a panel of scientists, but I flick past. In another is a report on the price of goods and projections on for the next week, month."
    "The news channel is replaying the anniversary broadcast again."
    "This is not what I was hoping for, and so, defeated, I turn the TV back off."

    scene apartment with shortfade
    #NOTE play sound relay_message #not a phone ringing, but something. should be repeated with bad stuff to the point the player dreads the sound. medium length, at least a few seconds

    #use our special phone conversation thingie? maybe?
    #^I think no. the story is from mc's eyes.

    "Fifteen minutes later the relay grabs my attention. Its light is on, and it sounds."
    "?" "'Hello?'"
    "It's Anne."
    mc "It's me, Anne."
    a "Oh good. Look, I'm not going to come back tonight."
    "I look at the clock on t he wall, it's already late, so that's no surprise."
    a "I wouldn't get back until the middle of the night and then, having to leave as early as I do, it just doesn't make sense for me to come back."
    mc "That's alright, you don't have to explain it to me."
    a "I feel like I should, since you depend on me. This is going to affect you."
    mc "Then thank you. But I meant you don't have to explain it because I understand." #<-- mc's a prick.
    a "Oh. Right."
    a "Anyway, make sure you take care of yourself and that Nai does too."
    mc "Yeah. Are you alright? Where are you right now?"
    a "Oh, I'm just at the apartment- the new one. I left work just less than an hour ago and I've been home less than ten." #been 'home'
    mc "That seems too late to be working."
    a "No, it's just especially busy this time of year. That's what everyone's been telling me. It seems I picked the worst time to move."
    mc "We were ready to help you all evening, too. You must have the worst luck."
    a "Then it's a good thing I've got good friends to make up for it."
    mc "..."
    a "I really am grateful that you guys have been going along with me these past weeks." #TODO not physically going along, but helping her move, etc.
    mc "Compared to how you've been helping since I started school, since we were kids... It doesn't even compare. Is this changing your plans at all?"
    a "No, it'll be alright. I'll bring more with me the rest of the days to make up for it."
    mc "If you say so."
    a "I do. Now, you should be going to bed. I wish I could but everything's kind of a mess here. I have to find clothes for tomorrow in one of these boxes."


    show ane_cutaway #here's the idea. it cuts away to ane in a dark apartment that's very empty (because she's in the middle of moving her stuff.)
    #ane's standing in the middle with one hand using the relay other hand like: 'what the hell am i supposed to do now'
    #this image isnt full screen size, instead it overlays. probably  (3/4 x 3/4 of the screem)
    #^image should be same background as the one in day1_scene3_j2

    #wait half a second
    a "Take care, you bastard."


    #end messsage
    "I've only spoken on the relays three times before: once with my parents and twice with Anne. I can't say I love it."

    jump day2_scene0


label day1_scene3_j2:
# -mc goes. mc has scene with yve while they walk. they see planes flying overhead or something, just ambient-like. get home. at home, nai passes on anne's message.
    "Yve has already stepped outside by the time I'm ready. She's waiting just outside."

    show yve

    y "It's a beautiful night."

    scene starry_sky #its a starry sky. pretty dark.

    mc "Yeah."
    "We fall into step along the dark roads. Even this moonlit night is far darker than the city ever gets."
    "It doesn't matter, though. The path from to school and back has worked its way into my feet over the months. I feel I could do it in my sleep."

    scene street_night
    show yve
    with dissolve

    "Yve is looking more at the sky than the ground in front of her. I watch her step lightly around a crack in the sidewalk before tripping on it myself."

    show yve grin

    "She grins at me and laughs silently."
    mc "You really do know your way around here, then."
    y "Sure I do. I didn't waste every moment of my first year, you know."
    mc "You learned the streets instead of what was being taught in your classes?"
    y "I mixed and matched."
    "It was obvious was a second-year from the beginning, since she took different classes. She's still in some of ours though."
    mc "You normally avoid talking about your first year."
    y "Do I? I don't mean to hide anything, it just doesn't interest me much. I don't care much for the person I used to be."
    mc "Are they different from the person you are now?"

    show yve sadsmile #as stated.

    y "...Maybe not."

    menu:
        "'What are the differences?'":
            $de4 = 1
            mc "What are the differences?"
            y "Well, I try to be more serious now. More reliable, kinder. Just silly stuff like that."
            y "There's still a lot"


        "'What's the same?'":
            $de4 = 2
            mc "What's the same?"
            y "The same? You're not trying to make me feel better, are you? I can tell you it's the things that are the same that I want to change."
            mc "I'm not trying to make you feel anything."

    y "Enough about me. Aren't you scared?"
    mc "Of what?"
    y "Pick something. Anne being caught in a fatal accident on the F-Train, the war, whatever you want. Surely you can find something."
    "I think about it for a moment."
    mc "Is this because of what happened this evening? Because this isn't the first time Anne's hasn't made it back. I'm less worried this time, because she's got her own place to stay."
    y "If you say so."
    mc "The war... Well on TV they say there's nothing to worry about."
    y "Some people think they're lying."
    mc "I'm not sure. It's not like I have a clear idea of what's going on either. I do think they are looking out for us, though."
    y "What a convenient way to look at it."
    "She's not being sarcastic. I suppose it really is convenient, though not for convenience's sake. There's no point worrying about this sort of thing."
    "Not that that's ever made anyone feel better."

    scene starry_sky

    y "Tell me something. Which star are you looking at?"
    mc "That one, I guess."
    "She grabs my arm and sights along it. Then, slowly, she looks right at me."
    mc "What?"

    scene street_night
    show yve
    with dissolve

    "She drops my arm and steps back, starting to walk again."
    y "I was thinking. If a person wants to understand another person, how should do it? If I look at the star you're watching, I can't see you. If I look at you, I can't see the star."
    mc "This is all coming a bit out of nowhere."
    y "Just play along."
    "As a werewolf, Yve sometimes says strange things on moonlit nights."
    menu:
        "'You could look at one first and then the other.'":
            mc "You could look at one first and then the other."
            y "That works as long as neither the person or the star change, but you'd have no way of knowing whether they do. Unrealiable."
            mc "If you set up a thing with mirrors, you could arrange it to see both at once."
            y "That's where the analogy breaks down. Matters of the mind are not stars and people are not faces. Besides, mirrors are cheating."
            "I think that sometimes the point where the analogy breaks down can be as useful as the analogy."
            y "This is a general case, by the way. I can already understand you."

        "'What does this have to do with looking at stars?'":
            mc "What does this have to do with looking at stars?"
            y "Nothing. Just an analogy. This is a general case, by the way. I can already understand you."

    mc "Oh, of course. I'd assumed from the start."
    "We walk the rest of the way with the stars."

    #glossary updated
    #$renpy.notify("Yve updated")

    scene campus_edge_night
    show yve_waving
    with longfade

    $renpy.pause() #the player clicks the scene ahead

    scene street_night
    with longfade

    "It happens that on the way back, looking at the stars somewhat more than usual, that I make out a shape in the sky. First one, then three, then five, blinking lights."

    scene starry_night_planes #five planes in the sky. just specks of light.

    "They dart across the sky with such speed that they can't be stars. They must be planes, then. They pass south over the mountain, high above even those peaks."
    "A minute passes and though I strain to follow them with my eyes, I lose them one after another."

    scene apartment_evening
    show nai
    with shortfade

    n "Welcome back. Anne called."

    show nai putupon #because he got stuck with the boring job

    n "Apparently she just got off like fifteen minutes ago."
    mc "That late?"
    n "That's what she said over the relay. She said there's no point coming home tonight and that she'd be back tomorrow like regular."
    mc "I see. Well, It's good that she had somewhere to stay."

    show ane_cutaway #here's the idea. it cuts away to ane sitting with her back to a wall hands around her knees in a dark apartment that's very empty (because she's in the middle of moving her stuff.)
    #this image isnt full screen size, instead it overlays. probably  (3/4 x 3/4 of the screem)
    #^image should be same background as the one in day1_scene3_j1

    #wait half a second

    scene apartment evening
    show nai

    extend " Yeah, it must be. Do you know, for how reluctant she is to move out, she hasn't missed any opportunities to sleep somewhere else."
    n "Moving out and spending the night out are two different things entirely. You must be tired, and you've been talking to Yve, too."
    mc "Worse, I've been listening."

    show nai smirk

    n "Yeah anyway, That's all she wrote. Until tomorrow."
    "He goes down the hall and into his room, closing the door behind him. I think again about what Yve said."
    "Here's someone I've spend every waking moment with for years, is it even possible we don't understand each other? How could anyone else if we don't. Nai and I are alike in many ways. Then again, we often argue. Then again, again, they say the people who are the most alike are the ones who argue the most."
    "The more I try to think the more I feel my grasp of language is insufficient. Maybe that's the point."
    n "You thinking about something stupid?"
    "His voice comes through the door."
    mc "Yeah."
    n "Just don't stand there all night, go and have stupid dreams instead."

    #fade to black

    "I go to bed."

    jump day2_scene0

#eof
