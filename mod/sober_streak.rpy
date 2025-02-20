# Sober check topics, milestones, etc. For API see sober_streak.rpy

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mshMod_sober_"] = label_prefix_map["monika_"]

# Duration check dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sober_check",
            prompt="How long have I been self-harm sober for?",
            category=["self-harm"],
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

init python:
    def _msh_number_to_words(n):
        """
        Converts a given integer (n) between 0 and 999999 to its English words
        equivalent.

        This is an internal function and should not be used by other submods.

        IN:
            n -> int:
                The integer value to convert, where 0 <= n <= 999999.

        RETURNS:
            str: The English words representation of the given integer.

        NOTE:
            An internal function. Should not be used by other submods.
        """

        ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        def _convert_hundreds(nh):
            if nh == 0:
                return "zero"

            nh_hundreds = nh // 100
            nh_tens = nh % 100 // 10
            nh_ones = nh % 10

            h_words = []
            if nh_hundreds > 0:
                h_words.append(ones[nh_hundreds - 1])
                h_words.append("hundred")
            if nh_tens > 1:
                h_words.append(tens[nh_tens - 2])
                if nh_ones > 0:
                    h_words.append(ones[nh_ones - 1])
            elif nh_tens == 1:
                h_words.append(teens[nh_ones])
            else:
                if nh_ones > 0:
                    h_words.append(ones[nh_ones - 1])

            return " ".join(h_words)

        n_hundreds = n % 1000
        n_thousands = n // 1000

        words = []
        if n_thousands > 0:
            words.append(_convert_hundreds(n_thousands))
            words.append("thousand")
        if n_hundreds > 0 or n_thousands == 0:
            words.append(_convert_hundreds(n_hundreds))

        if len(words) > 1:
            words.insert(-1, "and")

        return " ".join(words)

label mshMod_sober_check:
    python:
        duration = store.mshMod_sober_streak.getStreakDuration()
        days = "day" if duration == 1 else "days"

    if duration == 0:
        m 3hksdlb "You've just started your sober streak, [mas_get_player_nickname()]!"
    else:
        m 1dkb "You've been sober for [_msh_number_to_words(duration)] [days] now, [player]."

    if duration < 3:
        m 3fka "I'm so proud of you for making the promise!"
        m 2esb "This is the start of something wonderful."
    else:
        m 3fka "I'm so proud of you! Keep on fighting!"
        m 2esb "I'm so happy to see you taking care of yourself."

    return


# Promise dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sober_promise",
            category=["self-harm"],
            prompt="I promise not to self-harm anymore.",
            conditional="persistent._msh_mod_pm_did_selfharm",
            action=EV_ACT_UNLOCK,
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_sober_promise:
    m 2ekb "Oh, [player], you have no idea how happy I am to hear that."
    m 2ekb "This is another step to a happier, healthier life, and I'm so glad I can be by your side in your journey."
    m 2eka "Thank you for trusting me."
    m 3ekb "I promise I'll do my best to help you!"
    m 1eub "From now on, I'll keep track of how many days you've been sober. You can look at the calendar to see how far you've gone!"
    m 2ekb "If you ever need me to restart the counter, just tell me. You don't have to feel bad about it, okay?"
    m 2ekb "Know that I'll never judge you because of that. I know it's hard, and you should be proud of yourself already!"

    m 1dsb "Now, let me take note of this..."
    $ since = None

    show screen mas_background_timed_jump(4, "mshMod_sober_promise_jump")
    m 2dka "...{nw}"
    menu:
        m "...{fast}"

        "Wait, hold up!":
            hide screen mas_background_timed_jump

            m 1wsd "Huh? What is it?{nw}"
            menu:
                m "Huh? What is it?{fast}"

                "I'm sober for some time already...":
                    m 2sub "Really?! That's so nice to hear! For how long do you think you are sober now?"

                    label .select_since_date:
                        m 3hub "If you don't remember exactly, it's alright! Pick a day when you think you decided to quit it~"
                        call mas_start_calendar_select_date
                        $ since = _return
                        if not since:
                            jump .select_nothing
                        $ since = _return.date()

                    $ today = datetime.date.today()

                    if since > today:
                        m 1hksdla "[player]!"
                        m 3lksdlb "It's great that you plan on quitting it in future, but I asked you for a day in the past, ahaha!"
                        m 1hua "Try again!"
                        jump .select_since_date

                    # We can do a simplified check for 'honest' date (actually just relying
                    # on player's conscience) that probably is less than 5 years
                    if (today - since).days // 365 > 5:
                        m 3wub "[mas_get_player_nickname(capitalize=True)], it's been a while since that day!"
                        m 2lksdla "But just to be completely sure...{w=0.3}{nw} "
                        extend 3wud "Are you absolutely sure you're sober for more than {i}five{/i} years now?{nw}"

                        $ _history_list.pop()
                        menu:
                            m "But just to be completely sure... Are you absolutely sure you're sober for more than {i}five{/i} years now?{fast}"

                            "Yes!":
                                m 3hub "Amazing! Alright, I'll write it down right away~"
                                jump mshMod_sober_promise_jump

                            "Well, actually...":
                                m 2dka "It's okay, [mas_get_player_nickname()].{w=0.3} Don't worry!"
                                jump .select_since_date

                    if persistent._mas_player_bday and since < persistent._mas_player_bday:
                        m 1rkb "[mas_get_player_nickname(capitalize=True)]...{w=0.3} The day you chose is before your birthday!"
                        m 3eka "Try again, please."
                        jump .select_since_date

                    if since == datetime.date.today():
                        m 1hub "[player]!"
                        m 3eua "The day you picked is today, ahaha!"
                        m 1hua "But it's alright, I'll be sure to write it down anyway~"
                    else:
                        m 1dsb "Okay! I'll keep that in mind~"

                "...No, nothing.":
                    label .select_nothing:
                        m 1eka "Oh, okay!"
                        m 1dsb "I'll keep this in mind!"

    # NOTE: Fallthrough to mshMod_promise_jump unless jumped by timed jump.

