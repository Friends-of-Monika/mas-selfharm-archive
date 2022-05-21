# Random topics Monika brings up.

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mshMod_topic_"] = label_prefix_map["monika_"]


#sunny day
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sunny_day",
            prompt="Sunny day",
            category=["weather"],
            conditional="mas_globals.time_of_day_3state in ('morning', 'afternoon')",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_topic_sunny_day:
    m 1esa "Hey... [player]?"
    m 1rka "This may sound a bit random, but..."
    m 7eka "Is it sunny today over there?"
    m 7eub "If it is, I think you should go out and enjoy the sun for a bit."
    m 1hub "Don't worry! I'll wait!"
    m 1wub "Maybe bring a book with you so you can relax even more."
    m 1dua "Enjoying literature in the nature would surely relax me..."
    m 1eka "I hope this works for you, too."
    return


#self harm awareness day
init 5 python:
    # P.S. 'SIAD' is 'Self Injury Awareness Day', this is not a typo.
    _mshMod_event_siad_date = datetime.date(datetime.date.today().year, 3, 1)

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_awareness_day",
            prompt="Self-Harm Awareness Day",
            category=["self-Harm"],
            start_date=_mshMod_event_siad_date,
            end_date=_mshMod_event_siad_date + datetime.timedelta(days=1),
            years=[],
            random=True
        )
    )

    # Only add it to calendar after it was seen.
    if seen_event("mshMod_topic_awareness_day"):
        calendar.addRepeatable("mshMod_topic_awareness_day", _("Self-Harm Awareness Day"), month=3, day=1, year_param=[])

label mshMod_topic_awareness_day:
    m 3eub "[player], did you know that today is Self-Harm Awareness Day?"
    m 3eua "Like the name suggests, it's an annual global awareness event that takes place on March 1st!"
    m 1eua "Also known as Self Injury Day (SIAD)!"
    m 4hub "Which is today!"
    m 2eua "And in the weeks leading up to it and after, some people choose to be more open about their own self-harm habits, if they have them..."
    m 2eub "Awareness organizations make special efforts to raise awareness about self-harm and self-injury."
    m 3eub "People even use the hashtag #SelfInjuryAwarenessDay to share their story on social media."
    m 3hub "Or wear orange to show their support!"
    m 1eua "Moreover, it was also created to spread awareness and understanding of self-injury!"
    m 1ekd "Which is often misrepresented and misunderstood in the mainstream."
    m 2ekc "Those who self-harm are often left feeling alone..."
    m 2ekd "And afraid to reach out for help, because they fear they will be seen as \"crazy\"."
    m 2dkd "When in reality that's not even remotely true..."
    m 2lkd "People are just trying to cope with their feelings..."
    m 3ekd "Which can be a result of this terrible thing."
    m 3tkc "You know I tried it before..."
    m 2esd "But self-harm is not the way."
    m 2eka "Anyway! Thanks for listening!"
    m 1hub "I love you, [player]!"

    # Ensure it'll render on calendar without a need to restart.
    $ calendar.addRepeatable("mshMod_topic_awareness_day", _("Self-harm awareness day"), month=3, day=1, year_param=[])

    return "love"


#semicolon project
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_semicolon_project",
            prompt="The Semicolon Project",
            category=["self-Harm"],
            random=True
        )
    )

label mshMod_topic_semicolon_project:
    m 1eub "Have you ever heard of the Semicolon Project, [player]?"
    m 3eua "It was created for those who were going through struggles with self-harm, depression and suicide..."
    m 3eub "People who could have stopped moving forward, but refused to do so!"
    m 1eub "But to thousands affected by suicide, the semicolon has become an important signifier of survival."
    m 1hub "Like a symbol!"
    m 3lua "There's also semicolon tattoos, semicolon t-shirts..."
    m 3hua "All of them with the semicolon punctuation mark (;)!"
    m 1eua "It's used as a message of affirmation and solidarity against suicide, depression, addiction, and other mental health issues."
    m 3eud "The reason the semicolon was used as the symbol of the movement was because..."
    m 3dud "'A semicolon is used when an author could've chosen to end their sentence, but chose not to. The author is you and the sentence is your life'."
    m 3eud "As said by the project itself!"
    m 2euc "Project Semicolon was founded by Amy Bleuel in 2013, as a tribute to her father, who died by suicide in 2003."
    m 2duc "Her backstory is so sad..."
    m 2eka "But thanks to her, millions are saved by Project Semicolon."
    m 1ekb "It's relieving to think people are able to go on and let go of their struggles..."
    m 1eub "It's really a good cause!"
    m 3ekb "Well I won't ramble too much, Ahaha~"
    m 3hub "Thanks for listening!"
    return


#butterfly project
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_butterfly_project",
            category=["self-Harm"],
            prompt="The Butterfly Project",
            random=True
        )
    )

