"""
Class used to create a section explaining and listing out abilities for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class AbilitySection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
       Class used to create a section explaining and listing out abilities for a system

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
        # = Abilities Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("abilities")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Abilities can be thought of as extra perks or advantages which make
            a character unique or give a character an edge over other characters
            in certain situations. Generally speaking, everyone starts the game
            with at least 2 abilities due to their race. As a general rule and
            to keep any one character from getting too overpowered A character
            is limited to 3 abilities. However, in an effort to keep characters
            dynamic, abilities can be forgotten similar to techniques. For more on
            this see the section labeled "Forgetting Abilities" at the end of
            this section
            <h3>Forgetting Abilities</h3>

            Like techniques, abilities can be forgotten by striking through them,
            crossing them out or otherwise marking them as forgotten in some way.
            This is done to keep characters flexible. Additionally, unlike techniques;
            abilities don't really level up so there's less of a penalty for
            forgetting them. This being said, the DM may attach conditions to
            learning certain abilities and so like techniques, when an ability is
            forgotten it should be assumed that re-learning that ability will result
            in relearning from scratch.
            <h3>Creating Custom Abilities</h3>
            
            Like most aspects of the system, if there is a particular ability a
            player wants for their character; the DM and that player should work
            together to make that ability a reality. That being said there are a few
            suggestions for creating abilities to keep the game balanced and as
            always the DM may add to or override any of the suggested rules below:
            <ul>
                <li>
                    If the ability is an active ability, it is recommended to limit the
                    number of uses a character can use that ability per session. Most
                    active abilities can only be used once. However, this is not a
                    steadfast rule and there may be times when an active ability can
                    be permitted to be used multiple times per rest period or may
                    recharge under completely different circumstances.
                </li><br/>
                <li>
                    If a passive ability gives an advantage under certain conditions
                    e.g. weather, location, using certain types of magic, etc. It is
                    recommended that the ability give a proportional disadvantage under
                    some other condition. For example, if the character gets a +2 to
                    speed when the weather is sunny, give the character -2 to speed
                    when it's raining.
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
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in skills
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('abilities')
        ]
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