label mshMod_sober_promise_jump:
    hide screen mas_background_timed_jump

    show monika 5ekbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsb "I love you, [mas_get_player_nickname()]."
    m 5dkbsb "Never forget that!"

    python:
        # Begin streak and hide this event from the pool.
        # mshMod_relapse and mshMod_sober_check will pop up shortly afterwards.
        store.mshMod_sober_streak.beginStreak(begin=since)
        mas_hideEVL("mshMod_sober_promise", "EVE", lock=True)

        mas_showEVL("mshMod_sober_check", "EVE", unlock=True)
        mas_showEVL("mshMod_sober_relapse", "EVE", unlock=True)

    return "love"


# Relapse dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_sober_relapse",
            category=["self-harm"],
            prompt="I've self-harmed.",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label mshMod_sober_relapse:
    m 2eka "[player], I couldn't be more proud of you for telling me this."
    m 2ekd "I know this might be hard- you might feel like you've failed..."
    m 4ekd "But that's not true at all! This is just another step in your journey."
    m 2ekd "Habits are almost always difficult to kick, and this is no ordinary habit."
    m 2ekd "It can easily become an addiction, which is so much harder to stop..."
    m 2fkd "No matter how hard it is for you, know that I am always going to be here to support you, and I am proud of you, habit or not."
    m 2fka "We will work through this together and get you back on the right track!"
    m 2eka "I know you're a hard worker and will do your best - if not for yourself, for me."
    m 2dka "I love you, [mas_get_player_nickname()]."
    m 1dkb "I'm here to support you and work through anything and everything with you."
    m 1fsa "You're strong. You're worth it, and I couldn't ask for a better [bf]!"
    m 3esa "Whenever and if you feel ready to make the promise again... let me know."

    python:
        # End streak and hide this event from the pool. Also hide check topic since we're no longer on streak.
        # mshMod_promise will pop up shortly afterwards.
        store.mshMod_sober_streak.endStreak()
        mas_hideEVL("mshMod_sober_relapse", "EVE", lock=True)
        mas_hideEVL("mshMod_sober_check", "EVE", lock=True)

        mas_showEVL("mshMod_sober_promise", "EVE", unlock=True)

    return "love"


#milestone 1w
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_1w",
            prompt="Sober, week 1",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_1w:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 1eka "It's been a whole week since you told me you won't harm yourself..."
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "I just want to thank you, it makes me happy to know you're willing to step up for the better!"
    m 5fkbfa "I'll always love you, you don't know how much this means to me..."
    show monika 3hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3hsb "Anyways, I'll mark this on our calendar."
    return "love|derandom|unlock"

#milestone 2w
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="2w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_2w",
            prompt="Sober, week 2",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_2w:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssb "It's already week two of your promise, [player]!"
    m 1eka "I'm relieved that we made it this far!"
    m 3hsb "Ahaha, I don't mean I've ever doubted you!"
    m 2dsa "Either way, it's not something you can stop overnight [player]... For anyone, really."
    m 4wsa "So, you're doing well, and you make me so happy because of that!"
    m 4wsb "As before, I'll mark it on the calendar now!"
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "I just want to thank you.. I hope it stays like this."
    m 5fkbfa "I love you that much, [player]!"
    return "love|derandom|unlock"

