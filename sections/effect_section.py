"""
Class used to create a section explaining and listing out skills for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class EffectSection:
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
        self.__html.append(f'    {self.__contents.single("effects & status conditions")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Effects and status conditions are temporary conditions which alter an
            entity's abilities. The effect may be short term, lasting a single battle
            or action; or could be long term, lasting several game sessions. How long
            an effect lasts as well as any specifics needed to get rid of the effect
            are determined by the DM and as always the DM has the freedom to define
            new effects or to modify existing effects as needed.
            """
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in skills
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('effects')
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