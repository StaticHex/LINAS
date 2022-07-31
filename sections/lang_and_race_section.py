"""
Class used to create a section explaining and listing out skills for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os
import re

class LangRaceSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
       Class used to create a section explaining and listing out languages and
       races for a system

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
        # = Languages & Races Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("languages & races")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            LINAS includes several races to choose from . Some are traditional
            fantasy tropes such as elves and dwarves and some such as the Mu are
            unique to LINAS itself. This is also the place where languages are
            defined as they tie in with race. By default; races generally only
            know the languages corresponding to their class. However, a player
            can choose to assign more languages to their character so long as
            the character knowing that language makes sense in the context of
            their experience and background and also so long as it's OK with
            the DM.
            """
        )]
        self.__html.append("""<u><h3>Languages</h3></u>""")
        
        # Load in languages
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('languages')
        ]
        self.__html.append("""
        <u><h3 style="page-break-before: always;">Races</h3></u>
        """)
        self.__html += [ f'    {x.replace("ZCustom","Custom")}' for x in 
            data.typeToHTMLList('races')
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