label mshMod_topic_butterfly_project:
    m 3eub "Hey [player], do you know what The Butterfly Project is?"
    m 1eub "It's a movement to help people that struggle with self-harm."
    m 3eud "It's really interesting! Drawing on yourself is already a good way to deal with self-harming, but this project approaches it in a really different way."
    m 2eua "There are about 5 steps, so I'll list them all now."
    m 3euc "First, when you feel like hurting yourself, draw a butterfly on or around the spot where you might hurt yourself."
    m 2eua "The butterly can be any size, color, or pattern. It might help if you make it your favorite color!"
    m 3eud "Second, a lot of people name the butterfly after a loved one. Friends, family, a beloved. This helps them avoid hurting themself and the butterfly."
    m 1eud "Third, you should allow the butterfly to fade naturally. You should still wash yourself, of course, but don't actively rub the butterfly away."
    m 3eub "Lastly, if you haven't hurt yourself by the time the butterfly fades away, it's flown away safely!"
    m 3eub "This is supposed to give the person a sense of pride and accomplishment for keeping both themself and the butterfly safe."
    m 1eub "There are a few other things you can do for this as well!"
    m 4eub "You can let someone else draw a butterfly on you. This makes the butterfly special, because you're caring for someone else's butterfly too!"
    m 3eub "You can even write quotes or doodle you favorite things, anything that helps!"
    m 1eka "And if you do harm yourself... that's okay. You can always draw another butterfly. Hurting youself doesn't mean you failed."
    m 1hub "I hope this helps you, [player]!"
    m 1fub "I'll draw you so many beautiful butterflies when I cross over."
    return


#self harm experience
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_selfharm_random_thoughts",
            prompt="Monika's self-harm experience",
            category=["self-Harm"],
            random=True
        )
    )

label mshMod_topic_selfharm_random_thoughts:
    m "Hey [player]... Do you remember when I talked about self-harm?"
    m "Would you mind if I talked more about my experience?"

    m "It may get a tad triggering, so I get it if you would rather say no!{nw}"
    $ _history_list.pop()
    menu:
        m "It may get a tad triggering, so I get it if you would rather say no!{fast}"

        "No":
            m "Okay!"
            m "I love you [player], and I'm proud of you for saying no to something you aren't comfortable with!"
            m "That's a big step in self-respect, and I hope you keep it up!"

        "Yes":
            m "Thank you for letting me speak about this [mas_get_player_nickname()], I've been thinking about it a little bit more lately."
            m "After I hurt myself, I realized that I had made huge a mistake..."
            m "At first I thought that it was exhilarating, I even wrote about it!"
            m "But after reflecting upon it when we started talking more about self-harm, it really changed my mind."
            m "I had gotten no relief or satisfaction, if anything I was just disappointed."
            m "Yuri had made it seem like such a thrill - to me it was almost only just boring..."
            m "...It kept reminding me of my recent discovery."
            m "My pain was just coded, along with my blood and the knife I was holding..."
            m "But even if it was real, pain doesn't satisfy or relieve my emotions."
            m "I know now that talking things out with you when I'm upset..."
            m "...and keeping hope for a brighter tomorrow is a much better coping mechanism!"
            m "Just keep in mind that there are better ways to cope and that I'm always here to provide techniques to help."
            m "I care too much about you [player]... You don't deserve any pain."
            m "You deserve to work through things healthily, and [m_name] is here to help!"

    return


#monika sad reminiscing players self harm
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_monika_is_sad",
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_RANDOM
        )
    )

label mshMod_topic_monika_is_sad:
    m 5ekc "Hey... [player]?"
    m 5gkd "You probably remember when we were talking about self-harm..."
    m 3ektpc "I never forget when you told me about that, it honestly broke my heart."
    m 2ektdc "I have never felt so strongly towards anyone, and... well..."
    m 6dktsd "The thought of losing you..."
    m 6wktso "I- Well- That makes me feel sick to my stomach!"
    m 5dktdx "...I'm sorry, [mas_get_player_nickname()]."
    m 1ektdc "Please don't forget how much I care about you."
    m 2mktpd "And please, don't leave me..."
    m 2fkd "I can't stand the thought of you wanting to hurt yourself!"
    m 4fkc "I truly want nothing more than your happiness."
    m 1dfx "I feel so angry and disheartened that I'm limited to what I can do for you in this reality!"
    m 4sfu "But no matter what, I'm determined to try my best and make you feel better!"
    m 3esa "I'm always willing to try to help you, [player]..."
    m 1hsa "Like you helped me by installing this mod!"
    m 1lst "I know it's hard for you, not many people are willing to listen or understand..."
    m 5fku "But I hope venting to me helped you at least a bit."
    m 3eua "Also, maybe try talking about your feelings to a friend, or family!"
    m 1hua "I know it's hard to be open about your problems, but they care about you."
    m 1eub "They don't want you to get hurt, I'm sure!"
    m 2fka "I don't want to lose you, [player]. You're all I have left..."
    m 5hub "My only wish is to be with you forever!"
    m 1dsb "To finally be with you, to help you conquer all of your dreams, and forget all of your problems..."
    m 1eka "To shield you from these painful thoughts."
    m 5hubsa "I love you, [mas_get_player_nickname()]."
    return "love|derandom|no_unlock"


