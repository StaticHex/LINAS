"""
Class used to hold and modify data for LINAS' skills
"""
from __future__ import print_function, division
from typing import List, Tuple, Dict
from obj_classes.data_manager import DataManager
from obj_classes.data_collection import DataCollection
from obj_classes.linas_abil import LINASAbility
import re
import os

from obj_classes.linas_abil import LINASAbility

class LINASRace:
    def __init__(
        self,
        name        : str,
        description : str,
        stats       : List[Tuple[str, int]] ,
        abilities   : List[Tuple[str, str]],
        languages   : List[str],
        data        : DataManager,
        image       : str = "empty_image.png",
        template    : List[Dict[str,str]] = None,
        notes       : List[str] = []
    ) -> None:
        """
        Class used to hold and modify data for LINAS' races

        Parameters
        ----------
        name : `str`
            The name of the skill
        description : `str`
            The text description for the skill
        stats : `List[Tuple[str, int]]`
            List of stats and their values to assign to the race
        abilities : `List[Tuple[str, str]]`
            List of abilities and their types (active/passive) to assign
            to the race
        languages : `List[str]`
            List of languages to assign to the race
        data : `DataManager`
            The data for the class, needed load in the abilities for the race
        image : `str`
            Image to use for the race, image must exist under the assets
            directory
        template : `List[Dict[str,str]]`
            An (optional) template to expand the current template by
        notes : `List[str]`
            A list of notes to display about the class
        """
        self.name      = name
        self.desc      = re.sub(r'[\ \n]+', ' ', description)
        self.stats     = stats
        self.abilities = abilities
        self.languages = languages
        self.image     = f"file:///{os.getcwd()}/assets/{os.path.basename(image)}"
        self.template  = template
        self.notes     = notes

        # Post processing of abilities i.e. find the abilities in the data
        # manager and cache them
        expandedAbilities : LINASAbility = []
        for ability in self.abilities:
            if isinstance(ability, LINASAbility):
                expandedAbilities.append(ability)
            elif isinstance(ability, tuple):
                abilityName, abilityType = ability
                section : DataCollection = data.getItem(
                    'abilities', 
                    abilityType.title()
                )
                abil : LINASAbility = section.getChild(
                    abilityName.title()
                )
                expandedAbilities.append(abil)
        self.abilities = expandedAbilities

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
        noSpace="padding: 0px; spacing: 0px; margin: 0px;"
        langStyle=f'width:50%; float: right; {noSpace}'
        statStyle=f'width:50%; {noSpace}'
        html = [
            f'<div class="container pop">',
            f'    <div class="cont-title">',
            f'        <h3 class="nopad">{self.name}</h3>',
            f'    </div>',
            f'    <div class="cont-inner">',
            f'        <img class="img-wrapped" src="{self.image}"/>',
            f'        {self.desc}',
            f'    </div>',
            f'    <div style="overflow: hidden; margin:0px;">'
            f'        <div class="cont-inner" style="{langStyle}">',
            f'            <div class="cont-sub-title cont-inner">',
            f'                <strong>Languages</strong>',
            f'            </div>',
            f'            <div class="cont-inner">',
            f'                <ul>'
        ]
        for lang in self.languages:
            html.append(f'                <li>{lang}</li>')
        html += [
            f'                </ul>',
            f'            </div>',
            f'        </div>'
            f'        <div class="cont-inner" style="{statStyle}">',
            f'            <div class="cont-sub-title cont-inner">',
            f'                <strong>Stat Bonuses:</strong>',
            f'            </div>',
            f'            <div class="cont-inner">',
            f'                <ul>'
        ]
        for stat in self.stats:
            name, val = stat
            fVal = f'+{val}' if val >= 0 else val
            html.append(
                f'                <li>{name.upper()}: {fVal}</li>'
            )
        html+=[
            f'                </ul>',
            f'            </div>',
            f'        </div>',
            f'    </div>',
            f'    <div class="cont-sub-title cont-inner">',
            f'        <strong>Abilities</strong>',
            f'    </div>',
            f'    <div class="cont-inner">'
        ]
        for abil in self.abilities:
            html+=abil.toHTMLList()
        html+=[
            f'    </div>',
            f'</div>',
        ]
        if len(self.notes):
            html += [
                f'<strong><u>Notes: </u></strong>',
                f'<ul>'
            ]
            for note in self.notes:
                note = re.sub(r'[\ \n]+',' ', note)
                html.append(f"    <li>{note}</li>")
            html.append('</ul>')
        html += [

            f'<div style="page-break-before: always;"></div>'
        ]
        return html