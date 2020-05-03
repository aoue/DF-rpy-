label day2_scene0:
#day2: Secondday
#-morning:
#school. mc + nai + yve meet in class.
#yve makes mc + nai promise to head to the cafe in the afternoon.
#class. prof m. citizenship. (the revolutionary guy.)
    $date = 24

    #black screen with longfade. a day passes.

    centered "Twenty Fourth of Undim\nSecondday 07:55"


    #everyone is in class. Prof M is five minutes away from starting.

    scene campus_class
    show nai at left
    show yve at right
    with longfade

    y "So... How do we think we're going to get sidetracked today?"
    n "Is that a confession?"
    y "Really, a preemptive confession? 'It was me who thought about doing it, officer!'"
    "It's just a few minutes before the second class of the week starts. Citizenship. Between the duller classes, this one is a general favourite."
    "It helps that the professor is not like most of them here, certainly not like Professor G. On the contrary, really. Where she's all business, he struggles to stay on topic."
    "While she's a specialist in her field, he's one of his own discipline's biggest opponents."

    scene campus_class_front
    show profm # loose tie probably.
    with dissolve

    "He's a bit of a revolutionary, if anything. It's a wonder how he wound up here."
    "He's concentrating on something on his desk for now, leaning back and reading through a folder. What's in the folder though is anyone's guess. I wouldn't be surprised if he himself didn't know."

    scene campus_class
    show nai at left
    show yve at right
    with dissolve

    y "Anyway-"
    "On Secondday, we all have class together."
    y "-did you guys hear about the new hire at the cafe?" #it's her. (obviously)
    "I can't say I have."
    y "Wait, what am I saying. Of course you guys haven't. This one's way outside of your circle."
    n "What is it, then?"

    show yve dejected at right

    "Yve looks at me."
    y "You're listening, right?"
    mc "Yeah."
    n "The whole world is listening, Yve."

    show yve at right

    y "I'm not sure what that's supposed to mean, but OK."

    show yve_excited at right

    y "Word is this new hire is to die for. I would, for one."
    n "That's really something."
    y "Isn't it? They're calling her 'The Queen of the Cafe.'" #TODO think up a better title that 'the queen of the cafe.' title should be referenced later.
    n "I don't believe that."
    y "Well, not yet. But it's only a matter of time before they start. It's definitely something special."
    "She nods to herself a bit. Nai starts rummaging down into his bag."

    show yve at right #she's calmed down

    y "Something you wouldn't want to miss."

    show nai_pencilcase at left

    n "Pencil case."
    "And so it is."

    y "Aren't you guys interested?"
    n "Sure I am. Why don't we go there for lunch."
    mc "Sounds good."
    n "Yve?"

    show yve smirk

    y "I would, but I have plans."

    show yve wink

    extend " Sorry ♪" #TODO  unicode doesn't work. shows a dumb box instead
    n "... What was the point of this whole thing then?"
    mc "Obviously she wanted us out of her hair. No, I know, she's planning to rob the apartment."
    y "Hm, you learn fast. Trust me, though, this will be worth getting robbed."
    mc "I don't know, maybe we shouldn't go. I'm getting a little nervous."

    show yve smirk

    y "No, it's too late. You've committed."
    "A noise from the front of the class distracts us momentarily."
    y "It's just the Professor."
    mc "He's begun the class, I think."
    y "Mhm."

    #-------Citizenship Start-------#

    #don't even bother cutting away to him. Show just part of his portrait off to the side when he's talking or something lol
    m "Good morning, Class! Thank you for coming today, I know I don't want to be here any more than you do, ha-ha!"
    y "Oh yeah, I almost forgot. I meant to ask if your sister made it back last night?"

    if de3 == 2:
        #mc wasnt there to answer the phone, so nai says
        n "No, they had her working too late."
        y "You have a sister, Nai?"
        n "Ah, no. but I was the one who answered the phone."
        y "I see. But you understand how someone could be confused if you answered like she was your sister."
        "He shrugs."

    else:
        #mc answered the phone, so he'll say
        mc "She didn't. It was too late by the time she could have gotten on the train."
        y "That's too bad."
        mc "Yeah."

    #TODO
    #a bit of filler here where prof m starts

    #easily distracted. it doesnt work on prof g, on him it has 110% success rate.


    m "Excuse me, young lady in the back."

    show profm cross #hes not cross, but hes trying his best to look it.

    m "is there a reason you're talking while class is in session."
    y "Oh, sorry about that. There's a reason. I have to tell these guys something and it's really important."

    show profm sheepish

    m "Oh... OK. If it's really important that's alright. Take her as your example, everyone. She's living true to herself within the confines of the system."
    m "This is the kind of thing that makes me proud to be your teacher! ha-ha! Look at me, I feel proud when my students {i}don't listen to me{/i}."

    show profm upset

    m "What am I doing with my life..."
    "A woman sitting in the front coughs politely."

    show profm

    m "Right, thanks Gladys, you're an angel. Everyone, look at her. Who deserves a woman like-"
    "She coughs again, louder this time."
    m "Ahh... Look Gladys, stop that coughing thing, I already heard you. It's gross. No one is fooled by it."
    m2 "Yes they are! Now hush up and get back to your job."
    m "Gladys, I've told you before, I don't believe in this stuff."
    "He sets his chin."
    m "And I'm not going to teach what I don't believe in. This is my line in the sand."
    m2 "This is your line in the sand, is it?"
    m "Ah... Right. It is."
    m2 "So when the university fires you for not doing your job, you'll tell them this."
    m "Um... I Will..."
    m2 "And when the bank takes the house, that's alright I suppose, because you've got your line. You've got your line in the sand to keep you warm, right?"
    "He brightens."
    m "Yes! When I'm true to my heart, its burn keeps me warm on the coldest nights!"
    m2 "No dear, that's your gastroesophageal reflux, but I'm sure you'll grow to understand it much better once you can't pay the doctors. I'm glad it keeps you warm, though, you'll need it on the cold nights." #gastroesophageal reflux: heartburn is a symptom. it's a poor joke in poor taste.
    m "We'll keep each other warm, surely Gladys."
    m2 "Surely not. Your mother told me I was making a mistake marrying you, it's a shame she hasn't lived to see herself vindicated."
    m "Gladys! I'm trying to teach a class here."
    m2 "Oh, now? Now you're trying to teach a class? Don't let me keep you, it's the only thing someone will half-pay you to do."

    #cut back to the gang

    show nai at left
    show yve at right
    with dissolve

    y "I'm feeling like we don't really belong here..."
    "Yve speaks in hushed tones."
    y "Maybe we should just go, yeah?"
    n "That's not right."
    y "There's no point to staying. There's no getting off this tangent, they've got to ride it out to the end."
    n "Anne would want us to stay."

    if de3 == 2:
        y "Your sister would agree with me! Didn't she teach you guys not to waste time."
        n "My sister? Didn't you just lecture about that... ?"
        y "I wasn't even talking to you Nai."
        n "Oh... Then it makes sense I guess- "

        show nai indignant

        n "Wait, aren't you just covering up your mistake? While being as rude as you can too, for some reason."

    y "Okay, let's get going."
    n "Don't just ignore me."
    mc "Let's stay. This is the same thing we'd be doing outside, too."
    "Yve stares straight ahead for a second."
    y "Okay, let's get going."
    "She starts to get to her feet."
    mc "Sit down, Yve. You've been overruled."

    scene campus_class
    show profm
    with longfade

    "Eventually, seeing the class time rapidly disappering, Professor M gets back on topic."
    "He begins while glancing nervously at the front row, trying to smile."

    m "This class is probably the most important one you'll ever take. The information given in here is not something you can find anywhere else."
    "Despite the brief time we have left, he's incapable of being brief himself."
    m "What you really need to learn here are two things. First, your rights. That is, the limits of the government can push you to. This class is comparable to self-defense training."
    m "The other thing is just as important. What you have to do for your government, but do not disparage this. The collaboration between individual and state is a beautiful thing when handled properly. It is the duty of everyone involved to ensure that it functions as it should."
    m "I guess when put that way, it's all really one thing. It all boils to one thing, anyway, everything does."
    m "ha-ha, but you don't care right now, do you? You're thinking, 'who cares'? Not me! Well you should!"
    m "Who here is worried about the war at all? Even a little. Show of hands, please."
    m2 "Dear, this-"
    m "I'll have a show of hands, please."

    scene campus_class_hands # a few ppl, maybe 20% ?
    show profm
    with dissolve

    "A few people raise their hands. "

    #if yve asked mc about this earlier.
    if de3 == 1 or de3 == 3:

        show yve smile

        "Yve smiles at me from her seat."
        y "Well?"
        "I'm not about to raise my hand here. I'm not even sure if I'm worried."
        "I smile back."

        hide yve smile

    m "That's good. Not that you're worried- No, I mean, thank you for raising your hands. You can put them down now."

    scene campus_class
    show profm
    with dissolve

    m "Anyway, let me dispel those fears right now. We're not in any danger {i}here{/i}, for one, and there's no reason to fear conscription."
    m "Conscription? What's conscription? That's a word only the history students among you know, I'm sure. And for good reason, it's been more than a hundred and thirty one years. Now that's history!"

    show profm smile #he's smiling at his joke. Also, he never explains it. He's too caught up in his own world.

    m "Anyway, you have to be eighteen. You guys are one year too young."
    "No, that's not right."
    m "You're sixteen some of you, and seventeen some of you. Maybe this won't be any comfort next year, though, ha-ha!"
    m "Wait a second... if... Hmm, but {i}she's{/i} seventeen and..."

    show profm sheepish

    m "So, some of you are eighteen then?"
    "A chorus of yesses." #NOTE yesses?
    m "I see..."

    show profm #he recovers

    m "There's no way that conscription will come to pass, of course. Don't Worry. There'd be mass rioting in the streets, if you can believe it." #<-- prof m's opinion.

    #-------Citizenship End-------#

    scene campus_class #the class is over, so there are less people here and fewer sitting down, most are standing.
    show nai at left
    show yve at right
    with longfade

    n "See? He did get back on topic at the end there."
    y "But was it worth it..."

    jump day2_scene1


