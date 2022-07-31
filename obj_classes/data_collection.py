"""
Class used to organize data in the LINAS system by type
"""
from __future__ import print_function, division
from typing import List, Any
import copy

class DataCollection:
    def __init__(
        self,
        name : str,
        description : str,
        children : List[Any]
    ) -> None:
        # Copy parameters to class vars
        self.name = name
        self.desc = description
        # create map of children
        self.__children = {}
        self.__indent = "&emsp;"*3
        for child in children:
            if child.template == None:
                self.__children[child.name.lower()] = child
            else:
                for element in child.template:
                    ch = copy.deepcopy(child)
                    ch.name = ch.name.format(**element)
                    ch.desc = ch.desc.format(**element)
                    self.__children[ch.name.lower()] = copy.deepcopy(ch)
    
    def getChild(self, name):
        if name.lower() in self.__children:
            return self.__children[name.lower()]
        return None

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
        html = [
            '<p style="page-break-before: always;"><p/>'
            f"<u><h3>{self.name}</h3></u>",
            f"<p>{self.__indent}{self.desc}</p>",
        ]
        for key in sorted(self.__children):
            html += self.__children[key].toHTMLList()
        return html
    