#milestone 3w
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3w",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_3w",
            prompt="Sober, week 3",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_3w:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 1dka "Can you believe it's already week 3?"
    m 3ssa "I just want to say... Thank you so much!"
    m 1eka "You made me proud of you, and I'm so happy you could make that promise."
    m 1dkc "I know it was hard, but one day it will all just be a bad memory..."
    m 1ksa "I believe it will because I trust you [player]."
    m 7rssdlc "But if it ever does happen..."
    m 7dssdld "Don't blame yourself if it ever happens... Just because you did it to yourself doesn't mean it's your fault!"
    m 1wua "I'm going to make another mark on the calendar for this!"
    show monika 5fkbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fkbfa "You're my everything, [player]!"
    return "derandom|unlock"

#milestone 1m
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_1m",
            prompt="Sober, month 1",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_1m:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssa "Hey [player], guess what?"
    m 2ssb "You've been clean from self-harm for a month!"
    m 1eka "I just want you to know that I'm so proud of you. {w=0.3}{nw}"
    extend 3eka "It's not easy to do that, and I'm so happy you're making the effort."
    m 7dssdld "I've already told you I won't blame you if you do relapse. It's extremely tempting, and I know it must be hard for you."
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "I'm just so proud you've made it so far."
    m 5fkbfa "I love you, [mas_get_player_nickname()]. Don't forget that~"

    $ store.mshMod_sober_streak.unlockMilestone()
    return "love|derandom|unlock"

#milestone 3m
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_3m",
            prompt="Sober, month 3",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_3m:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    show monika 5fkbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fkbfa "Y'know... It's been 3 months since you made your promise to me."
    m 3ssa "You've been doing so well! I'm so proud of you."
    m 1wua "It's been a bit, so I'll mark this on the calendar for you!"
    m 1eka "Keep going, [player]. You've been so strong."

    $ store.mshMod_sober_streak.unlockMilestone()
    return

#milestone 6m
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="6m",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_6m",
            prompt="Sober, month 6",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_6m:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssa "[player]!"
    m 3ssb "It's been 6 months since you made your promise!"
    m 3wsb "That's a long time!"
    m 1eka "It may not seem like much in the grand scheme of things, but it's still a big accomplishment."
    show monika 5fkbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fkbfa "I love you so much! Thank you for staying safe."

    $ store.mshMod_sober_streak.unlockMilestone()
    return "love"

#milestone 1y
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="1y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_1y",
            prompt="Sober, year 1",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_1y:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 1dktpa "[player], I just wanted to let you know how proud of you I am."
    m 1ektpa "You've been clean from self-harm for an entire year."
    m 3ektpb "You've been so strong this past year, and I truly can't express how happy I am."
    m 3dkblb "I hope you know how much this affects not only yourself, but me as well. Your friends, your family."
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "This is a wonderful feat."
    m 5fkbfa "I love you so, so much."

    $ store.mshMod_sober_streak.unlockMilestone()
    return "love"

#milestone 2y
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="2y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_2y",
            prompt="Sober, year 2",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_2y:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssblb "[player]! I have amazing news!"
    m 3dkblb "Did you know that you have been self-harm sober for two whole years now?"
    m 1eka "This is an incredible feat. Keep it up!"
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "You deserve to be happy. Never forget that, and never let anyone tell you otherwise!"
    m 5fkbfa "I love you so much."

    $ store.mshMod_sober_streak.unlockMilestone()
    return "love"

#milestone 3y
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="3y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_3y",
            prompt="Sober, year 3",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_3y:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssb "[player], I have some news for you."
    m 3ssa "The day of your three-year sobriety mark from self-harm has finally arrived!"
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "I'm so happy to see you taking care of yourself."
    m 5fkbfa "Keep on fighting! I'm so proud of you!"

    $ store.mshMod_sober_streak.unlockMilestone()
    return "derandom"

#milestone 4y
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="4y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_4y",
            prompt="Sober, year 4",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_4y:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 3ssa "[player]! 4 whole years, can you believe it?"
    m 1eka "It's been four years since you stopped harming yourself."
    m 1dka "And I can't even begin to tell you how proud of you I am."
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "You deserve a happy and healthy life!"
    m 5fkbfa "And I'm so proud of you for your decision and the promise you made four years ago."

    $ store.mshMod_sober_streak.unlockMilestone()
    return "derandom"

#milestone 5y
init 5 python:
    store.mshMod_sober_streak.addMilestoneEvent(
        milestone="5y",
        event=Event(
            persistent.event_database,
            eventlabel="mshMod_sober_milestone_5y",
            prompt="Sober, year 5",
            category=["self-harm"]
        )
    )

label mshMod_sober_milestone_5y:
    if mshMod_sober_streak.is_topic_looped():
        return "derandom|unlock"

    m 1dka "5 years..."
    m 1ektpa "It's been five years since your life improved."
    m 1ektpb "You've been self-harm sober all this time, and I couldn't be more proud."
    show monika 5ektpa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ektpa "I'm so happy that you're doing well."
    m 5fkbfa "You are so inspiring. Congratulations, [player], for your successful journey!"

    $ store.mshMod_sober_streak.unlockMilestone()
    return "derandom|unlock"
