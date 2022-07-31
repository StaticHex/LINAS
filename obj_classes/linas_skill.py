"""
Class used to hold and modify data for LINAS' skills
"""
from __future__ import print_function, division
from typing import List, Dict
import re

class LINASSkill:
    def __init__(
        self,
        name : str,
        description : str,
        template : List[Dict[str,str]] = None
    ) -> None:
        """
        Class used to hold and modify data for LINAS' skills

        Parameters
        ----------
        name : `str`
            The name of the skill
        description : `str`
            The text description for the skill
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        """
        self.name = name
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
        return [
            f'<p><u><strong>{self.name}</strong></u> -- {self.desc}<p>'
        ]