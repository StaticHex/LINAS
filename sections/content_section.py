"""
Class used to create a table of contents for a pdf document
"""
from __future__ import print_function, division
from typing import List

class ContentSection:
    def __init__(
        self,
        contentList : List[str]
    ) -> None:
        """
        Class used to create a table of contents for a pdf document

        Parameters
        ----------
        contentList : `List[str]`
            A list of sections for the table of contents
        """
        self.contentList = contentList
        self.__contentMap = {}

        # Map number to content name here
        for i, c in enumerate(self.contentList):
            self.__contentMap[c.lower()] = i+1
    
    def single(
        self,
        name : str
    ) -> str:
        """
        Returns a single content item formatted as a title line

        Parameters
        ----------
        name : `str`
            The content item to search for

        Returns
        -------
        html : `str`
            A single HTML tag containing the content item's name and number
        """
        num = self.__contentMap[name.lower()]
        return f'<h2>{num}. {name.title()}</h2>'

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
        # Start HTML
        html = [
            '<div class="section">',
            '    <h2>Table Of Contents</h2>',
            '    <ol>'
        ]
        # Add contents
        for c in self.contentList:
            html.append(f'        <h3 class="nopad"><li>{c}</li></h3>')

        # Finalize HTML and return
        html += [
            '    </ol>',
            '</div>'
        ]
        return html