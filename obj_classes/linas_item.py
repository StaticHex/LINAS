"""
Class used to hold and modify data for LINAS' items
"""
from __future__ import print_function, division
from typing import List, Dict
from utils.assets import AssetManager
import re

class LINASItem:
    __am = AssetManager()
    __image_style='style="height:16px; width:autopx;"'

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
        points          : int                 = -1
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

        if self.points == -1:
            if artifact or not self.equipment():
                self.points = 0
            else:
                self.points = 5
                self.points -= self.equipment() // 2
                if self.m_damage:
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
            return 'MAG'
        else:
            return 'PHYS'
    
    def protection(self):
        if self.p_protection and self.m_protection:
            return self.p_protection + self.m_protection
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
            '        <span class="rel" style="width: 30%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 27%; padding-top: 0px;">',
            f'            <strong>Req. Skill:</strong> {self.linkedSkill.title()}',
            '        </span>',  
            '        <span class="rel" style="width: 15%; padding-top: 0px;">',
            f'            <strong>Max Points:</strong> {self.__formatField(self.points)}',
            '        </span>',        
            '        <span class="rel" style="width: 18%; text-align: right;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',
    
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%; text-align:center;">',
            f'            {LINASItem.__am.tag("patk")}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align:center;">',
            '            <strong>Range</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align:center;">',
            '            <strong>Stat</strong>',
            '        </span>',
            '        <span class="rel" style="width: 15%; text-align:center;">',
            f'            {LINASItem.__am.tag("pen")}',
            '        </span>',
            '        <span class="rel" style="width: 45%;">',
            '            <strong>Effect(s)</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%;">',
            f'            {self.damage()} [{self.damageType()}]',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align:center;">',
            f'            {self.range}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align:center;">',
            f'            {self.stat.upper()}',
            '        </span>',
            '        <span class="rel" style="width: 15%; text-align:center;">',
            f'            {self.__formatField(self.speedPenalty)}',
            '        </span>',
            '        <span class="rel" style="width: 45%;">',
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
    
    def __armorToHtmlList(self):
        html = [
            '<div class="container pop">',
            '    <div class="cont-title">',
            '        <span class="rel" style="width: 45%;">',
            f'            <h4 class="nopad">{self.name}</h4>',
            '        </span>',
            '        <span class="rel" style="width: 17.85%; padding-top: 0px;">',
            f'            <strong>Max Points:</strong>{self.__formatField(self.points)}',
            '        </span>',     
            '        <span class="rel" style="width: 30%; text-align: right;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            <strong>{LINASItem.__am.tag("pdef")}</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            <strong>{LINASItem.__am.tag("mdef")}</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center; overflow: hidden;">',
            f'            &nbsp;{LINASItem.__am.tag("pen")}&nbsp;',
            '        </span>',
            '        <span class="rel" style="width: 60%;">',
            '            <strong>Effect(s)</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.__formatField(self.p_protection)}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.__formatField(self.m_protection)}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.__formatField(self.speedPenalty)}',
            '        </span>',
            '        <span class="rel" style="width: 60%; text-align: left;">',
            f'            {self.desc}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd; text-align: center;">',
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
            '        <span class="rel" style="width: 47.85%; text-align: right;">',
            f'            <strong>Cost:</strong> {self.formattedCost()}',
            '        </span>',     
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            '            <strong>Uses</strong>',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            '            <strong>Range</strong>',
            '        </span>',
            '        <span class="rel" style="width: 70%; text-align: left;">',
            '            <strong>Effect(s)</strong>',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd;">',
            '    </div>',
            '    <div class="cont-inner">',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.__formatField(self.uses)}',
            '        </span>',
            '        <span class="rel" style="width: 10%; text-align: center;">',
            f'            {self.__formatField(self.range)}',
            '        </span>',
            '        <span class="rel" style="width: 70%; text-align: left;">',
            f'            {self.desc}',
            '        </span>',
            '        <hr style="border: 1px solid #dddddd; text-align: center;">',
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
           