label day2_scene1:
#-afternoon:
#the group disbands and mc+nai decide get ready to go to the cafe.
    scene campus_busy #it is. there's a bunch of people all over.
    show nai at left
    show yve at right
    with shortfade

    "By the time we make it back outside, there's people all over the campus grounds. The press of bodies near the doors is crushing."
    y "If only we'd left earlier, we'd already be though here by now."
    "It's slow going, but the campus isn't that large. We're on the front walk in a few minutes."
    "At the branch to the dorms, Yve turns to leave."
    y "Okay, you two. You'd better not have forgotten your promise."
    n "Of course we haven't."
    "He looks at me."
    mc "Of course."

    show yve narrowed_eyes

    y "Okay. Well, you'll enjoy it. You should bring something to do, too. I think once you get there you may not want to leave."
    "She waves at us over her shoulder as she starts down the path."

    show yve wink

    y "See you later."

    hide yve

    show nai at cen #just a boy and his bro now.

    n "Well, I guess we have our afternoon all planned out then. Let's stop by the apartment first to drop off our stuff."
    mc "Sounds good to me."

    ##----------map call---------##
    #unlocked locations: home, library, cafe, dorms

    #home: jump day1_scene2
    #library: jump scene of yve saying lets not go to the library, it will be [[excuse].
    #cafe: jump scene of yve saying lets not go to the cafe, it will be too crowded.
    python:
        map_unlocks[0] = True
        map_jumps[0] = "day2_scene2"

        map_unlocks[1] = True
        map_jumps[1] = "day2_scene1_j1"

        map_unlocks[2] = True
        map_jumps[2] = "day2_scene1_j2"

        map_unlocks[3] = True
        map_jumps[3] = "day2_scene1_j3"

    call screen map_nav_town(map_unlocks, map_jumps, map_descriptions)


