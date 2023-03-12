"""
Class used to hold and modify data for LINAS' spells
"""
from __future__ import print_function, division
from typing import List, Dict
import re
from math import ceil

class LINASSpell:
    def __init__(
        self,
        name        : str,
        description : str,
        damage      : int,
        range       : int,
        numTargets  : int,
        skill       : str,
        status      : bool = False, # inflicts status condition
        aoe         : bool = False, # Targets whole field
        fnf         : bool = False, # Targets friend and foe
        points      : int = -1,
        cost        : int = -1,
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
        self.skill      = skill
        self.desc       = re.sub(r'[\ \n]+', ' ', description)
        self.damage     = damage
        self.cost       = cost
        self.range      = range
        self.points     = points
        self.numTargets = numTargets
        self.notes      = notes
        self.template   = template

        if self.cost == -1:
            self.cost = ceil(self.damage / 2)
            if status:
                self.cost += 1
            if aoe:
                self.cost += 3
            else:
                self.cost += (self.range - 3)
            self.cost += self.numTargets - 1
            if fnf:
                self.cost -= 1
            if self.cost < 1:
                self.cost = 1
            
        if self.points == -1:
            self.points = 5
            self.points -= self.damage // 2
            if aoe:
                self.points -= 3
            else:
                self.points -= (self.range - 3)
            if status:
                self.points -= 1
            if fnf:
                self.points += 1
            if self.points > 5:
                self.points = 5
    
        if numTargets == 0:
            if aoe:
                self.numTargets = '-'
            else:
                self.numTargets = 'self'


    
    def __formatField(self, value : int, replacement : str = '-'):
        return value if value > 0 else replacement
    
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
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 45%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 30%">',
            f'            <strong> Req. Skill:</strong> {self.skill.title()}',
            '        </span>',
            '        <span class="rel" style="width: 17.85%; padding-top: 0px; text-align: right;">',
            '            {points}'.format(points=self.points*"&nbsp;&#9734;"),
            '        </span>',            
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%;">',
            '            <strong>Damage</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            '            <strong>MP Cost</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            '            <strong>Range</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            '            <strong>Targets</strong>',
            '        </span>',
            '        <span class="rel" style="width: 50%; text-align: left;">',
            '            <strong>Effect(s)</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%;">',
            '            {damage}'.format(damage=self.__formatField(self.damage)),
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            '            {mpCost}'.format(mpCost=self.__formatField(self.cost)),
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            '            {range}'.format(range=self.__formatField(self.range)),
            '        </span>',
            '        <span class="rel" style="width: 10%;">',
            f'            {self.numTargets}',
            '        </span>',
            '        <span class="rel" style="width: 50%; text-align: left;">',
            f'            {self.desc}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <ul>',
        ]
        for note in self.notes:
            html.append(f'            <li>{note}</li>')
        html += [
            '        </ul>',
            '    </div>'
            '</div>'
        ]
        return html
        #return [
        #    f'<p><u><strong>{self.name}</strong></u> -- {self.desc}<p>'
        #]