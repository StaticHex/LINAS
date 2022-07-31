"""
Class used to hold and modify data for LINAS' items
"""
from __future__ import print_function, division
from typing import List, Dict, Tuple
import re

class LINASItem:
    def __init__(
        self,
        name            : str,
        description     : str,
        cost            : int,
        damage          : int                 = None,
        damageType      : str                 = "p",
        linkedSkill     : str                 = None,
        range           : int                 = None,
        protection      : int                 = None,
        protectionType  : str                 = "p",
        speedPenalty    : int                 = None,
        uses            : int                 = None,
        notes           : List[str]           = [],
        template        : List[Dict[str,str]] = None
    ) -> None:
        """
        Class used to hold and modify data for LINAS' items

        Parameters
        ----------
        name : `str`
            The name of the item
        description : `str`
            The text description for the item
        cost : `int`
            How many gold coins an item is worth.
        linkedSkill: `str`
            The skill used to roll to use the item (if applicable)
        range : `int`
            Primarily for ranged weapons but not exclusive to them, this
            is how far the item can be thrown/fired
        damage : `int`
            [weapons only] How much base damage the weapon does
        damageType : `str`
            [weapons only] Whether the weapon does physical or magical
            damage
        protection : `int`
            [armor only] How much base damage the armor prevents
        protectionType : `str`
            [armor only] Whether the armor prevents physical or magical
            damage
        speedPenalty : `int`
            [equipment only] A value to deduct from the speed stat while the
            item is equipped
        uses : `int`
            How many times an item can be used before breaking or becoming
            unusable
        notes: `List[str]`
            A list of additional bullet points to list out for a particular item
        template : `List[Dict[str,str]]`
            An (optional) template to expand the item by
        """
        self.name            = name
        self.desc            = re.sub(r'[\ \n]+', ' ', description)
        self.cost            = cost
        self.linkedSkill     = linkedSkill
        self.range           = range
        self.damage          = damage
        self.damageType      = damageType.title()
        self.protection      = protection
        self.protectionType  = protectionType.title()
        self.speedPenalty    = speedPenalty
        self.uses            = uses
        self.notes           = notes
        self.template        = template
    
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
        html = []
        uses = self.uses if self.uses else "-"
        range = self.range if self.range else "-"
        sPen = self.speedPenalty if self.speedPenalty else "-"
        lSkill = self.linkedSkill if self.linkedSkill else "-"
        cost = self.cost if self.cost > 0 else "-"
        styles='width: 37.85%; padding-top: 0px; text-align: right;'
        html += [
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 55%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            f'        <span class="rel" style="{styles}">',
            f'            <strong>Cost:</strong> {cost}',
            '        </span>',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 15%;">',
            f'            <strong>Uses:</strong> {uses}',
            '        </span>',
            '        <span class="rel" style="width: 25%;">',
            f'            <strong>SpeedPenalty:</strong> {sPen}',
            '        </span>',
            '        <span class="rel" style="width: 18%;">',
            f'            <strong>Range:</strong> {range}',
            '        </span>',
            '        <span class="rel" style="width: 34.85%;">',
            f'            <strong>Linked Skill:</strong> {lSkill}',
            '        </span>',            
            '    </div>'
        ]
        if self.damage or self.protection:
            dpLabel = "Damage" if self.damage else "Protection"
            dpValue = self.damage if self.damage else self.protection
            dpType = self.damageType if self.damage else self.protectionType
            html += [
                '    <div class="cont-inner">',
                '        <span class="rel" style="width: 92.85%;">',
                f'            <strong>{dpType} {dpLabel}:</strong> {dpValue}',
                '        </span>',
                '    </div>'
            ]
        html+=[
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 92.85%;">',
            f'            {self.desc}',
            '        </span>',
            '    </div>'
        ]
        if len(self.notes) > 0:
            html += [
                '    <div class="cont-inner">',
                '        <ul>',
            ]
            for note in self.notes:
                html.append(f'            <li>{note}</li>')
            html += [
                '        </ul>',
                '    </div>'
            ]
        html+= [
            '</div>'
        ]
        return html