label day2_scene1_j1:
    #player clicked on cafe.
    $map_unlocks[1] = False #so player can't click it again
    mc "Alright, let's head to the cafe."
    n "Are you an idiot? I said we should go to the apartment {i}first{/i}."
    return

label day2_scene1_j2:
    #player clicked on library.
    $map_unlocks[2] = False #so player can't click it again
    mc "Let's stop by the library."
    n "I guess we have time, it's not like the cafe is going to get up and leave."
    "We head to the library."
    return

label day2_scene1_j3:
    #player clicked on dorms.
    $map_unlocks[3] = False #so player can't click it again
    mc "Let's pop in at the dorms."
    n "Oh? Have something you forgot to tell Yve?"
    mc "No, just feel like it."

    scene campus_dorm
    with shortfade
    show nai
    with dissolve

    "There are a few people milling around the dorms' lobby, but none of them give us a second look."
    n "It looks different this time of day, but smells the same."

    menu:
        "[[Go to Yve's Room.]":
            $de6 = 1
            "We find our way through the corridors to Yve's room."
            n "The lights are out. I guess she's already left. Or she's sleeping."

            show nai surprised

            n "She wouldn't go to all this pretense just to hide taking a nap, surely."
        "[[Leave.]":
            $de6 = 2
            n "What did we even come for?"

        "[[Walk aimlessly through the halls.]":
            $de6 = 3
            "Nai follows behind as I walk aimlessly through the halls. We pass a few people rushing on their way somewhere."
            n "Hoping to run into someone?"
            mc "No."
    "We should be getting a move on."
    return


