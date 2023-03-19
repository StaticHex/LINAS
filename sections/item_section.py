"""
Class used to create a section explaining and listing out items for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
from utils.assets import AssetManager
import os

class ItemSection:
    __am = AssetManager()
    def __init__(
        self,
        system : ContentManager,
        data : DataManager
    ) -> None:
        """
       Class used to create a section explaining and listing out skills for a system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        data : `DataManager`
            The data for the class, needed load in the skills for the section
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        # Build out HTML here
        # ======================================================================
        # = Skills Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("items")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            This section contains a list of items for the system. As with most
            things in the system; this shouldn't be considered an absolute list as
            the DM may choose to add more items or make certain items off limits.

            Unless the DM states otherwise, any items which have a set cost
            associated with them should be considered as valid items to purchase
            during character creation.

            <h3>Weapon Format</h3>
            <div class="container pop">
                <div class="cont-title">
                    <span class="rel" style="width: 30%;">
                        <h4 class="nopad">Item Name</h4>
                    </span>
                    <span class="rel" style="width: 27%; padding-top: 0px;">
                        <strong>Req. Skill:</strong> Skill Name
                    </span>  
                    <span class="rel" style="width: 15%; padding-top: 0px;">
                        <strong>Max Points:</strong> #
                    </span>        
                    <span class="rel" style="width: 18%; text-align: right;">
                        <strong>Cost:</strong> #G
                    </span>
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%; text-align:center;">
                        """+f'{ItemSection.__am.tag("patk")}'+"""
                    </span>
                    <span class="rel" style="width: 10%; text-align:center;">
                        <strong>Range</strong>
                    </span>
                    <span class="rel" style="width: 10%; text-align:center;">
                        <strong>Stat</strong>
                    </span>
                    <span class="rel" style="width: 15%; text-align:center;">
                        """+f'{ItemSection.__am.tag("pen")}'+"""
                    </span>
                    <span class="rel" style="width: 45%;">
                        <strong>Effect(s)</strong>
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%;">
                        # [TYPE]
                    </span>
                    <span class="rel" style="width: 10%; text-align:center;">
                        #
                    </span>
                    <span class="rel" style="width: 10%; text-align:center;">
                        STAT
                    </span>
                    <span class="rel" style="width: 15%; text-align:center;">
                        #
                    </span>
                    <span class="rel" style="width: 45%;">
                        Description of what the item does goes here
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <ul>
                        <li>Notes describing extra effects go here</li>
                    </ul>
                </div>
            </div>
            <ul>
                <li><strong>Item Name</strong> - The name of the weapon</li>
                <li><strong>Req. Skill</strong> - The skill used when rolling to use the weapon</li>
                <li>
                    <strong>Max Points</strong> - The maximum number of modifications which can be made to the weapon
                    for more info about this, see the 'Modifying Equipment' section
                </li>
                <li><strong>Cost</strong> - How much the item costs to purchase (sell price is 1/2 cost)</li>
                <li>
                    """+f'<strong>Damage ({ItemSection.__am.tag("patk")}) [Damage Type] </strong>'+""" - Amount of 
                    damage the weapon does as well as the type of damage it does. Will either be PHYS for physical 
                    or MAG for magical. A weapon can only deal one type of damage.
                </li>
                <li><strong>Range</strong> - How many squares away the weapon can hit it's target</li>
                <li>
                    <strong>Stat</strong> - The stat to use when adding onto the weapon's base damage from attack rolls. 
                </li>
                <li>Speed Penalty """+f'({ItemSection.__am.tag("pen")})'+"""- How much the weapon slows the user
                down when equipped. This can be offset by strength</li>
                <li><strong>Effect(s)</strong> - Description of the item as well as any effects the weapon has</li>
                <li><strong>Notes</strong> - Additional conditions or considerations for using the weapon</li>
            </ul>
            <h3 style="page-break-before: always;">Armor Format</h3>
            <div class="container pop">
                <div class="cont-title">
                    <span class="rel" style="width: 45%;">
                        <h4 class="nopad">Item Name</h4>
                    </span>
                    <span class="rel" style="width: 17.85%; padding-top: 0px;">
                        <strong>Max Points:</strong> #
                    </span>     
                    <span class="rel" style="width: 30%; text-align: right;">
                        <strong>Cost:</strong> #G
                    </span>
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%; text-align: center;">
                        """+f'<strong>{ItemSection.__am.tag("pdef")}</strong>'+"""
                    </span>
                    <span class="rel" style="width: 10%; text-align: center;">
                        """+f'<strong>{ItemSection.__am.tag("mdef")}</strong>'+"""
                    </span>
                    <span class="rel" style="width: 10%; text-align: center; overflow: hidden;">
                        &nbsp;"""+f'{ItemSection.__am.tag("pen")}'+"""&nbsp;
                    </span>
                    <span class="rel" style="width: 60%;">
                        <strong>Effect(s)</strong>
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%; text-align: center;">
                        #
                    </span>
                    <span class="rel" style="width: 10%; text-align: center;">
                        #
                    </span>
                    <span class="rel" style="width: 10%; text-align: center;">
                        #
                    </span>
                    <span class="rel" style="width: 60%; text-align: left;">
                        Description of what the item does goes here
                    </span>
                    <hr style="border: 1px solid #dddddd; text-align: center;">
                </div>
                <div class="cont-inner">
                    <ul>
                        <li>Notes describing extra effects go here</li>
                    </ul>
                </div>
            </div>
            <ul>
                <li><strong>Item Name</strong> - The name of the armor</li>
                <li>
                    <strong>Max Points</strong> - The maximum number of modifications which can be made to the armor
                    for more info about this, see the 'Modifying Equipment' section
                </li>
                <li><strong>Cost</strong></li> - How much the item costs to purchase (sell price is 1/2 cost)</li>
                <li>"""+f'<strong>Physical Defense ({ItemSection.__am.tag("pdef")})</strong>'+""" - Amount of physical damage the armor can absorb.</li>
                <li>"""+f'<strong>Magic Defense({ItemSection.__am.tag("mdef")})</strong>'+""" - Amount of magical damage the armor can absorb.</li>
                <li>Speed Penalty """+f'({ItemSection.__am.tag("pen")})'+"""- How much the armor slows the user
                down when equipped. This can be offset by strength</li>
                <li><strong>Effect(s)</strong> - What the technique does when used</li>
                <li><strong>Notes</strong> - Additional conditions or considerations for using the technique
            </ul>
            <h3>General Item Format</h3>
            <div class="container pop">
                <div class="cont-title">
                    <span class="rel" style="width: 45%;">
                        <h4 class="nopad">Item Name</h4>
                    </span>
                    <span class="rel" style="width: 47.85%; text-align: right;">
                        <strong>Cost:</strong> #G
                    </span>     
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%; text-align: center;">
                        <strong>Uses</strong>
                    </span>
                    <span class="rel" style="width: 10%; text-align: center;">
                        <strong>Range</strong>
                    </span>
                    <span class="rel" style="width: 70%; text-align: left;">
                        <strong>Effect(s)</strong>
                    </span>
                    <hr style="border: 1px solid #dddddd;">
                </div>
                <div class="cont-inner">
                    <span class="rel" style="width: 10%; text-align: center;">
                        #
                    </span>
                    <span class="rel" style="width: 10%; text-align: center;">
                        #
                    </span>
                    <span class="rel" style="width: 70%; text-align: left;">
                        Description of what the item does goes here
                    </span>
                    <hr style="border: 1px solid #dddddd; text-align: center;">
                </div>
                <div class="cont-inner">
                    <ul>
                        <li>Notes describing extra effects go here</li>
                    </ul>
                </div>
            </div>
            <ul>
                <li><strong>Item Name</strong> - The name of the item</li>
                <li><strong>Cost</strong> - How much the item costs to purchase (sell price is 1/2 cost)</li>
                <li><strong>Uses</strong> - Items with charges only, this is the number of charges the item has before being used up.</li>
                <li><strong>Range</strong> - How far away the item can be used.</li>
                <li><strong>Effect(s)</strong> - What the technique does when used</li>
                <li><strong>Notes</strong> - Additional conditions or considerations for using the technique
            </ul>
            <h3>Modifying Equipment</h3>
            Equipment is typically modified up through crafting of some kind. Although
            there may be other ways equipment is modified is well depending on the DM.

            Each piece of equipment has a certain maximum number of points associated with 
            it representing the maximum number of modifications a piece of equipment can have. 
            The following aspects of a weapon or piece of armor can be modified.
            WEAPONS:
            <ul>
                <li><b>Damage</b> - 1 point = damage +1 (cannot modifiy a damage of -)</li>
                <li><b>Range</b> - 1 point = range +1 (cannot modify a range of -)</li>
                <li><b>Speed Penalty """+f'({ItemSection.__am.tag("pen")})'+"""</b> - 1 point = -1 to penalty (cannot modify, - or 0)</i>
            </ul>
            ARMOR:
            <ul>
                <li><b>Physical Protection """+f'({ItemSection.__am.tag("pdef")})'+"""</b> - 1 point = physical protection +1 (cannot modifiy a damage of -)</li>
                <li><b>Magical Protection """+f'({ItemSection.__am.tag("mdef")})'+"""</b> - 1 point = magical protection +1 (cannot modify a range of -)</li>
                <li><b>Speed Penalty """+f'({ItemSection.__am.tag("pen")})'+"""</b> - 1 point = -1 to penalty (cannot modify, - or 0)</i>
            </ul>
            As with everything in this system, these are not the only things which can be
            improved. There may be campaign specific modifications or other modifications
            not listed here which the DM chooses to allow the player to do. As always, it's
            up to the DM and players to work out what exactly about the equipment in question 
            can be modified but the above are good guidelines if you're not sure where to start.
            """
        )]

        # Page break
        self.__html.append(f'    {system.pageBreak()}')

        # Load in skills
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('items')
        ]

        self.__html += [ f'    {x}' for x in system.collapse(
            """
            <h3 style="page-break-before: always;">Creating Custom Items</h3>
            Items are probably one of the areas which will receive custom entries most often. 
            Whether it's a simple flavor item to round out a custom character or a tool or 
            piece of armor relating to a custom class. Items are for the most part much easier
            to work into place. That being said, like with techniques; there are a few
            guidelines regarding modification points for weapons and armor. Once again these
            are not hard set rules and are simply the guidelines used on the items in this
            book.<br/><br/>WEAPONS:
            <ol>
                <li>Start with 5 modification points. This is the maximum number of points allowed.</li>
                <li>Subtract 1 level for every 2 damage done</li>
                <li>If weapon deals magic damage, subtract 1 level</li>
                <li>If weapon is enchanted, subtract 2 levels</li>
                <li>Add 1 level for every 2 points in speed penalty</li>
            </ol><br/>ARMOR:
            <ol>
                <li>Start with 5 modification points. This is the maximum number of points allowed.</li>
                <li>Subtract 1 level for every 2 protection (Add together magic and physical protection for this)</li>
                <li>If armor is enchanted, subtract 2 levels</li>
                <li>Add 1 level for every 2 points in speed penalty</li>
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