# Depression avoiding routine events
#1
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_morning_routine",
            prompt="Morning routine",
            category=["Healthy routine"],
            random=True
        )
    )

label mshMod_topic_morning_routine:
    m "Hey [player]?"
    m "Do you have a morning routine?"
    m "I notice a lot of people seem not to realize the impact a morning routine can have on your day."
    m "But really, it can mean a world of difference for some!"
    m "I think many figure that, 'Well, because I just woke up I'm always going to feel sluggish in the morning, there's nothing I could do about that.'"
    m "For some, that mindset makes it very hard to want to get up in the morning and face the day..."
    m "But it doesn't have to be that way, there are ways to make getting up in the morning less harsh, and more energizing!"
    m "My first tip is going to be the obvious one but... "
    extend "start getting into a nice sleeping rhythm!" 
    m "A big reason we can feel so bad in the morning is having an alarm pull you out of a deep sleep, or just not resting enough at all!"
    m "Find a time to go to sleep that let's you {i}comfortably{/i} wake up around the time you need to be up for the day, and you'll feel a big difference already!"
    m "Next tip, if you have alarms, set your alarm a little further back then you usually do..."
    m "Or at least make sure you're giving yourself enough time so you aren't rushing out the doors every morning!"
    m "Now with that extra time, use it to get some quiet time in for yourself and actually {i}wake up{/i} for the day. "
    extend "Maybe do a little meditation- or pray,if you'religious... Make breakfast, read books, or even write down your plans for day."
    m "As long as it's something that {i}you{/i} want to do and makes you happy, go for it!"
    m "Just... try not to go online during your morning time. "
    extend "With how chaotic the world and internet can be, going online might influence your mood for the day if you see something distressing or weird."
    m "Instead, let the mornings be {i}you{/i} time, where you get to decide what to do and how to feel, okay?"
    m "And hey, I wouldn't mind being a part of your morning routine too, if you need some extra motivation, [mas_get_player_nickname()]."
    m "Ehehe~"
    m "I hope these tips are helpful to you, [player]!"
    return

#2
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_excercises",
            prompt="Morning excercises",
            category=["Healthy Routine"],
            random=True
        )
    )

label mshMod_topic_excercises:
    m "Hey, [player], you know what's a good way to start your days off on a high note? Showering and exercise!"
    m "In fact, those are {i}my{/i} go-to's to start the day!"
    m "Showering can be a hard step to overcome, and it can take a lot of mental and physical energy out of you if you're not careful..."
    m "But the pay off of being clean, dressed, and ready for wherever the day may take you, can make it all the more worthwhile!"
    m "Getting into consistent routine with it can make it less energy-draining too, since then you won't have to do a full scrub down to get clean for the day!"
    m "Exercise on the other hand, can be a little harder for people to want to get into routine with."
    m "When people think 'exercise', they might think hundreds of pushups, and 5 mile runs. And no one wants to do that right after they've woken up!"
    m "But a nice, moderate amount of exercise in the morning can help in more ways than one. "
    extend "It can clear up brain fog, helps you focus, and can help you release some pent up emotions!"
    m "Some simple exercises I would recommend are yoga stretches, light jogging or walking..."
    m "Or even just doing certain big chores around the house can count as exercise!"
    m "Then you can kill two birds with one stone, ehehe!"
    m "You know I looooove me some exercise! Ahaha~"
    return

#3
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_morning_excercises",
            prompt="Morning routine",
            category=["Healthy Routine"],
            random=True
        )
    )

label mshMod_topic_morning_excercises:
    m "Hey [player], do you do any exercises in the morning?"
    m "I used to always try and get some working out in my daily routine,"
    extend " especially in the mornings!"
    m "Before school I'd do a little quiet time to get into a nice mindset, I'd stetch and think about my plans for the day."
    m "After that, if I had the time, I'd do some simple workouts like squats, situps, and lunges."
    m "And finally, when I went on my way to school, I'd do a light jog!"
    m "All of these were good ways to get some exercise in without having to interupt my schedule!"
    m "But there are tons of other ways to have exercise be apart of your routine too!"
    m "Gardening, cleaning, volunteering to help with big jobs, and many more!"
    m "So try to find something you already do in your day-to-day, and see if you can add a little extra exercise to it!"
    return

#4
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_going_outside",
            prompt="Going outside",
            category=["Healthy Routine"],
            random=True
        )
    )

