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
        self.__html += self.__technique_section()
        self.__html += self.__notes_section()
        self.__html += self.__extra_item_section()
        self.__html += self.__extra_technique_section()
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
            '<i style="font-size: 8pt;">Start With Racial Stats (+2 in any stats for custom race), Then Set HP to 3, Then +7 divided between HP/TP, Finally +2 in any other stats</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Stats</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '             <strong>HP:</strong>______/______',
            '             &emsp;&emsp;<strong>TP:</strong>______/______',
            '             &emsp;&emsp;<i style="font-size: 10pt;">HP + TP Cannot be > 25. Cap for all other stats is 5</i><br/>'
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
            '             </div>',
            '        </div>',
            '    </div>',
        ]

    def __skills_block(self):
        html = [
            '<i style="font-size: 8pt;">Start With Class Skills (+4 in any skills for custom class), Then +2 points in any other skills</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Skills</h4>',
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
            '    <i style="font-size: 8pt;">Allocate Abilities Here (1 active and 1 passive if building custom class)</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Abilities</h4>',
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
            '    <i style="font-size: 8pt;">Can only check 1 out of PHYS or MAG. Cannot Check DUAL if SHLD is checked or if using 2-handed weapons.</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Weapon</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <strong>Name:</strong>___________________________________________',
            '            <strong>Skill:</strong>__________________________',
            '            <strong>Damage:</strong>____',
            '            <strong>Range:</strong>____',
            '            &emsp;&#9744;&nbsp;PHYS&emsp;&#9744;&nbsp;MAG&emsp;&#9744;&nbsp;DUAL'
            '            &emsp;<strong>Stat:</strong>_____&emsp;',
            '            <strong>SPD. Penalty:</strong> ____',
            '            <strong>Effect(s):</strong>________________________________________________________________________',
            '        </div>',
            '    </div>'
        ]
        html+=[
            '    <i style="font-size: 8pt;">Cannot check SHLD if DUAL is checked or if using a 2-handed weapon.</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Armor</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <strong>Name:</strong>___________________________________________',
            '            <strong>Skill:</strong>__________________________<br/>',
            '            <strong>AR Value:</strong>_____',
            '            &emsp;<strong>Physical:</strong>_____'
            '            &emsp;&emsp;<strong>Magical:</strong>_____',
            '            &emsp;&#9744;&nbsp;SHLD',
            '            &emsp;<strong>SPD. Penalty:</strong> _____',
            '            <strong>Effect(s):</strong>________________________________________________________________________',
            '        </div>',
            '    </div>'
        ]
        html+=[
            '    <i style="font-size: 8pt;">Can only have 2 items equipped at a time by default, DM may allow more or less.</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 65%;">',
            '                <h4 class="nopad">Items</h4>',
            '            </span>'
            '            <span class="rel" style="width: 30%; text-align: right;">',
            '                <h4 class="nopad">Gold: _________</h4>',
            '            </span>'
            '        </div>',
        ]
        for _ in range(6):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>________________________________________&emsp;',
                '            <strong>Uses:</strong>______&emsp;',
                '            <strong>#:</strong>______&emsp;',
                '            <strong>Equip:</strong>&#9744;<br/>'
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
    
    def __extra_item_section(self):
        html=[
            '    <i style="font-size: 8pt;">Can only have 2 items equipped at a time by default, DM may allow more or less.</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <span class="rel" style="width: 65%;">',
            '                <h4 class="nopad">Backpack (Extra Items)</h4>',
            '            </span>'
            '            <span class="rel" style="width: 30%; text-align: right;">',
            '                <h4 class="nopad">Gold: _________</h4>',
            '            </span>'
            '        </div>',
        ]
        for _ in range(15):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>________________________________________&emsp;',
                '            <strong>Uses:</strong>______&emsp;',
                '            <strong>#:</strong>______&emsp;',
                '            <strong>Equip:</strong>&#9744;<br/>'
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
    
    def __extra_technique_section(self):
        html=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Skill Book (Extra Techniques)</h4>',
            '        </div>',
        ]
        for _ in range(11):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>__________________________________________',
                '            <strong>Skill:</strong>____________________________'
                '            <strong>TP Cost:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Range:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Targets:</strong>_____',
                '            &nbsp;&emsp;&emsp;&emsp;&emsp;<strong>Points:</strong>_____/_____',
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
            
    def __technique_section(self):
        html=[
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Techniques</h4>',
            '        </div>',
        ]
        for _ in range(7):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>__________________________________________',
                '            <strong>Skill:</strong>____________________________'
                '            <strong>TP Cost:</strong>_____',
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