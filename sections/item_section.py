"""
Class used to create a section explaining and listing out items for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class ItemSection:
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
            """
        )]

        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in skills
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('items')
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