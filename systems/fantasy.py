"""
Class used to manage content for the fantasy branch of the LINAS PnP system
"""
from   __future__ import print_function, division
from   sections.introduction_section       import IntroductionSection
from   sections.stat_section               import StatSection
from   sections.skill_section              import SkillSection
from   sections.combat_section             import CombatSystem
from   sections.free_time_section          import FreeTimeSection
from   sections.player_setup_section       import NewPlayerSetupSection
from   sections.lang_and_race_section      import LangRaceSection
from   sections.ability_section            import AbilitySection
from   sections.technique_section          import TechniqueSection
from   sections.effect_section             import EffectSection
from   sections.class_section              import ClassSection
from   sections.item_section               import ItemSection
from   obj_classes.content_manager         import ContentManager
from   obj_classes.data_manager            import DataManager
from   obj_classes.linas_stat              import LINASStat
from   obj_classes.linas_skill             import LINASSkill
from   obj_classes.linas_lang              import LINASLanguage
from   obj_classes.linas_abil              import LINASAbility
from   obj_classes.linas_effect            import LINASEffect
from   obj_classes.linas_race              import LINASRace
from   obj_classes.linas_item              import LINASItem
from   obj_classes.linas_technique         import LinasTechnique
from   obj_classes.linas_class             import LINASClass, ItemRecord
from   obj_classes.data_collection         import DataCollection

