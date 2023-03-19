"""
Class used to create a section explaining and listing out abilities for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
from utils.assets import AssetManager
import os

class TechniqueSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
        Class used to create a section explaining and listing out techniques and 
        battle abilities for a system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        data : `DataManager`
            The data for the class, needed load in the abilities for the section
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        am = AssetManager()
        icon = 'style="height: 16px; width: auto;"'

        # Build out HTML here
        # ======================================================================
        # = Spell Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("techniques")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Spells and battle skills can be thought of as special abilities which entities
            can use to attack with in lieu of weapons. Additionally, techniques can be
            improved by studying or training and provide an additional way to strengthen 
            one's character. 

            Like most of the system, the technique system has been purposely kept fairly
            barebones and there are no formal weaknesses or resistances. That being said,
            the players and the DM should definitely discuss if a scenario arises which
            could constitute an advantage for extra damage

            <i>Example 1:
            The party is fighting a tree monster. One of the players is a mage and unleashes
            a fire technique. The mage points out that they're using fire on a tree. The DM
            agrees this would be effective and awards and extra 2 points of damage
            </i>

            <i>Example 2:
            The party has been caught in a thunder storm. The party's mage uses a thunder technique.
            The mage asks the DM if there's a bonus for using thunder in a thunderstorm. The
            DM allows the mage to target 2 additional people with the technique as a bonus
            </i>
            <div class="container pop">
                <div class="cont-title">
                    <span class="rel" style="width: 30%;">
                        <h4 class="nopad">Technique Name</h4>
                    </span>
                    <span class="rel" style="width: 25%">
                        <strong> Req. Skill:</strong> Skill Name
                    </span>
                    <span class="rel" style="width: 20%">
                        <strong> Req. Stat:</strong> STAT
                    </span>
                    <span class="rel" style="width: 15%; padding-top: 0px; text-align: right;">
                        <strong>Max Points:</strong> #
                    </span>            
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%;">
                        """+f'<strong><img src="{am.get("atk")}" {icon}"/></strong>'+"""
                    </span>
                    <span class="rel" style="width: 10%;">
                        """+f'<strong><img src="{am.get("tp")}" {icon}"/></strong>'+"""
                    </span>
                    <span class="rel" style="width: 10%;">
                        <strong>Range</strong>
                    </span>
                    <span class="rel" style="width: 10%;">
                        <strong>Targets</strong>
                    </span>
                    <span class="rel" style="width: 50%; text-align: left;">
                        <strong>Effect(s)</strong>
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%;">
                        #
                    </span>
                    <span class="rel" style="width: 10%;">
                        #
                    </span>
                    <span class="rel" style="width: 10%;">
                        #
                    </span>
                    <span class="rel" style="width: 10%;">
                        #
                    </span>
                    <span class="rel" style="width: 50%; text-align: left;">
                        Description of technique goes here
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <ul>
                        <li>Notes appear here</li>
                    </ul>
                </div>
            </div>
            <ul>
                <li><strong>Technique Name</strong> - The name of the technique</li>
                <li><strong>Req. Skill</strong> - The skill used when rolling to see if the technique hits</li>
                <li><strong>Req. Stat</strong> - The stat used to add damage to the technique's damage</li>
                <li>
                    <strong>Max Points</strong> - The maximum number of modifications which can be made to the technique
                    for more info about this, see the 'Leveling Up Techniques' section
                </li>
                <li>"""+f'<strong><img src="{am.get("atk")}" {icon}"/></strong>'+""" - Amount of damage the technique does.</li>
                <li>"""+f'<strong><img src="{am.get("tp")}" {icon}"/></strong>'+""" - How much TP the technique costs to use.</li>
                <li><strong>Range</strong> - How many squares away the technique can hit it's target</li>
                <li>
                    <strong>Targets</strong> - How many entities a single use of the technique can target at one time. 
                    If the target specifies 'self' the user can only use the technique on themselves. 
                    If the target specifies 'field' ALL entities must roll to see if the technique hits.
                </li>
                <li><strong>Effect(s)</strong> - What the technique does when used</li>
                <li><strong>Notes</strong> - Additional conditions or considerations for using the technique
            </ul>
            <h3>Leveling Up Techniques</h3>

            Spells are typically leveled up through training or studying. The exact
            amount of time needed for a technique to level up is up to the DM.
            Additionally, the DM can decide to have the player roll to level up.
            one nice idea when rolling to level up and to keep things from getting
            to stale is to add a bonus of some kind if the player rolls a 6. 

            Each technique has a certain maximum level associated with it denoted by a series of &#9734;. 
            This level denotes the maximum number of modifications a technique can have. The following
            aspects of a technique can be modified.
            <ul>
                <li><b>Damage</b> - 1 point = damage +1 (cannot modifiy a damage of -)</li>
                <li><b>TP Cost</b> - 1 point = TP Cost -1 (can go down to 0)</li>
                <li><b>Range</b> - 1 point = range +1 (cannot modify a range of -)</li>
                <li><b>Targets</b> - 1 point = targets +1 (cannot modify, self, or -)</i>
            </ul>
            As with everything in this system, these are not the only things which can be
            improved. There may be campaign specific modifications or other modifications
            not listed here which the DM chooses to allow the player to do. As always, it's
            up to the DM and players to work out what 'leveling up' means but the above are
            good guidelines if you're not sure where to start.
            <h3>Forgetting Techniques</h3>

            Forgetting techniques is much less involved than forgetting skills. You simply strike
            through or cross out the technique from your skill book (something to indicate you no
            longer know that technique). However, before forgetting a technique it should be noted that
            once forgotten, all the time spent training that technique will be lost. If you decide
            to re-learn the technique at a later time; you will have to start from scratch.
            """
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in techniques
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('techniques')
        ]

        # Suffix
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            <h3>Creating Custom Techniques</h3>

            Like most aspects of the system, technique creation is completely open and the system
            kind of assumes that at some point there will be a need to create some technique the
            system doesn't support. With that in mind, there are a few recommended guidelines
            designed to keep techniques from becoming too powerful. It is largely up to the DM
            to enforce these and they are certainly not mandatory. However, if a player or
            the DM are unsure of how to go about creating a custom technique, these are certainly
            good guidelines to follow.
            
            <h4>Guidelines for Calculating Custom Technique TP</h4>

            The set of guidelines below were used to calculate the TP cost for all the techniques
            in this guidebook. Keeping close to these guidelines should ensure your techniques
            are fairly balanced as a large amount of testing went into refining them. However,
            as always these are just in fact guidelines not hard set rules and the players and
            DM should feel free to tweak custom techniques as needed.

            <ol>
                <li>
                    Start by computing base technique cost by taking 1/2 of damage done by technique 
                    (rounded up) 
                </li>
                <li>
                    +1 TP if the technique causes or heals a status effect. To keep things simple
                    it's suggested limiting each technique to a single status effect.
                </li>
                <li>
                    +1 TP for each square of range > 3 and -1 TP for each square of range < 3.
                </li>
                <li>
                    +1 TP for every target past the first
                </li>
                <li>
                    -1 TP if technique targets both friends and foes alike
                </li>
                <li>
                    +3 TP if technique targets entire field or targets an area
                </li>
            </ol>

            <h4>Guidelines for Calculating Custom Spell Max Level</h4>

            Spell levels are used to denote the maximum number of times a technique can be
            modified. For more information on what technique modifications are check the
            guide at the beginning of the technique section. The guidelines below are the
            guidelines all the techniques in this guide where generated with. It is recommended
            to try and stay as close as possible to said guidelines. However, if the
            number of modifications doesn't make sense or feels under or overwhelming, 
            feel free to modify it.            

            <ol>
                <li>Start by assigning a base max level of 5</li>
                <li>-1 level for every 2 damage</li>
                <li>-1 level if technique causes a status effect or heals a status effect</li>
                <li>-3 levels if range targets entire field or an area</li>
                <li>
                    -1 level for each square of range > 3 and +1 level for each square of
                    range < 3. <i>Number of levels cannot exceed 5</i>
                </li>
                <li>+1 level if technique targets friend and foe</li>
            </ol>
            """
        )]

        self.__html.append('</div>')

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