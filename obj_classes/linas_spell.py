"""
Class used to hold and modify data for LINAS' spells
"""
from __future__ import print_function, division
from typing import List, Dict
import re

class LINASSpell:
    def __init__(
        self,
        name        : str,
        description : str,
        damage      : int,
        cost        : int,
        range       : int,
        points      : int,
        numTargets  : int,
        targetType  : str,
        element     : str = "null",
        notes       : List[str] = [],
        template    : List[Dict[str,str]] = None
    ) -> None:
        """
        Class used to hold and modify data for LINAS' spells

        Parameters
        ----------
        name : `str`
            The name of the spell
        description : `str`
            The text description for the spell
        damage : `int`
            The amount of damage the spell does
        cost : `int`
            The MP cost for the spell
        range : `int`
            The range of the spell
        points : `int`
            The number of points the spell has available for upgrades
        numTargets : `int`
            The number of entities a single casting of the spell can target at
            once
        targetType : `int`
            The type of target the spell can target. Valid values are entity, 
            all, hostile, friendly, and area [1-2].
        element : `str`
            The element the spell is
        notes : `List[str]`
            List of notes about the spell
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        """
        self.name       = name
        self.desc       = re.sub(r'[\ \n]+', ' ', description)
        self.damage     = damage
        self.cost       = cost
        self.range      = range
        self.points     = points
        self.numTargets = numTargets
        self.targetType = targetType
        self.element    = element
        self.notes      = notes
        self.template   = template
    
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