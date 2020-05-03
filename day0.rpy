##day 0 - undim 22 ##

label day0_scene0:
    #day 0: seventhday
    #-evening:
    #news, introduce kurt-Blaney act, the war.
    #introduce Anne, nai, and mc's background
    #Anne comes home bearing food and whatnot.

    $persistent.act = 1
    $date = 22

    centered "Year 131"
    $renpy.pause(1.0)
    centered "Twenty second of Undim\nSeventhday, 18:00"



    #play sound news_jingle #the intro jingle for the war programme
    scene newslogo with longfade #create a special transform for the news logo. should be it appearing and then holding for a second or two.
    scene sineb_bank #where the war correspondant reports from. on a hill overlooking a base.
    show tvannouncer

    tv "All that is good comes from within. It was one hundred and thirty-one years ago that our forefathers, in their wisdom, destroyed the bridges and the tunnels, the harbours and the lighthouses, the airports and the observatories.'Keep thee within and banish that which is without, so that you may find the fruit of your isolation.' And we have prospered."
    tv "Today, on its anniversary, let us celebrate the peace that held for one hundred and thirty-one years and the new age it brought with it. Let us remember the words of our ancestors and remember the wisdom they each held, and thank them for their guidance."
    "The television host shifts uneasily on the dirt."
    tv "Today, I have been forced to do something we wished never to do. This is not the soil of our land."
    "He gestures at the ground around his feet."
    tv "It is the necessity of our time that a child is pulled away from his homeland."
    tv "Today more than ever we must remember that all that is good does come from within. The peace and prosperity we found in our nation may no longer exist, but a part of it persists in the minds of each of us, for it is we built it together to begin with. Keep hold of it, for your country will need it again."

    scene apartment_tv
    show nai

    #activate nai's entry in the glossary. the glossary is a way to introduce a character without rambling exposition. The entry's can be updaed as the story progresses.
    #information should be of the nature: name, age, short background, relation to mc, mech(later). All written from mc's point of view, things he noticed about them.
    #update them when the character dies too.
    ##glossary subversion:
    #after the events of the end of act I, go back and modify everything to show mc's distate with life kind of thing. the entries will be altered in tone and be rude/confrontational.

    $renpy.notify("Glossary entry \'Nai\' updated")

    n "Your sister's here."
    "He looks over at the TV."
    n "What's this?"
    mc "The Kurt-Blaney Act anniversary broadcast."
    n "Oh, is that still on? A bunch of us saw it together this morning."
    mc "They've been running it all day."
    n "And you're just watching it now. Be warned, it gets zesty."
    hide nai
    "He sits on the floor near the TV."

    #some kind of transition
    scene sineb_bank with shortfade
    show tvannouncer at midleft
    show lord_chairman at midright

    "There's a second man on the screen now, standing to the right of the host. I don't recognise him."
    tv "Thank you for joining us, Lord-Chairman."
    lc "Of course."
    "He nods gravely. He looks different from the last time I saw him, not in person of course. Two years since then, I think?"

    show tvannouncer interviewing #he's asking questions now, and he looks different doing it.

    tv "Lord-Chairman, I believe there were some developments yesterday the people are entitled to hear."
    lc "Of course."
    "Again comes the dignified nod. He thinks in nods, this man."

    lc "Yesterday, the Second Army conducted a series of raids on the enemy's positions along the Sineb River. They succeeded in loosening his grip such that they were forced to give up the position or risk encirclement."
    lc "Yesterday was the first time anyone has set foot on foreign ground since the Kurt-Blaney Act, hence the offensive location. This is a day for the marking, both of our victory in arms as well as our defeat in the means we were forced to undertake to achieve it."
    lc "We are on the enemy's soil, if not quite in its nest. Would that this is the beginning of the end of the war."
    tv "Sobering news, Lord-Chairman, but I share your optimism. How is the Second Army holding up through all this?"
    lc "Splendidly. They're missing home but have never been higher on morale. They have the same feelings as you and I in their hearts. No, there is no shortage of eager men and women among the soldiers of the Second Army."
    tv "I'm- We're all glad to hear that. And the First Army, how do they fare?"
    lc "They fare well."
    tv "I understand positions held by the First Army were recently supplanted by the Second Army?"
    lc "That is correct. The First Army is now undergoing recuperation and maintenance that became necessary after a number of engagements with the enemy."
    tv "What can you tell us the rumours of divison between the first and the second armies? Is there any cause for concern?"
    lc "Absolutely not, there is no place for emnity in a professonial army. Are we not all from the same land? Did we not grow up in the same towns and use the same roads? "
    tv "Well said, Lord-Chairman. I am reassured to know the First Army has such a wise and well-meaning man at their head. I hope that anyone watching tonight will think hard about what you've said."

    scene apartment_tv with shortfade

    mc "Didn't you say something when you first came in?"

    show nai

    n "Ah yeah, Anne's here."
    mc "She's taking a long time."
    n "You mean you are. How long exactly are you planning to make her wait outside?"

    scene apartment with longfade
    show nai grin
    show Anne frown

    mc "I'm really sorry! I didn't know you were waiting outside, well I did, but not that you were waiting."

    show Anne armscrossed

    extend "{w=1.0}It's Nai's fault."
    a "Hmmmmm?"

    $ renpy.notify("Glossary entry \'Anne\' updated")
    #unlock Anne entry.

    n "I didn't do anything-"
    show nai affronted #betrayed, shocked, etc
    extend "Don't blame this on me!"
    mc "I'll blame it on you if it's your fault."

    a "It's alright you two, don't fight. I know you didn't mean it."
    mc "Nai was the one-"
    a "I said there's no harm done. Listen to your sister, okay?"
    show Anne smile #otae smile more like
    a "Good boy. And more importantly, turn that off. People have been talking about all it week and little else since it aired. I'm sick of it."
    mc "This is huge, you can't just be sick of it. The first people to leave in more than a hundred years!"
    a "They don't deserve to suffer like that. You should know better to take interest in people's suffering."
    mc "Well, I'm not, but I can't help being interested in what's happening. It's monumental."
    a "It'll still be monumental tomorrow, you bastard. Turn it off."
    #unlock more Anne entry. adds a 'you bastard' to the end.

    scene apartment

    "I do as she says. I can't really muster the energy to argue with her given the circumstances. I don't want to fight with her right before she goes."
    "She's moving out this week. Having finished her degree earlier this year, she's been on the hunt for work all of Autumn. Work is somewhat scarce for geologists in this climate, so the place she ended up finding is in the next city. Living here while working there is silly, it's just too far."
    "She could take the M-Train, but when I suggested it she brushed it off. Too expensive to pay every day, she said. She's been taking the F-Train to work in the meantime. It's free, but it means she has a lot of travel time, so it's not so free in that way."

    #M-train: maglev. very fast, but expensive.
    #F-train: free train. not fast, but free for anyone!

    scene kitchen with shortfade

    "Anne moves to the kitchen, trailing us along behind her."

    show Anne

    "Unpacking the bags she brought in with her, she gives us a quick rundown on what we should or shouldn't eat. Since she was living here long before either Nai or myself, it's her way that goes. That will be another change."
    a "You'll have to feed yourselves. Make sure to eat everyday."
    mc "It's not like we could forget that."
    a "I won't be able to keep an eye on you guys all the time anymore, so you need to keep an eye on each other."

    show Anne serious

    a "With the half brain each of you has, you stick together and you'll be alright. Or maybe that would be worse... one half times one half is a quarter."
    n "We'll be sure not to multiply our brainpower."
    a "Feel free to multiply it, just not by each other's. If you want to give me a parting gift feel free to double the size of your brain."
    "They keep talking nonsense."

    scene apartment with shortfade

    extend " I head back into the living room. If Anne's too busy to notice, she won't mind if I finish the broadcast. I'll keep it quiet."
    "I turn the tv on."

    scene apartment_tv
    #play sound static

    scene sineb_bank
    show tvannouncer
    show lord_chairman at midright

    tv "-And what about after the war?"
    lc "After the war will be a different time. Our isolation has been ended, that was beyond our power to prevent. But cannot a thing ended be started Annew?"
    lc "We are concerned that the men and women of the Second Army will be haunted by this experience after it has ended. It is a horrible thing to wake up in an unknown land."
    tv "Do you have anything to say regarding the post-war occupation?"
    lc "What occupation?"
    tv "That is to say, the possibility of military occupation of the foreign lands, maintaining a presence the land beyond the Sineb."

    show lord_chairman patronizing #patronizing smile

    lc "First rumours, now possibilities? And who would you have me put across the Sineb? Surely, that is too cruel."
    tv "Of course, Lord-Chairman. It's just that there has been talk."
    lc "Then I will make it so that there can be no talk. These are the facts: There will be no occupation. We are a people best-suited to our homeland."
    lc "Pity the soldiers beyond the Sineb, who have died once just in crossing, and hope that they return home without having to do so again." #they die once just by leaving home.
    lc "We are not a nation of {i}conquerors.{/i}"
    "He spits the last word."
    tv "Of course not. Our last item for tonight, Lord-Chairman: I understand the usual commemorations are not going to be held this year to mark the Kurt-Blaney Act?"

    show lord_chairman bitter #a bitter smile

    lc "It hardly seemed appropriate to celebrate something while we live its contradiction. Next year, perhaps."
    tv "Certainly, I'm sure I'll see you there. And to all our viewers-"

    scene apartment_tv
    show Anne frown at midright #not mad, just confused. how could you be doing this after what i said to you?-type of thing.

    mc "Sorry."

    scene apartment

    a "Station One's broadcast?"
    "I nod."
    a "If you want to fill your head with propaganga that's your problem, but not while I'm here. I'm supposed to be keeping an eye on you, what will Mom and Dad say when they see your brain's turned to mush?"

    show nai at midleft

    n "It's all lies, anyway."
    mc "How do you know?"
    n "They're hardly going to be telling the truth to everyone. The truth is a hammer, it has no sensibility, but a lie is like a wedge."

    show nai excited #he gets excited like a fool

    extend " Lift or hold or whatever you want. A well-placed lie delivers just enough force to the right place."
    a "What did I say? Talk about this some place else, you bastards."
    "As Anne sits down in the living room the place seems to straigten up, like a dog running to greet its master at the door. 'Sit pretty,' she says, and the room does."
    a "You know, there's more to keeping this place alive than you think there is. There's the plants, for one."
    "I have a feeling that terrible things will be done to those plants."
    a "There's cleaning, too. That can take a lot of time if you let it pile up. I'm not going to keep taking care of this place, I'll have my hands full on my own."

    a "This is a lot of responsibility for you two to take on. {p=0.5}Are you sure you'll be alright? The F-Train takes only two hours, so it wouldn't be too much to come back a few times a week."
    "Nai and I exchange a look."
    "I do love my sister, hell, I even like her, but do I want to live with her? See her now and then, certainly, but not everyday. For living in a new town, there's still a lot of familiar people."
    "I would, I think, like less of that. This is when I'm supposed to be expanding my horizons, not hiding behind my sister's skirts."
    mc "Don't be silly, you have to take this step. There's nothing for someone with your skills in this town; you've outgrown it. You can't keep looking after me forever."
    n "Besides, you somehow managed it on your own for four years. Have some faith in your brother."

    show Anne gentle     #she momentarily softens, she's beginning to be convinced.
    $renpy.pause(0.5)
    extend " He's got me."
    show Anne frown      #she realizes that, in fact, mc does.  haha youre not funny moron. this is a stupid and terrible joke. be embarassed

    a "Well, fine. Even if you two do tend to get into trouble, you also tend to get out of it. You're slippery like eels."
    mc "Nai is the one who gets us into trouble, I get us out."
    n "Shut up, you eel."
    "He hesitates."
    n "The Eel goes what? I want to say some kind of scarfing?"
    a "They hoot."
    "She answers absentmindedly She truly os the backbone of this house."
    a "Don't worry, this won't be long. If it doesn't work out, we'll figure something out back at home during break."
    "I can't help but smile at that. After three months away from home, I find myself looking forward to going back more all the time. Mom, Dad... There's something to be said for freedom(bw), but home is home. It can't be beaten yet, it has a decade of nostalgia on its side."
    "I wonder how long it will be until this place feels like home."

    #end of scene. I feel like it went okay.

    jump day1_scene0




    #eof
