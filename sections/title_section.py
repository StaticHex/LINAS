"""
Class used to create title pages for PDF documents
"""
from __future__ import print_function, division
from typing import List
class TitleSection:
    """
    Class used to create title pages for PDF documents

    Parameters
    ----------
    title : `str`
        The title of the document
    author : `str`
        The author who wrote the document
    revision : `float`
        The revision number for the document, if none is provided 1.0 is affixed
    """
    def __init__(
        self,
        title : str,
        author : str,
        revision : float = 1.0,
    ) -> None:
        self.title = title
        self.author = author
        self.revision = f"{revision:3.2f}"
    
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
        return [
            '<div class="title">',
            f'    <h1>{self.title} (v{self.revision})</h1>',
            f'    <h3>Written By: {self.author}</h3>',
            f'</div>'
        ]