"""
Class used to create the introduction section for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List
import os

class CharacterSheet:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used to create a character sheet for the system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        # Build out HTML here
        self.__html.append('<div class="section">')
        self.__html += [
            f'    <img src="file:///{os.getcwd()}/assets/logo.png" style="padding: 0px; float: left;"/>',
            '     <h2 class="nopad" style="font-size: 44pt; padding-top: 24pt; text-align: right;">Character Sheet</h2>'
        ]
        self.__html += self.__char_info_block()
        self.__html += self.__bg_info_block()
        self.__html += self.__stats_block()
        self.__html += self.__skills_block()
        self.__html += self.__abilities_block()
        self.__html += self.__equipment_block()
        self.__html += self.__spell_section()
        self.__html += self.__notes_section()
        self.__html.append('</div>')

    def __char_info_block(self):
        return [
            '    <div class="container pop">',
            '        <div class="cont-title">',
            '            <h4 class="nopad">Character Info</h4>',
            '        </div>'
            '        <div class="cont-inner">',
            '            <strong>Character Name:</strong>____________________________',
            '            <strong>Player Name:</strong>____________________________',
            '            <strong>Race:</strong>_________________ ',
            '            <strong>Class:</strong>__________________&nbsp;&nbsp;&nbsp;',
            '            <strong>Height:</strong> __________ <strong>Weight:</strong> __________',
            '            <strong>Age:</strong> __________ <strong>Gender:</strong>__________&nbsp;&nbsp;',
            '            <strong>Spoken Languages</strong>________________________________',
            '        </div>',
            '    </div>',
        ]

    def __bg_info_block(self):
        return [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '             <h4 class="nopad">Background Info</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <span class="rel" style="width: 35%;">',
            '                <div class="container">',
            f'                   <img src="file:///{os.getcwd()}/assets/camera.png" style="padding: 10px;"/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>'
            '                </div>',
            '            </span>',
            '            <span class="rel" style="width: 60%;">',
            '                <div class="cont-inner" style="padding-right:0px;">',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                    _________________________________________________',
            '                </div>',
            '            </span>',
            '        </div>',
            '    </div>'
        ]
    
    def __stats_block(self):
        return [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 30%;">',
            '                <h4 class="nopad">Stats</h4>',
            '            </span>'
            '            <span class="rel" style="width: 65%; text-align: right; font-size: 8pt;">',
            '                <i class="nopad">STARTING STATS: Allocate Racial Stats. 3 HP + 7 divided between HP/MP, +1 in any other stat </i>',
            '            </span>'
            '        </div>',
            '        <div class="cont-inner">',
            '             <strong>HP:</strong>______/______',
            '             &emsp;&emsp;<strong>MP:</strong>______/______',
            '             &emsp;&emsp;<i style="font-size: 10pt;">NOTE: HP + MP Cannot be > 25. Cap for all other stats is 5</i><br/>'
            '             <strong>SPD:</strong>______',
            '             &nbsp;&nbsp;&emsp;<strong>STR:</strong>______',
            '             &nbsp;&nbsp;&emsp;<strong>INT:</strong>______',
            '             &nbsp;&nbsp;&emsp;<strong>DEX:</strong>______',
            '             &nbsp;&nbsp;&emsp;<strong>END:</strong>______',
            '             &nbsp;&nbsp;&emsp;<strong>SPR:</strong>______<br/>',
            '             <hr style="border: 1px solid #dddddd;">'
            '             <div style="color: #777777">',
            '                 <strong>Move (SPD + 2 - Tot. Penalty):</strong>_____',
            '                 &emsp;&emsp;<strong>Physical Attack (Weapon Atk + STR or DEX):</strong>_____<br/>',
            '                 <strong>Physical Defense (P. AR Value + END):</strong>_____',
            '                 &nbsp;&emsp;<strong>Magic Defense (M. AR Value + Spirit):</strong>_____',
            '             </div>'
            '        </div>',
            '    </div>',
        ]

    def __skills_block(self):
        html = [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 30%;">',
            '                <h4 class="nopad">Skills</h4>',
            '            </span>'
            '            <span class="rel" style="width: 65%; text-align: right; font-size: 8pt;">',
            '                <i class="nopad">STARTING SKILLS: Allocate Class Skills +2 points in any</i>',
            '            </span>'
            '        </div>',
            '        <div class="cont-inner">',
            '            <span class="rel" style="width: 40%;">',
            '                <strong>Skill Name</strong>',
            '            </span>',
            '            <span class="rel" style="width: 5%; text-align: right;">',
            '                <strong>Val</strong>',
            '            </span>',
            '            <span class="rel" style="width: 40%;">',
            '                <strong>Skill Name</strong>',
            '            </span>',
            '            <span class="rel" style="width: 5%; text-align: right;">',
            '                <strong>Val</strong>',
            '            </span>',
            '        </div>',
        ]
        for _ in range(5):
            html += [
                '        <div class="cont-inner">',
                '            <span class="rel" style="width: 40%;">',
                '                __________________________________',
                '            </span>',
                '            <span class="rel" style="width: 5%; text-align: right;">',
                '                ____',
                '            </span>',
                '            <span class="rel" style="width: 40%;">',
                '                __________________________________',
                '            </span>',
                '            <span class="rel" style="width: 5%; text-align: right;">',
                '                ____',
                '            </span>',
                '        </div>'                
            ]
        html.append('<br/>    </div>')
        return html

    def __abilities_block(self):
        html = [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 30%;">',
            '                <h4 class="nopad">Abilities</h4>',
            '            </span>'
            '            <span class="rel" style="width: 65%; text-align: right; font-size: 8pt;">',
            '                <i class="nopad">STARTING ABILITIES: Allocate Racial Abilities</i>',
            '            </span>'
            '        </div>',
        ]
        for _ in range(3):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>_____________________________________&emsp;Active&emsp;Passive&emsp;'
                '            <strong>Uses Remaining:</strong> _____',
                '            <strong>Effect:</strong>___________________________________________________________________________<br/>',
                '        </div>',
            ]
        html.append('    </div>')
        return html

    def __equipment_block(self):
        html=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Weapon</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <strong>Name:</strong>___________________________________________',
            '            <strong>Skill:</strong>__________________________',
            '            <strong>Damage:</strong>_____',
            '            <strong>Range:</strong>_____',
            '            &emsp;&emsp;Physical&emsp;Magical&emsp;Dual Wielding&emsp;&emsp;',
            '            <strong>Speed Penalty:</strong> _____',
            '            <strong>Effect(s):</strong>________________________________________________________________________',
            '        </div>',
            '    </div>'
        ]
        html+=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Armor</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <strong>Name:</strong>___________________________________________',
            '            <strong>Skill:</strong>__________________________<br/>',
            '            <strong>AR Value:</strong>_____',
            '            &emsp;&emsp;Physical&emsp;Magical&emsp;&emsp;',
            '            <strong>Speed Penalty:</strong> _____',
            '            <strong>Effect(s):</strong>________________________________________________________________________',
            '        </div>',
            '    </div>'
        ]
        html+=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 65%;">',
            '                <h4 class="nopad">Items</h4>',
            '            </span>'
            '            <span class="rel" style="width: 30%; text-align: right;">',
            '                <h4 class="nopad">Gold: _________</h4>',
            '            </span>'
            '        </div>',
        ]
        for _ in range(8):
            html += [
                '        <div class="cont-inner">',
                '            <strong>Name:</strong>_____________________________________________',
                '            <strong>Uses:</strong>________',
                '            <strong>Amount:</strong>________<br/>',
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
    
    def __spell_section(self):
        html=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Spells</h4>',
            '        </div>',
        ]
        for _ in range(7):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>__________________________________________',
                '            <strong>Skill:</strong>____________________________'
                '            <strong>MP Cost:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Range:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Targets:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Points:</strong>_____/_____',
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
    
    def __notes_section(self):
        return [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Notes</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>'
            '        </div>',
            '    </div>',
        ]
    
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
        return self.__html