label day2_scene2:
#-afternoon
#continue from after the map call.
#mc + nai head to the cafe. surprise, yve is there.
#emery is there and she toys with him for her own amusement and so she doesnt have to work hard. then she does anyway, just to prove she could.

    "After a brief stop at home we're back on the road, this time headed to the cafe."
    "Compared to yesterday the air's a bit warmer. Still cold, but a bit warmer. I wonder what this town is like other times of the year. For now, it seems unthinkable to imagine it without snow covering the ground."

    scene pessevaine #far off distance shot. this should have been used previously

    "The mountaintop is covered with snow year round, I'm sure."
    n "What do you think it does to a person who grows up here?"
    mc "What?"
    n "You're staring at the mountain."
    "I guess I was."
    n "Imagine having this collosus there with you everyday. It must warp the mind. "

    show nai smile

    n "What with its permanence, I bet people who grew up here are super calm and relaxed."
    n "Doesn't it get you thinking? How you'd be if you were from here. Or who you'd be, I guess is more correct."

    menu:
        "'I don't think it has much to do with anything.'":
            $de7 = 1
            $express += 1
            mc "I don't think it has much to do with anything. We had permanence growing up. We were always together, we had Anne, too."
            n "Ehh, I don't know if it's the same. Anne went off to school before we were even teenagers. A mountain's not going anywhere, and no matter where you go, it'll still be there."
            mc "Just like your parents?"
            "He makes a face."
            n "You know both mine and your parents are going to die, right? Not someday soon, I hope, but someday."
            "I shrug."
            mc "As permanent as a mountain may be, I doubt it's something that matters to children."
            n "Well, maybe not to children that eat mud." #mc once ate mud. no big deal. so did grif.

        "'I wonder...'":
            $de7 = 2
            $repress += 1
            mc "I wonder..."
            n "Makes you think, doesn't it? For example, maybe if you had had a huge mountain in front of your all your life, you could have given a straight answer."

    "We walk for a bit more."

    mc "What do you think about this whole business with the cafe?"
    n "I don't know what to think. On one hand it's Yve, so who knows what's going on. I'm sure we'll know once we get there."
    mc "Probably."
    n "I'd say there's a fifty-fifty chance it's the ugliest thing you've ever seen or a genuine angel."
    mc "Maybe it's a store dog or cat."
    n "Could be that. Forty-Forty-Ten chance, then. Speaking of which, isn't the spelling of forty just terrible? I mean, the number is 'four' not for. What a joke this whole language is." #sorry translators.
    "I can't bring myself to share Nai's passion for spelling right now."

    scene flashback0 #greyed out image of this from de2: y "Is that it? There's nothing besides this?"
    with dissolve

    #scene back

    "This would be just like Yve. I feel a pit forming in my stomach."
    "Objectively, it's a lot of fuss she's raising about some random person. It follows that it's likely it's not some about some random person after all."

    scene flashback1 #greyed out image of dg at the door.
    with dissolve

    #scene back

    "There's no way. To die for? I admit she's maybe a little to die for, but I feel like she'd kill me before I had the chance."
    "Then."

    scene field_dg # dg's chilling in the azalea field. there's snow in that field, you stupid girl. but under the snow, there's the flowers. No, under the snow, there's more snow. there's snow under snow.

    scene street
    #with jerk #a quick movement of the camera. i'm sure we'll have other uses for it later down the line as well.

    "I snap my head back to the road in front of me."
    "And, slowly, I find my gaze drawn back."

    scene field_dg

    "It's the girl from the door. She's sitting in the middle of a field. There's snow on the ground and a light dust on her pants. I can't imagine it's very warm. What reason could she possibly have for this?"
    "At least if she's here she can't be the new hire."
    "Slightly shaken, but on the whole more relaxed, we continue onwards to the cafe."

    scene cafe_full #its pretty full.

    "It's warm inside. The heating system accounts for some of it, but most of the warthm is from the press of bodies."
    "We find a seat amidst the lunch crowd. There's no empty tables at this time of day, but we manage to keep a bit of space from the closest group. Though you can hear everyone in here, you should pretend you can't."
    "I scan the crowd for someone in a uniform, but it's impossible to see pick one out on the floor. There's a uniformed man standing behind the counter, but the line in front of him promises to keep him there for a while."
    "I don't mind waiting a while."

    show nai

    n "It's warm in here."
    "Nai can sometimes be a little slow on the uptake. He cranes his neck to look among the crowd, just as I had done a few moments before."
    n "Do you think that's the one?"
    "He gestures with his head at the man behind the counter."
    mc "Nah."
    "He shrugs."
    n "Well, you never know. "

    show nai frown

    extend "Hey. Listen to those guys."

    $r1_name = "Naive Student"
    $r2_name = "Contrary Student"

    #the people sitting at the table next to mc+nai are the ones talking:
    r1 "She was smiling at me."
    r2 "No way. That was meant for me."
    r1 "Maaaaaan... Who knew they hired such... such..."
    "He grasps at the air like he was searching for the word amid the particles."
    r2 "Such babes?"
    r1 "No! I mean, don't demean her like that."
    r2 "What? Babe? That's hardly demeaning."
    r1 "No, it's disparaging to women. It's not nice to be called a 'babe.'" #haha dante
    r2 "What do you know, anyway."
    r1 "I know lots."
    r2 "You been called babe?"
    r1 "As a matter of fact, I have."
    "He looks sharply to his left and straightens in his chair. From where I'm sitting, the backs of the people at the next table stop me from seeing what he's looking at.s"
    r1 "There she is!"
    r1r2 "Ahhhhhhhhh." #both of them. heavy sigh.
    "They sigh the wistful sigh of the lovestruck and I can finally see the girl. The one stands up and smiles at her." #TODO better way of putting it.
    r1 "We were just talking about you, can you believe it?"
    "And she walks past."

    show yve_uniform_shaded at right #face shadowed out.
    show nai at left
    with dissolve

    $uname = "Woman's Voice"

    u "Hello you two, new here aren't you? Well, I'm new here myself, so I'm sure we'll get along fine. Can I trouble you to order, or maybe you'd prefer a little more time. Oh, and of course, I'm happy to tell you about our specials. I swear I forget that as soon as I learn it..."
    u "So, what'll it be?"
    n "{w=1,0}Seriously?"
    u "Oh, absolutely. It's definitely not normal for me, either. Normally my memory is pristine."
    "He looks at me like 'are you kidding me?'"
    n "Hi Yve."

    show yve_uniform at right #demasked!

    y "Hi, hi."
    n "That's hardly qualifies as a disguise, you know. I mean, you're still wearing the same headband as you were this morning."
    y "It's my coolest one. Anyway, it's not a disguise, it's my uniform. I work here, now."
    n "So I gathered."
    mc "Congratulations, Yve!"
    y "Thank you."
    mc "Are you sure it's your uniform, though? I think it has a mistake on it if it is." #TODO rephrase last sentence

    show yve_nametag_popup #a closeup of yve's nametag as a rectangle in the middle of the screen. small, like a pop-up. #yve's nametag is {i}Yvette{/i}. mc thought her name was just 'yve.' it never occured to him it was short for something.

    y "It's mine, and no, there's no mistake on it."
    "She looks down at it."
    y "Yeah, it's right."

    hide yve_nametag_popup

    mc "Oh, is Yve not your real name?"
    y "Of course it is. What are you talking about?"
    mc "It doesn't say 'Yve' on your nametag."

    show yve grin

    y "... You're messing with me."
    mc "I'm not. Is Yve short for Yvette, then?"
    y "Of course. What were you thinking?"
    mc "I thought your name was Yve. Just."
    y "What, Even all this time?"
    "I nod. So I can sometimes be a little slow on the uptake, sue me." #mirroring the statement from earlier about nai.
    n "Don't be silly. If her name was Yve, she'd have to go by 'Y' or something." #another joke
    y "Nai?"
    n "Of course I knew it was Yvette, Yvette."
    y "... Nai?"
    n "Yvette."

    show yve serious

    y "Yve works fine, thanks."
    n "Is this it? Have I finally found your weakness? Your fatal flaw? Kind of benign, really."
    y "Yes, it is benign. It's just a name, it doesn't matter."

    menu:
        "[[Yve.]":
            $de8 = 1
            "Nothing wrong with Yve."

        "[[Yvette.]":
            $de8 = 2
            $yve_name = "Yvette"
            "Yvette has a nice sound to it, but it looks like she prefers to be called Yve. Well, that's fine."

    n "Fine, fine. Yvette is too hard to scream anyway. " #nai accidently makes a s*x joke

    show yve eyes_narrowed

    extend " Ah- as in 'Yvette! You're tracking mud through the house!' Yve is so much easier."
    y "Mhm."

    "She eventually manages to get us to order and, after eating, Nai and I settle in for the afternoon."

    scene cafe_sparse with longfade #later on the same day, fewer people. the lunch crowd has come and gone.

    "In the eve of the afternoon the cafe empties out once again. A place like this never quite clears out, but once it's gotten as close as it ever will, Yve finds her way back to our table."

    show yve at right

    y "There's a better table over there." #yve is nice/caring
    "She points at an empty table on the other side of the room."

    show nai at left

    n "This one's fine."
    "She slumps down on the bench next to him."
    y "Fine, fine, the world doesn't stop at fine, you know. There are many layers that go beyond it. 'Good', for a start."
    mc "Are there only two of you working?"
    y "That's right. We work in pairs. Some extra people would have been helpful during the lunch rush, though, or maybe we would have just gotten in each other's way."
    mc "And the rest of the time it's this empty?"
    y "Basically. I mean, this is only my, what, fourth shift, but at this time of the afternoon, this is pretty normal. Theres's nothing that needs doing."
    n "Someone should tell the guy behind the counter, then."
    "The man who'd been behind the counter is busily wiping it down. Behind him, the sink is filling with soapy water."
    y "Oh, that's just Emery. He's supposed to be showing me the ropes, but it's been more of the reverse. Speaking of, the sink is too full. It's going to splash everywhere when he washes the dishes."

    show nai grin at left

    n "Maybe he's leaving them for you to do when you get off your break."

    show yve surprised at right

    y "Oh, I'm not on break. Emery's just giving me a hand. "

    show nai at left
    show yve grin at right

    extend "The sink is gonna overflow. Sloppy."
    "Sure enough, the sink begins to overflow. Soap and water spill over the edge onto the floor."
    y "He'll have to mop that up too."
    "She sighs and shakes her head. A moment passes and the contents of the sink continue to fall."
    n "... Aren't you going to tell him?"
    y "He'll never learn that way."
    mc "Emery, you said he was called?"
    "She nods."
    mc "Emery!"
    "He whips around. Yve rolls her eyes at me."
    mc "The sink."
    "I point at it. He springs into action and gets onto his knees, disappearing behind the counter."
    "All the while the sink continues to overflow."
    n "What's he doing?"
    y "He's cleaning up the spill, of course."
    "Half a minute passes before Yve gets to her feet."
    y "Good grief..."

    hide yve grin

    "She heads behind the counter and turns the tap off."
    n "Well. "

    show nai frown

    extend "She's not going to say anything about the way she got us here, is she?"
    mc "It doesn't look like it."

    menu:
        "'We'll have to ask her.'": #mc will have a later decision whether to ask it or not.
            $de9 = 1
            $express +=1
            mc "We'll have to ask her."
            n "Are you sure? I admit I'm curious, but Yve's way of doing things is sometimes odd. I don't know if she'd like you to point that out." #we --> you. disassociation

        "'Maybe we should just forget about it.'":
            $de9 = 2
            $repress +=1
            mc "Maybe we should just forget about it."
            n "I was thinking the same thing."

    "The two of them reappear from behind the counter. Spare of people, I can finally get a good lock at this Emery guy."

    hide nai frown
    show emery at cen
    with dissolve

    "He's wearing the same uniform as Yve, but his pants are wet along the hems from when he was on the floor. The whole thing hangs loosely on his shoulders like borrowed clothes. He looks around guility."

    show emery bashful at cen

    extend "He doesn't look much older than the rest of us."

    hide emery bashful

    "Yve starts lecturing him and he nods in rhythm with the shaking of her finger. After some time and some new directions, she walks back and sits down with us at the table."

    show yve at right
    show nai at left
    with dissolve

    y "Emery's a... well, he's not a bad guy. He's sort of like talking to a tree. I don't mean talking to him is like talking to a tree, I mean he is like the act of talking to a tree. Senseless. Maybe that's too harsh."
    "She gathers her thoughts."
    y "Emery is someone life happens to. He's living on borrowed willpower."
    n "That's quite the analysis for someone you hardly know."

    show yve frown #she realizes this, but she's known emery from childhood. She tries to cover her tracks:

    y "I've worked with him on four occasions, that's plenty."

    if de3 == 2: #referencing the star conversation.
        "She looks at me."
        y "You know what I'm talking about. I {i}understand{/i} Emery."

    if de9 == 1:
        menu:
            "[[Ask her now.]":
                $de10 = 1
                #yve doesn't think anything of this question, so no change on yve_rel. it's pretty normal to her.
                mc "Why did you invite us here in such a roundabout way?"
                y "Oh. It was funny, right? 'I would die for her.' You have to admit that was clever."
                mc "I guess so."
                y "If I could get out of dying for her, then I would. The other stuff is true, though."
                mc "That's the whole reason? It seems like a lot of effort."

                show yve frown at right

                y "Yeah, it was to set up that joke. To be honest, if I knew how little you guys would appreciate it I wouldn't have bothered." #obviously this is a convenient excuse.

            "[[...]":
                $de10 = 1
                $express -= 1 #undoes the express gain earlier.
                $repress += 1
                "I think better of asking her. Maybe Nai's right."

    n "Is he going to be alright on his own? Emery."
    y "I'll help him out if it looks like he won't make it in time for shift change. More importantly, how long are you guys planning on sticking around?"
    n "Do you want us to leave?"
    y "No, the opposite. If you guys don't mind waiting another hour, we can walk back together."

    #depending on attitude towards escorting in de3

    if de3 == 1: #nai went
        "She turns to me."
        y "I wouldn't want you to get jealous or anything."

    elif de3 == 2: #mc went
        y "Poor Nai missed his chance yesterday while we had such a lovely time."
        n "I'm sure."

    else: #i.e. de3 =3. nai went
        "She turns to me."
        y "I wouldn't want you to get jealous or anything."
        mc "Won't you be fine on your own?"

        show yve patronizing at right

        n "It's not about being fine or not fine, you bus. We can walk together because we're friends who like being around each other."
        mc "You sure told me."
        n "I'll tell you anytime, free of charge."

    y "Now, I've got to go and do my job. Just wait up."
    "We watch Yve rush around the cafe. She moves through the tasks one after another and rather than working with Emery, she's put him into a corner."
    "She sweeps and mops with tremendous speed."

    scene street_evening #while they walk back:
    with shortfade

    show yve at right
    show nai at left
    with dissolve

    y "Why would I do it slowly?"
    n "To clean it properly. It's not possible to do a thorough cleaning at the speed you were going at. You were just pushing the dirt around."
    "We're on our way back to the university dorms with Yve, and Nai and I will continue home from there. She said she had some work she needed to do tonight, or she would have come with us."
    y "That floor was shining when I was done with it."
    n "It so was not."
    "They're arguing. Yve grabs Nai's arm and pulls him to a stop."
    y "It was clean. I cleaned it myself, I should know. If you've got a problem with the way I did it, why don't we go back right now."
    "The next shift came to relieve her and Emery a few minutes ago."
    n "No... It'll be dirty again by now."
    "He's probably right. People have been coming and going along the streets, but there are far more heading towards than away from the cafe. There's been a lot of students too."
    "I try to change the subject."
    mc "It's going to be filled to bursting and then some in there. All these people going past are far too many for the cafe."

    show yve frown

    y "No, it's the normal amount. It'll be tight, but there's enough room for everyone. Take this from someone on the other side." #yve is local, so cafe -> cafes, both of them.
    n "Uh, no matter how you look at it, we've passed way more people than can fit in the cafe. There's only, like, twelve tables."
    y "There's more than twelve tables, plus the seats at the counter, plus not everyone we've passed is going to the cafe."
    n "Well, the exact number doesn't matter."
    "Some people will fight about anything. "

    scene pessevaine #far shot, same as the other ones.
    with dissolve

    extend "Isn't that right, mister mountain."

    python:
        map_unlocks[0] = False
        map_unlocks[1] = True
        map_unlocks[2] = False
        map_unlocks[3] = True
        map_unlocks[4] = True

        map_jumps[1] = "day2_scene2_j1"
        map_jumps[3] = "day2_scene3"
        map_jumps[4] = "day1_scene2_j4"

    call screen map_nav_town(map_unlocks, map_jumps, map_descriptions)

    #early evening:
    #call map. three locations unlocked: cafe, azalea field, dorms.
        #cafe: y "... we just came from there, you know."
        #azalea field: "we pass by on our way to the dorms." "expecting to find something?"
        #dorms: continue. Yve leaves them there, she has stuff to do.