class Fantasy (ContentManager):
    def __init__(
        self
    ) -> None:
        # Set up title and contents for class
        super().__init__(
            title="LINAS - Fantasy Edition",
            author="Joseph Bourque",
            revision=1.0,
            contents=[
                "Introduction",
                "Stats",
                "Skills",
                "Combat",
                "Free Time",
                "New Player Setup",
                "Languages & Races",
                "Classes",
                "Techniques",
                "Abilities",
                "Effects & Status Conditions",
                "Items",
                "Entities",
                "Tools",
                "Campaigns"    
            ]
        )

        # Get contents from super class
        self.__contents = self.getContents()

        # Get HTML from super class
        self.__html = self.toHTMLList()

        # ======================================================================
        # = Set up templates used by data manager
        # ======================================================================
        # NOTE: Templates are used to quickly define parameters for similar
        #       items without having to define them by hand. When the item(s)
        #       are added to the data manager they are expanded out
        #       automatically
        self.__templates = {
            'environments':[
                {"name":"Forest", "adv":"forest", "dis":"prairie"},
                {"name":"Mountain", "adv":"mountain", "dis":"swamp"},
                {"name":"Swamp", "adv":"swamp", "dis":"snow"},
                {"name":"Field", "adv":"prairie", "dis":"mountain"},
                {"name":"Snow", "adv":"snowy", "dis":"desert"},
                {"name":"Sand", "adv":"desert", "dis":"forest"}
            ]
        }
        # ======================================================================
        # = Create Data Manager And Define Data
        # ======================================================================
        self.__dataManager = DataManager({
            "abilities":[
                DataCollection(
                    name="Active",
                     description="""
                         Active abilities as the name suggests are abilities 
                         which must be manually  activated by the entity 
                         they're attached to. They can be thought of kind of  
                         like a entity's ace in the hole, so to speak. These 
                         abilities are usually  extremely limited, and offer a 
                         chance to do significantly more damage or  greater 
                         opportunities to succeed at using skills or some other 
                         aspect of the  game. A entity can have up to 2 active 
                         abilities and a entity always has the  option to give 
                         up their current active ability (if no restrictions 
                         apply  preventing them from doing so.).  
                     """,
                     children=[
                         LINASAbility(
                             name="Blood Magic",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. An ancient form of magic where 
                                 the user expends their own lifeforce to use 
                                 techniques in lieu of TP. All other 
                                 requirements of the technique such as stat 
                                 requirements or required items are still 
                                 required.  
                             """
                         ),
                         LINASAbility(
                             name="Perfect Seal",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. An advanced magic technique which 
                                 binds the user's body  and mind. Target entity 
                                 is now sealed (cannot use techniques), and bound.  
                             """
                         ),
                         LINASAbility(
                             name="Snow Veil",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user cloaks themselves in a 
                                 mixture of snow and ice. Until the beginning 
                                 of the user's next turn, the user is cloaked 
                                 in a veil of  snow and ice. All attack made 
                                 against the user are rolled at -2, any entity  
                                 within 2 squares of the user takes 2 ice 
                                 damage at the beginning of their turn.  
                             """
                         ),
                         LINASAbility(
                             name="Prayer",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user prays for  divine 
                                 intervention and is allowed to re-roll a 
                                 single roll on any roll once.  The user then 
                                 takes the highest roll of the two.  
                             """
                         ),
                         LINASAbility(
                             name="Calculated Shot",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user takes careful  aim and 
                                 fires a long-shot using their bow or rifle. 
                                 Double the range of the  next shot made from a 
                                 bow or rifle (includes trebuchets, cannons, 
                                 etc).  
                             """
                         ),
                         LINASAbility(
                             name="Resonance",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user takes  advantage of the 
                                 environment to carefully distribute the sound 
                                 of their song.  The user can choose exactly 
                                 which entities the next song they play 
                                 affects.  
                             """
                         ),
                         LINASAbility(
                             name="Cleaver",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. Can only be used while  wielding 
                                 a sword or axe; the user raises their weapon 
                                 above their head and  brings it down with 
                                 devastating force. The next attack made with a 
                                 sword or axe  deals 2x damage.  
                             """
                         ),
                         LINASAbility(
                             name="Double-Cast",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user uses both  hands to 
                                 weave magical ruins allowing them to use two 
                                 techniques simultaneously.  The user may use an 
                                 additional technique this turn. Any other 
                                 requirements of the technique such as TP cost, 
                                 required items, stat requirements, etc. still 
                                 count. The user may choose a new target for 
                                 the second technique.  
                             """
                         ),
                         LINASAbility(
                             name="Rage",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user stores up all  their 
                                 anger and aggression and releases it in a 
                                 single blow. The user deals  damage equal to 
                                 the amount of damage they have taken (Max HP - 
                                 HP).  
                             """
                         ),
                         LINASAbility(
                             name="Kamikaze",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user sacrifices  themselves 
                                 in order to deal massive damage to their 
                                 opponent. The user deals 25  fire damage to 
                                 target entity up to 2 squares away. The user's 
                                 HP is now reduced  to 0  
                             """
                         ),
                         LINASAbility(
                             name="Mug",
                             type="a",
                             description="""
                                 This ability can only be used once per full 
                                 rest period. The user mugs their  opponent 
                                 stealing an item while also dealing damage. 
                                 Deal 5 damage to target  entity and if the 
                                 attack was successful. Roll to see if you get 
                                 to steal an  item as well.  
                             """
                         )
                     ]
                ),
                DataCollection(
                    name="passive",
                     description="""
                         Passive abilities are abilities which are always on. 
                         The name passive means the  user doesn't have to 
                         activate them and as such; passive abilities can be  
                         thought of more in terms of advantages or experience 
                         which sets the entity  apart from others. This might 
                         be things like quicker reflexes, higher  tolerances to 
                         pain, the ability to think straight in danger, etc. An 
                         entity can  have up to 3 passive abilities at a time 
                         and like active abilities an entity  always has the 
                         choice to give up a passive ability in order to learn 
                         a new one  (if no restrictions apply preventing them 
                         from doing so.)  
                     """,
                     children=[
                         LINASAbility(
                            name="{name} Walker",
                            type="p",
                            description="""
                                +2 speed when battling or traveling in a {adv}
                                region. -2 speed when battling or traveling
                                in a {dis} region. If speed drops below 0,
                                subtract from dice roll vs. adding
                            """,
                            template=self.__templates['environments']
                         ),
                         LINASAbility(
                             name="Fast Study",
                             type="p",
                             description="""
                                 The user is extremely gifted and flexible when 
                                 learning new skills. When  attempting to learn 
                                 or improve skills; the user may roll 1d6 and 
                                 attempt to  learn the skill instantly. This 
                                 may only be attempted once per skill, if the  
                                 roll fails the user must learn the skill the 
                                 normal way.  
                             """
                         ),
                         LINASAbility(
                             name="Heightened Reflexes",
                             type="p",
                             description="""
                                 The user has mastered the art of jump first, 
                                 look later. In battle, all attacks  made 
                                 against the user are rolled at -1. Outside 
                                 battle, when rolling perception  to avoid an 
                                 attack or trap; the user may re-roll a failed 
                                 roll once and take  the higher of the two 
                                 rolls.  
                             """
                         ),
                         LINASAbility(
                            name="Silver Tongue",
                            type="p",
                            description="""
                                The user has a brilliant personality! Any 
                                rolls involving the speech skill made  by the 
                                user are rolled at +1. Any speech rolls made 
                                against the user are made  at -1.  
                            """
                         ),
                         LINASAbility(
                             name="Iron Body",
                             type="p",
                             description="""
                                 Sitting under waterfalls, powering through 
                                 freezing blizzards, and scorching  heat have 
                                 caused the user's once soft body to become 
                                 hard as steel. User gets  +2 added to armor 
                                 value  
                             """
                         ),
                         LINASAbility(
                             name="Calm Mind",
                             type="p",
                             description="""
                                 Meditation and focus training have made it to 
                                 where the user can control their  spirit more 
                                 efficiently. TP cost for all techniques is reduced 
                                 by 2.  
                             """
                         ),
                         LINASAbility(
                             name="Cardio",
                             type="p",
                             description="""
                                 Hours of running, climbing, and swimming have 
                                 made the user's body even more  efficient 
                                 allowing them to run longer before tiring out. 
                                 Movement increased by  2  
                             """
                         ),
                         LINASAbility(
                             name="Haggle",
                             type="p",
                             description="""
                                 The user never fails to find the best deal, 
                                 even if they aren't set out for  display. All 
                                 shop prices reduced (DM determines how much) 
                                 and there may be some  items available that 
                                 wouldn't normally be (again DM determines what 
                                 items if  any)  
                             """
                         ),
                         LINASAbility(
                             name="Master Craftsman",
                             type="p",
                             description="""
                                 The user has spent a long time honing and 
                                 training their skills. The user must  specify 
                                 a crafting skill to apply this to. Finished 
                                 products related to this  skill get +2 added 
                                 to their value.  
                             """
                         ),
                         LINASAbility(
                             name="Spectral",
                             type="p",
                             description="""
                                 The entity is a spirit not of this world. The 
                                 entity cannot be targeted by physical attacks. 
                                 The entity takes 2x damage from magical 
                                 attacks. The entity cannot equip standard 
                                 equipment 
                             """
                         )
                     ]
                )
            ],
            "items":[
                DataCollection(
                    name="General Use",
                    description="""
                        The items in this category are considered useful for all 
                        races and classes. However, some classes will rely
                        more heavily on the items in this category than others.
                    """,
                    children=[
                        LINASItem(
                            name="Red Potion",
                            description="""
                                Target entity recovers 5HP
                            """,
                            cost=30,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Greater Red Potion",
                            description="""
                                Target entity recovers 10HP
                            """,
                            cost=60,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Blue Potion",
                            description="""
                                Target entity recovers 5TP
                            """,
                            cost=40,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Greater Blue Potion",
                            description="""
                                Target entity recovers 10TP
                            """,
                            cost=70,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Bubbling Potion",
                            description="""
                                Deals 3 fire damage to target entity
                            """,
                            cost=50,
                            uses=1,
                            range=2
                        ),
                        LINASItem(
                            name="Green Potion",
                            description="""
                                Removes poisoned status from target entity
                            """,
                            cost=30,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Panacea",
                            description="""
                                Removes all status conditions except for death
                                from target entity.
                            """,
                            cost=75,
                            uses=1
                        ),
                        LINASItem(
                            name="Angel Feather",
                            description="""
                                Removes death and restores 5HP to target entity
                            """,
                            cost=120,
                            range=1,
                            uses=1
                        ),
                        LINASItem(
                            name="Grenade",
                            description="""
                                Deals 5 fire damage to target square and deals
                                1 fire damage to all squares adjacent to that
                                square
                            """,
                            cost=75,
                            uses=1,
                            range=3
                        ),
                        LINASItem(
                            name="Smoke Ball",
                            description="""
                                -1 to all attack rolls made against target
                                entity until that entity's next turn.
                            """,
                            cost=30,
                            uses=1,
                            range=3
                        ),
                        LINASItem(
                            name="Torch",
                            description="""
                                Used to illuminate dark areas. Must be lit
                                to use
                            """,
                            cost=5,
                            uses=3
                        ),
                        LINASItem(
                            name="Flint",
                            description="""
                                Gives +1 to roll when lighting a fire or torch
                            """,
                            cost=15,
                            uses=3
                        ),
                        LINASItem(
                            name="Arrow",
                            description="""
                                Ammunition for bows and longbows
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                                "Can be retrieved after firing"
                            ]
                        ),
                        LINASItem(
                            name="Bolt",
                            description="""
                                Ammunition for crossbows
                            """,
                            cost=7,
                            uses=1,
                            notes=[
                                "Can be retrieved after firing"
                            ]
                        ),
                        LINASItem(
                            name="Iron Pellet",
                            description="""
                                Ammunition for pistols and rifles
                            """,
                            cost=7,
                            uses=1
                        ),
                    ]
                ),
                DataCollection(
                    name="Accessories",
                    description="""
                    Accessories are special items which grant the user a special
                    effect or bonus as long as they are worn. Most of the time
                    accessories refer to either jewelry or clothing items and
                    most of the time the effects are passive not active meaning
                    the player doesn't have to manually use them. While there are
                    general use accessories, most are geared towards a specific
                    class or skill.

                    Accessories may be able to be modified in order to improve
                    their effects. However the details of the modification such
                    as how many times the item can be improved or which skills
                    are required to improve the item are largely left up to
                    the DM and the players to discuss
                    """,
                    children=[
                        LINASItem(
                            name="Snow Shoes",
                            description="""
                                Entity gets +2 to all movement rolls made in
                                snowy environments
                            """,
                            cost=25
                        ),
                        LINASItem(
                            name="Red Ring",
                            description="""
                                +2 STR, -2 END while worn
                            """,
                            cost=50,
                            notes=[
                                "Does not count toward stat caps",
                                "END cannot go below 0"
                            ]
                        ),
                        LINASItem(
                            name="Blue Ring",
                            description="""
                                +2 END, -2 STR while worn
                            """,
                            cost=50,
                            notes=[
                                "Does not count toward stat caps",
                                "STR cannot go below 0"
                            ]
                        ),
                        LINASItem(
                            name="Skull Necklace",
                            description="""
                                -1TP Cost to all dark magic techniques
                            """,
                            cost=100,
                            notes=[
                                "TP cost for techniques cannot drop below 0"
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Weapons",
                    description="""
                        As the name suggests, these are the items which are
                        primarily meant for combat and include both melee and
                        ranged weapons. Pay close attention to the notes each
                        of these items list out however, as picking the wrong
                        weapon could put your character at a serious
                        disadvantage.<br/><br/>&emsp;&emsp;&emsp;

                        Additionally, heavier weapons and armor give a penalty
                        to speed. Which requires an equal amount of the
                        strength stat to negate.<br/><br/>&emsp;&emsp;&emsp;

                        Weapons may be able to be modified in order to improve
                        damage, or to reduce their speed penalty. However the
                        details of the modification such as how many times the
                        item can be improved or which skills are required to
                        improve the item are largely left up to the DM and the
                        players to discuss
                    """,
                    children=[
                        LINASItem(
                            name="Knife",
                            description="""
                                A small bladed weapon which can be wielded
                                directly or thrown
                            """,
                            cost=15,
                            p_damage=1,
                            range=1,
                            stat="dex",
                            linkedSkill="Fencing",
                            notes=[
                                """
                                If dual wielding add +1 to damage""",
                                """
                                Cannot use items or use techniques in battle while
                                dual wielding.
                                """,
                                "Can be thrown, increases range to 3, once thrown item may be retrieved"
                            ]
                        ),
                        LINASItem(
                            name="Dagger",
                            cost=25,
                            description="""
                                A short bladed weapon which favors speed over
                                power
                            """,
                            p_damage=2,
                            range=1,
                            stat="dex",
                            linkedSkill="Fencing",
                            notes=[
                                """
                                If dual wielding add +1 to damage and +1 to
                                speed penalty
                                """,
                                """\
                                Cannot use items or use techniques in battle while
                                dual wielding.
                                """                            
                            ]
                        ),
                        LINASItem(
                            name="Sword",
                            description="""
                                Standard bladed weapon used for armed combat
                            """,
                            cost=40,
                            p_damage=3,
                            range=1,
                            stat="str",
                            linkedSkill="Swordsmanship",
                            speedPenalty=1,
                            notes=[
                                """
                                If dual wielding add +1 to damage and +1 to
                                speed penalty
                                """,
                                """
                                Cannot use items or use techniques in battle while
                                dual wielding.
                                """
                            ]
                        ),
                        LINASItem(
                            name="Two-Handed Sword",
                            description="""
                            A large bladed weapon which uses weight vs.
                            sharpness to tear through armor and flesh
                            """,
                            cost=65,
                            p_damage=5,
                            range=1,
                            stat="str",
                            linkedSkill="Swordsmanship",
                            speedPenalty=2,
                            notes=[
                                "Cannot be dual wielded",
                                """
                                Cannot use items or use techniques in battle while
                                wielding this weapon.
                                """
                            ]
                        ),
                        LINASItem(
                            name="Axe",
                            description="""
                            A large bladed weapon which can be used either for
                            battle or for chopping wood
                            """,
                            cost=50,
                            p_damage=4,
                            range=1,
                            stat="str",
                            linkedSkill="Swordsmanship",
                            speedPenalty=2,
                            notes=[
                                "Cannot be dual wielded"
                            ]
                        ),
                        LINASItem(
                            name="Hatchet",
                            description="""
                            A small hand-held axe which can be wielded directly
                            or thrown
                            """,
                            cost=35,
                            p_damage=2,
                            range=3,
                            stat="str",
                            linkedSkill="Swordsmanship",
                            notes=[
                                """
                                If dual wielding add +1 to damage and +1 to
                                speed penalty
                                """,
                                """
                                Cannot use items or use techniques in battle while
                                dual wielding.
                                """,
                                """
                                Range is only 3 if being thrown, otherwise 
                                it's 1.
                                """,
                                "Once thrown, item may be retrieved"                                
                            ]

                        ),
                        LINASItem(
                            name="Mace",
                            description="""
                            A heavy metal weapon covered in spikes.
                            """,
                            cost=60,
                            p_damage=3,
                            speedPenalty=2,
                            linkedSkill="Bashing",
                            stat="str",
                            range=1,
                            notes=[
                                """
                                If dual wielding add +1 to damage and +1 to
                                speed penalty
                                """,
                                """
                                Cannot use items or use techniques in battle while
                                dual wielding.
                                """
                            ]
                        ),
                        LINASItem(
                            name="Hammer",
                            description="""
                            An extremely heavy metal hammer. Deals a lot of
                            damage but is extremely slow and unwieldy to use
                            """,
                            cost=75,
                            p_damage=5,
                            range=1,
                            stat="str",
                            linkedSkill="Bashing",
                            speedPenalty=3,
                            notes=[
                                "Cannot be dual wielded",
                                """
                                Cannot use items or use techniques in battle while
                                wielding this weapon.
                                """                                
                            ]
                        ),
                        LINASItem(
                            name="Staff",
                            description="""
                            A large piece of wood often carried by monks and 
                            hikers
                            """,
                            cost=35,
                            p_damage=2,
                            range=2,
                            stat="str",
                            linkedSkill="Fencing",
                            speedPenalty=1,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """
                            ]
                        ),
                        LINASItem(
                            name="Spear",
                            description="""
                            A long nimble weapon used to combat foes both on the 
                            ground and on horseback
                            """,
                            cost=45,
                            p_damage=2,
                            range=2,
                            stat="str",
                            linkedSkill="Fencing",
                            speedPenalty=1,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """
                            ]
                        ),
                        LINASItem(
                            name="Lance",
                            description="""
                            A long bladed spear with a large hand-guard 
                            traditionally used from horseback.
                            """,
                            cost=70,
                            p_damage=5,
                            range=2,
                            stat="str",
                            linkedSkill="Fencing",
                            speedPenalty=3,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """
                            ]
                        ),
                        LINASItem(
                            name="Bow",
                            description="""
                            Ranged weapon crafted from a flexible piece of wood 
                            and elastic draw string
                            """,
                            cost=30,
                            p_damage=2,
                            range=4,
                            stat="dex",
                            linkedSkill="Archery",
                            notes=[
                                """
                                Cannot be dual wielded
                                """
                            ]
                        ),
                        LINASItem(
                            name="Long Bow",
                            description="""
                            An enormous bow used for taking down large prey
                            """,
                            cost=50,
                            p_damage=3,
                            range=4,
                            stat="dex",
                            linkedSkill="Archery",
                            speedPenalty=1,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """
                            ]
                        ),
                        LINASItem(
                            name="Rapier",
                            description="""
                            Small slender sword used which relies on speed and 
                            sharpness over weight
                            """,
                            cost=20,
                            p_damage=2,
                            range=1,
                            stat="dex",
                            linkedSkill="Archery",
                            speedPenalty=0,
                            notes=[
                                """
                                Cannot be dual wielded
                                """
                            ]
                        ),
                        LINASItem(
                            name="Crossbow",
                            description="""
                            Powerful mechanical bow which takes bears a heavy 
                            speed penalty but flies farther than a traditional 
                            bow
                            """,
                            cost=60,
                            p_damage=4,
                            range=5,
                            stat="dex",
                            linkedSkill="Archery",
                            speedPenalty=2,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """,
                                """
                                1 turn to load 1 turn to fire
                                """,
                                """
                                holds single shot
                                """
                            ]
                        ),
                        LINASItem(
                            name="Pistol",
                            description="""
                            A small high power pistol which fires iron pellets
                            """,
                            cost=50,
                            p_damage=4,
                            range=4,
                            stat="dex",
                            linkedSkill="Marksmanship",
                            notes=[
                                """
                                Add +1 to damage if dual wielding
                                """,
                                """
                                Can select multiple targets if dual wielding
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """,
                                """
                                1 turn to load 1 turn to fire
                                """,
                                """
                                holds a single shot
                                """
                            ]
                        ),
                        LINASItem(
                            name="Rifle",
                            description="""
                            A high power lightweight long range weapon which 
                            fires iron pellets
                            """,
                            cost=70,
                            p_damage=5,
                            range=5,
                            stat="dex",
                            linkedSkill="Marksmanship",
                            speedPenalty=1,
                            notes=[
                                """
                                Cannot be dual wielded
                                """,
                                """
                                Cannot use techniques or use items while wielding
                                """,
                                """
                                1 turn to load 1 turn to fire
                                """,
                                """
                                holds single shot
                                """
                            ]
                        ),
                        LINASItem(
                            name="Trebuchet",
                            description="""
                            A large ranged weapon used for siege warfare. This 
                            weapon primarily found in various location on the 
                            map during combat situations
                            """,
                            cost=0,
                            p_damage=7,
                            range=5,
                            stat="int",
                            linkedSkill="Marksmanship",
                            notes=[
                                """
                                This weapon cannot be moved from it's location 
                                on the map
                                """,
                                """
                                This weapon can only be fired while there is 
                                ammo in it's ammo box
                                """,
                                """
                                Must take 1 turn to load and 1 turn to fire
                                """,
                                """
                                This weapon must be mounted/unmounted
                                """,
                                """
                                Cannot be chosen as a player weapon or purchased
                                """
                            ]
                        ),
                        LINASItem(
                            name="Catapult",
                            description="""
                            A large ranged weapon used for siege warfare. This 
                            weapon primarily found in various locations on the 
                            map during combat situations
                            """,
                            cost=0,
                            p_damage=5,
                            range=6,
                            stat="int",
                            linkedSkill="Marksmanship",
                            notes=[
                                """
                                This weapon cannot be moved from it's location 
                                on the map
                                """,
                                """
                                This weapon can only be fired while there is 
                                ammo in it's ammo box
                                """,
                                """
                                Must take 1 turn to load and 1 turn to fire
                                """,
                                """
                                This weapon must be mounted/unmounted
                                """,
                                """
                                Cannot be chosen as a player weapon or purchased
                                """
                            ]
                        ),
                        LINASItem(
                            name="Cannon",
                            description="""
                            A large ranged weapon used for siege warfare. This 
                            weapon primarily found in various locations on the 
                            map during combat situations
                            """,
                            cost=0,
                            p_damage=7,
                            range=7,
                            stat="int",
                            linkedSkill="Marksmanship",
                            notes=[
                                """
                                This weapon cannot be moved from it's location 
                                on the map
                                """,
                                """
                                This weapon can only be fired while there is 
                                ammo in it's ammo box
                                """,
                                """
                                Must take 1 turn to load and 1 turn to fire
                                """,
                                """
                                This weapon must be mounted/unmounted
                                """,
                                """
                                Cannot be chosen as a player weapon or purchased
                                """
                            ]
                        ),
                        LINASItem(
                            name="Drill Harpoon",
                            description="""
                            A large spiked spear used for siege warfare. This 
                            weapon is typically fired out of a cannon and is 
                            primarily found in various locations on the map 
                            during combat situations
                            """,
                            cost=0,
                            p_damage=7,
                            range=5,
                            stat="int",
                            linkedSkill="Archery",
                            notes=[
                                """
                                This weapon cannot be moved from it's location 
                                on the map
                                """,
                                """
                                This weapon can only be fired while there is 
                                ammo in it's ammo box
                                """,
                                """
                                Must take 1 turn to load and 1 turn to fire
                                """,
                                """
                                This weapon must be mounted/unmounted
                                """,
                                """
                                Cannot be chosen as a player weapon or purchased
                                """
                            ]
                        ),
                        LINASItem(
                            name="Padded Gloves",
                            description="""
                            A set of gloves designed to protect the hands and 
                            knuckles while fighting
                            """,
                            cost=15,
                            p_damage=1,
                            range=1,
                            stat="dex",
                            linkedSkill="Martial Arts",
                            notes=[
                                """
                                This weapon cannot be dual wielded
                                """
                            ]
                        ),
                        LINASItem(
                            name="Brass Knuckles",
                            description="""
                            A set of joined metal rings worn during fights. Not 
                            acceptable to use during tournaments
                            """,
                            cost=25,
                            p_damage=2,
                            range=1,
                            stat="dex",
                            linkedSkill="Martial Arts",
                            notes=[
                                """
                                This weapon cannot be dual wielded
                                """
                            ]
                        ),
                        LINASItem(
                            name="Magic Rod",
                            description="""
                            A golden rod with a bright gem embedded in the top.
                            doesn't deal much damage but amplifies magic
                            abilities
                            """,
                            cost=85,
                            p_damage=1,
                            range=1,
                            stat="str",
                            linkedSkill="Bashing",
                            notes=[
                                """
                                Adds +1 to INT, this does not count towards the
                                stat cap.
                                """
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Armor & Clothing",
                    description="""
                    Armor provides a way for characters to protect themselves
                    from damage. Entities can equip only a single armor set at
                    a single time and can also equip a shield for a bit of extra
                    protection if they choose.

                    Like weapons, heavier shields and armor give a penalty
                    to speed. Which requires an equal amount of the
                    strength stat to negate.<br/><br/>&emsp;&emsp;&emsp;

                    Armor and Shields may be able to be modified in order to 
                    improve protection, or to reduce their speed penalty. 
                    However the details of the modification such as how many 
                    times the item can be improved or which skills are required
                    to improve the item are largely left up to the DM and the
                    players to discuss
                    """,
                    children=[
                        LINASItem(
                            name="Robe",
                            description="""
                            A heavy robe made out of woven linen. Offers very
                            little physical protection but moderate magical
                            protection. It is also fairly lightweight and
                            doesn't restrict movement of the arms or hands in
                            any way.
                            """,
                            cost=10,
                            p_protection=1,
                            m_protection=2,
                            notes=[
                                """
                                Can restrict the protection type to a specific
                                element (e.g. fire) to add +1 to protection and
                                change the protection type to the chosen
                                element
                                """
                            ]
                        ),
                        LINASItem(
                            name="Leather Armor",
                            description="""
                            Armor made from dried animal skins. Provides a 
                            little protection and is extremely lightweight. Can 
                            also be dyed a variety of colors
                            """,
                            cost=15,
                            p_protection=2,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Chainmail Armor",
                            description="""
                            Armor made from interwoven links of metal. Provides 
                            moderate protection while still being fairly 
                            lightweight
                            """,
                            cost=40,
                            p_protection=3,
                            speedPenalty=1,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Plate Armor",
                            description="""
                            Armor made from heavy plates of metal. Provides a 
                            decent amount of protection but is also fairly 
                            heavy.
                            """,
                            cost=65,
                            p_protection=4,
                            speedPenalty=3,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Dragon Scale Armor",
                            description="""
                            Lightweight armor made from the scales of a dragon. 
                            Provides fairly decent magical protection.
                            """,
                            cost=480,
                            p_protection=2,
                            m_protection=3,
                            speedPenalty=1,
                            notes=[
                                """
                                Magical protection is usually aligned to a 
                                specific element corresponding to the element of 
                                the dragon the scales came from (e.g. fire 
                                dragon = fire protection)
                                """
                            ]
                        ),
                        LINASItem(
                            name="Dragon Bone Armor",
                            description="""
                            Armor made from the bones of a dragon. Extremely 
                            durable, however also extremely heavy. Protects 
                            against both magical and physical damage
                            """,
                            cost=1000,
                            p_protection=4,
                            m_protection=5,
                            speedPenalty=3,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Mithrill Armor",
                            description="""
                            Lightweight armor made from woven mithrill wire. 
                            Provides a great amount of magic protection; and 
                            leaves the hands free for using techniques.
                            """,
                            cost=130,
                            p_protection=2,
                            m_protection=3,
                            speedPenalty=1,
                            notes=[
                            ]
                        ),
                    ]
                ),
                DataCollection(
                    name="Specialized",
                    description="""
                    The items in this category are items which are geared
                    towards specific classes/jobs.<br/><br/>&emsp;&emsp;&emsp;

                    Most of these items given for free when a specific class is
                    chosen, however there may be times when a player wants to
                    take additional items. Especially when creating custom
                    characters or trying to build a hybrid class.
                    """,
                    children=[
                        LINASItem(
                            name="Lockpick",
                            description="""
                            Required to use the lockpicking skill. Used to 
                            attempt to open a  lock without the corresponding 
                            key.
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Chemistry Set",
                            description="""
                            Required to use alchemy. A set of instruments, 
                            labeled vials, and blank notebooks, perfect for 
                            setting up alchemical experiments
                            """,
                            cost=20,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Carpenter's Tools",
                            description="""
                            Required to use carpentry. Contains tools for 
                            cutting, carving, and shaping wood.
                            """,
                            cost=10,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Chef's tools",
                            description="""
                            Contains pots, pans, mixing bowls, and a whole array 
                            of tools for creating fine cuisine
                            """,
                            cost=30,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Scribe's Tools",
                            description="""
                            Required for enchanting, cartography, and general 
                            writing. A set of pens, scrolls, and various inks 
                            which can write on a variety of surfaces.
                            """,
                            cost=45,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Pickaxe",
                            description="""
                            Required for mining. A sharp piece of metal 
                            connected to a wooden shaft. Perfect for breaking 
                            apart stone to access the contents inside
                            """,
                            cost=35,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Smith's Tools",
                            description="""
                            Required for blacksmithing. Contains a hammer, 
                            tongs, various mixing agents and a host of  other 
                            tools for forging and shaping metal.
                            """,
                            cost=15,
                            uses=0,
                            notes=[
                            ]
                        ),
                        LINASItem(
                            name="Toolbox",
                            description="""
                            Required to use tinkering . Contains  all the tools
                            needed to create and maintain gadgets  and machines.
                            """,
                            cost=30,
                            uses=0,
                            notes=[
                            ]
                        )
                    ]
                )
            ],
            "languages":[
                LINASLanguage(
                    name="Alyssian",
                     description="""
                         An ancient and dead language once wide spoken but now 
                         a relic of ages gone by.  This language is however 
                         still spoken by Vampires and originated in the Mu  
                         kingdom.  
                     """
                ),
                LINASLanguage(
                    name="Common",
                     description="""
                         This language is spoken by all races and is usually 
                         the preferred language for  speaking with townsfolk or 
                         merchants. However, some communities who are  
                         particularly wary of outsiders may choose to use some 
                         other language in an  attempt to shut out prying ears. 
                     """
                ),
                LINASLanguage(
                    name="Draconic",
                     description="""
                         The language spoken by dragons and those who grew up 
                         near dragon communities.  This language is a bit of an 
                         oddity and because of this, usually only those who  
                         have direct dealings with dragon society know this 
                         language  
                     """
                ),
                LINASLanguage(
                    name="Dwarven",
                     description="""
                         To an untrained ear, this language sounds very similar 
                         to the Dark Elvish  dialect. However, it is distinctly 
                         different and trying to use Elven dialects  to 
                         understand this only results in gibberish. Unlike the 
                         elves there aren't  very many dialects of Dwarven; 
                         only Ancient and Modern. Players wishing to  converse 
                         with living Dwarves should choose modern while Ancient 
                         is primarily  used for reading ancient ruins and text. 
                     """
                ),
                LINASLanguage(
                    name="Elvish",
                     description="""
                         As the name suggests, this is the language of the 
                         elves. When taking this  skill; players must choose a 
                         dialect: Forest, Dark, Ice, High, etc. Each dialect  
                         is in it's own a unique language. However, someone 
                         knowing one dialect can  attempt to understand another 
                         at a -1 roll penalty.  
                     """
                )
            ],
            "stats":[
                LINASStat(
                    name = "Health Points",
                    abbr = "HP",
                    description = """
                    This represents the amount of damage an entity can take
                    before going unconscious (or dying in the case of some 
                    monsters or NPCs)
                    """
                ),
                LINASStat(
                    name = "Technical Points",
                    abbr = "TP",
                    description = """
                    This represents the amount of energy an entity is
                    able to utilize towards battle skills and techniques.
                    """
                ),
                LINASStat(
                    name = "Strength",
                    abbr = "STR",
                    description = """
                    This determines how physically strong the entity is. This is
                    added to the attack roll for most physical non-ranged weapons
                    and is also used to determine whether the entity can equip
                    some of the heavier weapons and armors.
                    """
                ),
                LINASStat(
                    name = "Dexterity",
                    abbr = "DEX",
                    description = """
                    This represents a measure of an entity's hand-eye
                    coordination. This is added to the attack roll for most
                    physical ranged weapons (mainly bows and crossbows).
                    This is also added to the attack roll for most martial arts
                    abilities.
                    """
                ),
                LINASStat(
                    name = "Intelligence",
                    abbr = "INT",
                    description = """
                    Represents how easily an entity can understand techniques and
                    other forms of magic. This is added to the attack roll for
                    most non-physical attacks.
                    """
                ),
                LINASStat(
                    name = "Endurance",
                    abbr = "END",
                    description = """
                    A measure of how resilient an entity's body is against
                    physical damage. This is added to the defense roll for all
                    physical weapons (both ranged and melee).
                    """
                ),
                LINASStat(
                    name = "Spirit", 
                    abbr = "SPR",
                    description = """
                    A measure of how resilient an entity's mind is against
                     magical damage (including spectral damage). This is added
                     to the defense roll for all non-physical attacks.
                    """
                ),
                LINASStat(
                    name = "Speed",
                    abbr = "SPD",
                    description = """
                    How fast the user can move. This is both used to calculate
                    initiative and is also added to the number of squares an
                    entity can move during a single round of combat.
                    """
                )
            ],
            "skills":[
                DataCollection(
                    name = "Combat Skills",
                    description = """
                    As their name suggests; these skills are primarily used for 
                    combat and are generally associated with a certain weapon 
                    type or group 
                    """,
                    children = [
                        LINASSkill(
                            name = "Archery",
                            description = """
                            A ranged weapon skill. This primarily refers to 
                            bows, longbows, and crossbows. For rifles 
                            marksmanship should be used instead. The reason for 
                            splitting this skill into two is that the usage of 
                            a bow is so different from a gun that it wouldn't 
                            make sense to combine the two. 
                            """,
                        ),
                        LINASSkill(
                            name = "Bashing",
                            description = """
                            This is the skill required to fight with clubs, 
                            maces, shields and virtually any other non-bladed 
                            weapon. This also encompasses abilities related to 
                            these weapons; although there are far fewer 
                            abilities associated with this class vs. 
                            swordsmanship. 
                            """,
                        ),
                        LINASSkill(
                            name = "Fencing",
                            description = """
                            Like swordsmanship, this groups several weapons 
                            together in an effort to keep the system simple and 
                            is primarily used for rapiers, knives, and pole 
                            arms such as spears and quarterstaves 
                            """,
                        ),
                        LINASSkill(
                            name = "Marksmanship",
                            description = """
                            This skill is primarily used for rifles and 
                            mechanical ranged weaponry like the tinker class' 
                            dart gun. This is also the skill needed to fire 
                            cannons, catapults and trebuchets. 
                            """,
                        ),
                        LINASSkill(
                            name = "Martial Arts",
                            description = """
                            When fighting unarmed, this is the skill which is 
                            used. By default; all unarmed characters do 2 
                            damage + strength. However, there are also many 
                            abilities which supplement this skill which can 
                            turn an unarmed user into a formidable foe. 
                            """,
                        ),
                        LINASSkill(
                            name = "Swordsmanship",
                            description = """
                            This skill is a bit broad, used both for attacking 
                            with swords and axes as  well as for using abilities
                            related to these weapons.
                            """,
                        ),
                        LINASSkill(
                            name = "Bushido",
                            description= """
                            A specialized form of eastern swordsmanship focusing
                            on speed rather than power. Unlike standards swordsmanship,
                            the abilities for this skill can only be used with as sword.
                            """
                        ),
                        LINASSkill(
                            name = "Assassination",
                            description = """
                            A specialized form of combat using speed, dexterity, and
                            stealth to dispatch opponents. 
                            """
                        )
                    ]
                ),
                DataCollection(
                    name = "General Skills",
                    description = """
                    These are skills which are equally useful to all classes. 
                    While it may be tempting to take multiple skills from this 
                    category, some may be more useful than others. The DM and 
                    player should work together to pick skills which both fit 
                    with their character's background and also which will end 
                    up benefiting the player or the party. 
                    """,
                    children = [
                        LINASSkill(
                            name = "Forecasting",
                            description = """
                            Weather can be an important aspect of a campaign 
                            and being able to forecast the weather can give the 
                            party significant advantages; especially in 
                            locations where it changes often. 
                            """,
                        ),
                        LINASSkill(
                            name="First Aid",
                            description="""
                            This skill is generally used to treat either the
                            user's wounds or those of a nearby entity. This is
                            meant more as an emergency treatment and as such
                            it has the power to restore HP but generally doesn't
                            do anything for status conditions or more serious
                            problems such as broken bones or internal injuries
                            the way healing magic can.
                            """
                        ),
                        LINASSkill(
                            name = "Perception",
                            description = """
                            This skill generally refers to how aware an entity 
                            is to their surroundings. A high perception skill 
                            can help avoid ambushes, traps, and other 
                            environmental hazards before springing them. 
                            """,
                        ),
                        LINASSkill(
                            name = "Sensing",
                            description = """
                            While perception typically corresponds with the 
                            physical aspects of the environment; sensing refers 
                            to the spiritual, magical, or otherwise unseen 
                            aspects of the environment. These two skills are 
                            mutually exclusive, meaning an entity with a high 
                            perception would be unaware of a curse or evil 
                            spirit without seeing the physical signs of their 
                            presence. 
                            """,
                        ),
                        LINASSkill(
                            name = "Speech",
                            description = """
                            Another area where the system has been simplified 
                            is speech. This pretty much includes everything 
                            related to charisma. Intimidation, flattery, 
                            haggling, persuasion, etc. Meaning, everything 
                            related to speech is encompassed by this skill. 
                            """,
                        )
                    ]
                ),
                DataCollection(
                    name = "Specialized Skills",
                    description = """
                    Specialized skills are skills which are geared towards a 
                    specific class or job. With this being said, there are no 
                    rules against picking one of the skills below regardless as 
                    LINAS in general strives to promote creativity and character 
                    development. 
                    """,
                    children = [
                        LINASSkill(
                            name = "Foraging",
                            description = """
                            The ability to gather plants or other natural 
                            resources from a given area. This is primarily used 
                            for alchemists and cooks to gather ingredients for 
                            crafting but can sometimes be used in a pinch if 
                            the user has no way to heal themselves or otherwise 
                            give themselves aid. 
                            """,
                        ),
                        LINASSkill(
                            name = "Lockpicking",
                            description = """
                            Allows an entity to get into places (or chests) 
                            which they normally wouldn't have access to. This 
                            only applies to physical locks, not magic locks and 
                            seals 
                            """,
                        ),
                        LINASSkill(
                            name = "Pickpocket",
                            description = """
                            This is the ability to lift items off of an entity 
                            without them noticing. While it's most often used 
                            to acquire a bit of extra pocket change; it can be 
                            quite useful for getting things like keys, maps, or 
                            other required quest items without having to resort 
                            to battle. 
                            """,
                        ),
                        LINASSkill(
                            name = "Stealth",
                            description = """
                            The ability to move and operate unseen or otherwise 
                            unnoticed. While some classes rely more heavily on 
                            this skill than others; it is a useful skill for 
                            almost any class and can help avoid wasting time 
                            and resources unnecessarily. 
                            """,
                        ),
                        LINASSkill(
                            name = "Taming",
                            description = """
                            This is used to determine how easily wild animal 
                            and beasts trust the user. It should be noted that 
                            in this game; dragons, mu, and a few other races 
                            which share features with beasts are considered 
                            sentient and as such require speech to persuade 
                            them in lieu of this skill. 
                            """,
                        ),
                        LINASSkill(
                            name = "Tracking",
                            description = """
                            The ability to detect an entity's movement either 
                            towards or away from a given location over time. 
                            This is different than perception and is limited to 
                            detecting the direction an entity has moved or the 
                            presence of entities over a given time. 
                            """,
                        ),
                        LINASSkill(
                            name = "Magic",
                            description = """
                            In order to keep LINAS's skill system from becoming 
                            too bloated; every form of magic has been 
                            consolidated into a single skill. That being said, 
                            different schools of magic do exist and allow for a 
                            great range of flexibility despite this. 
                            """,
                        ),
                        LINASSkill(
                            name = "Music",
                            description = """
                            Music as expected is the ability to perform songs 
                            using an instrument. While seemingly innocuous, 
                            music can be used to impart a variety of effects on 
                            an entity both inside and outside of battle and can 
                            also be used as a form of income during freetime 
                            making it a fairly versatile skill. 
                            """,
                        ),
                        LINASSkill(
                            name = "Ninjitsu",
                            description = """
                            This skill is about controlling the flow of battle. 
                            Abilities of this class involve a heavy amount of 
                            item use as well as heavy use of the environment. 
                            This class also combines a few assassination 
                            techniques as well which make it a good work in 
                            with the rogue class. 
                            """,
                        )
                    ]
                ),
                DataCollection(
                    name = "Crafting Skills",
                    description = """
                    As the name suggests, the main goal of these skills is to 
                    create items out of various materials and resources. There 
                    are several advantages to crafting items such as: superior 
                    quality, being able to save gold, and obtaining items not 
                    found in shops. This list is a bit long but includes both 
                    crafting skills as well as the skills needed to gather 
                    resources for these skills. 
                    """,
                    children = [
                        LINASSkill(
                            name = "Alchemy",
                            description = """
                            This can be thought of as "magic chemistry". 
                            ALchemists primarily study the art of extracting 
                            the base essence of various items into potions. 
                            However, alchemists also possess the ability to 
                            make several advanced compounds such as gunpowder 
                            and distilled alcohol as well. 
                            """,
                        ),
                        LINASSkill(
                            name = "Carpentry",
                            description = """
                            This skill combines fletching and carpentry 
                            together into one skill. With that in mind; this is 
                            used to craft wooden weapons as well as arrows. 
                            """,
                        ),
                        LINASSkill(
                            name = "Cooking",
                            description = """
                            This skill is a bit limited and generally is used 
                            to create meals which can be eaten immediately to 
                            heal status conditions or HP/TP outside battle. 
                            Usually cooks have a set menu of things they can 
                            prepare; although this menu is subject to change 
                            depending on whether the cook chooses variety over 
                            improving existing recipes. 
                            """,
                        ),
                        LINASSkill(
                            name = "Enchanting",
                            description = """
                            This is used to give items and equipment magical 
                            abilities. This skill can also  be used to recharge 
                            magic abilities for further use. 
                            """,
                        ),
                        LINASSkill(
                            name = "Logging",
                            description = """
                            Used to obtain logs from trees. Items obtained can 
                            be used for crafting, sold, or for things like 
                            torches or campfires. 
                            """,
                        ),
                        LINASSkill(
                            name = "Mining",
                            description = """
                            Primarily used to dig ore and gems out of the 
                            earth. Items obtained can either be used for 
                            crafting or sold. 
                            """,
                        ),
                        LINASSkill(
                            name = "Sewing",
                            description = """
                            Tailors are able to work with both leather and 
                            cloth to make various forms of equipment. In some 
                            cases, tailors can even use unconventional 
                            materials for cloth such as spider silk or mythrill. 
                            """,
                        ),
                        LINASSkill(
                            name = "Smithing",
                            description = """
                            Used primarily for crafting equipment (weapons and 
                            armor) from different types of metal. Although 
                            depending on the DM and the campaign, it might be 
                            possible to use this skill as a sort of side job 
                            between quests. 
                            """,
                        ),
                        LINASSkill(
                            name = "Tinkering",
                            description = """
                            This is sort of an early form of engineering. 
                            Tinkers use a combination of wood, leather, metal, 
                            and other natural resources in order to create 
                            gadgets and simple machines. They're also extremely 
                            useful at repairing broken tools and equipment.<p 
                            style="page-break-before: always;"></p> 
                            """,
                        )
                    ]
                ),
                DataCollection(
                    name = "Lore and Knowledge",
                    description = """
                    Lore skills are primarily used to give players specialized 
                    information which may help them solve problems more 
                    effectively or use items to a better degree than someone 
                    without that knowledge. Unlike other skills; lore skills 
                    can have a specialization which may permit the entity to 
                    know additional knowledge that an unspecialized entity 
                    wouldn't know. The extent of this difference is largely 
                    dependent on what the DM allows an entity to know however 
                    and no official guidelines are defined. 
                    """,
                    children = [
                        LINASSkill(
                            name = "Arcane Lore",
                            description = """
                            This is lore pertaining to history involving the 
                            magic arts or the occult. Examples of this would 
                            include knowing who specific magic figures are, 
                            knowing about specific magic items, being able to 
                            detect magic properties on an item, as well as 
                            knowing about events related to magic which 
                            happened in a given area. This can be specialized 
                            to a particular branch of magic or unspecialized 
                            encompassing all branches of magic 
                            """,
                        ),
                        LINASSkill(
                            name = "Profession Lore",
                            description = """
                            This is lore pertaining to a specific job or class. 
                            Examples of this would be knowing a specific 
                            military tattoo having been in the military, or 
                            being able to tell whether the vegetables in a 
                            market stand are fresh or not based on their 
                            appearance. This can be specialized only as it 
                            wouldn't really make sense for this to be 
                            unspecialized. 
                            """,
                        ),
                        LINASSkill(
                            name = "Regional Lore",
                            description = """
                            This is lore corresponding to a particular area or 
                            region. Like profession lore, this cannot be 
                            unspecialized. This is usually taken if a character 
                            has strong ties to the area or region from which 
                            they originate. If a character wishes to take a 
                            regional lore they should work with the DM to 
                            discuss the specifics of their knowledge ahead of 
                            time. 
                            """,
                        ),
                        LINASSkill(
                            name = "Undercity Lore",
                            description = """
                            The undercity is not actually a city at all but 
                            rather is a sociological structure within all 
                            cities consisting of thieves, degenerates, and 
                            those who don't let the confines of the law 
                            restrain them. Entities with knowledge of this 
                            society are less likely to get conned or taken 
                            advantage of and will also be able to obtain 
                            information and get items that normal upstanding 
                            citizens wouldn't be able to obtain. This can be 
                            specialized to a specific group within the 
                            undercity or unspecialized to the entire undercity. 
                            """,
                        ),
                        LINASSkill(
                            name = "Language",
                            description = """
                            This is used to declare additional languages which 
                            an entity knows in addition to common; which all 
                            races know by default. It is also important to note 
                            that each individual language must be taken as an 
                            additional lore skill. For a list of languages a 
                            player can learn; please see the race section of 
                            this guide. 
                            """,
                        )
                    ]
                )
            ],
            "techniques":[
                DataCollection(
                    name="Light Magic Techniques",
                    description="""
                    The techniques in this category are generally defensive and 
                    restorative in nature. Even if your character isn't 
                    specializing in healing or magic in general; picking up one 
                    or two of these techniques can be extremely helpful; especially 
                    if you don't feel like spending a huge amount of money on 
                    potions..
                    """,
                    children=[
                        LinasTechnique(
                            name="Barrier",
                            description="""
                            Prevents the next X physical damage that would be 
                            done to the technique's target and then pops. Where X 
                            is equal to this technique's damage. Barrier stays
                            active until destroyed
                            """,
                            damage=1,
                            range=0,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Magic Barrier",
                            description="""
                            Prevents the next X magical damage that would be 
                            done to the technique's target and then pops. Where X 
                            is equal to this technique's damage. Barrier stays active
                            until destroyed
                            """,
                            damage=1,
                            range=0,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Heal Wound",
                            description="""
                            Restores X HP to technique's target where X is equal 
                            to this technique's damage.
                            """,
                            damage=3,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Cure",
                            description="""
                            Removes X status conditions from target where X is 
                            equal to this technique's damage.
                            """,
                            damage=1,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                                """
                                Can remove any status condition except for death
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Bless",
                            description="""
                            Increases the damage of target's next attack by X 
                            where X is equal to this technique's damage
                            """,
                            damage=2,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Resurrect",
                            description="""
                            Returns target back to life with X HP where X is 
                            equal to this technique's damage
                            """,
                            damage=5,
                            range=1,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Arcane Magic Technique",
                    description="""
                    The techniques in this category tend to focus on dealing direct 
                    damage to enemies. However, there are also a few techniques 
                    which don't fit the pattern as well. Generally speaking, 
                    this school of magic tends to focus on elemental magic; and 
                    in order to keep things simple. Many classic specialized 
                    forms of magic such as nature magic end up falling under 
                    this category as well.
                    """,
                    children=[
                        LinasTechnique(
                            name="Magic Missile",
                            description="""
                            Shoots a magical arrow at the target.
                            """,
                            damage=2,
                            range=3,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Fireball",
                            description="""
                            Shoots a magical fireball at target entity. This 
                            technique can be given burn as a status effect.
                            """,
                            damage=2,
                            range=3,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                                """
                                Target is burned if 6 is rolled while using this technique
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Lightning",
                            description="""
                            A forked bolt of lightning cracks through the air. 
                            Deals damage to multiple targets.
                            """,
                            damage=2,
                            range=3,
                            numTargets=3,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                Each target rolls to see if attack hits
                                """,
                                """
                                If target rolls a 1 they are paralyzed in 
                                addition to taking damage
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Blizzard",
                            description="""
                            A ferocious snowstorm envelopes the user and all 
                            nearby entities. Deals damage to all entities within 
                            X squares of the user where X is equal to this 
                            technique's range (both friend and foe)
                            """,
                            damage=3,
                            range=5,
                            numTargets=0,
                            fnf=True,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                Each entity on the battlefield rolls to see if 
                                attack hits. Entities not on the ground aren't 
                                effected by this technique
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Earthquake",
                            description="""
                            A massive earthquake shakes the area. All entities 
                            (both friend and foe) are impacted by the technique
                            """,
                            damage=5,
                            range=-1,
                            numTargets=0,
                            aoe=True,
                            fnf=True,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                Each entity on the battlefield rolls to see if 
                                attack hits. Entities not on the ground aren't 
                                effected by this technique
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Teleport",
                            description="""
                            User teleports up to X squares away from current 
                            position where X is equal to this technique's damage.
                            """,
                            damage=1,
                            range=0,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                This does not count as movement roll for the 
                                turn
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Transform",
                            description="""
                            User transforms into an animal or monster of their 
                            choice. Technique must be reused every turn to keep it
                            active. Reusing a technique can be taken as a bonus action.
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            skill="magic",
                            stat='int',
                            points=1,
                            notes=[
                                """
                                While transformed, stats are equal to those of 
                                the chosen animal/monster
                                """,
                                """
                                If the chosen animal/monster has a higher HP/TP 
                                than the user, the user keeps their current 
                                HP/TP (do not scale HP/TP)
                                """,
                                """
                                Paying the continuation cost for this technique does 
                                not count as the entity's action for the turn.
                                """
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Dark Magic Techniques",
                    description="""
                    Dark magic techniques tend to focus on weakening opponents, 
                    attacking indirectly and summoning. Many dark mages also 
                    employ a mixture of status techniques and poisons to make life 
                    as hard as possible for their adversaries.
                    """,
                    children=[
                        LinasTechnique(
                            name="Gravity",
                            description="""
                            Deals damage to entity equal to their armor value. 
                            Causes enemies in the air to return to the ground
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Curse",
                            description="""
                            Decreases the damage of target's next attack by X 
                            where X is equal to this technique's damage.
                            """,
                            damage=2,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                Damage from entity's next attack cannot be 
                                reduced below 1
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Animate Dead",
                            description="""
                            Animates fallen corpse to fight for the user. Corpse
                            animates with X+1 HP where X is equal to this technique's
                            damage. Technique must be reused every turn to keep it
                            active. Reusing a technique can be taken as a bonus action.
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                                """
                                Reanimated corpse's stats (aside from HP), 
                                equipment, etc are equal to what they were when 
                                the original entity died
                                """,
                                """
                                Animated corpses are given the 'zombie' status
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Drain HP",
                            description="""
                            Absorbs life energy from target entity. Reduces 
                            target entity's HP by X and restores user's HP 
                            by X where X is equal to this technique's damage.
                            """,
                            damage=1,
                            range=1,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                This attack is not counted as direct damage and 
                                therefore it's effects cannot be prevented, 
                                absorbed by armor, or redirected.
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Drain TP",
                            description="""
                            Absorbs energy from target entity. Reduces 
                            target entity's TP by X and restores user's TP 
                            by X where X is equal to this technique's damage.
                            """,
                            damage=1,
                            range=1,
                            cost=0,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                This attack is not counted as direct damage and 
                                therefore it's effects cannot be prevented, 
                                absorbed by armor, or redirected.
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Summon",
                            description="""
                            Summons a monster or animal to help the user.
                            Technique must be reused each turn to keep going.
                            Reusing a technique can be taken as a bonus action.
                            )
                            """,
                            damage=0,
                            range=1,
                            numTargets=0,
                            skill="magic",
                            stat='int',
                            notes=[
                                """
                                In addition to the using cost of this technique,
                                must also pay X TP when first using where X is
                                1/2 of the target summoned entity's HP
                                (rounded up)
                                """
                            ]
                        )
                    ],
                    
                ),
                DataCollection(
                    name="Status Techniques",
                    description="""
                    The techniques in this category don't cause any direct damage 
                    nor are they aligned with any element. Instead, these techniques
                    focus on inflicting special conditions on the target. These 
                    techniques are usually taken in combination with the techniques from 
                    other schools as a way to control the flow of battle or as 
                    part of a larger more complex strategy.
                    """,
                    children=[
                        LinasTechnique(
                            name="Poison",
                            description="""
                            Target entity is now poisoned
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Sleep",
                            description="""
                            Target entity is now asleep
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Madness",
                            description="""
                            Target entity is now insane
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Charm",
                            description="""
                            Target entity is now charmed
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Seal",
                            description="""
                            Target entity is now sealed
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="magic",
                            stat='int',
                            status=True,
                            notes=[
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Combat Techniques",
                    description="""
                    The techniques in this section are unique in the aspect that 
                    they are more geared towards physical combat vs. magical. 
                    These techniques tend to have fairly low TP costs but are also 
                    much more limited in terms of improvement.
                    """,
                    children=[
                        LinasTechnique(
                            name="Protect",
                            description="""
                            Until your next turn if target entity would take 
                            damage, you take that damage instead
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="Any combat skill",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Berserk",
                            description="""
                            Physical melee damage dealt is doubled until your 
                            next turn. This does not count as your action for 
                            the turn.
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            skill="any combat",
                            points=1,
                            notes=[
                                """
                                Can no longer use techniques or use items
                                """,
                                """
                                Can no longer counter or defend
                                """,
                                """
                                Can no longer use abilities and all passive 
                                abilities stop working
                                """,
                                """
                                Can no longer recover HP
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Flip thrust",
                            description="""
                            Flips the opponent onto the ground and stabs them in one fluid motion.
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="assassination",
                            stat="dex",
                            notes=[
                                """
                                If 6 is rolled, target is now prone and must
                                spend 1 turn picking themselves up off the ground
                                """,
                                """
                                Can only be used with knives and daggers
                                """,
                                """
                                Can only be used while in stealth
                                """,
                                """
                                target is no longer in stealth after combat 
                                resolves
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Pressure Point",
                            description="""
                            A quick sharp thrust is used to hit vital pressure points on
                            the opponent and incapacitate them.
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            status=True,
                            skill="assassination",
                            notes=[
                                """
                                Deals damage to opponent equal to user's speed
                                """,
                                """
                                If 6 is rolled, target is now paralyzed
                                """,
                                """
                                Upgrade: Can be upgraded such that
                                If 6 is rolled, target is now sealed
                                IF 3 is rolled, target is now paralyzed
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Whirlwind Cut",
                            description="""
                            Deals damage to all adjacent entities (both friend 
                            and foe)
                            """,
                            damage=2,
                            range=0,
                            numTargets=0,
                            fnf=True,
                            aoe=True,
                            skill="swordsmanship",
                            stat="str",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Aero Cut",
                            description="""
                            A fast slash which sends out a wave of wind ahead of it
                            """,
                            damage=2,
                            range=3,
                            numTargets=1,
                            skill="swordsmanship",
                            stat="str",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Cleave",
                            description="""
                            Powerful attack which has the potential to break armor
                            """,
                            damage=4,
                            range=1,
                            numTargets=1,
                            skill="swordsmanship",
                            stat="str",
                            notes=[
                                """
                                If 6 is rolled, Reduce target's armor to 0 for
                                the round. (This takes effect before dealing
                                damage))
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Backstab",
                            description="""
                            Attack with equipped weapon ignoring armor value of 
                            target.
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            skill="fencing",
                            notes=[
                                """
                                Can only be used with knives and daggers
                                """,
                                """
                                Can only be used while in stealth
                                """,
                                """
                                target is no longer in stealth after combat 
                                resolves
                                """
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Music Techniques",
                    description="""
                    Music techniques are special songs which when played on a 
                    musical instrument cause unpredictable effects in and 
                    outside of battle.In the true spirit of bardship, many of 
                    these techniques and effects are random and have the chance to 
                    hit either friend or foe. However, when used at the right 
                    time; these techniques can also turn the tides of battle as 
                    their effects are usually widespread.
                    """,
                    children=[
                        LinasTechnique(
                            name="Lullaby",
                            description="""
                            Causes a soft melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            avoid the attack. All entities who fail the roll are 
                            now asleep
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            status=True,
                            aoe=True,
                            fnf=True,
                            skill="music",
                            notes=[
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Battle March",
                            description="""
                            Causes an upbeat melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            are effected by the attack. All entities who pass 
                            this roll get X added to their next attack where X 
                            is equal to this techniques's damage
                            """,
                            damage=2,
                            range=0,
                            numTargets=0,
                            skill="music",
                            stat="int",
                            aoe=True,
                            fnf=True,
                            notes=[
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Heavy Metal",
                            description="""
                            Causes a brutal melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            avoid the attack. Any entities who fail this roll 
                            take X damage where X is the damage of this techniques.
                            """,
                            damage=2,
                            range=0,
                            numTargets=0,
                            aoe=True,
                            fnf=True,
                            skill="music",
                            stat="int",
                            notes=[
                                """
                                Any entities who roll 1 on this check are now 
                                paralyzed in addition to taking damage
                                """,
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Holy Chorus",
                            description="""
                            Causes an uplifting melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            are effected by the attack. All entities who pass 
                            this roll get X HP restored where X is equal to this 
                            techniques's damage
                            """,
                            damage=2,
                            range=0,
                            numTargets=0,
                            skill="music",
                            stat="int",
                            aoe=True,
                            fnf=True,
                            notes=[
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Freestyle Jazz",
                            description="""
                            Causes a chaotic melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            avoid the attack. Any entities who fail this roll 
                            are now insane
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            skill="music",
                            status=True,
                            aoe=True,
                            fnf=True,
                            notes=[
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Song of Silence",
                            description="""
                            Causes a stifling melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            avoid the attack. Any entities who fail this roll 
                            are now sealed
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            skill="music",
                            status=True,
                            aoe=True,
                            fnf=True,
                            notes=[
                                """
                                This targets the user as well
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Song of Provocation",
                            description="""
                            Causes a raucous melody to drift across the 
                            battlefield. All entities roll 1d6 to see if they 
                            are effected by the attack. All entities who pass 
                            this roll get their physical melee damage dealt 
                            doubled until your next turn.
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            points=1,
                            aoe=True,
                            fnf=True,
                            skill="music",
                            notes=[
                                """
                                Can no longer use techniques or use items
                                """,
                                """
                                Can no longer counter or defend
                                """,
                                """
                                Can no longer use abilities and all passive 
                                abilities stop working
                                """,
                                """
                                Can no longer recover HP
                                """,
                                """
                                This targets the user as well
                                """
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Ninjitsu Techniques",
                    description="""
                    Ninjitsu is one of three technique categories inspired by 
                    eastern culture. Ninjitsu techniques focus on surprising the 
                    enemy and attacking from the shadows. Ninjitsu is strongest 
                    when paired up with items and combat abilities allowing 
                    characters to attack from close range while staying just out 
                    of their opponent's reach
                    """,
                    children=[
                        LinasTechnique(
                            name="Clone",
                            description="""
                            Summons a clone of user with X HP where X is
                            this technique's damage. Technique must be reused each
                            turn to keep going. Reusing a technique can be taken as
                            a bonus action.
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="ninjitsu",
                            stat="int",
                            notes=[
                                """
                                HP of summoned entity cannot exceed remaining
                                HP of user
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Substitute",
                            description="""
                            The next time the user is attacked they may trade 
                            places with an inanimate object on the battlefield 
                            up to X squares away where X is equal to this 
                            technique's damage
                            """,
                            damage=2,
                            range=0,
                            numTargets=0,
                            skill="ninjitsu",
                            stat="spd",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Mimic",
                            description="""
                            User copies the last attack used before this one. 
                            All damage and effects of the previous attack are 
                            copied; however this is counted as a new technique
                            """,
                            damage=1,
                            range=0,
                            numTargets=0,
                            skill="ninjitsu",
                            stat="int",
                            notes=[
                                """
                                Everything except for the mana cost of the 
                                previous technique is copied
                                """
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Bushido Techniques",
                    description="""
                    The second technique category based on eastern culture. Bushido 
                    techniques are similar to combat techniques but focus more on speed 
                    rather than strength for cutting enemies down. Additionally, 
                    many bushido techniques tend to be linked to a specific weapon 
                    so finding a weapon and mastering it is more important in 
                    bushido than simply learning a larger variety of techniques. 
                    However, there are a few techniques which can be used 
                    independent of weapons which are listed below
                    """,
                    children=[
                        LinasTechnique(
                            name="Draw",
                            description="""
                            This attack deals damage equal to the user's 
                            speed
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            skill="bushido",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Vacuum Cut",
                            description="""
                            Creates a negative space between the user and 
                            their target and then lashes out from the center of 
                            that space.
                            """,
                            damage=3,
                            range=2,
                            numTargets=1,
                            skill="bushido",
                            stat="spd",
                            notes=[
                                """
                                This attack ignores armor value
                                """,
                                """
                                This damage cannot be absorbed, prevented, or 
                                redirected
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Step Cut",
                            description="""
                            Move and attack in one fluid motion. Deal damage to 
                            target and then move to a square adjacent to them.
                            """,
                            damage=3,
                            range=3,
                            numTargets=1,
                            skill="bushido",
                            stat="spd",
                            notes=[
                            ]
                        )
                    ]
                ),
                DataCollection(
                    name="Martial Arts Techniques",
                    description="""
                    The third technique category based on eastern culture, Martial 
                    arts techniques are generally tied to a specific school and 
                    are geared towards physical (unarmed) combat vs. armed.
                    """,
                    children=[
                        LinasTechnique(
                            name="Fighting Spirit",
                            description="""
                            While unarmed user gets +X STR and +X END where X 
                            are equal to the damage of this technique. These values 
                            do not count towards the user's stat caps. 
                            Technique must be reused each turn to keep going.
                            Reusing a technique can be taken as a bonus action.
                            """,
                            damage=1,
                            range=0,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                            ]
                        ),
                        LinasTechnique(
                            name="Calm Mind",
                            description="""
                            Breathe in and prepare to strike. This does not count 
                            as the user's action for the turn. During the 
                            next attack made by the user a 5 or 6 counts as a 
                            critical hit
                            """,
                            damage=0,
                            range=0,
                            numTargets=0,
                            points=1,
                            skill="martial arts",
                            notes=[
                                """
                                Snake School
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Dosukoii",
                            description="""
                            The user uses their weight to shove their target 
                            backwards. Target entity is moved backwards one 
                            space
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="str",
                            notes=[
                                """
                                Sumo school
                                """,
                                """
                                If target falls off a cliff or cannot move 
                                backwards due to some boundary they take an 
                                additional 1 damage from this attack
                                """,
                                """
                                If user's weight is 250lbs or higher, this 
                                attack is rolled at +1
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Vital Jab",
                            description="""
                            Quick powerful strikes hit vital pressure points 
                            slowing movement and leave the target vulnerable.
                            """,
                            damage=1,
                            range=1,
                            numTargets=1,
                            status=True,
                            skill="martial arts",
                            stat="spd",
                            notes=[
                                """
                                Dragon school
                                """,
                                """
                                target cannot move during their next turn
                                """,
                                """
                                If a 6 was rolled target is now paralyzed
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Crane Kick",
                            description="""
                            An attack where the user balances on one foot and 
                            strikes swiftly and fluidly at their opponent. This 
                            technique cannot be used in the same turn the 
                            user moved and the user cannot move during the 
                            turn this technique was used
                            """,
                            damage=4,
                            range=2,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                                """
                                Crane school
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Flurry",
                            description="""
                            A high speed volley of punches barrages the 
                            opponent. Always succeeds (regardless of dice roll). 
                            Deals damage equal to the number rolled on the dice
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            notes=[
                                """
                                Tiger school
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Sweeping Kick",
                            description="""
                            A powerful circular kick capable of knocking 
                            opponents down as well as striking from a distance
                            """,
                            damage=2,
                            range=2,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                                """
                                Crane school
                                """,
                                """
                                If a 6 is rolled, target loses balance (falls 
                                down) and must spend one turn to regain it 
                                (loses turn)
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Dragon's Roar",
                            description="""
                            A high speed punch which causes disruption of the 
                            inner ear causing blurred vision, loss of balance 
                            and in some cases temporary insanity
                            """,
                            damage=3,
                            range=1,
                            numTargets=1,
                            status=True,
                            skill="martial arts",
                            stat="spd",
                            notes=[
                                """
                                Dragon school
                                """,
                                """
                                Target's next roll is made at -1
                                """,
                                """
                                If a 6 is rolled target is now insane
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Cobra strike",
                            description="""
                            A fluid punch which deals damage equal to the 
                            user's speed
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            notes=[
                                """
                                Snake School
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Afterimage",
                            description="""
                            User attacks with a false punch first and then 
                            quickly attacks with a real punch to throw their 
                            opponent off guard
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="spd",
                            notes=[
                                """
                                Tiger school
                                """,
                                """
                                Move cannot be countered or dodged
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Suplex",
                            description="""
                            The user grabs their opponent and slams them into 
                            the ground.
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="str",
                            notes=[
                                """
                                Sumo school
                                """,
                                """
                                If weight is 250lbs or more add +2 to damage 
                                done
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Dragon's Fangs",
                            description="""
                            An extremely risky all or nothing attack. Either 
                            deals no damage or instantly kills opponent
                            """,
                            damage=0,
                            range=1,
                            numTargets=1,
                            status=True,
                            skill="martial arts",
                            notes=[
                                """
                                Dragon school
                                """,
                                """
                                If a 6 is rolled target's HP is reduced to 0 
                                and they receive the death status
                                """,
                                """
                                Can only be used once per battle. Regardless of
                                failure or success.
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Flip kick",
                            description="""
                            A high powered kick that knocks down the opponent 
                            and also causes the user to move backwards 1 space
                            """,
                            damage=2,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                                """
                                Crane school
                                """,
                                """
                                if a 5 or 6 are rolled, opponent is knocked down 
                                and must spend 1 turn to recover
                                """,
                                """
                                User moves backwards 1 space after using 
                                this. This does not count as movement for the 
                                turn
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Flowing strike",
                            description="""
                            A quick and fluid punch which uses an opponents 
                            momentum against them
                            """,
                            damage=1,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                                """
                                Snake School
                                """,
                                """
                                If the target tried to dodge or counter at all, 
                                negate that action and add +2 to damage done
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Fancy Footwork",
                            description="""
                            Technique where the bobs from side to side balancing 
                            on the balls of their feet. Makes movements 
                            extremely hard to predict. Technique must be reused each
                            turn to keep going. Reusing a technique can be taken
                            as a bonus action.
                            """,
                            damage=1,
                            range=0,
                            numTargets=1,
                            skill="martial arts",
                            stat="dex",
                            notes=[
                                """
                                Tiger School
                                """,
                                """
                                If a successful counter attack is made in this 
                                state, add +2 to the damage done from that 
                                attack
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Heavy Toss",
                            description="""
                            Technique where the user picks up and throws their 
                            opponent. Takes one turn to pick up their opponent 
                            and 1 turn to throw
                            """,
                            damage=5,
                            range=1,
                            numTargets=1,
                            skill="martial arts",
                            stat="str",
                            notes=[
                                """
                                Sumo school
                                """,
                                """
                                If target weights 250lbs or more, add +2 to 
                                damage
                                """,
                                """
                                Target is knocked down after this resolves and 
                                must spend 1 turn to recover
                                """,
                                """
                                Target can roll to attempt to get out of the 
                                hold between when the move Is used and when it 
                                resolves
                                """
                            ]
                        )
                    ]
                )
            ],
            "effects":[
                DataCollection(
                    name="Effects",
                    description="""
                    Effects are similar to abilities; however, effects are only
                    temporary and cannot always be removed by choice. Usually
                    effects happen as a result of an action by the player or
                    some other entity. However, the GM may also put an effect
                    into play to balance out the game or to help bolster a
                    character which would otherwise have a hard time completing
                    the day's tasks.
                    """,
                    children=[
                        LINASEffect(
                            name="Berserk",
                            description="""
                            Damage dealt by physical melee attacks is doubled.
                            Entity cannot be healed and cannot use techniques or
                            use items until this condition is removed. Entity
                            MUST attack each turn if able (if entity could move
                            to attack a target they must move as well).
                            """
                        ),
                        LINASEffect(
                            name="Raining",
                            description="""
                            Entity's speed is reduced by 2. Add +1 to technique rolls
                            involving electric type techniques. Subtract -1 from rolls
                            involving fire type techniques. Subtract -1 to skill rolls
                            involving ranged weapons and perception.
                            """
                        ),
                        LINASEffect(
                            name="Exhausted",
                            description="""
                            Entity gets -1 to all skill rolls
                            """
                        ),
                        LINASEffect(
                            name="Haunted",
                            description="""
                            At the start of the entity's combat turn, they roll
                            1d6 and do the following based on result 1 = entity
                            skips turn, 2 = entity is now mad, 3 = entity is
                            paralyzed, 4 = entity loses 2 HP, 5 = entity gets
                            -1 to attack roll, 6 = nothing happens
                            (turn proceeds as normal)
                            """
                        ),
                        LINASEffect(
                            name="Inebriated",
                            description="""
                            Max TP cut by 1/2, immedately lose any TP over new
                            max. -2 to INT Must roll to move (standard skill roll).
                            -1 to all skill rolls and attack rolls. Cannot react.
                            """
                        ),
                        LINASEffect(
                            name="Well Rested",
                            description="""
                            Entity gets +1 to all skill rolls
                            """
                        ),
                        LINASEffect(
                            name="Snowing",
                            description="""
                            Entity's speed is reduced by 4. Add +1 to technique rolls
                            involving ice type techniques. Subtract -1 from rolls
                            involving wood type techniques.  Subtract -2 to skill
                            rolls involving ranged weapons and perception.
                            """
                        ),
                        LINASEffect(
                            name="Broken Weapon",
                            description="""
                            Entity's weapon deals 1/2 it's normal damage
                            (rounded down)
                            """
                        ),
                        LINASEffect(
                            name="Broken Armor",
                            description="""
                            Entity's armor does not recover at the end of the
                            round.
                            """
                        ),
                    ]
                ),
                DataCollection(
                    name="Status Conditions",
                    description="""
                    Status conditions are generally only placed on a player
                    during battle. However there may be some cases outside
                    battle where the player is effected by a satus condition
                    as well. However, generally speaking status effects go away
                    once the battle ends. The main difference between effects and
                    status conditions is that the player can remove status
                    conditions using potions, magic, or some other means whereas
                    effects are generally only removed by the GM or by fulfiling
                    some obligatory condition.
                    """,
                    children=[
                        LINASEffect(
                            name="Nausea",
                            description="""
                            Entity can no longer consume potions or food.
                            """
                        ),
                        LINASEffect(
                            name="Poison",
                            description="""
                            Entity takes +1 damage at the beginning of their turn.
                            """
                        ),
                        LINASEffect(
                            name="Sleep",
                            description="""
                            Entity must roll to see if wake up at the beginning
                            of their turn (standard skill roll). Entity also wakes
                            up if hit with an attack. Sleeping entities cannot
                            react when targeted with an attack and cannot attack
                            or move on their turn while asleep.
                            """
                        ),
                        LINASEffect(
                            name="Paralyzed",
                            description="""
                            Entity must roll to see if they can move when moving
                            and gets -2 added to attack and reaction rolls.
                            """
                        ),
                        LINASEffect(
                            name="Burn",
                            description="""
                            Entity receives +2 damage when moving, attacking,
                            or reacting.
                            """
                        ),
                        LINASEffect(
                            name="Madness",
                            description="""
                            Entity rolls at -2 to see if they control their
                            actions for the turn. If entity fails roll. GM
                            determines what entity does that turn.
                            """
                        ),
                        LINASEffect(
                            name="Sealed",
                            description="""
                            Entity cannot use techniques. Any ongoing techniques use
                            by the entity end immediately.
                            """
                        ),
                        LINASEffect(
                            name="Bind",
                            description="""
                            Entity cannot move, attack, or use techniques for 3 turns
                            """
                        ),
                        LINASEffect(
                            name="Charm",
                            description="""
                            Entity rolls at -1 to see if they control their
                            actions for the turn. If entity fails roll, the
                            entity who charmed this entity controls their
                            actions instead.
                            """
                        ),
                        LINASEffect(
                            name="Transformed",
                            description="""
                            Entity's stats are augmented based on transformation.
                            Transformed entities cannot use techniques nor can they
                            use items.
                            """
                        ),
                        LINASEffect(
                            name="Death",
                            description="""
                            Entity is removed from the game until either
                            Resurrect is use or until the GM has decided a
                            long enough time has passed that resurrection is
                            no longer an option; at which point the entity is
                            removed from the game permanently.
                            """
                        ),
                    ]
                ),
            ]
        })
        # ======================================================================
        # = End Define Data
        # ======================================================================

        # ======================================================================
        # = Begin Post-Process Data Definitions
        # ======================================================================
        # Some data objects have to be added to the data manager after the
        # initial object has been created because they rely on the data manager
        # for their own initialization -- JRB
        self.__dataManager.addKey(
            keyName="classes",
            keyData=[
                LINASClass(
                    name="Archer",
                    description="""
                    Archers fight primarily with bows and crossbows. As such, 
                    they tend to try and keep their opponents at a distance. 
                    They also typically equip light armor vs. heavy in order to 
                    both keep distance between them and their opponents as well 
                    as to ensure fewer chances that their attacks are countered.
                    """,
                    skills=[
                        ("Archery",0),
                        ("Perception",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=("Bow","Weapons"),
                            qty=1
                        ),
                        ItemRecord(
                            item=("Arrow","General use"),
                            qty=10
                        )
                    ],
                    notes=[
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Bard",
                    description="""
                    Bards use musical instruments both inside and outside 
                    battle. In battle they can use their instruments directly 
                    for smacking enemies around as well as for using powerful 
                    techniques which effect all who hear them. Outside battler bards 
                    use their weapons for entertainment purposes as well as to 
                    make some extra money on the side.
                    """,
                    skills=[
                        ("Music",0),
                        ("bashing",-1)
                    ],
                    items=[],
                    notes=[
                        """
                        For instrument, choose 2 techniques from the music school
                        """
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Knight",
                    description="""
                    Knights tend to favor physical combat using weapons and 
                    heavy armor. However, this isn’t a steadfast rule and some 
                    knights have been known to balance using ranged weapons or 
                    even magic for a fearsome combination. However, since 
                    knights tend to have high speed penalties; the bulk of their 
                    development does tend to be in strength and combat vs. other 
                    areas.
                    """,
                    skills=[
                        ("Any combat skill",0)
                    ],
                    items=[
                        ItemRecord(
                            item=("Sword","Weapons"),
                            qty=1
                        ),
                        ItemRecord(
                            item=("Plate Armor","Armor & Clothing"),
                            qty=1
                        )
                    ],
                    notes=[
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Mage",
                    description="""
                    Mages use a wide variety of magic techniques in order to deal damage, 
                    create illusions and control the flow of battle, as well as 
                    summon powerful enemies to fight alongside them. Mages are 
                    one of the more flexible and complex classes to set up and 
                    there are many details to consider such as the type of mage 
                    the player is (healer, elemental, necromancer, druid, etc.). 
                    And whether the mage is going to align themselves with a 
                    single element or be a jack of all trades so to speak. 
                    Before choosing to become a mage it’s recommended the 
                    player read the section on techniques to understand how magic 
                    works. It is also recommended first time mages work with the 
                    DM to ensure they have everything they need to play their 
                    class effectively.
                    """,
                    skills=[
                        ("Magic",0),
                        ("Bashing",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=("Robe","Armor & Clothing"),
                            qty=1
                        )
                    ],
                    notes=[
                        """
                        Choose 2 techniques from one of the schools 
                        of magic which best fits the type of mage the player is 
                        striving to be
                        """
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Martial Artist",
                    description="""
                    Martial artists use unarmed attacks to fight and through 
                    training are able to increase their physical attack and 
                    defense to a point which can rival armed combatants. 
                    Additionally, many martial artists are able to utilize TP to 
                    perform advanced techniques. However, unlike other classes, 
                    martial artists store their techniques in their bodies vs. 
                    items and technique slots/abilities are unlocked through 
                    training vs. buying items
                    """,
                    skills=[
                        ("Martial Arts",0),
                        ("Sensing",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=("Padded Gloves","Weapons"),
                            qty=1
                        )
                    ],
                    notes=[
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Ninja",
                    description="""
                    Ninjas are a class of fighter who use a mixture of stealth 
                    and magic to perform assassinations on their targets. Unlike 
                    rogues, ninjas focus more on combat vs. gathering 
                    information and stealing items. However, these activities 
                    aren’t outside the realm of possibility for a ninja 
                    either. Ninja’s also rely heavily on items and traps in 
                    addition to magic making them a very versatile class when 
                    played correctly
                    """,
                    skills=[
                        ("Ninjitsu",-1),
                        ("Fencing",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=("Dagger","Weapons"),
                            qty=1
                        )
                    ],
                    notes=[
                        """
                        For novice gauntlet, choose 2 techniques from the ninjitsu 
                        school
                        """
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Rogue",
                    description="""
                    Rogues favor stealth and resourcefulness over brute force. 
                    Rogues are also usually fairly decent at getting into places 
                    or acquiring information. However, this also means they tend 
                    to favor things such as using the environment, traps, 
                    poison, or other indirect means of dealing damage vs. facing 
                    their opponents directly
                    """,
                    skills=[
                        ("Pickpocket or Lockpicking",-1),
                        ("Stealth",-1),
                        ("Fencing",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=("Knife","Weapons"),
                            qty=1
                        )
                    ],
                    notes=[
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="Merchant",
                    description="""
                    Although the class says merchant, this is really a 
                    generalized class meant to encompass all crafting and 
                    merchant classes. Generally speaking a merchant’s goal is 
                    to manufacture or acquire items to sell. Merchants tend to 
                    play a more supportive role to the party, using items in 
                    battle for those who cannot and improving the party’s 
                    equipment when able. When played efficiently, they’re also 
                    able to generate quite a bit of money which in some cases 
                    can save the party a lot of time and trouble
                    """,
                    skills=[
                        ("Any Crafting Skill",0),
                        ("Speech",-1)
                    ],
                    items=[
                        ItemRecord(
                            item=LINASItem(
                                name="Any Required Item(s)",
                                description="""
                                Any required item(s) needed to perform the character's
                                desired trade. This primarily refers to tools needed to
                                craft specific items such as the chemist's set,
                                carpenter's tools, etc.
                                """,
                                cost=0,
                            ),
                            qty=1
                        )
                    ],
                    notes=[
                    ],
                    data=self.__dataManager
                ),
                LINASClass(
                    name="ZCustom",
                    description="""
                    Like with races, LINAS allows the player to define their own class
                    for their character if wanted. Since classes are more of templates
                    vs. hard defined rules, creating a custom class is pretty much a
                    blank canvass. However, like with races, there are a few guidelines
                    which need to be observed when creating a custom class. Additionally,
                    the DM should work with the player to make sure the class is both
                    balanced and also is as close to the role the player wants their
                    character to play as possible.
                    """,
                    skills=[("Any",3)],
                    items=[
                        ItemRecord(
                            item=LINASItem(
                                name="Any Required Item(s)",
                                description="""
                                Any required item(s) needed to perform the character's
                                desired trade. This primarily refers to tools needed to
                                craft specific items such as the chemist's set,
                                carpenter's tools, etc.
                                """,
                                cost=0,
                            ),
                            qty=1
                        )
                    ],
                    notes=[
                        """
                        For skills, this is 3 points distributed any way the
                        player chooses e.g. 3 skills at -1, 2 skills one at -1
                        and one at 0, or 1 skill at +1
                        """,
                        """
                        For required items, if picking an item with limited
                        uses such as arrows or lockpicks. A quantity greather
                        than 1 may be justified. In these cases, the player
                        should work with the DM to come up with a fair number of
                        these items.
                        """
                    ],
                    data=self.__dataManager
                )
            ]
        )
        self.__dataManager.addKey(
            keyName="races",
            keyData=[
                LINASRace(
                    name="Dragon Half",
                     description="""
                         The hybrid offspring of dragons and some other race. 
                         Usually fairly tall with scaled skin (color varying), 
                         tails, horns, and slit eyes. Despite their generally
                         light aligned moral standing  and genuinely calm nature,
                         they are often ostracized by both sides of their families.
                         Excluded from the dragon race for not being pure-blooded
                         dragons and excluded from the human race for their
                         appearance. Dragon halves  have an elemental affinity
                         with fire as well as increased strength and spirit
                         making them formidable opponents or allies.
                     """,
                    stats=[ ("Spr", 1), ("Str", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Fire Eater",
                            type="p",
                            description="""
                            Fire techniques used against the user are converted
                            to HP instead of damage (they heal them). In
                            return, ice techniques used against the user deal 
                            +2 damage to them, are rolled at +1, and cannot
                            be countered or dodged.
                            """
                        ),
                         LINASAbility(
                            name="Fire Breath",
                            type="a",
                            description="""
                            This ability can only be used once per full 
                            rest period. This ability can only be taken by 
                            the Dragon Half race. User deals 5 fire damage 
                            to target entity up to 2 squares away. All 
                            entities adjacent to target (except for the 
                            user) take 3 fire damage as well. 
                            """
                         )
                    ],
                    languages=[ "Common", "Draconic" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="Dwarf",
                     description="""
                         Dwarves tend to live around and in mountains as their
                         main sources of income are from mining, blacksmithing,
                         and tinkering. Despite their rough demeanor; Dwarves
                         are actually highly intelligent and often fight with
                         advanced firearms and machinery in addition to
                         preferring heavy weapons like axes and maces which
                         double as both work tools and weapons for combat. Dwarves
                         also tend to keep to themselves and it can be hard to
                         win their trust. However, once a Dwarf considers you a
                         friend they'll stick by your side for life.
                     """,
                    stats=[ ("End", 1), ("Str", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Advanced Metalworking",
                            type="p",
                            description="""
                                The user has gained advanced knowledge of the 
                                properties of a wide variety of  metals and 
                                how to craft with them. All metal weapons 
                                crafted by the user have  an additional 1 
                                added to their damage ratings. All additional 
                                metal armor  crafted by the user have an 
                                additional 1 added to their armor rating.  
                            """
                        ),
                        LINASAbility(
                            name="Last Stand",
                            type="a",
                            description="""
                            This ability can only be used once per full 
                            rest period and can only be  activated inside 
                            battle if the user has 3 HP or less. The user 
                            musters the last of their strength for one 
                            final attack. Until the user's next turn, they 
                            cannot be rendered unconscious even if their 
                            HP reaches 0. Additionally, add 2  to all 
                            damage dealt and subtract 2 from all damage 
                            taken. At the beginning of  the user's next 
                            turn, the user's HP is reduced to 0 and they 
                            are now  unconscious.  
                            """
                        )
                    ],
                    languages=[ "common", "Dwarven(modern)" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="Elf",
                     description="""
                         Elves are nimble and quick, preferring to make their
                         homes in the treetops of the various forests throughout
                         the region. It's said that the Elves were one of the
                         first races to harness magic and as such they tend to
                         be quite adept at wielding it. However, the elves also
                         have a long history as Shinobi and Assassins as well.
                         Generally speaking, the Elves are on good terms with
                         most other races and often offer help to weary travelers
                         and those in need. However, there are some among this
                         race who would rather keep to themselves much like the
                         Dwarves do. For this reason; there are still many
                         activities and rites which are closed to outsiders, even
                         those particularly close to the Elves.
                     """,
                    stats=[ ("Int", 1), ("Dex", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Arboreal Parkour",
                            type="p",
                            description="""
                            A life lived in the forest enables the user to 
                            travel much faster in the trees  than on the 
                            ground. When battling in a forest location, 
                            the user may move 2x  the distance they 
                            normally can move. Outside of battle, if the 
                            user fails a  climbing roll; they may re-roll 
                            once and take the higher of the two rolls.  
                            """
                        ),
                        LINASAbility(
                            name="Multi-Shot",
                            type="a",
                            description="""
                            This ability can only be used once per full 
                            rest period and can only be  activated inside 
                            battle. An advanced bow technique which allows 
                            the user to  split an arrow into pieces 
                            mid-flight. User may select 2 additional 
                            targets for  a single bow attack. The user 
                            must make a dice roll for each target.  
                            """
                        ),
                    ],
                    languages=[ "Elvish (forest)", "Common" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="Human",
                     description="""
                         While humans may not specialize in any one area. They 
                         are extremely flexible and adaptive. One of the newest
                         races in Kalimar, the humans are said to be responsible
                         for several wars between the 3rd and 4th eras relating
                         to territorial expansion (primarily among the elves).
                         To date, the humans still hold the most territory in
                         the area. Relations between the humans and other races
                         have also improved as well to the point where travel
                         for humans is moderately safe. Humans also have high
                         charisma resulting in many of the top merchants and
                         tradesmen in the region being human as well. 
                     """,
                    stats=[ ("Any", 1) ],
                    abilities=[
                        ("silver tongue", "passive"),
                        ("prayer", "active")
                    ],
                    languages=[ "Common" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="Mu",
                    description="""
                        The Mu are an ancient race whose original homeland was
                        destroyed by natural disaster. Resembling eastern dragons
                        and having bodies which are both scaled and have patches
                        of fur in places. It's said that the Mu alongside the
                        Dragons are the ones who created magic and as such the Mu
                        tend to have a higher understanding of both magic and
                        Alchemy than the other races. The Mu get along well with
                        the Elves, Dwarves, and Dragons but have a strong mistrust
                        of Humans who are thought to be responsible for the
                        species decline to near extinction due to poaching.
                        Relations between humans are improving due to recent
                        legislation outlawing Mu fur and scales, but the truce is
                        still much in it's early stages and the Mu are still very
                        wary of humans.
                     """,
                    stats=[ ("Spr", 1), ("Int", 1) ],
                    abilities=[
                        LINASAbility(
                        name="Advanced Decomposition",
                        type="p",
                        description="""
                        The user is able to see the makeup of things 
                        and how to deconstruct them. The  user is able 
                        to deconstruct items into their base 
                        components. The user can also  attempt to 
                        salvage broken items for parts. Both of these 
                        actions require a  skill roll to accomplish 
                        and only one roll can be made per item.  
                        """
                        ),
                        LINASAbility(
                            name="Borrowed Knowledge",
                            type="a",
                            description="""
                            This ability can only be used once per full 
                            rest period and is only learnable  by the Mu 
                            race. The user temporarily gains knowledge 
                            past their own  understanding allowing them to 
                            use a single magic based technique not known. Any 
                            requirements  to use the technique such as TP 
                            cost, stat requirements, required items, etc.  
                            still apply.  
                            """
                        )
                    ],
                    languages=[ "Alyssian", "Common" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="Vampire",
                    description="""
                    Vampires can both be created and birthed and are an 
                    actual race. Rather than  being true undead. In LINAS, 
                    vampires are merely creatures aligned with the  shadow 
                    element. Many other aspects of vampires such as being 
                    damaged by  sunlight hold true however. Vampires have 
                    naturally heightened speed as well as  a natural 
                    resistance to magic. To be transformed into a vampire; 
                    an entity must  both be bitten by the vampire as well 
                    as drink a small amount of that vampires  blood. Being 
                    transformed into a vampire replaces all racial 
                    abilities with the  vampire's. And the vampire's stat 
                    bonuses are immediately added to the  character's 
                    stats. However, to learn the Alyssian language, the 
                    entity will  still need to study that as a language 
                    skill. Despite their appearance, Vampires hold a positive
                    relation among the races and are thought to have played a
                    critical role in stopping the conflicts between the 3rd and
                    4th era as well as curbing human expansion into Kalimar
                    around that time.
                    """,
                    stats=[ ("Spr", 1), ("Spd", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Vampiric Curse",
                            type="p",
                            description="""
                            The user gains a weakness to the wood element. 
                            The user gains a weakness to the  light 
                            element and also takes damage from sunlight. 
                            This can only be taken and  must be taken by 
                            Vampires.  
                            """
                        ),
                        LINASAbility(
                            name="Vampiric Feeding",
                            type="a",
                            description="""
                            This ability can only be used once per full 
                            rest period and is only learnable  by the 
                            Vampire race. The user deals 5 direct damage 
                            to target entity and  regains 5 HP. This 
                            damage cannot be absorbed by armor, barriers 
                            or any other  damage redirection. This skill 
                            can only be used on flesh and blood creatures. 
                            """
                        ),
                    ],
                    languages=[ "Alyssian", "Common" ],
                    data=self.__dataManager
                ),
                LINASRace(
                    name="ZCustom",
                    description="""
                    As stated earlier; LINAS strives to be a flexible system
                    which rewards creativity and thinking outside the box. As
                    such, a custom race definition exists for players who want
                    to play a race not listed in the guide. That being said,
                    there are still a few guidelines to adhere to when creating
                    a custom race.
                    """,
                    stats=[ ("Any", 2)  ],
                    abilities=[
                        LINASAbility(
                            name="Any",
                            type="p",
                            description="""
                            Can be any passive ability listed in the abilities
                            section or any already defined passive racial ability 
                            or the player can define their own racial ability.
                            Player should work with the DM if creating their own.
                            """
                        ),
                        LINASAbility(
                            name="Any",
                            type="a",
                            description="""
                            Can be any active ability listed in the abilities
                            section or any already defined active racial ability 
                            or the player can define their own racial ability.
                            Player should work with the DM if creating their own.
                            """
                        ),
                    ],
                    languages=[ 
                        "Common", 
                        "Choice"
                    ],
                    notes=[
                        """
                        For stats, ANY can be 1 (at +2) or 2 stats (each at +1)
                        """,
                        """
                        For language, Choice can be any existing language or the 
                        player can define their own
                        """
                    ],
                    data=self.__dataManager
                )
            ]
        )
        # ======================================================================
        # = End Post-Process Data Definitions
        # ======================================================================

        # ======================================================================
        # = Add Sections To System Here
        # ======================================================================
        self.addContent(IntroductionSection(self))
        self.addContent(StatSection(self, self.__dataManager))
        self.addContent(SkillSection(self, self.__dataManager))
        self.addContent(CombatSystem(self))
        self.addContent(FreeTimeSection(self))
        self.addContent(NewPlayerSetupSection(self))
        self.addContent(LangRaceSection(self, self.__dataManager))
        self.addContent(ClassSection(self, self.__dataManager))
        self.addContent(TechniqueSection(self, self.__dataManager))
        self.addContent(AbilitySection(self, self.__dataManager))
        self.addContent(EffectSection(self, self.__dataManager))
        self.addContent(ItemSection(self, self.__dataManager))
        # TODO: "Entities"
        # TODO: "Campaigns"
        # TODO: "DM Tools (Character Sheets, Quick References, etc.)"