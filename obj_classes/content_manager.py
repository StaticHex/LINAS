"""
Super class used to initialize classes responsible for holding and managing the
data for a given system (techniques, items, enemies, etc.)
"""
from __future__ import print_function, division
from sections.title_section import TitleSection
from sections.content_section import ContentSection
from typing import List

class ContentManager:
    """
    Super class used to initialize classes responsible for holding and managing
    the data for a given system (techniques, items, enemies, etc.)

    Parameters
    ----------
    title : `str`
        The title of the document
    author : `str`
        The author who wrote the document
    contents : `List[str]`
        A list of contents to send into the section
    revision : `float`
        The revision number for the document, if none is provided 1.0 is affixed
    """
    def __init__(
        self,
        title : str,
        author : str,
        contents : List[str],
        revision : float = 1.0
    ) -> None:
        # Set up title
        self.__title = TitleSection(
            title,
            author,
            revision
        )

        # Begin initializing HTML list for class
        self.__html = self.__title.toHTMLList()

        # Initialize contents
        self.__contents = ContentSection(
            contents
        )

        # Add contents to HTML list
        self.__html += self.__contents.toHTMLList()

        self.__indent = "&emsp;"*3
        self.__page = '<p style="page-break-before: always;"><p/>'
    
    def pageBreak(self):
        """
        Used to create a page break in HTML content

        Returns
        -------
        pageBreakTag : `str`
            An HTML tag containing a page break
        """
        return self.__page

    def collapse(
        self, 
        stringToCollapse : str
    ) -> List[str]:
        """
        Collapses string into a series of <p> tags

        Parameters
        ----------
        stringToCollapse : `str`
            The string to collapse
        
        Returns
        -------
        collapsed : `List[str]`
            Formatted list of <p> tags
        """
        collapsed = []
        par = f'<p>{self.__indent}'
        lines =  [ x.strip() for x in stringToCollapse.strip().split('\n') ]
        for line in lines:
            if line == "":
                par = f'{par.strip()}</p>'
                collapsed.append(par)
                par = f'<p>{self.__indent}'
            else:
                par += f'{line} '
        if par != f'<p>{self.__indent}':
            par = f'{par.strip()}</p>'
            collapsed.append(par)
        return collapsed

    def getContents(self):
        """
        Used to access table of contents data for the class
        """
        return self.__contents

    def addContent(
        self,
        content
    ) -> None:
        """
        Expand out a section and add to internal HTML

        Parameters
        ----------
        content : `Section`
            The content to add to the internal html
        """
        self.__html += content.toHTMLList()

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