label day2_scene2_j1:
    $map_unlocks[1] = False

    scene street_evening #same street
    show yve at right
    show nai at left
    with shortfade

    y "We were just there..."
    n "For all afternoon, I might add. If you want to go back, you can do so alone."
    y "Nope, it's not allowed at all. We're all going together. Now, come on."
    return

label day2_scene2_j4:
    $map_unlocks[4] = False

    scene field_footprints #same street
    with shortfade

    "We pass by that field on our way back. It's empty now, and deep in the center it's quite dark, far from the lights of the buildings or the street."

    show yve at right
    show nai at left
    with dissolve

    n "I field like we've been here before."
    y "Feel. And yes, you have to walk past it if you're headed into the city centre from this way."
    n "Ah, no- {w=0.3}forget it."
    y "I Already have."
    "I know I must have passed it dozens of times over the months I've been here, but today was the first time I noticed it."
    "The field is empty save for footprints in the snow."

    return


label day2_scene3:
#mc+nai continue home.
    scene campus_edge #outside the dorm. you should have used it plenty of times.
    show yve at right
    show nai at left
    with shortfade

    y "Sorry for taking up your whole afternoon."
    if de3 == 2:

        show yve wink

        extend " Maybe we understand each other a little bit better, now."

    mc "Happy to."
    n "We'll come visit you at work some more if you like."
    y "Tell your sister hi for me, and I'm sorry to have missed her last night."

    if de3 == 2:
        n "... {size=14}Haven't got a sister."

    "We don't have class with Yve tomorrow, so we say our goodbyes."

    hide yve
    show nai at cen
    with dissolve

    n "I am {i}tired{/i}. It feels like it takes extra energy just to exist near that girl."
    mc "And she energizes you just by being around."
    n "And then when she goes, it leaves you doubly tired. What'd she say they called her, 'Cafe Queen?' I think I can believe it."
    "It's early evening, so Anne should be getting back around the same time as us."
    "We go back to the apartment."

    scene apartment #back home once again.
    with longfade

    show nai at left
    with dissolve

    "Anne's already home by the time we get back. She's in the kitchen when Nai pushes open the door, and shouts from there."
    a "{size=30}Welcome back, you guys!" #bigger size = louder.
    n "Anne's back early."
    mc "And she's making sure everybody knows it."
    a "{size=30} What? I can't hear you guys. I'm in the kitchen!"

    scene kitchen
    with shortfade
    $renpy.pause()
    show anne smile
    with dissolve

    mc "You're cooking?"
    a "Yeah. My way of saying sorry for last night."
    mc "There's nothing to be sorry about. We live seperate lives. Don't think I'm going to hold it against you. Or anything."
    a "Oh, you."
    "I peer into the various pots and pans on the stovetop. Anne and I are about equal cooks. Rather, we're equivalent."
    "We know how to make the exact same dishes and we make them the same way. We're both just emulating the way we were taught. Anne has more practical experience, but that just means she can follow the recipe better."
    "When it comes to cooking, neither of us has much imagination. 'Recipes are something to be followed,' our parents would say. It still doesn't turn out the same as it did at home."
    "I recognize the dish immediately."
    a "It seemed suitable for today."
    "She says as way of explanation."
    mc "Thank you."
    a "Is Nai not with you?"
    "I look around and see he isn't."
    mc "He was. I'll go get him."
    a "Don't bother, I doubt even he could get lost in here. More importantly, "

    show anne frown

    extend "you didn't look like that all day, I hope."
    "My first thought is that Nai stuck a 'kick me' note or something to me and I pat myself down accordingly, but to no avail."
    mc "Something in my hair?"
    "I run my hands through my hair but I can't find anything there either."

    show anne

    a "You won't find anything there. It's not just your clothes, either. You look extra... sketchy today."
    mc "I look sketchy?"
    a "Extra sketchy, you always look it somewhat. Don't tell me you've never noticed?"
    mc "How am I supposed to notice if no one's ever told me? Why is this suddenly happening now?"

    show ane frown

    a "In that case please forget about it, I was having a joke. Please don't waste time thinking about this conversation. And don't ask anyone about it." #she wasn't

    show anne busy #she has to juggle food now

    extend "Now go and get your useless friend, you bastard."

    scene apartment_room_nai
    show nai

    "Nai's holding a piece of paper in his hand, reading it intently. He looks up as I walk in."
    mc "What have you got there?"
    "He waves it through the air."
    n "Letter from home. I noticed it on the table when we came in."
    mc "Anything for me?"
    n "Yeah, on the table. Your stack is there, same as always."

    mc "You piled all my letters? Do you have a habit of looking through people's mail?"
    n "Just the enveloppes. I don't see anything wrong with that."
    mc "Nai, you don't understand letters. They're supposed to go from the gentle hands of the sender to the eager grasp of the recipient. Letters are words from person to person, direct-like. If you go around touching letters, you break that tender chain. Frome me, {i}to Nai,{/i} to you. {i}How personal{/i}."
    n "Except, I just touch the enveloppes? I literally sort all the mail here, stop making it sound like I'm an committing some kind of crime."
    mc "Touching the outside of the letter is enough of a crime."
    n "You know someone delivered it. And someone packed it. They all touched it, too. "

    show nai grin

    extend "Really it was them who broke the chain. By the time it gets to me, there's no link left to sever."
    n "Have whatever ideas you want about letters, but don't pretend I play a part in them."
    mc "... Nai. You have ruined letters. Thank you."
    n "No problem. Did you have something to say, or did you just want to harass me some?"
    mc "Oh yeah, food is ready."
    "It seems that we have a habit of getting distracted." #TODO better phrasing

    scene apartment
    show ane at right
    show nai at left
    with longfade

    #timeskip to after supper. cleaning up.
    "It's late in the evening by the time we finish eating, cleaning up, and a variety of other things. School for me and Nai, work-stuff for Anne."
    "We're sitting down, and the room is responding to Anne like always. the light from overhead seems to focus on her and make the shadows peel away impossibly."

    a "You guys finished everything you need to do today?"
    "We say that we have."
    a "Ah, to be a student again. The work never seems to end once you grow up. Pull an allnighter and it doesn't matter, it's still there no matter how much you hack away at it."
    mc "What have they got you doing at work that sounds so terrible?"
    "She takes a deep breath."

    show ane putupon

    a "We've been going over an old prospecting mission from over sixty years ago. It turns out they missed quite a few things, things we wouldn't miss with the technology we've got these days, especially in these times. This town could become quite busy in the next few years, wait and see." #it's the mauve-augeiorite

    show ane grin at right

    a "I won't bore you anymore than that. I think the team wouldn't want me to say anything more, either."

    show ane at right

    mc "It sounds important work."
    a "Yeah. There's no way I could handle it if I didn't think it was important. All of us there do."
    n "That sounds very... expensive."
    a "Some people stand to make a lot of money at least."
    a "Speaking of money, how are you guys going to manage the extra cost of the place once I leave?"
    n "What?"
    mc "Extra... cost?"
    a "Come on, you didn't think I was freeloading here, did you? A roof over your head costs money, and I've been paying a third of it."
    n "We'll work more, I guess."
    a "You'll have to, if you want to keep the place. You could always move."
    mc "After seeing you go through that? No thanks."
    n "I second that. It's a headache we don't need."
    a "Then, your options are two, as I see it. One, you kick the working into the next gear, which is no fun at all. Or... you find someone else to share the cost with."
    n "That's easy."

    scene flashback2
    with dissolve

    $renpy.pause()

    scene apartment
    show nai at left
    show ane at right
    with dissolve

    a "Someone in mind?"
    n "You could say that. You've met Yve before- "

    show ane frown

    a "Absolutely not." #with screenshake or something #TODO
    a "Anyone besides Yve. It's one thing to get into trouble and another entirely to invite it into your house."
    "She waves her hand dismissively."
    a "No girls at all, actually."
    n "That's not very open-minded, considering."
    a "Considering what?"
    n "Well, you're a girl, for one. {w=0.2}Aren't you?"
    a "Of course I am."
    n "And you're living here."
    a "With my {i}brother{/i}. You do understand my argument, don't you? I don't want to spell it out for you, but I will."
    n "No, I get it. But I mean, I live here too."

    show ane stare #jiii

    a "{w=0.75}I don't see your point."
    mc "Nai, stop. You're embarassing yourself. And Anne, I thought you wanted us to be more independent?"
    a "There's independent and there's {i}independent.{/i} I'll let you choose, so long as you make the right choice."
    a "Don't feel rushed to decide right now, there's still got a week before the room is even vacant and after that, well, your savings should last for a while, right ~"

    hide ane frown

    "A few minutes later she goes to bed saying something about having to get up again tomorrow or something crazy like that. Nai sits them thinking about something. You can always tell when he's thinking, he does it with his whole body."
    "I wait dutifully until he breaks silence."
    n "As soon as she moves out, she can't stop us from choosing whoever we want."
    mc "She'll be back."
    n "But she wouldn't throw someone out."
    "Would she? Probably not, but it's hard to tell. I know Anne has a bit of a soft spot for us."
    n "How long can we afford to live the two of us? She didn't even tell what she was paying."
    mc "You look through the mail, shouldn't you know?"
    "He shakes his head."
    n "No, that's out-mail. And I told you I sort the mail, not read it. Like I'd want even to."
    n "Forgetting what Anne's said, who do we know that we'd consider inviting?"

    scene flashback2 #image of yve

    mc "Yve,"

    scene flashback1 #image of dg

    extend " uh,"

    scene flashback3 #image of emery

    extend " I-"

    scene apartment
    show nai at left
    with dissolve

    mc "We really don't know many people."
    n "I was thinking that."

    show nai ready at left #he's ready to go. finger pointing. he's taking the lead.

    n "Mission: find a new roommate, preferably someone very attractive.{p}Method: any means necessary."

    show nai serious at left

    n "This may yet be the most important mission we've ever faced, old friend. One that will determine the rest of lives as students here." #ironic, because the whole thing is useless.
    mc "Right!"
    n "For now, let's follow Anne's example. Tomorrow comes early."
    "We march off to bed."

    jump day3_scene0

##eof
