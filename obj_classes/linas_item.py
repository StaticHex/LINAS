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
        p_damage        : int                 = None,
        m_damage        : int                 = None,
        linkedSkill     : str                 = None,
        range           : int                 = None,
        p_protection    : int                 = None,
        m_protection    : int                 = None,
        stat            : str                 = None,
        speedPenalty    : int                 = None,
        uses            : int                 = None,
        enchanted       : bool                = False,
        artifact        : bool                = False,
        notes           : List[str]           = [],
        template        : List[Dict[str,str]] = None,
        points          : int                 = -1,
        equippable      : bool                = False
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
        p_damage : `int`
            [weapons only] How much base physical damage the weapon does
        m_damage : `int`
            [weapons only] How much base magical damage the weapon does
        stat : `str`
            [weapons only] Stat the weapon uses for damage
        p_protection : `int`
            [armor only] How much base physical damage the armor prevents
        m_protection : `int`
            [armor only] How much base physical damage the armor prevents
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
        self.p_damage        = p_damage
        self.m_damage        = m_damage
        self.p_protection    = p_protection
        self.m_protection    = m_protection
        self.stat            = stat
        self.speedPenalty    = speedPenalty
        self.uses            = uses
        self.notes           = notes
        self.template        = template
        self.points          = points
        self.equippable      = equippable

        if self.points == -1:
            if artifact or not self.equipment():
                self.points = 0
            else:
                self.points = 5
                self.points -= self.equipment() // 2
                if self.m_damage or m_protection:
                    self.points -= 1
                if enchanted:
                    self.points -= 2
                if speedPenalty:
                    self.points += speedPenalty // 2
            if self.points > 5:
                self.points = 5
    

    def damage(self):
        return self.p_damage or self.m_damage
    
    def formattedCost(self):
        if self.cost > 0:
            return f'{self.cost:,}G'
        return '-'

    def damageType(self):
        if self.m_damage:
            return 'Magical'
        else:
            return 'Physcial'
    
    def protection(self):
        if self.p_protection and self.m_protection:
            return max(self.p_protection, self.m_protection)
        return self.p_protection or self.m_protection
    
    def equipment(self):
        return self.protection() or self.damage()

    def __formatField(self, value : int, replacement : str = '-'):
        if value == None:
            return replacement
        return value if value > 0 else replacement
    
    def __weaponToHtmlList(self):
        html = [
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 45%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 30%;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',
            '        <span class="rel" style="width: 17.85%; padding-top: 0px; text-align: right;">',
            '            {points}'.format(points=self.points*"&nbsp;&#9734;"),
            '        </span>',            
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 15%; text-align: center;">',
            '            <strong>Req. Skill</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            '            <strong>Damage</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            '            <strong>Range</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            '            <strong>Stat</strong>',
            '        </span>',
            '        <span class="rel" style="width: 15%; text-align: center;">',
            '            <strong>D. Type</strong>',
            '        </span>',
            '        <span class="rel" style="width: 25%; text-align: center;">',
            '            <strong>Speed Penalty</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 15%; text-align: center;">',
            f'            {self.linkedSkill.title()}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.damage()}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.range}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.stat.title()}',
            '        </span>',
            '        <span class="rel" style="width: 15%; text-align: center;">',
            f'            {self.damageType().title()}',
            '        </span>',
            '        <span class="rel" style="width: 25%; text-align: center;">',
            f'            {self.__formatField(self.speedPenalty)}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd; text-align: center;">',
            '    </div>',
            '    <div class="cont-inner">',
            f'        <strong>Effect(s):</strong>{self.desc}',
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
    
    def __armorToHtmlList(self):
        html = [
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 45%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 30%;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',
            '        <span class="rel" style="width: 17.85%; padding-top: 0px; text-align: right;">',
            '            {points}'.format(points=self.points*"&nbsp;&#9734;"),
            '        </span>',            
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>P. Protection</strong>',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>M. Protection</strong>',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>Speed Penalty</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.p_protection)}',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.m_protection)}',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.speedPenalty)}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd; text-align: center;">',
            '    </div>',
            '    <div class="cont-inner">',
            f'        <strong>Effect(s):</strong>{self.desc}',
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

    def __generalItemToHtmlList(self):
        html = [
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 45%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 30%;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',
            '        <span class="rel" style="width: 17.85%; padding-top: 0px; text-align: right;">',
            '            {points}'.format(points=self.points*"&nbsp;&#9734;"),
            '        </span>',            
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>Uses</strong>',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>Range</strong>',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            '            <strong>Equippable</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.uses)}',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.range)}',
            '        </span>',
            '        <span class="rel" style="width: 30%; text-align: center;">',
            f'            {self.__formatField(self.equippable)}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd; text-align: center;">',
            '    </div>',
            '    <div class="cont-inner">',
            f'        <strong>Effect(s):</strong>{self.desc}',
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
        if self.equipment() == None:   
            return self.__generalItemToHtmlList()
        else:
            if self.damage():
                return self.__weaponToHtmlList()
            else:
                return self.__armorToHtmlList()
           