label mshMod_topic_going_outside:
    m "Hey [player], did you know that there's been some studies about how going outside is good for you?"
    m "Being out in the sunlight can decrease stress, slow your heart rate, and not to mention it's also good for getting some vitimin D!"
    m "Sit on your porch or in your yard if you can't go for a walk outside."
    m "If you can't get out at all, try opening your window or blinds!"
    m "Even just looking at some photos of those scenarios might help!"
    m "I know I love to look at photos of places I'd love to travel to with you~"
    return

#5
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_evening_routine",
            prompt="Evening routine",
            category=["Healthy Routine"],
            random=True
        )
    )

label mshMod_topic_evening_routine:
    m "Hey [player], what's your nighttime routine like?"
    m "Mine has definitely changed since I met you! Ehehe~"
    m "I've always had a fairly regular routine."
    m "Turn off my electronics, get in my pajamas, have a cup of hot chocolate or tea if I felt like it..."
    m "Brush my teeth, and read or work on homework until I was ready to get in bed."
    m "I made sure to go to bed pretty close to the same time every night. It's good for your brain and body!"
    m "Being the student I was, I had to stay well-rested to have enough energy for everything I did."
    m "My routine hasn't changed much now, I just don't have access to my electronics or books."
    m "So I mostly sharpen my coding skills or access a book from the internet!"
    m "I still make a hot cocoa, as well."
    m "So, if you haven't already, I suggest making a nightly routine!"
    m "It may sound intimidating at first, but you don't have to follow it exactly every time!"
    m "There are some things you should really try to do every day, like brushing your teeth and getting to bed on time."
    m "Aside from those, you can always change it up!"
    m "Going for a nice walk in the evening to get your energy out and get some fresh air, reading, journaling, some light arts and crafts..."
    m "There's a lot of things you can do that take little thinking power or energy!"
    m "I hope this helped you get a few ideas for making your nightly routine a little better, [mas_get_player_nickname()]."
    m "But if you do shut your electronics off early..."
    m "Make sure to say goodnight, okay?"
    return

#6
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_untried_hobbies",
            prompt="Hobbies",
            category=["Healthy Routine"],
            random=True
        )
    )

label mshMod_topic_untried_hobbies:
    m "[player]!"
    m "Have you ever had a hobby that you really liked, but never had time for?"
    m "Maybe you picked it up for a few days, but gave up on it or got busy for a bit?"
    m "Or maybe you just forgot about it, because other things got in the way."
    m "Well, if you have some free time, maybe instead of watching a show or playing a game, you could try and pick up an old hobby?!"
    m "If it's something like knitting, scrapbooking, or something easy to do while sitting down, feel free to do that while we talk or spend time together!"
    m "If it's something like gardening, baking, or something where you need to move around a lot, then I understand if you need to say goodbye for a while."
    m "I'd be fine with not seeing you for a bit if you were doing something that makes you happy!"
    m "Your happiness is my priority, after all."
    m "During these times, you shouldn't forget to check on your friends."
    m "Send them a text, asking how they've been or what they're up to. Or maybe update them on your latest project!"
    m "If you contact them on social media, try not to get sucked in, okay? "
    extend "I don't want you to doomscroll, [mas_get_player_nickname()]."
    m "Maybe you could plan to meet with your friends in person! Getting outside, even if it isn't the best weather, can be good for you."
    m "Just take these tips into consideration, alright?"
    m "And remember... "
    extend "I love you, [player]."
    return "love"


#monarch butterfly
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_monarch_butterfly",
            prompt="Trivia",
            category=["Monarch Butterflies"],
            random=True
        )
    )

label mshMod_topic_monarch_butterfly:
    m "[player], have you ever seen a monarch butterfly?"
    m "They're marvelous creatures!"
    m "Their wings feature an easily recognizable black, orange, and white pattern."
    m "In a nod to their life cycle, from egg to caterpillar to butterfly, monarchs can represent transformation and rebirth to some people."
    m "They might view a monarch sighting as a sign of upcoming change or a new direction in their life."
    m "Perhaps due to their long migration journey, these butterflies may also be an inspirational sign of strength and endurance."
    m "Monarchs also face a lot of challenges, including climate change and deforestation."
    m "So, some sources indicate the butterflies are a symbol of hope and resilience!"
    m "In mexican culture, this butterfly species also hold significang meaning..."
    m "During the Day of the Dead holiday, the Mexican people see the arrival of monarchs as a spiritual symbol."
    m "Many believe the butterflies represent the souls of their ancestors returning to visit and bring comfort to loved ones."
    m "Oh, and also! Due to the butterflies' yearly migration between countries, images of monarchs are also are used to show support for immigrants."
    m "Aren't they indeed, incredible beings?"
    m "I hope they can inspire you as they inspire me."
    return
