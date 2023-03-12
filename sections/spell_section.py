"""
Class used to create a section explaining and listing out abilities for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class SpellSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
        Class used to create a section explaining and listing out spells and 
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

        # Build out HTML here
        # ======================================================================
        # = Spell Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("spells & battle skills")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Spells and battle skills can be thought of as special abilities which entities
            can use to attack with in lieu of weapons. Additionally, spells can be
            improved by studying or training and provide an additional way to strengthen 
            one's character. 

            Like most of the system, the spell system has been purposely kept fairly
            barebones and there are no formal weaknesses or resistances. That being said,
            the players and the DM should definitely discuss if a scenario arises which
            could constitute an advantage for extra damage

            <i>Example 1:
            The party is fighting a tree monster. One of the players is a mage and unleashes
            a fire spell. The mage points out that they're using fire on a tree. The DM
            agrees this would be effective and awards and extra 2 points of damage
            </i>

            <i>Example 2:
            The party has been caught in a thunder storm. The party's mage casts thunder.
            The mage asks the DM if there's a bonus for using thunder in a thunderstorm. The
            DM allows the mage to target 2 additional people with the spell as a bonus
            </i>

            <h3>Spell Format</h3>
            <div class="container pop">
                <div class="cont-title">
                    <span class="rel" style="width: 75%;">
                        <h4 class="nopad">Spell Name</h4>
                    </span>
                    <span class="rel" style="width: 10%;">
                        <strong>Range:</strong> #
                    </span>
                    <span class="rel" style="width: 10%; padding-top: 0px; padding-right: 0px; text-align: right;">
                        <text class="nopad">(1~#)<strong>&#9734;</strong></text>
                    </span>
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%;"><strong>Damage</strong></span>
                    <span class="rel" style="width: 10%;"><strong>MP Cost</strong></span>
                    <span class="rel" style="width: 20%;"><strong>Req. Skill</strong></span>
                    <span class="rel" style="width: 50%; text-align: right;"><strong>Effect(s)</strong></span>
                    <span class="rel" style="width: 10%;">#</span>
                    <span class="rel" style="width: 10%;"># MP</span>
                    <span class="rel" style="width: 20%;">Skill Name</span>
                    <span class="rel" style="width: 50%; text-align: right;">The effect the spell has</span>
                </div>
            </div>
            <h3>Leveling Up Spells</h3>

            Spells are typically leveled up through training or studying. The exact
            amount of time needed for a spell to level up is up to the DM.
            Additionally, the DM can decide to have the player roll to level up.
            one nice idea when rolling to level up and to keep things from getting
            to stale is to add a bonus of some kind if the player rolls a 6. 

            Each spell has a certain maximum level associated with it denoted by a series of &#9734;. 
            This level denotes the maximum number of modifications a spell can have. The following
            aspects of a spell can be modified.
            <ul>
                <li><b>Damage</b> - 1 point = damage +1 (cannot modifiy a damage of -)</li>
                <li><b>MP Cost</b> - 1 point = MP Cost -1 (can go down to 0)</li>
                <li><b>Range</b> - 1 point = range +1 (cannot modify a range of -)</li>
                <li><b>Targets</b> - 1 point = targets +1 (cannot modify, self, or -)</i>
            </ul>
            As with everything in this system, these are not the only things which can be
            improved. There may be campaign specific modifications or other modifications
            not listed here which the DM chooses to allow the player to do. As always, it's
            up to the DM and players to work out what 'leveling up' means but the above are
            good guidelines if you're not sure where to start.
            <h3>Forgetting Spells</h3>

            Forgetting spells is much less involved than forgetting skills. You simply strike
            through or cross out the spell from your spellbook (something to indicate you no
            longer know that spell). However, before forgetting a spell it should be noted that
            once forgotten, all the time spent training that spell will be lost. If you decide
            to re-learn the spell at a later time; you will have to start from scratch.
            """
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in spells
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('spells')
        ]

        # Suffix
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            <h3>Creating Custom Spells</h3>

            Like most aspects of the system, spell creation is completely open and the system
            kind of assumes that at some point there will be a need to create some spell the
            system doesn't support. With that in mind, there are a few recommended guidelines
            designed to keep spells from becoming too powerful. It is largely up to the DM
            to enforce these and they are certainly not mandatory. However, if a player or
            the DM are unsure of how to go about creating a custom spell, these are certainly
            good guidelines to follow.
            
            <h4>Guidelines for Calculating Custom Spell MP</h4>

            The set of guidelines below were used to calculate the MP cost for all the spells
            in this guidebook. Keeping close to these guidelines should ensure your spells
            are fairly balanced as a large amount of testing went into refining them. However,
            as always these are just in fact guidelines not hard set rules and the players and
            DM should feel free to tweak custom spells as needed.

            <ol>
                <li>
                    Start by computing base spell cost by taking 1/2 of damage done by spell 
                    (rounded up) 
                </li>
                <li>
                    +1 MP if the spell causes or heals a status effect. To keep things simple
                    it's suggested limiting each spell to a single status effect.
                </li>
                <li>
                    +1 MP for each square of range > 3 and -1 MP for each square of range < 3.
                </li>
                <li>
                    +1 MP for every target past the first
                </li>
                <li>
                    -1 MP if spell targets both friends and foes alike
                </li>
                <li>
                    +3 MP if spell targets entire field or targets an area
                </li>
            </ol>

            <h4>Guidelines for Calculating Custom Spell Max Level</h4>

            Spell levels are used to denote the maximum number of times a spell can be
            modified. For more information on what spell modifications are check the
            guide at the beginning of the spell section. The guidelines below are the
            guidelines all the spells in this guide where generated with. It is recommended
            to try and stay as close as possible to said guidelines. However, if the
            number of modifications doesn't make sense or feels under or overwhelming, 
            feel free to modify it.            

            <ol>
                <li>Start by assigning a base max level of 5</li>
                <li>-1 level for every 2 damage</li>
                <li>-1 level if spell causes a status effect or heals a status effect</li>
                <li>-3 levels if range targets entire field or an area</li>
                <li>
                    -1 level for each square of range > 3 and +1 level for each square of
                    range < 3. <i>Number of levels cannot exceed 5</i>
                </li>
                <li>+1 level if spell targets friend and foe</li>
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