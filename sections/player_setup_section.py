"""
Class used explain the basics of character creation for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List

class NewPlayerSetupSection:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used explain the basics of character creation for a system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        # Build out HTML here
        self.__html.append('<div class="section">')
        self.__html.append(f'    {self.__contents.single("new player setup")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Another one of the major goals of this system is to keep character
            creation as  flexible and open as possible. with this in mind,
            players should always be  encouraged to create new races, or classes
            for their characters. If a player  decides to create their own class
            or race they should work with the DM to  ensure that the addition
            makes sense. Start character creation by either passing out character
            sheets or by sending a link to the character sheet file. Players
            should fill out the sheet in the following way:
            """
        )]
        self.__html.append("    <h3><u>1. Create Your Character's Background:</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            The first step in character creation should be to flesh out each
            player's character as a living entity. A character's race, stats,
            class, etc. should  flow from who that character is as a living
            breathing creature; not the other  way around. Since LINAS relies
            so heavily on narration, it is very important  that characters be
            thought of in terms of their background vs. in terms of skills/stats.

            When filling this section out, players should think hard about who
            their character is? How do they fit into society? What are their
            beliefs or values? etc. Getting an idea of who the character is
            will be vital for filling out the later sections of the character
            sheet.
            """
        )]
        self.__html.append("    <h3><u>2. Fill Out Flavor Section:</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            The second section players should focus pretty heavily on is the
            flavor section. While this section is mainly just for fun and to add
            additional info to the player's background. This section can be
            extremely helpful if a player is stuck on their character's
            background. The flavor section is split into 3 Sections
            <ul>
                <li>
                    <u>Vices</u> - These are a player's negative personality traits.
                    Are they hot-headed? Do they like to gamble or have a weakness
                    for women? Do they refuse to fight if an opponent is unarmed?
                </li>
                <li>
                    <u>Virtues</u> - These are a player's positive personality
                    traits. Are they a smooth talker? Are they the kind of person
                    who's always prepared for anything? What motivates them?
                    Getting rich? Retiring early? Helping the weak? etc.
                </li>
                <li>
                    <u>Training</u> - These are a player's areas of expertise or
                    knowledge relating to skills. This could include things like
                    knowing a lot about history or magical items, having training
                    as a pilot, or even something as eclectic as being a cigar
                    aficionado. 
                </li>
            </ul>

            Once again, this section is really just here to help flesh out
            a player's character and shouldn't be taken too seriously. However,
            that being said it's also a good way for players to kind of have a
            quick reminder of the things which are important to their character
            in order to decide how/when to roll for things.
            """
        )]

        self.__html.append("    <h3><u>3. Choose a Race and Class</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            After players decide on their character's background, the next step
            is to  choose a race and class for the character. The race and class
            should support the character's background and most important it
            should be a race and class the character wants to play vs. a race
            and class the player "thinks will do the best." 

            The DM should be actively involved in all character creation
            regardless of  whether it's custom or stock. Also, it is advised that
            when creating custom  races or classes that the custom Race/Class
            sections be used as a template  (respectively) as this will help
            ensure that the created content is somewhat balanced.
            """
        )]
        self.__html.append("    <h3><u>4. Fill out Stats Section</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Filling out the stats section may look intimidating or complex at first
            glance, however the calculations are fairly simple and so it's best to
            take things one step at a time. If you are making custom race you'll need
            to allocate 2 points in either one stat or two different stats at this point.
            These points should highlight your character's race's strong points. If the
            race is physically strong that would be STR or END. If they're mentally strong
            that could be INT or SPR. Same thing for if the race is proficient at magic.

            As with all things work wth the DM to figure out what stats would best
            fit your characters background and make them effective both inside combat
            as well as outside. Once you've figured these points out. Follow the steps
            below to calculate the stats on your character sheet.
            <ol>
                <li>Assign 3 points to HP. All characters get at least 3 HP to start</li>
                <li>Allocate 7 points between HP/TP however you want. (HP+TP should be 10 when finished)</li>
                <li>Allocate the points listed for your chosen race. If making a custom race allocate 2
                stats in a way that makes sense. Your stats should be a reflection of your race's 
                strong points.</li>
                <li>Allocate 2 points in any stats other than HP/TP (total points in stats other than HP/TP should be 4)</li>
                <li>Calculate adjusted speed (&#8645;{CharacterSheet.__am.tag("spd")}) by subtracting the number of points in speed from 
                the total speed penalty ({CharacterSheet.__am.tag("pen")}) from <u>all</u> equipment, then add any points in strength and
                finally add 2. This value is used to calculate a wide number of things. Usually when the DM asks for speed, it's
                this value</li>
                <li>Calculate Weapon damage (&#8645;{CharacterSheet.__am.tag("patk")}) by adding together your weapon's base damage and
                the points in either STR or DEX (depending on which stat your weapon uses)</li>
                <li>Calculate physical armor points (&#8645;{CharacterSheet.__am.tag("patk")}) by adding together your armor's base 
                physical protection value ({CharacterSheet.__am.tag("pdef")}) and the points in END</li>
                <li>Calculate magic armor points (&#8645;{CharacterSheet.__am.tag("mdef")}) by adding together your armor's base 
                magic protection value ({CharacterSheet.__am.tag("mdef")}) and the points in SPR</li>
            </ol>

            Another thing to keep in mind while filling this out is that most stats
            can be seen as modifiers of some kind. STR, DEX, and INT modify damage,
            END and SPR modify damage taken, and SPD modifies movement and also
            determines how likely a character is to dodge or counter-attack. It's
            also important to keep in mind that all the values are meant to be
            fairly low. With most values having a maximum cap of 5. This is done
            purposely as the enjoyment of the system should be from playing as a cool
            character not from crunching numbers. Keep this in mind as you pick your
            stats and pick stats which fit for your race and your character's training
            not ones which will do the most damage.
            """
        )]
        self.__html.append('    <h3 style="page-break-before: always;"><u>5. Fill out Abilities Section</u></h3>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Each race has two custom abilities: one active ability which the player
            must consciously elect to use and one passive ability which is in play at
            all times. If the player is creating a custom race, they can choose one
            active and one passive ability from the book or create their own custom
            abilities.

            When creating custom abilities it's important to keep in mind that passive
            abilities are usually used automatically and are things which give bonuses
            or penalties under certain conditions. While active abilities can be seen
            kind of like a trump card or stronger version of a technique and are meant
            to be used in a clutch situation. 

            Additionally the DM may elect to give the character a negative passive ability
            if it fits with their character (see vampire race for example)
            """
        )]
        self.__html.append("    <h3><u>6. Fill out Skills Section</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Filling out skills section is much more straightforward than filling out
            stats. Simply copy the skills and the corresponding values listed under
            your chosen class and then add 2, you should have 6 points total allocated
            between all skills. It should be noted unlike stats, skills start at
            -2 not 0. If making a custom class, give yourself 4 points to allocate
            towards skills which make sense for your class. Remember, these are 
            skills required to do your job. More skills can be learned later or
            may be allocated by the DM, especially in cases where the characters
            are meant to be seasoned warriors or adventurers vs. just starting out.
            """
        )]
        self.__html.append("    <h3><u>7. Fill Out Techniques Section</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Techniques are usually related to a character's class and encompass
            both spells and battle techniques. Depending on your class you may
            find you need to rely more heavily on techniques to do your job.

            Jobs which rely on techniques more heavily usually give more vs.
            less. That being said even if the player's class doesn't list out
            any techniques they're always encouraged to discuss the possibility
            of taking one or more with the DM. Especially if they feel like their
            character should be able to use it.
            """
        )]
        self.__html.append("    <h3><u>8. Fill Out Equipment Section</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            If your class lists out any special weapons or armor look it up and
            fill out the section on the character sheet dealing with equipment.
            If you need to, go ahead and take a moment to also finish filling out
            the last row of the stat section at this point as well since it relies
            on some of the values from this section to fill out. 

            If your character is planning to dual wield weapons make sure to check the
            box and record the bonus listed on the weapon. Likewise if your character
            plans to use a shield.
            """
        )]
        self.__html.append('    <h3 style="page-break-before: always;"><u>9. Take/Buy Items</u></h3>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Start by taking any specialized items needed by your class. This
            includes things like lockpicks, musical instruments, crafting tools,
            etc. Players are also able to give their characters small flavor items
            which may relate specifically to that character. Things like jewelry or
            or access cards, pocket knives, etc. Things which relate to the
            character's background.

            Each player is also given 100G to start out. The DM may modify this amount
            to be  more or less depending on how much they want each player to
            start out with. Players may also want to save their gold as shop
            amounts may offer better deals 

            It should also be noted that while a player will not need to purchase 
            items required  for their craft the player may also want to give 
            their character a bit of an edge such as buying a better weapon than the one
            provided by their class.
            """
        )]
        self.__html.append("    <h3><u>10. Additional Items and finishing Touches</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            The goal here is to polish each character and make sure nothing feels
            off or incomplete. To put it another way; this is where you polish
            the rough draft of  your character into the final copy. The DM should
            work with players closely  during this last step to ensure they are
            aware of all changes being made so that there are no surprises and also
            to ensure the campaign is satisfying and  adequately takes advantage
            of each character's skill set.
            """
        )]

    def toHTMLList(
        self
    ) -> List[str]:
        """
        Returns contents of class as a formatted HTML block

        Returns
        -------
        html_tags : `List[str]`
            A list of strings representing the contained HTML
        """
        return self.__html