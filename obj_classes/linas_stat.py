"""
Class used to hold and modify data for Kite's stats
"""
from __future__ import print_function, division
from typing import List, Dict
import re

class LINASStat:
    def __init__(
        self,
        name : str,
        abbr : str,
        description : str,
        template : List[Dict[str,str]] = None
    ) -> None:
        """
        Class used to hold and modify data for Kite's stats

        Parameters
        ----------
        name : `str`
            The full name of the stat
        abbr : `str`
            The abbreviation for the stat (usually 3 or 4 letters)
        description : `str`
            The text description for the stat
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        """
        self.name     = name
        self.abbr     = abbr
        self.desc     = re.sub(r'[\ \n]+', ' ', description)
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
            f'<u><strong>{self.name} ({self.abbr})</strong></u> -- {self.desc}'
        ]

# ==============================================================================