from __future__             import print_function, division
from obj_classes.cssItem    import CSSItem
from obj_classes.loader     import Loader
import          json
import          pdfkit
import          os
import          re

"""
================================================================================
= PDF Generator Class                                                          =
= ---------------------------------------------------------------------------- =
= Written By: Joseph Bourque     Last Updated By: Joseph Bourque         5     =
= Completed On: --/--/----                                                     =
= Last Updated: --/--/----                                                     =
= ---------------------------------------------------------------------------- =
= description:                                                                 =
= Used to turn json files into html and to turn html into a pdf document       =
================================================================================
"""
class PDFGen:
    """
    ============================================================================
    = Constructor                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Creates a pdf generator, defines an HTML string to add to, and defines   =
    = the config settings for wktohtml.                                        =
    ============================================================================
    """    
    def __init__(
        self,           # (Ref) A reference to this class, required by all 
                        # members
        debug = False   # (Boolean) Whether to print debug statements or not
    ):
        # class vars:
        self.__loader   = Loader(   # (Loader) Object which holds section data
            debug=debug             # for guide and character sheet generation
        ) 
        self.__debug    = debug     # (Boolean) Store whether we're debugging
                                    # or not

        self.__indent   = 0         # (Int) used for formatting HTML

        self.__stack    = []        # (List<string>) used to ensure right html
                                    # tag is closed
        
        self.__estyle   = 'width: 12px; height: 12px;'
        curWorkDir      = os.getcwd()
        self.__elemTags = {
            'dark':f'<img src="file:///{curWorkDir}/assets/dark.png" style="{self.__estyle}"/>',
            'earth':f'<img src="file:///{curWorkDir}/assets/earth.png" style="{self.__estyle}"/>',
            'fire':f'<img src="file:///{curWorkDir}/assets/fire.png" style="{self.__estyle}"/>',
            'light':f'<img src="file:///{curWorkDir}/assets/light.png" style="{self.__estyle}"/>',
            'water':f'<img src="file:///{curWorkDir}/assets/water.png" style="{self.__estyle}"/>',
            'wind':f'<img src="file:///{curWorkDir}/assets/wind.png" style="{self.__estyle}"/>',
            'electricity':f"""
            <img src="file:///{curWorkDir}/assets/wind.png" style="{self.__estyle}"/>
            <img src="file:///{curWorkDir}/assets/light.png" style="{self.__estyle}"/>
            """,
            'ice':f"""
            <img src="file:///{curWorkDir}/assets/water.png" style="{self.__estyle}"/>
            <img src="file:///{curWorkDir}/assets/dark.png" style="{self.__estyle}"/>
            """,
            'wood':f"""
            <img src="file:///{curWorkDir}/assets/water.png" style="{self.__estyle}"/>
            <img src="file:///{curWorkDir}/assets/wind.png" style="{self.__estyle}"/>
            """,
            'metal':f"""
            <img src="file:///{curWorkDir}/assets/earth.png" style="{self.__estyle}"/>
            <img src="file:///{curWorkDir}/assets/fire.png" style="{self.__estyle}"/>
            """,
            'null':f'<img src="file:///{curWorkDir}/assets/null.png" style="{self.__estyle}"/>'
        }

        self.__config   = pdfkit.configuration(
            wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        )
        msize='1.0in'
        self.__options = {
            'footer-center': '[page]',
            'page-size': 'Letter',
            'margin-top': msize,
            'margin-bottom': msize,
            'margin-left': msize,
            'margin-right': msize,
        }
        self.__html     = ""
        self.__write('<!DOCTYPE html>')
        self.__open_tag('html')
        self.__header()
        self.__open_tag('body')

        # Create title page
        self.__add_title('./sections/title.json')

        # Create description page
        # self.__add_description('./sections/description.json')

        # Create contents page
        self.__add_contents([
            "Introduction",
            "Stats",
            "Skills",
            "Combat",
            "Free Time",
            "New Player Setup",
            "Languages & Races",
            "Classes",
            "Spells & Battle Skills",
            "Abilities",
            "Effects & Status Conditions",
            "Item",
            "Entities"
        ])

        # Create introduction section
        self.__add_section(
            "1. Introduction",
            self.__paragraph(
                """
                Welcome to Kite Tabletop; first I'd like to thank you for picking up our system
                and giving it a try. This system was developed by myself (Joseph Bourque) along
                with some of my close friends who not only helped me test the system but which
                also contributed to it immensely.                
                """
            )+self.__paragraph(
                """
                The initial inspiration for Kite came from my own experiences with different
                tabletop systems; as well as hearing about some of my friends' experiences. My
                goal with this system is to create a fluid and fast system which is easy to set
                up and start playing. I also wanted a system where battle calculations move
                quickly so that the flow of the game is interrupted as little as possible.`
                """
            )+self.__paragraph(
                """
                The system is purposely kept light with the intent that character development
                and progression be done primarily through questing and training vs. leveling up.
                The idea being to shift the focus more on the story being told and to try and to
                try and make characters more dynamic and rounded out vs. just a collection of
                stats.
                """
            )+self.__paragraph(
                """
                Most importantly, my goal is to develop something fun to play and with that in
                mind I hope you enjoy using this system and that you continue to use it in the
                future. Thank you so much again for giving our system a shot and I hope all your
                campaigns with this system go well.
                """
            )+self.__paragraph(
                "<br/>Sincerely,<br/>Joseph Bourque",
                indent = False,
                add_br = False
            )
        )

        # Create stats section
        self.__add_section(
            "2. Stats",
            self.__paragraph(
                """
                Kite, in general tries to keep it's scale for stat allocation fairly low. As
                stated in the introduction, the main drive for this is to keep damage
                calculations fast and straightforward. Stats can either be represented by
                numbers or by blocks (&#x25A1). For the fantasy system; the following stats are
                defined:
                """
            ),
            self.__paragraph(
                """
                <p style="page-break-before: always"></p>
                &emsp;&emsp;&emsp;&emsp;
                For the most part, a player can put points into whichever stats they see fit.
                However, that being said; there are a few restrictions:<br/>
                <ul><p><li>
                A user can only have a maximum of 25 points in HP and MP combined. Meaning, if
                the user already has 15HP, they can only have a maximum of 10MP.
                </li></p><p><li>
                Excluding HP and MP, the maximum number of points a user can have in any
                other stat is 5.
                </li></p><p><li>
                Excluding HP and MP, an entity can only have a total of 10 points in Strength,
                Intelligence, Dexterity, Spirit, Endurance, and Speed combined. Once again,
                this means that the sum of all stats (excluding HP and MP) cannot be over 10.
                </li></p></ul>
                """,
                indent=False,
                add_br=False
            )+self.__paragraph(
                """
                The restrictions above are put in place not only to keep damage calculations
                low; but also to try and ensure that no single player can run the entire
                campaign themselves. Additionally, this is done to try and keep the system from
                being too broken i.e. having mages equipped in steel plate.
                """
            ),
            self.__parse_stats
        )

        # Create skills section
        self.__add_section(
            "3. Skills",
            self.__paragraph(
                """
                One of the major goals for this system is to present skill usage in a way
                which is flexible and open. This means that the skills listed in this section
                can be thought of as guidelines or "recommended skills" only. An entity
                always has the ability to use any skill they desire even if they don't have it
                chosen as a skill. One caveat with this is that the DM has the right to veto
                the player's usage of a particular skill if using the skill wouldn't make sense
                from the standpoint of their character. An example of this would be an entity
                trying to use a flight skill when they do not possess wings or any means to
                fly.
                """,
                add_br = False
            )+self.__paragraph(
                """
                Skills themselves are kept fairly abstract and are more of roll modifiers vs.
                an actual measure of an entity's ability. Any skill an entity is considered
                "skilled" at gets a +1 or +2 added to their roll for that skill depending on
                the number of points in that skill. On the opposing end of this scale; any
                skill an entity is considered "unskilled" at gets a -1 or -2 added to their
                roll for that skill. If an entity tries to use a skill which they do not have
                any points in (i.e. they are neither "skilled" or "unskilled") they simply
                roll without any penalty or advantage. Once again; this is to allow entities 
                the ability to use any skill within their ability without having to take that
                skill.
                """,
                add_br = False
            )+self.__paragraph(
                """
                Rather than a simple pass/fail roll, Kite uses a more dynamic system for skill
                usage in an attempt to make the system more narrative focused vs. crunch and
                run so to speak. Most rolls use a single d6 laid out in the following manner:
                """,
                add_br = False
            )+self.__paragraph(
                """
                <strong>1 = You fail, and...</strong> (always fails regardless of roll
                modifiers)
                <br/><strong>2 = You fail</strong>
                <br/><strong>3 = You fail, but...</strong>
                <br/><strong>4 = You succeed, but...</strong>
                <br/><strong>5 = You succeed</strong>
                <br/><strong>6 = You succeed, and...</strong> (always succeeds regardless of
                roll modifiers)
                """,
                indent = False,
                add_br = False
            )+self.__paragraph(
                """
                Kite uses the above mapping in order to keep things from becoming sterile or
                rote and also to give the DM a bit more control over the flow of gameplay. For
                example, let's say a group really needs an artifact to continue with the
                campaign but the only character which could have identified the artifact's use
                rolled a 3 (you fail, but...). In this case, it could be that although the
                character failed to identify the artifact, they're able to sense it's related
                to the area allowing the party to still use the artifact albeit in a restricted
                manner.
                """,
                add_br = False
            )+self.__paragraph(
                """
                The DM may also choose to give additional bonuses or penalties to skill usage
                based on environmental conditions or party status. For example, if it's raining
                the DM may announce that all usage of the perception skill gets -1 since the
                rain would make it harder to discern what's going on at greater distances.
                <p style="page-break-before: always;">
                """,
                add_br = False
            )+self.__paragraph(
                """
                <img src="file:///"""+os.getcwd()+"""/assets/skill_roll.png" style="padding: 10px; float: right;"/>
                &emsp;&emsp;&emsp;&emsp;
                With all this taken into consideration, modifiers turn skill rolls into a sort
                of sliding scale. At the center, the scale is completely balanced; however the
                odds may be for or against an entity depending on the current situation.
                However, there is one caveat: a natural 1 is <u><strong>ALWAYS</strong></u>
                you fail and... and a natural 6 is <u><strong>ALWAYS</strong></u> you succeed
                and... This is done to ensure that there is never a case where the need to roll
                is completely eliminated due to a 100% pass or fail rate.
                """,
                add_br = False
            )+self.__paragraph(
                """
                Like stats, there are no rules about which skills an entity can/cannot use and
                using a specific skill is mainly up to the players and the DM to work out
                amongst themselves. That being said, there are a few set restrictions regarding
                skills which must be observed:
                <ul><li>
                If an entity takes a +1 or +2 in a particular skill, they must also take a -1
                or -2 in a different skill in a way which makes sense for that character. In
                other words; the sum of an entity's skill points (both positive and negative)
                must always equal 0. This is referred to as: <u>the net rule of zero</u>
                <ul><li>
                Example: An archer character takes +2 in archery and after talking things over
                with the DM, they agree to take a -2 in swimming.
                <ul><li>
                2 + (-2) = 0. This is a valid skill assignment because the net rule of zero is
                observed.
                </li></ul></li></ul></li>
                <li>
                The sum of an entity's positive skill points cannot exceed 7
                <ul><li>
                Example: A player's rogue character has +2 in stealth, +1 in pickpocketing, +2
                in fencing, +1 in archery, and +1 in lore (Undercity). 2 + 2 + 1 + 1 + 1 = 7.
                This is a valid skill assignment because the total number of points the
                character is "skilled" in is not greater than 7.
                </li></ul></li>
                <li>
                Any time a skill is learned or improved, another skill must be weakened. The
                net rule of zero must be observed.
                <ul><li>
                Example: A mage character spends some time in a magic library in order to
                improve their magery skill by +1 points. As a result, their swordsmanship
                skill also goes down by -1 points.
                </li></ul></li>
                <li>
                If an entity chooses to improve one of their negative skills, they must take an
                equal number of points away from one of their positive skills, even if the
                total number of positive skills would be less than 7. The net rule of 0 must
                be observed.
                <ul><li>
                Example: An elf ranger character took a bonus point in climbing. However, the
                campaign has mostly taken place in swamp where the -1 to swimming they took
                has proven to be a major obstacle. The ranger decides to take some time to
                improve their swimming skill and in doing so they remove the +1 from climbing
                This is a valid assignment as the net rule of zero is observed.
                </li></ul></li></ul>
                """,
                add_br = False
            )+self.__paragraph(
                """
                It is important taht both the DM and the players understand what each of these
                restrictions entails moving foroward as they play a crucial part in keeping the
                game balanced.
                """,
                add_br = False          
            ),
            parser      = self.__parse_skills
        )

        # Create Combat Section
        self.__add_section(
            "4. Combat",
            self.__paragraph(
                """
                Combat is one area of the system in which special attention was paid. The reason
                being that many systems I've played in the past (including my own) had the
                problem that once battle started, things sort of slowed down. After talking with
                some of my friends I realized I wasn't the only one who noticed this. This was a
                big part of the inspiration for moving towards a light 1d6 system; the theory
                being that the DM having to stop to do a large number of calculations is what
                leads to the slowdown. That being said, battle phases are usually very short and
                the flow of battle can be described below.
                """
            )+self.__htag(
                "<u>Pre-Battle</u>"
            )+self.__paragraph(
                """
                All entities roll 1d6 for initiative (both enemies and party members). The speed
                stat is added to each entity's dice roll and turn order proceeds based on
                initiative score (highest score first and lowest score last). If there is a tie
                in any score e.g. two entities both roll a 5, the tying entities re-roll until a
                winner is reached; with the winner taking the higher spot and the loser taking
                the lower spot. However, when rerolling to break a tie an entity keeps it's
                original initiative score instead of the re-rolled score. This is done mainly to
                provide a simple way to keep turn order consistent without having to re-roll
                more than needed which tends to break the flow of the game. 
                """
            )+self.__paragraph(
                """
                <i>
                Example: Let's say one entity has a speed of 3 and rolls a 3 and another entity
                has a speed of 4 and rolls a 2 such that both entities have an initiative score
                of 6. The two tying entities both roll again. Now one entity ends up with an
                initiative score of 4 and the other ends up with a score of 8.  The entity with
                the score of 8 takes the higher ranked spot and the entity with the score of 4
                takes the lower ranked spot. However, both entities are still ranked with a
                score of 6.
                </i>
                """,
                indent = False
            )+self.__paragraph(
                """
                One final note about initiative is that if an entity's speed changes for any
                reason the changes take effect immediately without the user having to re-roll.
                If the change moves their turn position past what would be the next entity's
                turn; they take their turn immediately instead.
                """
            )+self.__paragraph(
                """
                <i>
                Example: An entity who has an initiative score of 5 has a spell cast on them by
                an ally which boosts their speed by 3 points giving them an initiative score of
                8 and causing the entity to move earlier in turn order. The next entity after
                caster, only has an initiative score of 7. The boosted entity will take their
                turn immediately interrupting the entity with a score of 7; even though their
                turn was next.                
                </i>
                """,
                indent = False
            )+self.__htag(
                "<u>During Battle</u>"
            )+self.__paragraph(
                """
                Each entity gets 1 move and 1 action during their battle round by default. Some
                abilities or items may change this however. An entity can perform an action and
                a move in any order they wish. 
                """
            )+self.__paragraph(
                """
                The default movement range is 2; meaning an entity can move 2 squares in any
                direction (cannot move diagonally). If an entity has points in speed they are
                added to the entity's movement. For example, if an entity has a value of 2 in
                speed, they are able to move 4 squares.
                """
            )+self.__paragraph(
                """
                Actions consist of anything an entity does during a turn other than movement.
                This includes: using items, using skills and  attacking, etc. Each of these
                is outlined in more detail below. 
                """   
            )+self.__htag(
                "<u>Using Items</u>",
                "h4"
            )+self.__paragraph(
                """
                By default, an entity doesn't have to roll to use an item. The item is simply
                used, and any effects of the item go into place. However, some items do require
                a roll to be used and any items which require this will have the details
                pertaining ot their roll listed on them.
                """
            )+self.__htag(
                "<u>Using Skills</u>",
                "h4"
            )+self.__paragraph(
                """
                There is virtually no difference between using skills inside battle vs. outside.
                The entity using the skill simply performs their 1d6 dice roll to see if they
                succeed, and then resolves the skill's effects according to their dice roll. For
                more information on how skills resolve see section 3 of this guide for a full
                breakdown of skill usage.
                """
            )+self.__htag(
                "<u>Attacking</u>",
                'h4'
            )+self.__paragraph(
                """
                Attacking is very similar to skill usage and uses the same flow regardless of
                whether using a spell or physical weapon. Once again this is done to keep the
                system simple and battle flow itself unfolds in the following manner.
                <ol><li>
                Attacking entity chooses a weapon (or spell) and a skill to attack with as
                well as a target to attack (or targets if applicable)
                </li><li>
                Attacking entity rolls 1d6 against the chosen skill to see if attack succeeds
                <ul><li>
                Special effects of attacks such as poison or paralysis usually resolve during
                this step as well
                </li></ul></li><li>
                If the attack was successful, the attacking entity adds any stat points they
                have to the weapon's (or spell's) damage and then deals that much damage to
                their target (or targets).
                <ul><li>
                Note: each stat corresponds to a certain type of weapon. Strength to physical
                melee weapons, dexterity to physical ranged weapons, intelligence to magic
                weapons, etc.
                </li></ul></li><li>
                Damaged entities absorb as much damage as possible into their armor. Armor
                remains damaged for the remainder of the round and an entity gets their
                full armor value back at the beginning of the round.
                <ul><li>
                Note: Unless specifically stated, armor values typically are only for
                pysical attacks, not magic. This means that spell damage is not absorbed
                unless the armor specifically mentions preventing magic damage.
                </li></ul></li><li>
                Damaged entities take any damage not absorbed by armor as damage to HP.
                </li></ol>
                """,
                add_br = False
            )+self.__paragraph(
                """
                <i>
                Example: A rogue character with 1 point in strength targets a goblin with 1
                armor using a knife with 2 damage. The rogue rolls a 5 which is a success. The
                rogue adds their strength to their knife's damage for a total of 3 points of
                damage. The goblin's armor absorbs 1 damage and the goblin loses 2 HP. The
                goblin now has 0 armor until the start of the next round.
                </i>
                """,
                indent = False
            )+self.__paragraph(
                """
                It should also be noted that the only difference between attacking with a spell
                and a physical weapon is that spells have an MP cost which is consumed when the
                spell is used. This means that the MP is lost regardless of whether the spell is
                successful or not. Additionally, spells are not absorbed by physical armor
                meaning unless an entity has some sort of magic protection they take the full
                brunt of magic attacks.
                """
            )+self.__paragraph(
                """
                <i>
                Example: A mage with 2 intelligence chooses a fireball attack to attack a goblin
                with 1 armor. The fireball attack consumes 1 MP and deals 2 fire damage. The
                mage rolls a 2 which is a fail. The mage would normally have done 4 damage (2
                intelligence + 2 damage) to the goblin. However, since they failed, no damage is
                done. The mage still loses 1 MP for attempting the spell however.
                </i>
                """,
                indent = False
            )+self.__htag(
                "<u>Resolving Combat</u>"
            )+self.__paragraph(
                """
                Combat ends when one side has either been completely immobilized in some way or
                willingly surrenders (in some cases this isn't an option). In the case of
                immobilization, this usually means that all entities on one side of battle have
                their HP reach 0. This could also happen as the result of a spell or ability
                such as petrification. 
                """
            )+self.__paragraph(
                """
                After combat is finished, the DM determines what loot (if any) the defeated
                party leaves behind. If the players' party is defeated, the DM decides if
                something happens which would result in the campaign coming to an end or whether
                the party is able to continue their journey i.e. being captured or thrown in
                prison. 
                """
            )+self.__htag(
                "<u>Destroying The Environment</u>"
            )+self.__paragraph(
                """
                As a general rule; rocks, trees, and other obstacles can be destroyed by
                attacking them as well as by certain spells and abilities. Also as a general
                rule, obstacles usually have 5 HP unless the DM declares otherwise. The two most
                common classes of obstacles are wooden and stone. Wooden obstacles take double
                damage from earth and fire magic. Stone obstacles take double damage from wind
                magic. For more information on why this is; check out the element system
                explanation in section 9. Once an obstacle's HP reaches 0 it is destroyed and
                the DM determines what happens at that point. 
                """
            )+self.__paragraph(
                """
                <i>
                Example: A ninja uses a substitute skill to switch places with a nearby log. The
                log takes 10 damage the ninja would have taken otherwise and is destroyed. The
                ninja switches places with where the log was and the log ceases to be an
                obstacle. During the following round a mage casts a fire spell. The DM declares
                the wood chips from the log are still on the targeted space resulting in the
                fire spell dealing an additional point of damage. It should be noted the above
                example is just that, an example at as with most things in the system what
                happens is largely up to the DM 
                </i>          
                """,
                indent = False
            )
        )
        self.__add_section(
            "5. Free Time",
            self.__paragraph(
                """
                Free time is time between battles or events in the campaign where the players
                are free to explore and engage in events or activities which aren't part of the
                main goal the party as a group is trying to accomplish. Examples of these could
                be training skills, or studying new skills. This also includes visiting shops,
                socializing in taverns, or other areas of interest.
                """
            )+self.__paragraph(
                """
                The primary goal of free time is to provide breaks between action sequences both
                to help the DM manage the flow of the campaign and also to give the player's
                characters an opportunity to interact with each other as well as the surrounding
                environment outside of a battle setting.  Below is a list of some common
                free-time activities:
                """
            )+self.__htag(
                """
                <u>Training</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                Characters can train in order to level up physical skills and stats. For
                example, a fighter might train endurance by sitting under a waterfall or a mage
                might train their spirit by meditating. This might also refer to skill training
                such as a swordsman taking time to practice their sword stances or attacks or a
                blacksmith taking some time off to work in the town's forge.
                """               
            )+self.__htag(
                """
                <u>Studying</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                Similar to training; studying can learn new skills or spells either by reading
                books or by training with an NPC who specializes in the skill/spell required.
                This is especially useful if a particular skill chosen by a player for their
                character hasn't really come up much during the campaign. By improving the
                negative skill related to the unwanted one, both will disappear, freeing up the
                skill points for later.                
                """
            )+self.__htag(
                """
                <u>Shopping</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                As the name suggests, this would be visiting various shops to browse items. To
                make things interesting; the DM might consider doing things such as varying
                goods from town to town or possibly varying prices between regions to allow an
                extra incentive for checking shops as well as to keep things from getting stale.
                For players, it might be a good idea to save a bit of the money received during
                character creation in case the campaign's environment or circumstances make
                certain items more valuable than others.
                """,
            )+self.__htag(
                """
                <u>Information Gathering</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                Gathering information is extremely important, especially in cases where none of
                the party members have any connection to the area the campaign is taking place
                in. Information gathering can help the party be better prepared for challenges
                and obstacles which may appear later and could help avoid nasty surprises.
                <p style=\"page-break-before: always;\"></p>
                """
            )+self.__htag(
                """
                <u>Sightseeing</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                This primarily refers to exploring the area in which the party is currently
                resting in. This could involve visiting bars to gamble or drink, visiting a
                famous landmark such as a library or Colosseum, or conversing and interacting
                with townsfolk. Sightseeing is mainly used as a way for players to spend a few
                more minutes enjoying the game vs. being a purely functional activity and it is
                up to the DM and players to determine how valuable the time spent sightseeing
                truly is.
                """
            )+self.__htag(
                """
                <u>Side Quests</u>
                """,
                'h4'
            )+self.__paragraph(
                """
                During free time activities, one of the party members may stumble across the
                opportunity for a side quest. That is, a quest not related to the campaign but
                which may offer additional chances for rewards as well as additional battles
                within the campaign. Upon receiving the opportunity for a side quest; the DM has
                the players vote on whether they want to pursue or abandon the side quest or
                not. In most cases, it is better to not split the group and to keep side quests
                as an all or nothing mechanism. However, the DM has the freedom to change this
                and allow one or more members of the group to attempt the side quest without the
                rest of the group. This could be especially useful in cases where the members
                not partaking need some extra free time to train or study or to otherwise work
                on fine-tuning their characters.
                """
            )+self.__paragraph(
                """
                In addition to making the game less repetitive, free time is also a powerful
                tool for the DM and the following schedule is suggested (but not enforced) to
                help play time move smoothly.
                """
            )+self.__paragraph(
                """
                <ul><li>
                Warm Up + Free Time 10 ~ 15 min
                <ul><li>
                Review what happened during the previous session
                </li><li>
                DM gives feedback to players if needed
                </li><li>
                Players give feedback to DM if needed
                </li><li>
                Players do any of the free-time activities listed above
                </li></ul></li><li>
                Campaign Time: Depends on DM
                <ul><li>
                DMs should try to stick to a set schedule and leave in a bit of buffer time (at
                least 15 min) at the end of the play session. For example; if the party just
                reached a cave which the DM knows will take them a while to get through, but
                there's only 10 minutes left before the normal cut of time; it might be a good
                idea to announce free time.
                </li></ul></li><li>
                Free Time 10 ~ 15 min
                <ul><li>
                Players do any of the free-time activities listed above
                </li></ul></li></ul>
                """
            )+self.__paragraph(
                """
                It should also be noted that players can only perform one free time activity
                during a given free-time space. Although as always; the DM may choose to allow
                more/less free time activities as they see fit.
                """
            )
        )
        # Add section for Character Creation
        self.__add_section(
            "6. Character Creation",
            self.__paragraph(
                """
                Another one of the major goals of this system is to keep character creation as 
                flexible and open as possible. with this in mind, players should always be 
                encouraged to create new races, or classes for their characters. If a player 
                decides to create their own class or race they should work with the DM to 
                ensure that the addition makes sense. With that in mind; character creation 
                """
            )+self.__htag(
                """
                <u>
                    1. Create Your Character's Background:
                </u>
                """
            )+self.__paragraph(
                """
                The first step in character creation should be to flesh out each player's 
                character as a living entity. A character's race, stats, class, etc. should 
                flow from who that character is as a living breathing creature; not the other 
                way around. Since Kite relies so heavily on narration, it is very important 
                that characters be thought of in terms of their background vs. in terms of 
                """
            )+self.__htag(
                """
                <u>
                    2. Choose a Race and Class
                </u>
                """
            )+self.__paragraph(
                """
                After players decide on their character's background, the next step is to 
                choose a race and class for the character. The race and class should support 
                the character's background and most important it should be a race and class the 
                character wants to play vs. a race and class the player "thinks will do the 
                best." When creating a character, some good questions to ask are: How does the 
                character fit into society? Are they well liked? An outcast? Do they prefer to 
                """
            )+self.__paragraph(
                """
                The DM should be actively involved in all character creation regardless of 
                whether it's custom or stock. Also, it is advised that when creating custom 
                races or classes that the custom Race/Class sections be used as a template 
                (respectively) as this will help ensure that the created content is somewhat 
                """
            )+self.__htag(
                """
                <u>
                    3. Choose Stats and Skills
                </u>
                """
            )+self.__paragraph(
                """
                By default, each player gets 1 stat point and up to 2 skill points in addition 
                to any stats or skills provided by their race and class by default. The DM may 
                modify these amounts, especially if wanting to run a higher level campaign. The 
                idea being to try and make characters a bit more rounded out. Once again, the 
                DM should work with each player to make sure their character's skill selection 
                both follows the net rule of zero and also to ensure that all skills chosen 
                (both positive and negative) make sense in relation to the character's 
                """
            )+self.__htag(
                """
                <u>
                    4. Buy Items
                </u>
                """
            )+self.__paragraph(
                """
                Each player is given 250G to start out. The DM may modify this amount to be 
                more or less depending on how much they want each player to start out with. 
                Players may also want to save their gold as shop amounts may offer better deals 
                """
            )+self.__paragraph(
                """
                It should also be noted that a player will not need to purchase items required 
                for their craft in most cases as these are considered class items and the 
                player is given an item for free. However, the player may also want to give 
                their character a bit of an edge such as buying an iron sword instead of using 
                """
            )+self.__htag(
                """
                <u>
                    5. Additional Items and finishing Touches
                </u>
                """
            )+self.__paragraph(
                """
                Players can swap out their class ability for alternate abilities if desired and 
                also hammer out specific things about chosen lore, additional learned 
                languages, etc. The DM will also work with any characters with crafting skills 
                """
            )+self.__paragraph(
                """
                The goal here is to polish each character and make sure nothing feels off or 
                incomplete. To put it another way; this is where you polish the rough draft of 
                your character into the final copy. The DM should work with players closely 
                during this last step to ensure they are aware of all changes being made so 
                that there are no surprises or miss steps when running the campaign either on 
                """
            )
        )

        # Add languages and races section
        self.__add_section(
            "7. Languages & Races",
            self.__paragraph(
                """
                kite includes several races to choose from. Some are traditional fantasy tropes 
                such as elves and dwarves and some such as the Mu are unique to Kite itself. 
                This is also the place where languages are defined as they tie in with race. By 
                default; races generally only know the languages provided. However, a player 
                """
            ),
            parser=self.__parse_lang_and_race
        )

        # Add classes section
        self.__add_section(
            "8. Classes",
            self.__paragraph(
                """
                Classes in Kite can be thought of more as templates rather than hard enforced
                and certainly do not represent all the choices for character creation.
                Additionally, Kite does not use classes to restrict which types of items an
                entity can/can't equip and this is done based on stats  vs. class. Classes are
                here to primarily give players an idea of what to look for when creating their
                character and as such any one of the classes can be either modified or a new
                class created if the player desires. As always, the DM should work with players
                when creating or changing any classes to ensure that the changes both make sense
                and will also fit in with the campaign.
                """
            ),
            parser=self.__parse_classes
        )

        # Add Magic Section
        chartStyle = 'padding: 20px; '
        chartStyle+= 'float: right; '
        chartStyle+= 'width: 400px; '
        chartStyle+= 'height: 490px; '
        self.__add_section(
            "9. Spells & Battle Skills",
            self.__paragraph(
                """
                Spells and battle skills can be thought of as special abilities which entities
                can use to attack with in lieu of weapons. Additionally, many spells can be
                leveled up or improved by studying or training and provide an additional way
                to strengthen one's character. However, before delving too deeply into the magic
                list; there are a couple of things which need to be defined.
                """
            )+self.__htag(
                "Elemental Affinity"
            )+self.__paragraph(
                f"""
                <img src="file:///{curWorkDir}/assets/element_chart.png" style="{chartStyle}"/>
                Kite's magic system contains 6 elements: Earth, Fire, Wind, Water, Light, and
                Shadow. In order to keep things simple and to avoid a lot of unnecessary
                memorization, the elements are both weak and strong against one another in
                accordance to the diagram on the right.
                """
            )+self.__paragraph(
                """
                To explain this a bit further. Earth magic deals 2x damage (rounded up) to
                entities with the wind attribute and only deal &frac12; damage (rounded down) to
                entities with the earth element. In return, wind magic deals 2x damage to
                entities with the earth element and &frac12; damage to entities with the wind
                element. The same relationship is held by fire and water, and light and dark.
                """
            )+self.__paragraph(
                """
                The goal in setting things up this way was to keep elemental affinities and
                attacks easy to handle as well as to provide a system which allows players to
                take advantage of elemental attributes in order to beat enemies which would
                be much harder to beat otherwise.
                """
            )+self.__htag(
                "Elemental Specialization"
            )+self.__paragraph(
                """
                Many of the spells and abilities in the Kite Fantasy system talk about the
                concept of an elemental specialization. What taking a specialization does is
                align an entity's natural attribute with a specific element. For example, taking
                a wind specialization will give many normally non-elemental spells the wind
                attribute. This means that the spells will be doubly effective against wind
                attacks but will be only half as effective against earth attacks. Additionally,
                many spells also give an added bonus or additional behavior for having a
                specialization vs being unspecialized. 
                """
            )+self.__paragraph(
                """
                Additionally, some abilities such as the
                dragon half's fire breath may be able to be modified with a different element;
                even if they don't specifically say they can be. Meaning, the player may want
                to play as an ice type dragon half instead of a fire. As with most things This
                is up to the DM to decide.
                """
            )+self.__paragraph(
                """
                To simplify things, by default a character can only take one specialization at 
                a time and the times/places a specialization may be changed is largely up to
                the DM. However, there are some cases where this could mean taking more than
                one element at a time. See the complex elements section for more information.
                """
            )+self.__htag(
                "Complex Elements"
            )+self.__paragraph(
                """
                As stated previously, the magic system has been compacted in order to keep the 
                system from getting bloated with too many class choices. This being said; many of
                the spells normally associated with other schools of magic such as Necromancy,
                Geomancy (Druids), Summoning, etc. can still be found in the system by selecting
                spells which match the desired school's spell set. With this in mind, there are
                a few complex elemental types which are formed by combining the 6 elements
                listed in the previous section together:
                <ul>
                    <li>{wind} {light} Electricity</li>
                    <li>{water} {dark} Ice</li>
                    <li>{water} {wind} Wood</li>
                    <li>{earth} {fire} Metal</li>
                </ul>
                """.format(**self.__elemTags),
                add_br=False
            )+self.__paragraph(
                """
                When choosing an elemental specialization, a mage can choose one of the complex
                elements as their specialization. Since each complex element consists of two
                different elements; it means any attack which uses a complex element is strong
                against two elements and also weak against two elements. For example; Ice deals
                2x damage (rounded up) to both fire and light aligned entities, and deals
                &frac12; damage (rounded down) to both water and dark aligned entities.
                """
            )+self.__paragraph(
                """
                One final thing to note is that in order to keep things simple. Complex elements
                use an all or nothing system. Meaning there is no 4x damage or &frac14; damage.
                To better summarize this:
                <ul>
                    <li>
                        If both an opposing entity's elements are weak against an attack, it still only does 2x damage
                    </li><br/>
                    <li>
                        If both of an opposing entity's elements are strong against an attack, it still only does &frac12; damage
                    </li><br/>
                    <li>
                        If one element of an opposing entity's elements is strong against an
                        attack and the other is weak; then the two cancel out and the attack
                        deals it's normal damage.
                    </li>
                </ul>
                To reiterate, this is about as crunchy as the system gets and much work has been
                done to try and distill the system down so that neither the player nor the DM
                has to memorize too much.
                """+self.__page_break(True),
                add_br=False
            )+self.__paragraph(
                """
                <h3>Spell Format</h3>
                <div class="container pop">
                    <div class="cont-title">
                        <span class="rel" style="width: 60%;">
                            <h4 class="nopad">Spell Name</h4>
                        </span>
                        <span class="rel" style="width: 10%;">
                            <strong>Range:</strong> #
                        </span>
                        <span class="rel" style="width: 10%;">
                            <strong>Element(s)</strong>
                        </span>
                        <span class="rel" style="width: 10%; padding-top: 0px; text-align: right;">
                            (1~#)<strong>&#9734;</strong>
                        </span>
                    </div>
                    <div class="cont-inner">
                        <span class="rel" style="width: 10%;"><strong>Levels</strong></span>
                        <span class="rel" style="width: 10%;"><strong>MP Cost</strong></span>
                        <span class="rel" style="width: 10%;"><strong>Req. Stat</strong></span>
                        <span class="rel" style="width: 60%; text-align: right;"><strong>Effect(s)</strong></span>
                        <span class="rel" style="width: 10%;">(1 ~ #)&#9733;</span>
                        <span class="rel" style="width: 10%;"># MP</span>
                        <span class="rel" style="width: 10%;">Stat Name</span>
                        <span class="rel" style="width: 60%; text-align: right;">The effect the spell has</span>
                    </div>
                </div>
                """
            ),
            parser=self.__parse_spells,
            suffix=self.__htag(
                "Creating Custom Spells"
            )+self.__paragraph(
                """
                Like most aspects of the system, spell creation is completely open and the
                system itself kind of assumes that at some point there will be the need to
                create some spell which the system doesn't support simply because everyone's
                idea of what certain things are is different. For examply, what I view as a
                "druid spell" may differ vastly from what you view as a "druid spell".
                """
            )+self.__paragraph(
                """
                With the above in mind, spell creation is largely left up to the GM and Players
                to work out. That being said, there are a few recommended guidelines designed to
                keep spells from becoming too powerful. It is up to the GM to enforce these and
                they are certainly not mandatory. However, if the GM or player are uncertain on
                how to go about creating a spell, these are certainly good guidelines to follow:
                <ol>
                    <li>
                        Add 1 mana to the MP cost for the spell for every 1 block of damage a
                        spell inflicts, prevents, or restores.
                    </li><br/>
                    <li>
                        Add 2 MP to the MP cost for the spell if the spell inflicts a status
                        condition
                    </li><br/>
                    <li>
                        Only 1 status condition can be added to a spell at a time
                    </li><br/>
                    <li>
                        Add 1 MP to the MP cost for the spell for each entity the spell targets
                        past the first.
                    </li><br/>
                    <li>
                        If a spell targets an area vs. a single entity, double the mana cost
                        of the spell.
                    </li><br/>
                    <li>
                        If a spell targets an entire team or the entire field, triple the mana
                        cost of the spell
                    </li><br/>
                    <li>
                        If a spell targets a random entity, or team; half the mana cost of the
                        spell.
                    </li>
                    <li>
                        If a spell is ongoing, decrease the mana cost of the spell by 2
                    </li><br/>
                    <li>
                        If a spell is ongoing, caster must pay 1/2 of the spell's MP cost at
                        the beginning of each turn to keep the spell going.
                    </li><br/>
                    <li>
                        For every 3 mana the spell costs, increase the stat requirement by 1
                        e.g. a spell which costs 15 to cast has a stat requirement of 5
                    </li><br/>
                    <li>
                        When a spell levels up, multiply the damage and MP cost by the spell's
                        level to obtain the new damage and MP cost. e.g. if a spell does 2
                        damage and costs 4 MP at level 1, it will deal 4 damage and cost 8 MP
                        at level 2.
                    </li><br/>
                    <li>
                        A spell's "max level" is reached when either the spell reaches level 5,
                        the stat requirement goes above 5, or the MP cost goes above 20.
                    </li><br/>
                </ol>
                """
            )+self.__htag(
                "Leveling Up Spells"
            )+self.__paragraph(
                """
                Spells are typically leveled up through training or studying. The exact
                amount of time needed for a spell to level up is up to the GM.
                Additionally, the GM can decide to have the player roll to level up.
                one nice idea when rolling to level up and to keep things from getting
                to stale is to add a bonus point to damage if the player rolls a 6 or 
                add an additional point to the MP cost if they roll a 1. Like most other
                things in the system, the specifics on leveling up spells are largely
                between the GM and players to work out and nothing printed in this
                section or the one above detailing "spell creation rules" should be
                considered hardfast. The GM always has the ability to override the rules
                """
            )+self.__paragraph(
                "<h3>Forgetting Spells</h3>",
                add_br=False
            )+self.__paragraph(
                """
                Forgetting spells is much less involved than forgetting skills. You simply strike
                through or cross out the spell from your spellbook (something to indicate you no
                longer know that spell). However, before forgetting a spell it should be noted that
                once forgotten, all the time spent training that spell will be lost. If you decide
                to re-learn the spell at a later time; you will have to start from scratch.
                """
            )
        )

        self.__add_section(
            title  = "10. Abilities",
            prefix = self.__paragraph(
                """
                Abilities can be thought of as extra perks or advantages which make a character
                uniqoe or give a character an edge over other characters in certain situations.
                Generally speaking, everyone starts the game with at least 2 abilities due to
                their race. As a general rule and to keep any one character from getting too
                overpowered A character is limited to 3 abilities. However, in an effort to
                keep characters dynamic, abilities can be forgotten similar to spells. For more
                on this see the section labeled "Forgetting Abilities" at the end of this section
                """
            ),
            parser=self.__parse_abilities,
            suffix=self.__htag(
                "Forgetting Abilities"
            )+self.__paragraph(
                """
                Like spells, abilities can be forgotten by striking through them, crossing them out
                or otherwise marking them as forgotten in some way. This is doen to keep characters
                flexible. Additionally, unlike spells; abilities don't really level up so there's
                less of a penalty for forgetting them. This being said, the GM may attach conditions
                to learning certain abilities and so like spells, when an ability is forgotten it
                should be assumed that re-learning that ability will result in relearning from scratch.
                """
            )+self.__htag(
                "Creating Custom Abilities"
            )+self.__paragraph(
                """
                Like most aspects of the system, if there is a particular ability a player wants for
                their character; the GM and that player should work together to make that ability a
                reality. That being said there are a few suggestions for creating abilities to keep
                the game balanced and as always the GM may add to or override any of the suggested
                rules below:
                <ul>
                    <li>
                        If the ability is an active ability, it is recommended to limit the number
                        of uses a character can use that ability per session. Most active abilities
                        can only be used once. However, this is not a steadfast rule and there may
                        be times when an active ability can be permitted to be used multiple times
                        per rest period or may recharge under completely different circumstances.
                    </li><br/>
                    <li>
                        If a passive ability gives an advantage under certain conditions e.g.
                        weather, location, using certain types of magic, etc. It is recommended
                        that the ability give a proportional disadvantage under some other
                        condition. For example, if the character gets a +2 to speed when the
                        weather is sunny, give the character -2 to speed when it's raining.
                    </li><br/>
                    <li>
                        If the passive ability is dependent on a specific action to be
                        performed, a negative does not need to be assigned; however it is
                        recommended to keep abilities like these fairly weak to avoide the
                        game becoming unbalanced. e.g. If character rolls a 6 when resting
                        HP is restored to full, regardless of location.
                    </li><br/>
                </ul>
                """
            )
        )


    # ==========================================================================
    # = THROW PUBLICLY ACCESSIBLE FUNCTIONS HERE                               =
    # ==========================================================================
    """
    ============================================================================
    = Write Out PDF Method                                                     =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Adds the body and html tags to the end of the HTML document and then     =
    = writes the document out to file.                                         =
    ============================================================================
    """
    def writeOutPdf(
        self,       # (Ref) A reference to this class, required by all members
        file_path   # (String) pdf file to write out to
    ):
        self.__close_tag()
        self.__close_tag()
        pdfkit.from_string( 
            self.__html, 
            file_path, 
            configuration=self.__config,
            options=self.__options
        )
        if self.__debug:
            html = '.'.join(file_path.split('.')[:-1])
            html += '.html'
            f = open(html, 'w')
            f.write(self.__html)
            f.close()

    # ==========================================================================
    # = GENERATE HEADER METHOD HERE                                            =
    # ==========================================================================
    """
    ============================================================================
    = Header Method                                                            =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Creates the header for the HTML page.                                    =
    ============================================================================
    """
    def __header(
        self    # (Ref) A reference to this class, required by all members
    ):
        self.__open_tag('head')
        self.__open_tag('style')

        # Generic CSS rules, impact entire document
        self.__open_css("body", CSSItem.TAG)
        self.__write("font-family: Arial, Helvetica, Sans-Serif;")
        self.__write("font-size: 105%")
        self.__close_css()

        self.__open_css("div", CSSItem.TAG)
        self.__write('page-break-inside: avoid;')
        self.__close_css()

        # CSS For Title Page
        self.__open_css('title',CSSItem.CLASS)
        self.__write('text-align: center;')
        self.__write('padding-top: 50%;')
        self.__close_css()

        # CSS For Section Page
        self.__open_css('section',CSSItem.CLASS)
        self.__write('text-align: left;')
        self.__write('line-height: 150%;')
        self.__write('page-break-before: always;')
        self.__close_css()

        # Container title
        self.__open_css('cont-title',CSSItem.CLASS)
        self.__write('background: #cccccc;')
        self.__write('border-bottom: 1px solid #999999;')
        self.__write('padding: 5px;')
        self.__close_css()

        # Active Ability title
        self.__open_css('a-abil-title',CSSItem.CLASS)
        self.__write('background: #ffffcc;')
        self.__write('border-bottom: 1px solid #999999;')
        self.__write('padding: 5px;')
        self.__close_css()
    
        # Passive Ability title
        self.__open_css('p-abil-title',CSSItem.CLASS)
        self.__write('background: #cce5ff;')
        self.__write('border-bottom: 1px solid #999999;')
        self.__write('padding: 5px;')
        self.__close_css()

        # Sub Title
        self.__open_css('cont-sub-title',CSSItem.CLASS)
        self.__write('background: #cccccc;')
        self.__write('border-top: 1px solid #999999;')
        self.__write('border-bottom: 1px solid #999999;')
        self.__write('padding: 5px;')
        self.__close_css()

        # Pop (Adds box shadow)
        self.__open_css('pop',CSSItem.CLASS)
        self.__write('box-shadow:3px 3px 5px #cccccc;')
        self.__write('margin: 20px 0px 0px 0px;')
        self.__close_css()

        # Inner Container class
        self.__open_css('cont-inner',CSSItem.CLASS)
        self.__write('width: auto;')
        self.__write('padding: 5px;')
        self.__close_css()

        # Container class
        self.__open_css('container', CSSItem.CLASS)
        self.__write('border: 1px solid #999999;')
        self.__write('margin-bottom: 5px;')
        self.__close_css()

        # Nopad class
        self.__open_css('nopad',CSSItem.CLASS)
        self.__write('padding:0px;')
        self.__write('margin:0px;')
        self.__close_css()

        # rel class
        self.__open_css('rel', CSSItem.CLASS)
        self.__write('display: inline-block;')
        self.__write('vertical-align: top;')
        self.__write('padding-left: 5px;')
        self.__write('padding-right: 5px;')
        self.__close_css()

        # Close out header section
        self.__close_tag()
        self.__close_tag()
        
    # ==========================================================================
    # = PAGE GENERATION FUNCTIONS HERE (IN ORDER)                              =
    # ==========================================================================
    """
    ============================================================================
    = Add Title Method                                                         =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Loads in the title.json file and creates an HTML element for it          =
    ============================================================================
    """
    def __add_title(
        self,       # (Ref) A reference to this class, required by all members
        file_path   # (String) json file to load title from
    ):
        # Load json file into memory
        f = open(file_path, 'r')
        jdata = json.loads(f.read())
        f.close()

        # Process json file into html
        self.__open_tag('div',{'class':'title'})
        self.__open_tag('h1')
        self.__write(jdata['title']+' ('+str(jdata['version'])+')')
        self.__close_tag()
        self.__open_tag('h3')
        self.__write('Written By: '+jdata['author'])
        self.__close_tag()
        self.__close_tag()

    """
    ============================================================================
    = Add Description Method                                                   =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Loads in the description.json file and creates an HTML element for it    =
    ============================================================================
    """    
    def __add_description(
        self,       # (Ref) A reference to this class, required by all members
        file_path   # (String) json file to load title from
    ):
        # Load json file into memory
        f = open(file_path, 'r')
        jdata = json.loads(f.read())
        f.close()

        # Process json file into html
        self.__open_tag('div',{'class':'section'})

        # Process Description
        self.__open_tag('h2')
        self.__write('Description')
        self.__close_tag()
        self.__write('<hr/>')
        self.__open_tag('p')
        self.__write(' '.join(jdata['description']))
        self.__close_tag()

        # Process Overrides
        self.__open_tag('u')
        self.__open_tag('h3')
        self.__write('Overrides')
        self.__close_tag()
        self.__close_tag()
        self.__open_tag('ul')
        for o in jdata["overrides"]:
            self.__open_tag('li')
            self.__write(o)
            self.__close_tag()
        self.__close_tag()
        
        # Process Optional Components
        self.__open_tag('u')
        self.__open_tag('h3')
        self.__write('Optional Components')
        self.__close_tag()
        self.__close_tag()
        self.__open_tag('ul')
        for o in jdata["optional-components"]:
            self.__open_tag('li')
            self.__write(o)
            self.__close_tag()
        self.__close_tag()

        # Process Added Components
        self.__open_tag('u')
        self.__open_tag('h3')
        self.__write('Added Components')
        self.__close_tag()
        self.__close_tag()
        self.__open_tag('ul')
        for c in jdata["added-components"]:
            key = [ x for x in c.keys()][0]
            self.__open_tag('li')
            self.__open_tag('p')
            self.__open_tag('u')
            self.__open_tag('strong')
            self.__write(key+':')
            self.__close_tag()
            self.__close_tag()
            self.__write(' '.join(c[key]))
            self.__close_tag()
            self.__close_tag()
        self.__close_tag()

        # Close div
        self.__close_tag()

    """
    ============================================================================
    = Add Contents Method                                                      =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Loads in the contents.json file, and creates an HTML element for it      =
    ============================================================================
    """       
    def __add_contents(
        self,       # (Ref) A reference to this class, required by all members
        contents    # (List<String>) Table of contents items to display
    ):
        # Process json file into html
        self.__open_tag('div',{'class':'section'})

        # Process Description
        self.__open_tag('h2')
        self.__write('Table Of Contents')
        self.__close_tag()
        self.__write('<hr/>')
        self.__open_tag('h3')
        self.__open_tag('ol')
        for c in contents:
            self.__open_tag('li')
            self.__write(c)
            self.__close_tag()
        self.__close_tag()
        self.__close_tag()
        self.__close_tag()

    """
    ============================================================================
    = Add Introduction Method                                                  =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Loads in the introduction.json file, and creates an HTML element for it  =
    ============================================================================
    """      
    def __add_section(
        self,               # (Ref) A reference to this class, required by all 
                            # members

        title,              # (String) The text to display at the very top of
                            # the section

        prefix,             # (String) A block of text to display at the
                            # beginning of the section

        suffix      = "",   # (String) A block of text to display at the end of
                            # the section

        parser      = None, # (Ref) a reference to a function used to parse
                            # the passed in file once it's been loaded into
                            # memory
    ):
        # Process json file into html
        self.__open_tag('div',{'class':'section'})

        # Process Description
        self.__open_tag('h2')
        self.__write(title)
        self.__close_tag()
        self.__write('<hr/>')
        self.__write(prefix)

        if parser:
            parser()

        self.__write(suffix)

    """
    ============================================================================
    = Parse Stats Method                                                       =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in stats data loaded from file and adds it to the appropriate html =
    = section.                                                                 =
    ============================================================================
    """      
    def __parse_stats(
        self        # (Ref) A reference to this class, required by all members
    ):
        statCat = self.__loader.get('stats')
        self.__open_tag('ul')
        for stat in statCat.getContentNames(True):
            s = statCat.get(stat)
            abbr = s['abbr'] and ' ({abbr})'.format(abbr=s['abbr']) or ''
            name = '<u><strong>'+s['name']+' '+abbr+'</strong></u> -- '
            desc = ' '.join(s['description'])
            self.__open_tag('p')
            self.__open_tag('li')
            self.__write(name+desc)
            self.__close_tag()
            self.__close_tag()           
        self.__close_tag()

    """
    ============================================================================
    = Parse Skills Method                                                      =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in skill data loaded from file and adds it to the appropriate html =
    = section.                                                                 =
    ============================================================================
    """        
    def __parse_skills(
        self        # (Ref) A reference to this class, required by all members
    ):
        skill_cat = self.__loader.get('skills')
        skill_sec = skill_cat.getContentNames()
        for section in skill_sec:
            sec = skill_cat.get(section)
            sec_skills = sec.getEntryNames()
            self.__open_tag('u')
            self.__open_tag('h3')
            self.__write('<br/><br/>'+sec.name)
            self.__close_tag()
            self.__close_tag()
            self.__open_tag('p')
            self.__write(' '.join(sec.description))
            self.__close_tag()
            for entry in sec_skills:
                sk = sec.get(name=entry)
                self.__open_tag('p')
                self.__write(
                    '<u>'+sk['name']+'</u>'+' -- '+' '.join(sk['description'])
                )
                self.__close_tag()
        self.__close_tag()

    """
    ============================================================================
    = Parse Abilities Method                                                   =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in ability data loaded from file and adds it to the appropriate    =
    = html section.                                                            =
    ============================================================================
    """   
    def __parse_abilities(
        self    # (Ref) A reference ot this class, required by all members
    ):
        ability_tree = self.__loader.get('abilities')
        keys = ability_tree.getContentNames()
        for key in keys:
            section = ability_tree.get(key)
            abilities = section.getEntryNames()
            self.__open_tag('u')
            self.__open_tag('h3')
            self.__write(section.name.title())
            self.__close_tag()
            self.__close_tag()
            self.__open_tag('p')
            self.__write(' '.join(section.description))
            self.__close_tag()
            for entry in abilities:
                ability = section.get(name=entry)

                #sect = cat.get(ability['type'])
                #a = sect.get(ability['name'])
                atype = section.name.title()
                self.__open_tag('div',{'class':'container'})
                self.__open_tag('div',{'class':f'{atype.lower()[0]}-abil-title cont-inner'})
                self.__write(f"<strong>{ability['name']}</strong>")
                self.__close_tag()
                self.__open_tag('div',{'class':'cont-inner'})
                self.__write(' '.join(ability['description']))
                self.__close_tag()
                self.__close_tag()
                self.__write("<br/>")
            if key != keys[-1]:
                self.__page_break()

    """
    ============================================================================
    = Parse Spells Method                                                      =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in spell data loaded from file and adds it to the appropriate html =
    = section.                                                                 =
    ============================================================================
    """   
    def __parse_spells(
        self     # (Ref) A reference to this class, required by all members
    ):
        spell_cat = self.__loader.get('spells')
        spell_sec = spell_cat.getContentNames()
        for section in spell_sec:
            sec = spell_cat.get(section)
            sec_spells = sec.getEntryNames()
            self.__open_tag('u')
            self.__open_tag('h3')
            self.__write(sec.name.title())
            self.__close_tag()
            self.__close_tag()
            self.__open_tag('p')
            self.__write(' '.join(sec.description))
            self.__close_tag()
            for entry in sec_spells:
                sp = sec.get(name=entry)

                # Use spell rules to define MP cost here
                targetTypes = {
                    'self':1,
                    'ground':1,
                    'entity':1,
                    'area':2,
                    'team':3,
                    'all':3,
                    'rentity':0.5,
                    'rarea':1,
                    'rteam':1.5,
                    'rall':1.5

                }
                # First calculate spell's base cost
                base_cost = sp['dmg']                                  # 1. spell damage determines base mana cost
                base_cost += (2 if sp['condition'] else 0)             # 2. If spell causes a status condition +2 to cost
                base_cost += max(0, sp['numTargets'] - 1)              # 3. Increase mana cost by 1 for each target past the 
                                                                       #    first
                base_cost *= targetTypes[sp['targetType']]             # 4. If spell targets an area, double the  mana cost
                                                                       # 5. If spell targets entire team or entire field triple
                                                                       #    mana cost
                                                                       # 6. If spell target is random, half mana cost
                base_cost = max(                                       # 7. If spell is ongoing, decrease MP cost by 2
                    0, 
                    base_cost - (2 if sp['ongoing'] else 0)
                )
                base_cost = max(0, base_cost + sp["bonus"])            # 8. GM may choose to increase/decrease MP cost for 
                                                                       #    a spell
                
                # Next, check to see if max level needs to be updated
                m_lev_adj = 0
                mp_cost = int(round(base_cost*(m_lev_adj+1)))
                req_stat = int(round(mp_cost / 3))
                level_check = m_lev_adj < sp["maxLevel"]
                mp_check    = mp_cost <= 20
                stat_check  = req_stat <= 5
                while level_check and mp_check and stat_check:
                    m_lev_adj += 1
                    mp_cost = int(round(base_cost*(m_lev_adj+1)))
                    req_stat = int(round(mp_cost / 3))
                    level_check = m_lev_adj < sp["maxLevel"]
                    mp_check    = mp_cost <= 20
                    stat_check  = req_stat <= 5
                sp["maxLevel"] = m_lev_adj

                rng = ('?' if sp['range'] == '?' else sp['range'])
                elem = self.__elemTags[sp['element']]
                self.__open_tag('div',{'class':'container pop'})
                self.__open_tag('div',{'class':'cont-title'})
                self.__open_tag('span',{'class':'rel','style':'width: 55%;'})
                self.__open_tag('h4',{'class':'nopad'})
                self.__write(sp['name'])
                self.__close_tag()
                self.__close_tag()
                self.__open_tag('span',{'class':'rel','style':'width: 10%;'})
                self.__write(f'<strong>Range: {rng}</strong>')
                self.__close_tag()
                self.__open_tag('span',{'class':'rel','style':'width: 10%; text-align: center;'})
                self.__write(elem)
                self.__close_tag()
                styles='width: 17.85%; padding-top: 0px; text-align: right;'
                self.__open_tag('span',{'class':'rel','style':f'{styles}'})
                self.__write(sp['maxLevel']*'&nbsp;&#9734;')
                self.__close_tag()
                self.__close_tag()
                self.__open_tag('div',{'class':'cont-inner'})
                self.__open_tag('span',{'class':'rel','style':'width: 15%;'})
                self.__write('<strong>Levels</strong>')
                self.__close_tag()
                self.__open_tag('span',{'class':'rel','style':'width: 10%;'})
                self.__write('<strong>MP Cost</strong>')
                self.__close_tag()
                self.__open_tag('span',{'class':'rel','style':'width: 10%;'})
                self.__write('<strong>Req. Stat</strong>')
                self.__close_tag()
                styles = 'width: 55%; text-align: left;'
                self.__open_tag('span',{'class':'rel','style':f'{styles}'})
                self.__write('<strong>Effect(s)</strong>')
                self.__close_tag()
                self.__write('<hr style="border: 1px solid #dddddd;">')
                
                if sp['ongoing']:
                    sp['notes'].append(
                        ' '.join(
                            [
                                "Must pay 1/2 cost of spell (rounded up)",
                                "at the beginning of each turn to keep",
                                "the spell going."
                            ]
                        )
                    )

                for i in range(0, sp["maxLevel"]):
                    mp_cost = int(round(base_cost * (i+1)))
                    req_stat_val = int(round(mp_cost / 3))
                    req_stat = ("{stat} {val}" if req_stat_val else "-").format(
                        stat=sp['stat'],
                        val = req_stat_val
                    )
                    level_desc = ' '.join(sp['description']).format(
                        dmg=sp['dmg']*(i+1)
                    )
                    color = 'background: {col};'.format(
                        col = i % 2 and '#e0e0e0' or '#ffffff'
                    )
                    self.__open_tag('div',{'class':'cont-inner','style':f'{color}'})
                    self.__open_tag('span',{'class':'rel','style':'width: 17%;'})
                    self.__write((i+1)*'&#9733;&nbsp;')
                    self.__close_tag()
                    self.__open_tag('span',{'class':'rel','style':'width: 10%;'})
                    self.__write(f'{mp_cost}')
                    self.__close_tag()
                    self.__open_tag('span',{'class':'rel','style':'width: 10%;'})
                    self.__write(f'{req_stat}')
                    self.__close_tag()
                    self.__open_tag('span',{'class':'rel','style':f'{styles}'})
                    self.__write(level_desc)
                    self.__close_tag()
                    self.__close_tag()
                self.__close_tag()
                if len(sp['notes']):
                    self.__open_tag('div',{'class':'cont-inner'})
                    self.__open_tag('ul')
                    for note in sp['notes']:
                        self.__open_tag('li')
                        self.__write(note)
                        self.__close_tag()
                    self.__close_tag()
                    self.__close_tag()
                self.__close_tag()
            self.__page_break()
        self.__close_tag()

    """
    ============================================================================
    = Parse Classes Method                                                     =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in class data loaded from file and adds it to the appropriate html =
    = section.                                                                 =
    ============================================================================
    """          
    def __parse_classes(
        self     # (Ref) A reference to this class, required by all members
    ):
        classCat = self.__loader.get('classes')
        for kClass in classCat.getContentNames(True):
            c = classCat.get(kClass)
            self.__open_tag('div',{'class':'container pop'})
            self.__open_tag('div',{'class':'cont-title'})
            self.__open_tag('h3',{'class':'nopad'})
            self.__write(c['name'])
            self.__close_tag()
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__write('&nbsp;'*8+' '.join(c['description']))
            self.__close_tag()

            # Generate skills section
            self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
            self.__write('<strong>Skills</strong>')
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__open_tag('ul')
            for s in c['skills']:
                val = self.__format_value(s['value'])
                name = s['name']
                self.__write(f'<li>{name}: {val}</li>')
            self.__close_tag()
            self.__close_tag()

            self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
            self.__write('<strong>Items</strong>')
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__open_tag('ul')
            for it in c['items']:
                name = it['name']
                qty = it['qty']
                qty = qty > 1 and f' x {qty}' or ''
                notes = it['notes']
                self.__write(f'<li>{name}{qty}</li>')
                if notes:
                    self.__write(f'<ul><li>{notes}</li></ul>')
            self.__close_tag()
            self.__close_tag()

            # close container
            self.__close_tag()
            self.__page_break()

        # Create custom class
        c = {
            'name':'Custom',
            'description':[
                "As with race, a custom class template is provided for the event that the player",
                "wishes to play a class not listed above. As stated throughout this guide; Kite",
                "strives to build classes, races, etc. around characters, not the other way",
                "around. If a player wishes to create their own class, they should always be",
                "free to do so. However, it should also be noted that as always, the DM has final",
                "say on any class created to both ensure it makes sense and also to ensure it",
                "doesn't leave the player at a disadvantage during the campaign."
            ],
            'skills':[
                {
                    "name":"Up to 3 skills",
                    "value":1
                },
                {
                    "name":"A number of skills equal to the +1 skills chosen",
                    "value":-1
                }
            ],
            'items':[
                {
                    'name':'up to 3 items needed by the class to perform their skills',
                    'qty':1,
                    'notes':'Must be the weakest items in their class: e.g. copper, pine, etc.'
                }
            ]
        }
        self.__open_tag('div',{'class':'container pop'})
        self.__open_tag('div',{'class':'cont-title'})
        self.__open_tag('h3',{'class':'nopad'})
        self.__write(c['name'])
        self.__close_tag()
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__write('&nbsp;'*8+' '.join(c['description']))
        self.__close_tag()

        # Generate skills section
        self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
        self.__write('<strong>Skills</strong>')
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__open_tag('ul')
        for s in c['skills']:
            val = self.__format_value(s['value'])
            name = s['name']
            self.__write(f'<li>{name}: {val}</li>')
        self.__close_tag()
        self.__close_tag()

        self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
        self.__write('<strong>Items</strong>')
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__open_tag('ul')
        for it in c['items']:
            name = it['name']
            qty = it['qty']
            qty = qty > 1 and f' x {qty}' or ''
            notes = it['notes']
            self.__write(f'<li>{name}{qty}</li>')
            if notes:
                self.__write(f'<ul><li>{notes}</li></ul>')
        self.__close_tag()
        self.__close_tag()

        # close container
        self.__close_tag()
        #self.__page_break()
    


    """
    ============================================================================
    = Parse Languages & Race Method                                            =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Reads in language and race data loaded from file and adds it to the      =
    = appropriate html                                                         =
    = section.                                                                 =
    ============================================================================
    """          
    def __parse_lang_and_race(
        self     # (Ref) A reference to this class, required by all members
    ):
        self.__write('<u><h3>Languages</h3></u>')
        langCat = self.__loader.get('languages')
        self.__open_tag('ul')
        for language in langCat.getContentNames(True):
            lang = langCat.get(language)
            name = '<u><strong>'+lang['name']+':</strong></u> '
            desc = ' '.join(lang['description'])
            self.__open_tag('p')
            self.__open_tag('li')
            self.__write(name+desc)
            self.__close_tag()
            self.__close_tag()           
        self.__close_tag()
        self.__page_break()
        self.__write('<u><h3>Races</h3></u>')
        raceCat = self.__loader.get('races')
        for race in raceCat.getContentNames(True):
            r = raceCat.get(race)
            self.__open_tag('div',{'class':'container pop'})
            self.__open_tag('div',{'class':'cont-title'})
            self.__open_tag('h3',{'class':'nopad'})
            self.__write(r['name'])
            self.__close_tag()
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__write('&nbsp;'*8+' '.join(r['description']))
            self.__close_tag()

            self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
            self.__write('<strong>Stat Bonuses</strong>')
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__open_tag('ul')
            for s in r['stats']:
                val = self.__format_value(s['value'])
                name = s['name']
                self.__write(f'<li>{name}: {val}</li>')
            self.__close_tag()
            self.__close_tag()

            self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
            self.__write('<strong>Abilities</strong>')
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            cat = self.__loader.get('abilities')
            for abil in r['abilities']:
                sect = cat.get(abil['type'])
                a = sect.get(abil['name'])
                atype = abil['type'][0].upper()+abil['type'][1:]
                self.__open_tag('div',{'class':'container'})
                self.__open_tag('div',{'class':f'{atype.lower()[0]}-abil-title cont-inner'})
                self.__write(f"<strong>{a['name']} ({atype})</strong>")
                self.__close_tag()
                self.__open_tag('div',{'class':'cont-inner'})
                self.__write(' '.join(a['description']))
                self.__close_tag()
                self.__close_tag()        
            self.__close_tag()

            self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
            self.__write('<strong>Languages</strong>')
            self.__close_tag()
            self.__open_tag('div',{'class':'cont-inner'})
            self.__open_tag('ul')
            for lang in r['languages']:
                self.__write(f'<li>{lang}</li>')
            self.__close_tag()
            self.__close_tag()
            # close container
            self.__close_tag()
            self.__page_break()
    
        # Create custom class entry
        self.__open_tag('div',{'class':'container pop'})
        self.__open_tag('div',{'class':'cont-title'})
        self.__open_tag('h3',{'class':'nopad'})
        self.__write("Custom")
        self.__close_tag()
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__write(self.__paragraph(
            """
            As stated earlier; kite strives to be a flexible system which rewards creativity
            and thinking outside the box. As such, a custom race definition exists for
            players who want to play a race not listed in the guide. That being said; there
            are a few guidelines for creating a custom race. 
            """,
            add_br=False
        ))
        self.__close_tag()

        self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
        self.__write('<strong>Stat Bonuses</strong>')
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__open_tag('ul')
        self.__write(
            '<li>Any: +2 (These can both be put in the same stat or in different stats)</li>'
        )
        self.__close_tag()
        self.__close_tag()

        self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
        self.__write('<strong>Abilities</strong>')
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__open_tag('ul')
        self.__write('<li>Passive: +1</li>')
        self.__write('<li>Active: +1</li>')
        self.__close_tag()
        self.__close_tag()

        self.__open_tag('div',{'class':'cont-sub-title cont-inner'})
        self.__write('<strong>Languages</strong>')
        self.__close_tag()
        self.__open_tag('div',{'class':'cont-inner'})
        self.__open_tag('ul')
        self.__write('<li>Common</li>')
        self.__write(
            """<li>
                Choice of any languages from the language section or the player
                can define their own.
            </li>"""
        )
        self.__close_tag()
        self.__close_tag()
        self.__close_tag()

    # ==========================================================================
    # = THROW HELPER FUNCTIONS DOWN HERE                                       =
    # ==========================================================================
    """
    ============================================================================
    = Open Tag Method                                                          =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Specifies we're opening a new HTML tag up. Creates the tag and then      =
    = auto-increments the indent                                               =
    ============================================================================
    """
    def __open_tag(
        self,           # (Ref) A reference to this class, required by all 
                        # members
        name,           # (String) Name of the tag to open
        options = {}    # (Dict) any options to add to the tag
    ):
        opts = self.__format_options(options)
        self.__html += self.__tab()+'<'+name+" "+opts+">\n"
        self.__indent += 1
        self.__stack.append(name)

    """
    ============================================================================
    = Close Tag Method                                                         =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Specifies we're closing an HTML tag. Creates the tag and then auto       =
    = decrements the indent                                                    =
    ============================================================================
    """
    def __close_tag(
        self,   # (Ref) A reference to this class, required by all members 
    ):
        name = self.__stack.pop()
        self.__indent -= 1
        tag = self.__tab()+'</'+name+'>\n'
        self.__html += tag

    """
    ============================================================================
    = Open Tag Method                                                          =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Calculates the number of spaces to add to the beginning of an HTML tag   =
    = based on the current indent level                                        =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (String) A string of whitespace to pad the beginning of a line with      =
    ============================================================================
    """
    def __tab(
        self    # (Ref) A reference to this class, required by all members
    ):
        return ' '*4*self.__indent

    """
    ============================================================================
    = Write Method                                                             =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Writes out text or HTML to the body of a tag without changing the indent =     
    ============================================================================
    """    
    def __write(
        self,   # (Ref) A reference to this class, required by all members
        text    # (String) Text to write out to the body of the tag
    ):
        self.__html += self.__tab()+text+'\n'

    """
    ============================================================================
    = Img Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Specialized write method for writing an img tag to html                  =    
    ============================================================================
    """    
    def __img(
        self,       # (Ref) A reference to this class, required by all members
        path,       # (String) Path to image to display
        options={}  # (Dict) any options to add to the tag
    ):
        opts = self.__format_options(options)
        self.__html += self.__tab()+'<img src="'+path+'" '+opts+'/>\n'

    """
    ============================================================================
    = Link Method                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Specialized write method for writing an a href tag to html               =    
    ============================================================================
    """    
    def __link(
        self,       # (Ref) A reference to this class, required by all members
        path,       # (String) URL to target with the link
        text,       # (String) text or HTML to display as the link
        options={}  # (Dict) any options ot add to the tag
    ):
        opts = self.__format_options(options)
        tag +=  self.__tab()+'<a href="'+path+'" '+opts+'>'+text+'</a>\n'
        self.__html += tag

    """
    ============================================================================
    = Open CSS Method                                                          =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Opens a new css block appending the appropriate prefix and then indents  =
    = the block and gets it ready to accept data.                              =
    ============================================================================
    """       
    def __open_css(
        self,       # (Ref) A reference to this class, required by all members
        name,       # (String) The name of the css item to add
        item_type   # (CSSItem) The type of item to add CLASS, ID, or TAG
    ):
        self.__html += self.__tab()+item_type.value+name+' {\n'
        self.__indent += 1

    """
    ============================================================================
    = Header Tag Method                                                        =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Formats a line of text as a header                                       =
    = ------------------------------------------------------------------------ =
    = return:                                                                  =
    = String containing passed in text wrapped in html. Returns instead of     =
    = adding to self.__html directly so it can be passed into function         =
    = parameters.                                                              =
    ============================================================================
    """
    def __htag(
        self,           # (Ref) A reference to this class, required by all members
        text,           # (String) The text to write out
        tag = 'h3'      # (String) the specific tag to use for the section
    ):
        text = re.sub(r'[\ ]+',' ', text)
        return '{tab}<{h}>\n{tab}    {text}\n{tab}</{h}>'.format(
            tab=self.__tab(), h=tag, text=text
        )


    """
    ============================================================================
    = Paragraph Method                                                         =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Writes a block of text and inserts a break tag at the end                =
    = ------------------------------------------------------------------------ =
    = return:                                                                  =
    = String containing passed in text wrapped in html. Returns instead of     =
    = adding to self.__html directly so it can be passed into function         =
    = parameters.                                                              =
    ============================================================================
    """    
    def __paragraph(
        self,           # (Ref) Reference to this class, required by all members
        text,           # (String) The text to write out
        indent = True,  # (Boolean) Whether to indent or not
        add_br = True   # (Boolean) Whether to add a break at the end of the
                        # paragraph or not
    ):
        text = re.sub(r'[\ ]+',' ', text)
        p_tag = self.__tab()+'<p>\n'+self.__tab()+'    '
        if indent:
            p_tag   +='&nbsp;'*8
        p_tag       += text
        if add_br:
            p_tag   += '<br/>'
        p_tag       += '\n'+self.__tab()+'</p>\n'
        return p_tag

    """
    ============================================================================
    = Close CSS Method                                                         =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Closes a css tag and updates the indentation                             =
    ============================================================================
    """  
    def __close_css(
        self    # (Ref) A reference to this class, required by all members
    ):
        self.__indent -= 1
        self.__html += self.__tab()+'}\n'

    """
    ============================================================================
    = Format Options Method                                                    =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Takes in a dict of options for a tag and strings them together into the  =
    = proper format.                                                           =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (String) A string consisting of all the options for a tag                =   
    ============================================================================
    """     
    def __format_options(
        self,   # (Ref) A reference to this class, required by all members
        options # (Dict) Options to concatenate into a string
    ):
        # Lambda function which adds quotes to option if it's a string and
        # converts the option to a string otherwise.
        f = lambda x: '"'+x+'"' if isinstance(x, str) else str(x)
        return ' '.join([k+"="+f(options[k]) for k in options])

    def __format_value(
        self,   # (Ref) A reference to this class, required by all members
        val     # (Number) The value to format
    ):
        if val > 0:
            return f'+{val}'
        return f'{val}'
    
    def __page_break(self, ret=False):
        if ret:
            return '<p style="page-break-before: always;"></p>'
        else:
            self.__write('<p style="page-break-before: always;"></p>')
