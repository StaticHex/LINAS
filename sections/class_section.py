"""
Class used to create a section explaining and listing out classes 
(jobs) for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class ClassSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
       Class used to create a section explaining and listing out classes 
       (jobs) for a system

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
        self.__html.append(f'    {self.__contents.single("classes")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            <p>Classes in LINAS can be thought of more as templates rather than 
            hard enforced and certainly do not represent all the choices for
            character creation. Additionally, LINAS does not use classes to
            restrict which types of items an entity can/can't equip and there are
            no real restrictions on this matter. However, there are mechanics
            such as speed penalty which do make it harder for certain classes
            to use certain items/equipment.</p>
            <p>Classes are here to primarily give players an idea of what to
            look for when creating their character and as such any one of the
            classes can be either modified or a new class created if the player
            desires. As always, the DM should work with players when creating
            or changing any classes to ensure that the changes both make sense
            and will also fit in with the campaign.</p>
            <p>In general, classes are meant to be a tool to help guide players
            in creating a character, not a container defining what the player
            can or can't do.</p>
            """
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in skills
        self.__html += [ f'    {x.replace("ZCustom","Custom")}' for x in 
            data.typeToHTMLList('classes')
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