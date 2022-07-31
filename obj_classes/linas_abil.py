"""
Class used to hold and modify data for LINAS' skills
"""
from __future__ import print_function, division
from typing import List, Dict
import re

class LINASAbility:
    def __init__(
        self,
        name : str,
        type : str,
        description : str,
        template: List[Dict[str,str]] = None
    ) -> None:
        """
        Class used to hold and modify data for LINAS' abilities

        Parameters
        ----------
        name : `str`
            The name of the ability
        type : `str`
            Either a for active or p for passive, used to get css 
            class name
        description : `str`
            The text description for the ability
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        """
        self.name = name
        self.type = type.lower()[0]
        self.desc = re.sub(r'[\ \n]+', ' ', description)
        self.template = template
    
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
        indent = "&emsp;"*3
        return [
                f'<div class="container">',
                f'    <div class="{self.type}-abil-title cont-inner">',
                f'        <strong>{self.name}</strong>',
                f'    </div>',
                f'    <div class="cont-inner">',
                f'        {indent}{self.desc}',
                f'    </div>',
                f'</div>'
            ]
