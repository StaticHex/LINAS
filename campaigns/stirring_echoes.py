from __future__ import print_function, division
from   obj_classes.data_manager    import DataManager
from   obj_classes.content_manager import ContentManager
from   obj_classes.pdf_generator   import PDFGenerator
from   obj_classes.data_collection import DataCollection
from   obj_classes.linas_lang      import LINASLanguage
from   obj_classes.linas_abil      import LINASAbility
from   obj_classes.linas_race      import LINASRace
from   obj_classes.linas_item      import LINASItem
from   obj_classes.linas_technique import LinasTechnique
from   obj_classes.linas_skill     import LINASSkill
from   obj_classes.linas_entity    import LinasEntity
from   sections.data_package       import LINASDataPackage
import os
class StirringEchoes (ContentManager):
    def __init__(self):
        self.contents=[
            "Skills",
            "Languages & Races",
            "Techniques",
            "Abilities",
            "Effects & Status Conditions",
            "Items",
            "Entities",
        ]
        self.dm = DataManager({
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
                            name="Field Medicine",
                            type="a",
                            description="""
                            Once per full rest can fully restore HP to target 
                            entity and remove all status conditions from that 
                            entity (including death). This can be taken as a
                            bonus action.
                            """
                         ),
                         LINASAbility(
                            name="Berate",
                            type="a",
                            description="""
                            If used outside combat add +2 to next speech roll made
                            If used inside combat, can be used against any entity which
                            can understand speech. Entity gets -2 to all rolls made for
                            the remainder of the battle. if a 6 is rolled while using
                            this, the entity leaves the battlefield in shame and is
                            removed from the game. This can be use once per long rest.
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
                            name="Anatomy Nerd",
                            type="p",
                            description="""
                            +1 to all rolls involving medicine, repairing
                            cybernetics, or crafting cybernetics.
                            """
                        ),
                        LINASAbility(
                            name="Superior Intellect",
                            type="p",
                            description="""
                            +1 to all rolls involving ESP based spells. +2
                            damage to all ESP based spells. +1 to all 
                            hacking rolls.
                            """
                        ),
                        LINASAbility(
                            name="Metallic Skin",
                            type="p",
                            description="""
                            -2 physical and acid damage. +2 lightning and ice
                            damage. Immune to poison.
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
                            name="HP Spray",
                            description="""
                            Target entity recovers 5HP
                            """,
                            cost=35,
                            range=1,
                            uses=1,
                        ),
                        LINASItem(
                            name="Stimpack",
                            description="""
                                Target entity recovers 5TP
                            """,
                            cost=50,
                            range=1,
                            uses=1,
                        ),
                        LINASItem(
                            name="Pharmaceuticals",
                            description="""
                                Removes all status conditions except for death
                                from target entity.
                            """,
                            cost=75,
                            uses=1,
                            range=1
                        ),
                        LINASItem(
                            name="Dried Salamander",
                            description="""
                            Thraxian delicacy. Tastes extremely salty with a
                            taste similar to chicken. Restores 3HP a single
                            target.
                            """,
                            cost=75,
                            uses=1,
                            range=1
                        ),
                        LINASItem(
                            name="USF Military Rations",
                            description="""
                            Despite the name, these are the unit of food most
                            commonly sold in stores and by merchants belonging
                            to the USF. Restores 2HP to a single target
                            """,
                            cost=10,
                            uses=1,
                            range=1
                        ),
                        LINASItem(
                            name="Hydros",
                            description="""
                            USF name for water. Just ordinary filtered drinking
                            water. Given most water aboard freighters and space
                            stations is recycled wastewater you can start to
                            see why the fresh stuff is so precious. Restores
                            1TP to a single target.
                            """,
                            cost=15,
                            uses=1,
                            range=1
                        ),
                        LINASItem(
                            name="Energy Cell",
                            description="""
                            Standard ammunition for all energy based weapons.
                            Fits most energy weapons
                            """,
                            cost=10,
                            uses=1,
                        ),
                        LINASItem(
                            name="Energy Charge",
                            description="""
                            High power energy cell designed for use in BFG type
                            weapons
                            """,
                            cost=2000,
                            uses=1,
                        ),
                        LINASItem(
                            name="Upgrade",
                            description="""
                            Used to instantly improve an energy based weapon by
                            one point.
                            """,
                            cost=2500,
                            uses=1,
                        ),
                        LINASItem(
                            name="Starship Fuel",
                            description="""
                            Used to refuel spacecraft of all sizes.
                            """,
                            cost=10000,
                            uses=1,
                        ),
                        LINASItem(
                            name="Warp Drive Fuel",
                            description="""
                            Fuel required to use FTL engines.
                            """,
                            cost=15000,
                            uses=1,
                        ),
                        LINASItem(
                            name="Coffee",
                            description="""
                            The finest coffee-like beans brewed in hot water.
                            Tastes kinda close to the real thing with 2x the
                            punch.
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                                "Restores 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Powerthirst",
                            description="""
                            Popular energy drink guaranteed to keep you awake
                            for a full 48 hours or your money back. There's a
                            sticker on the can which says "made with real
                            lightning"
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 3TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Recycled Hydros",
                            description="""
                            Recycled wastewater. It's not much but it'll keep
                            you alive.
                            """,
                            cost=0,
                            uses=1,
                            notes=[
                                "Restores 1TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Tea",
                            description="""
                            The finest leaves from somewhere boiled in hot water
                            until they could hold their flavor no longer. Has
                            a slightly bitter taste with a hint of sweetness.
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Beer",
                            description="""
                            Various grains stuffed into a barrel and left to
                            rot until they turned into something which makes you
                            dizzy. Popular choice among both military personnel
                            civilians alike.
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                                "Consumes 1TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Sogatastic Hotdog",
                            description="""
                            Nobody's really sure what's in this one. But it
                            tastes sort of like a regular hotdog so it's
                            probably safe to eat.
                            """,
                            cost=10,
                            uses=1,
                            notes=[
                                "Restores 2HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Pixza",
                            description="""
                            The box boasts it contains 7 types of toppings. It
                            doesn't go into much more detail than that. Also
                            is the sauce actually fuchsia or is box is just 
                            discolored?
                            """,
                            cost=15,
                            uses=1,
                            notes=[
                                "Restores 3HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Synthmeat Burger",
                            description="""
                            Boasting that it tastes just like real elysium beef
                            synthmeat is fairly popular. However, those who have
                            tried it say it tastes closer to chicken than beef.
                            """,
                            cost=15,
                            uses=1,
                            notes=[
                                "Restores 2HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Microgreen Salad",
                            description="""
                            Stretching the definition of what a salad is. The
                            bowl of green goo may not look like much but it's
                            actually highly nutritious.
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 5HP when consumed",
                                "Causes nausea"
                            ]
                        ),
                        LINASItem(
                            name="Nutripaste",
                            description="""
                            A tube of paste containing a completely balanced
                            meal at least from a nutrition standpoint. However
                            the taste and texture leave much to be desired.
                            """,
                            cost=1,
                            uses=1,
                            notes=[
                                "Restores 1HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Fresh Hydros",
                            description="""
                            Clean sparkling water; especially refreshing on a
                            hot day.
                            """,
                            cost=10,
                            uses=1,
                            notes=[
                                "Restores 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Sports Drink",
                            description="""
                            Contains electrolytes to quench thirst and hydrate
                            better than water alone.
                            """,
                            cost=15,
                            uses=1,
                            notes=[
                                "Restores 3TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Popples",
                            description="""
                            A thraxian snack. Popples are vibrant glowing
                            blue grub worms around the size of grapes which have 
                            a slightly sour taste and pop when bitten into
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                                "Restores 3HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Popcicle",
                            description="""
                            Mostly just sugar and water. Comes in a variety of
                            flavors and colors.
                            """,
                            cost=1,
                            uses=1,
                            notes=[
                                "Restores 1HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Latte",
                            description="""
                            Combines fine ground coffee-like beans with a frothy
                            milk like liquid. Packs 2x the punch of regular
                            coffee and 10x the flavor.
                            """,
                            cost=7,
                            uses=1,
                            notes=[
                                "Restores 3TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Scone",
                            description="""
                            A small pastry somewhere between a cookie and cake
                            with a slightly sweet taste to it. Goes great with
                            tea or coffee
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 1HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Green Tea",
                            description="""
                            The finest leaves from somewhere boiled in hot water
                            until they could hold their flavor no longer. Has
                            been dyed green for exotic look and taste
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Moss Tea",
                            description="""
                            A Thraxian beverage which is a dark greenish black
                            in color and which glows blue slightly when stirred.
                            Has a heavy earthy flavor and goes well on cold and
                            rainy days.
                            """,
                            cost=2,
                            uses=1,
                            notes=[
                                "Restores 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Void Fish",
                            description="""
                            A species of fish found on the Thraxian's homeworld.
                            The fish's name comes from it's ink black appearance
                            and sunken in eyes cavities on the side of it's body
                            which make it appear hollow. It has a surprisingly
                            light taste and goes weill with citrus.
                            """,
                            cost=15,
                            uses=1,
                            notes=[
                                "Restores 4HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Saguero Tiger Steak",
                            description="""
                            100% real Saguero Tiger Meat. The accompanied sauces
                            are strongly recommended to help mellow out the
                            strong taste. 
                            """,
                            cost=15,
                            uses=1,
                            notes=[
                                "Restores 4HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="\"Chicken\" Ranchero",
                            description="""
                            Top food scientists combined several types of
                            cheaper meat to create a food that tastes almost
                            exactly like chicken. They then made chicken
                            ranchero with it. 
                            """,
                            cost=7,
                            uses=1,
                            notes=[
                                "Restores 3HP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Thraxian Wine",
                            description="""
                            A wine with a surprisingly vibrant pink color. 
                            Thraxian wine is actually made from a type of 
                            fermented root. Despite this it has a very light
                            almost floral taste to it making it a delicacy.
                            """,
                            cost=100,
                            uses=1,
                            notes=[
                                "Drains 2TP when consumed"
                            ]
                        ),
                        LINASItem(
                            name="Jazz Cola",
                            description="""
                            Said to be the favorite soda of jazz musicians
                            everywhere. Each can contains a flavor tablet which
                            adds a little extra something and ensures no two
                            cans are ever the same.
                            """,
                            cost=5,
                            uses=1,
                            notes=[
                                "Restores 1TP when consumed"
                            ]
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
                    """,
                    children=[
                        LINASItem(
                            name="High Quality Ocular Implants",
                            description="""
                            While Equipped, user has +2 in perception.
                            """,
                            cost=3000,
                            uses=1,
                        ),
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
                            name="Laser Pistol",
                            description="""
                            A small compact energy based weapon capable of
                            completely destroying all physical matter and
                            standard issue weapon for the USF
                            """,
                            cost=150,
                            uses=1,
                            range=3,
                            m_damage=1,
                            stat="dex",
                            linkedSkill="Marksmanship",
                            notes=[
                                """
                                If dual wielding add +1 to damage""",
                                """
                                Cannot use items or use techniques in battle 
                                while dual wielding.
                                """,
                            ]
                        ),
                        LINASItem(
                            name="Energy Sword",
                            description="""
                            A high-tech sword with a blade made of pure light.
                            The color of the blade may be customized to
                            whatever color the user desires
                            """,
                            cost=250,
                            uses=1,
                            range=1,
                            m_damage=2,
                            stat="dex",
                            speedPenalty=0,
                            linkedSkill="Swordsmanship",
                            notes=[
                                "If dual wielding add +1 to damage",
                                """
                                Cannot use items or use techniques in battle 
                                while dual wielding.
                                """,
                            ],
                        ),
                        LINASItem(
                            name="Laser Rifle",
                            description="""
                            Heavy duty laser weapon used primarily by military
                            personnel. Offers improved damage and range over the
                            laser pistol in exchange for speed and 
                            maneuverability
                            """,
                            cost=200,
                            uses=1,
                            range=5,
                            m_damage=3,
                            stat="dex",
                            speedPenalty=1,
                            linkedSkill="Marksmanship",
                            notes=[
                                "This weapon cannot be dual wielded"
                            ],
                        ),
                        LINASItem(
                            name="BFG",
                            description="""
                            Strongest energy weapon available. Primarily used
                            to take out large swaths of enemies at once. Firing
                            it at close range is not recommended.
                            """,
                            cost=10000,
                            uses=1,
                            range=7,
                            m_damage=10,
                            stat="dex",
                            speedPenalty=2,
                            linkedSkill="Marksmanship",
                            notes=[
                                "This weapon cannot be dual wielded",
                                """
                                When fired, all enemies within 2 squares of 
                                target take 5 damage (including self)
                                """
                            ],
                        ),
                        LINASItem(
                            name="Gauss Cannon",
                            description="""
                            Portable high powered long range energy weapon with
                            a rechargeable battery
                            """,
                            cost=1500,
                            uses=3,
                            range=7,
                            m_damage=3,
                            stat="dex",
                            speedPenalty=2,
                            linkedSkill="Marksmanship",
                            notes=[
                                "This weapon cannot be dual wielded",
                                """
                                Weapon does not disappear when uses reach 0.
                                Weapon recharges to 3 on full rest.
                                """
                            ],
                        ),
                    ]
                ),
                DataCollection(
                    name="Armor & Clothing",
                    description="""
                    Armor provides a way for characters to protect themselves
                    from damage. Entities can equip only a single armor set at
                    a single time and can also equip a shield for a bit of 
                    extra protection if they choose.

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
                            name="Technique Disk [Mesmerise]",
                            description="""
                            Data disk which holds engram data for the 
                            mesmerise technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=500,
                            uses=1,
                        ),
                        LINASItem(
                            name="Technique Disk [Push]",
                            description="""
                            Data disk which holds engram data for the 
                            push technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=250,
                            uses=1,
                        ),
                        LINASItem(
                            name="Technique Disk [Telepathy]",
                            description="""
                            Data disk which holds engram data for the 
                            telepathy technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=1500,
                            uses=1,
                        ),
                        LINASItem(
                            name="Technique Disk [Telekinesis]",
                            description="""
                            Data disk which holds engram data for the 
                            telekinesis technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=2000,
                            uses=1,
                        ),
                        LINASItem(
                            name="Technique Disk [Pyrokinesis]",
                            description="""
                            Data disk which holds engram data for the 
                            pyrokinesis technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=2000,
                            uses=1,
                        ),
                        LINASItem(
                            name="Technique Disk [Suffocate]",
                            description="""
                            Data disk which holds engram data for the 
                            suffocate technique. When used the technique is
                            learned instantly. Must find an engram writer to
                            use
                            """,
                            cost=5000,
                            uses=1,
                        ),
                    ]
                )
            ],
            # Define Languages Here
            "languages":[
                LINASLanguage(
                    name="Harmonic",
                    description="""
                    Language spoken by the thraxian race to each other. While 
                    the thraxians don't have vocal chords to communicate audibly,
                    they do have a language they use to communicate telepathically
                    with each other. The language sounds like a series of chimes or
                    bell notes. The notes produced can vary between genders and
                    there are also regional dialects.
                    """
                ),
                LINASLanguage(
                    name="Better Common",
                    description="""
                    The language spoken by the race calling themselves "The
                    Oracles". Like their race, the name "Better Common" is not
                    actually the name of their language. The Oracles simply
                    believe their language to be superior to all others and so
                    have been pressuring the USF into replacing the common
                    language with "Better Common" for quite some time.
                    """
                ),
            ],
            "techniques":[
                DataCollection(
                    name="Other Techniques",
                    description="""
                    Techniques that don't fit.
                    """,
                    children=[
                        LinasTechnique(
                            name="Hardlight Terraforming",
                            description="""
                            Coats the surrounding terrain in hardlight. Inclines
                            and bridges the terrain making it difficult to
                            traverse. All terrain within range is considered 
                            'difficult' and takes 2 points of movement per
                            square to traverse instead of 1
                            """,
                            damage=0,
                            range=2,
                            numTargets=0,
                            status=True,
                            skill="magic",
                            stat='int',
                            notes=[
                            ]
                        ),
                    ]
                ),
                DataCollection(
                    name="ESP Techniques",
                    description="""
                    The techniques in this category use psychic energy to
                    perform a wide variety of actions from moving objects,
                    starting fires, and even being able to talk to creatures
                    who cannot talk themselves.
                    """,
                    children=[
                        LinasTechnique(
                            name="Mesmerize",
                            description="""
                            Used to hypnotize a target and control them for a
                            short period of time.
                            """,
                            damage=0,
                            range=2,
                            numTargets=1,
                            status=True,
                            skill="esp",
                            stat='int',
                            notes=[
                                """
                                You may only control targets who have a lower 
                                intelligence value than yourself
                                """,
                                """
                                Outside of battle can be used to add +2 to a
                                speech roll
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Push",
                            description="""
                            Can be used to apply force to an object in order to
                            move it. Can also be used to deal damage in a pinch
                            """,
                            damage=1,
                            range=2,
                            numTargets=1,
                            skill="esp",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Telepathy",
                            description="""
                            Allows the user to communicate with another creature
                            without speaking.
                            """,
                            damage=0,
                            range=3,
                            numTargets=1,
                            skill="esp",
                            stat='int',
                            notes=[]
                        ),
                        LinasTechnique(
                            name="Telekinesis",
                            description="""
                            The ability to pick up and manipulate objects with
                            brain waves. Can be used to either retrieve or hurl
                            objects.
                            """,
                            damage=1,
                            range=3,
                            numTargets=1,
                            skill="esp",
                            stat='int',
                            notes=[
                                """
                                Damage equal to size of object used. As user
                                increases damage, bigger objects may be moved.
                                DM decides how this scales.
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Pyrokinesis",
                            description="""
                            The ability to manipulate the temperature of objects
                            at will. Can be used to make an object erupt into
                            flame.
                            """,
                            damage=2,
                            range=2,
                            numTargets=1,
                            skill="esp",
                            status=True,
                            stat='int',
                            notes=[
                                """
                                If 6 is rolled, target is burned.
                                """
                            ]
                        ),
                        LinasTechnique(
                            name="Strangle",
                            description="""
                            A malicious telekinetic attack which lifts the user
                            off the ground by their throat and strangles them.
                            using negative brain waves.
                            """,
                            damage=3,
                            range=2,
                            numTargets=1,
                            skill="esp",
                            status=True,
                            stat='int',
                            notes=[
                                """
                                If 6 is rolled, target is asleep.
                                """
                            ]
                        ),
                    ]
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
                            name = "Hacking",
                            description = """
                            A skill which allows the user to gain access to 
                            computing systems, open doors, operate electronics
                            remotely, and virtually any other instance where the
                            user has a need to interact with some form of tech
                            they don't have access or ownership of.
                            """,
                        ),
                        LINASSkill(
                            name = "Engineering",
                            description = """
                            A skill which can be used to diagnose a variety of
                            mechanical and electrical problems. Engineers are
                            also able to craft items out of junk and can really
                            make items last.
                            """,
                        ),
                        LINASSkill(
                            name = "ESP",
                            description = """
                            A skill which allows the use of special techniques
                            utilizing brain waves as a weapon. ESP can also be
                            used on its own for various purposes such as
                            detecting energy or sensing danger.
                            """,
                        ),
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
                    ]
                )
            ],
        })
        self.dm.addKey(
            # Define Races Here
            keyName="races",
            keyData=[
                LINASRace(
                    name="Thraxian",
                    description="""
                    Appearance is a large humanoid arthropod with an appearance
                    between a dragon and a crayfish. Covered in dark bluish
                    green color to dark bluish black segmented scales. Smaller
                    scales lighter in color (pale blue to white) can be observed
                    growing along head, back, and tail. Bioluminescence can be
                    observed on the tips of the lighter colored scales as well
                    as at the very edges of the segmented plates. The face contains
                    a series of 8 eyes also with bioluminescence with an arrangement
                    similar to that of a spider. The mouth is similar to that of a
                    shark (think sergal).  Females tend to be smaller than males and
                    have a weaker bioluminescence and darker overall scale color.
                    Males have more exaggerated spines and tend to be more blue
                    green or in some cases even dark emerald in color. 

                    Behavior: Despite their monstrous appearance, Thraxians are
                    highly intelligent, gentle, and are highly empathetic. While
                    incapable of speech due to lack of vocal cords, Thraxians can
                    understand speech and can also communicate via telepathy.
                    Despite being advanced, thraxians are also fairly spritual
                    and believe the souls of the departed watch over and guide
                    those still alive. 

                    USF: Thraxians tend to specialize in technology and medicine
                    and as such they specialize in the development of both
                    cybernetic implants and genetic modification. Thraxians are
                    one of the oldest races to have entered into the USF and are
                    a huge contributor to it's success
                     """,
                    stats=[ ("End", 1), ("Str", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Anatomy Nerd",
                            type="p",
                            description="""
                            +1 to all rolls involving medicine, repairing
                            cybernetics, or crafting cybernetics.
                            """
                        ),
                         LINASAbility(
                            name="Field Medicine",
                            type="a",
                            description="""
                            Once per full rest can fully restore HP to target 
                            entity and remove all status conditions from that 
                            entity (including death). This can be taken as a
                            bonus action.
                            """
                         )
                    ],
                    languages=[ "Common", "Thraxian" ],
                    data=self.dm
                ),
                LINASRace(
                    name="The Oracles",
                    description="""
                    Appearance: A tall, slender humanoid with blue skin, a bulbous
                    head, beady black eyes, and a small beak (resembling that of a
                    nighthawk). They have an affinity for black leather and most
                    wear goggles of some sort to both protect the eyes as well as
                    to help see better as they have very poor eyesight. 

                    Behavior: They are highly intelligent and most can use
                    telepathy, telekinesis, or other forms of ESP. They also are
                    not only aware of their intelligence but tend to lord it over
                    other species. They have a bit of a god complex and can be
                    irritating but for the most part are considered friendly and
                    non-hostile.

                    USF: One of the original races to join together to form the
                    USF, the real name of their race is unknown as they demanded
                    to be known only as "Oracles". They tend to favor tech and
                    also have a penchant for creating rules. Many of the USF's
                    guidelines were written by the oracles and much of the tech
                    used from starships to weaponry is also based off Oracle
                    designs
                    """,
                    stats=[ ("Int", 1), ("Spr", 1) ],
                    abilities=[
                        LINASAbility(
                            name="Superior Intellect",
                            type="p",
                            description="""
                            +1 to all rolls involving ESP based spells. +2
                            damage to all ESP based spells. +1 to all 
                            hacking rolls.
                            """
                        ),
                         LINASAbility(
                            name="Berate",
                            type="a",
                            description="""
                            If used outside combat add +2 to next speech roll made
                            If used inside combat, can be used against any entity which
                            can understand speech. Entity gets -2 to all rolls made for
                            the remainder of the battle. if a 6 is rolled while using
                            this, the entity leaves the battlefield in shame and is
                            removed from the game. This can be use once per long rest.
                            """
                         )
                    ],
                    languages=[ "Common", "Better Common" ],
                    data=self.dm
                ),
            ]
        )
        self.dm.addKey(
            # Define Races Here
            keyName="entities",
            keyData=[
                LinasEntity(
                    name = "Liquid Metal Ooze",
                    desc = """
                    An alien life-form which looks like an amorphous puddle of
                    metal. It is parasitic and can fuse it's own DNA to that of
                    a compatible host life-form. It is extremely resistant to
                    physical attacks, extreme caution recommended when dealing
                    with this life-form.
                    """,
                    stats = {
                        "hp":3,
                        "tp":2,
                        "str":1,
                        "dex":0,
                        "spd":0,
                        "int":0,
                        "end":2,
                        "spr":0
                    },
                    isBoss = False,
                    weapon = LINASItem(
                        name = "Slime Body",
                        description = """
                        Use gelatinous body as a whip to strike or bind the
                        target. If 6 is rolled, player is grappled and must roll
                        to break free.
                        """,
                        linkedSkill="Bashing",
                        stat="Str",
                        p_damage=1,
                        range=1,
                        points=0,
                        cost=0
                    ),
                    armor = LINASItem(
                        name = "Gelatinous Metal",
                        description = """
                        Strong springy metal which is extremely resistant to
                        physical attacks
                        """,
                        p_protection=5,
                        points=0,
                        cost=0
                    ),
                    skills={
                        "Bashing":"0"
                    },
                    abilities=[
                        LINASAbility(
                            name="Osmosis",
                            type="a",
                            description="""
                            You cease to exist but permanently bind yourself to
                            another character on the map. That character gains
                            the metal skin ability. Can only be used if when
                            grappling another character.
                            """
                        ),
                        LINASAbility(
                            name="Metal Skin",
                            type="p",
                            description="""
                            -2 physical and acid damage. +2 lightning and ice
                            damage. Immune to poison.
                            """
                        )
                    ]
                ),
                LinasEntity(
                    name = "Infected Thief",
                    desc = """
                    This hapless thief snuck into the station's biology lab 
                    looking for research samples to steal. However they got more
                    than they bargained for when they accidentally broke one of
                    the petri dishes crawling back into the vent, contaminating
                    themselves in the process
                    """,
                    stats = {
                        "hp":5,
                        "tp":0,
                        "str":2,
                        "dex":0,
                        "spd":0,
                        "int":0,
                        "end":3,
                        "spr":0
                    },
                    isBoss = True,
                    weapon = LINASItem(
                        name = "Infected Claw",
                        description = """
                        Mutagenic growth triggered by viral infection. Rolling 6
                        causes poison.
                        """,
                        linkedSkill="Claws",
                        stat="Str",
                        p_damage=1,
                        range=1,
                        points=0,
                        cost=0
                    ),
                    armor = LINASItem(
                        name = "Rotten Flesh",
                        description = """
                        The virus has dampened pain response and hardened the
                        hosts skin like leather, normal wounds won't be very
                        effective
                        """,
                        p_protection=2,
                        points=0,
                        cost=0
                    ),
                    skills={
                        "Claws":"0"
                    },
                    abilities = [
                        LINASAbility(
                            name = "Vent Spores",
                            type = "Active",
                            description = """
                            Can only be used once per battle. All entities
                            within 2 squares roll to see if they're poisoned or
                            not.
                            """
                        ),
                        LINASAbility(
                            name = "Fast Acting Pathogen",
                            type = "Passive",
                            description = """
                            Targets you poison take 2 damage from poison per
                            turn instead of 1
                            """
                        )
                    ],
                    items = [
                        LINASItem(
                            name = "Stolen Lab Samples",
                            uses = 1,
                            cost = 0,
                            description = """
                            Samples stolen from the space station's biology lab
                            """
                        ),
                        LINASItem(
                            name = "Galax",
                            uses = 150,
                            cost = 0,
                            description = "Common galactic currency"   
                        )
                    ]
                )
            ]
        )
        #     # Define Classes Here
        #     "classes":[],
        #     # Define Techniques Here
        #     "techniques":[],
        #     # Define Abilities Here
        #     "abilities":[],
        #     # Define Effects Here
        #     "effects":[],
        #     # Define Status Conditions Here
        #     "status_conditions":[],
        #     # Define Items Here
        #     "items":[],
        #     # Define Entities Here
        #     "entities":[]
        # })
       
        
        
        # Define Techniques Here
        # Define Abilities Here
        # Define Effects Here
        # Define Status Conditions Here
        # Define Items Here
        # Define Entities Here