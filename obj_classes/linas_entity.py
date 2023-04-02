"""
Class used to hold and modify data for LINAS' entities
"""
from __future__ import print_function, division
from typing import List, Dict
from utils.assets import AssetManager
from obj_classes.linas_stat      import LINASStat
from obj_classes.linas_skill     import LINASSkill
from obj_classes.linas_abil      import LINASAbility
from obj_classes.linas_technique import LinasTechnique
from obj_classes.linas_item      import LINASItem
import re

class LinasEntity:
    __am = AssetManager()
    __image_style='style="height:16px; width:autopx;"'

    def __init__(
        self,
        name       : str,
        desc       : str,
        stats      : Dict[str,int],
        weapon     : LINASItem,
        armor      : LINASItem,
        skills     : Dict[str,int],
        abilities  : List[LINASAbility],
        image      : str = None,
        techniques : List[LinasTechnique] = [],
        items      : List[LINASItem] = [],
        isBoss     : bool = False,
        shield     : bool = False,
        dualWield  : bool = False,
        template   : List[Dict[str,str]] = None
    ) -> None:
        # Start by just feeding in base values
        self.name : str = name
        self.desc : str = desc

        # Split out base stats here
        for key in stats.keys():
            self.__assign_stat(key, stats[key])
        self.weapon : LINASItem = weapon
        self.armor  : LINASItem = armor
        self.skills : Dict[str, str] = skills
        self.abilities : List[LINASAbility] = abilities
        self.image : str = image if image else LinasEntity.__am.get('empty_image')
        self.techniques : List[LinasTechnique] = techniques
        self.items : List[LINASItem] = items
        self.dualWield = dualWield
        self.shield = shield

        # Compute complex stats here
        speedPenalty   = self.__nullable(self.weapon.speedPenalty) + self.__nullable(self.armor.speedPenalty)
        self.adj_spd   = self.spd - (speedPenalty) + self.str + 2
        self.damage    = self.__get_weapon_stat(self.weapon.stat) + self.weapon.damage()
        self.p_defense = self.__nullable(self.armor.p_protection) + self.end
        self.m_defense = self.__nullable(self.armor.m_protection) + self.spr
        if isBoss:
            self.hp *= 2

    def __get_weapon_stat(self, name : str):
        formatted = name.lower()
        if formatted == 'str':
            return self.str
        if formatted == 'dex':
            return self.dex
    
    def __nullable(self, value : int):
        return value if value else 0
    
    def __assign_stat(self, name : str, val : int) -> None:
        formatted = name.lower()
        if formatted == 'hp':
            self.hp : int = val
        elif formatted == 'tp':
            self.tp : int = val
        elif formatted == 'str':
            self.str : int = val
        elif formatted == 'dex':
            self.dex : int = val
        elif formatted == 'int':
            self.int : int = val
        elif formatted == 'end':
            self.end : int = val
        elif formatted == 'spr':
            self.spr : int = val
        elif formatted == 'spd':
            self.spd : int = val

    def __stats_block(self):
        spacing="6.5%"
        return [
            '    <strong style="margin-left:10px;">STATS</strong>',
            '    <div class="container nopad" style="margin:10px;">',
            '        <div class="cont-inner" style="padding-right: 0px;">',
            f'             <div>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("hp")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("tp")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("spd")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("str")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("int")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("dex")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("end")}</span>',
            f'                 <span class="rel" style="width: {spacing};">{LinasEntity.__am.tag("spr")}</span>',
            f'                 <span class="rel" style="width: {spacing};">&#8645;{LinasEntity.__am.tag("spd")}</span>',
            f'                 <span class="rel" style="width: {spacing};">&#8645;{LinasEntity.__am.tag("patk")}</span>',
            f'                 <span class="rel" style="width: {spacing};">&#8645;{LinasEntity.__am.tag("pdef")}</span>',
            f'                 <span class="rel" style="width: {spacing}; padding-right: 0px;">&#8645;{LinasEntity.__am.tag("mdef")}</span>',
            '              </div>'
            '              <hr style="border: 1px solid #dddddd;">',
            f'             <div>',
            f'                 <span class="rel" style="width: {spacing};">{self.hp}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.tp}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.spd}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.str}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.int}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.dex}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.end}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.spr}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.spd}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.damage}</span>',
            f'                 <span class="rel" style="width: {spacing};">{self.p_defense}</span>',
            f'                 <span class="rel" style="width: {spacing}; padding-right: 0px;">{self.m_defense}</span>',
            '              </div>'
            '        </div>',
            '    </div>',
        ]

    def __skills_block(self):
        adj_skills = [ x for x in self.skills.keys() ]
        while len(adj_skills) % 4 != 0:
            adj_skills.append("")
        html =  [
            '    <strong style="margin-left:10px;">SKILLS</strong>',
            '    <div class="container nopad" style="margin:10px;">',
        ]
        for i in range(0,len(adj_skills)):
            skill = str(adj_skills[i])
            val = self.skills[skill] if skill in self.skills else ""
            s_style="width: 23%;"
            if skill != "":
                skill = f'{skill.title()}: {val}'
            if i % 4 == 0:
                if i > 0:
                    html.append('        </div>')
                html.append('        <div class="cont-inner" style="padding-right: 0px;">')
            if i % 3 == 0:
                html.append(f'             <span class="rel" style="{s_style} padding-right: 0px;">{skill}</span>')
            else:   
                html.append(f'             <span class="rel" style="{s_style}">{skill}</span>')
        html.append('        </div>')
        html.append('    </div>')
        return html
    
    def __abilities_block(self):
        html =  [
            '    <strong style="margin-left:10px;">ABILITIES</strong>',
            '    <div class="container nopad" style="margin:10px;">',
        ]
        for abil in self.abilities:
            t = 'Active' if abil.type.upper() == 'A' else 'Passive'
            html += [
                '        <div class="container nopad" style="margin:10px;">',
                '            <div style="padding: 5px;">'
                f'                <strong>{abil.name.title()} [{t}]</strong><br/>',
                '                 <hr style="border: 1px solid #dddddd;">',
                f'                {abil.desc}',
                '            </div>',
                '        </div>'
            ]
        html.append('    </div>')
        return html

    def __equipment_block(self):
        spacer='&emsp;&emsp;&emsp;'
        html =  [
            '    <strong style="margin-left:10px;">EQUIPMENT</strong>',
            '    <div class="container nopad" style="margin:10px;">',
            '        <div class="container nopad" style="margin:10px;">',
            '            <div style="padding: 5px;">',
            f'                <strong>{self.weapon.name} [Weapon]</strong>{spacer}',
            f'                {spacer}<strong>Req. Skill:</strong> {self.weapon.linkedSkill.title()}<br/>',
            '                 <hr style="border: 1px solid #dddddd;">',
            f'                {LinasEntity.__am.tag("patk")}: {self.weapon.damage()}',
            f'                {spacer}{"&#9745;" if self.weapon.damageType() == "MAG" else "&#9744;"}&nbsp;MAG',
            f'                {"&#9745;" if self.weapon.damageType() == "PHYS" else "&#9744;"}&nbsp;PHYS',
            f'                {"&#9745;" if self.dualWield else "&#9744;"}&nbsp;DUAL',
            f'                {spacer}<strong>Range:</strong> {self.weapon.range}',
            f'                {spacer}<strong>Stat:</strong> {self.weapon.stat.upper()}',
            f'                {spacer}{LinasEntity.__am.tag("pen")}: {self.__nullable(self.weapon.speedPenalty)}',
            '                 <hr style="border: 1px solid #dddddd;">',
            f'                {self.weapon.desc}'
            '            </div>',
            '        </div>',
            '        <div class="container nopad" style="margin:10px;">',
            '            <div style="padding: 5px;">',
            f'                <strong>{self.armor.name} [Armor]</strong><br/>',
            '                 <hr style="border: 1px solid #dddddd;">',
            f'                {LinasEntity.__am.tag("pdef")}: {self.__nullable(self.armor.p_protection)}',
            f'                {spacer}{LinasEntity.__am.tag("mdef")}: {self.__nullable(self.armor.m_protection)}',
            f'                {spacer}{LinasEntity.__am.tag("pen")}: {self.__nullable(self.armor.speedPenalty)}',
            f'                {spacer}{"&#9745;" if self.shield else "&#9744;"}&nbsp;SHLD',
            '                 <hr style="border: 1px solid #dddddd;">',
            f'                {self.armor.desc}'
            '            </div>',
            '        </div>',
            '    </div>'
        ]
        return html
    
    def __items_block(self):
        s_style="width: 23%;"
        html =  [
            '    <strong style="margin-left:10px;">ITEMS</strong>',
            '    <div class="container nopad" style="margin:10px;">',
        ]
        for i, item in enumerate(self.items):
            it = f'{item.name} x{item.uses}'
            if i % 4 == 0:
                if i > 0:
                    html.append('        </div>')
                html.append('        <div class="cont-inner" style="padding-right: 0px;">')
            if i % 3 == 0:
                html.append(f'             <span class="rel" style="{s_style} padding-right: 0px;">{it}</span>')
            else:   
                html.append(f'             <span class="rel" style="{s_style}">{it}</span>')
        html.append('        </div>')
        html.append('    </div>')
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
        html = [
            f'<div style="page-break-before: always;"></div>',
            f'<div class="container pop">',
            f'    <div class="cont-title">',
            f'        <h3 class="nopad">{self.name}</h3>',
            f'    </div>',
            f'    <div class="cont-inner" style="padding-left:10px;">',
            f'        <div class="image-bg" style="background-image: url({self.image}); margin:5px;"></div>',
            f'        {self.desc}',
            f'    </div>',
        ] 
        html += self.__stats_block()
        html += self.__skills_block()
        html += self.__abilities_block()
        html += self.__equipment_block()
        html += self.__items_block()
        html.append('</div>')
        return html
        