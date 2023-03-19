"""
Class used to create the introduction section for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List
from utils.assets import AssetManager
import os

class CharacterSheet:
    __am = AssetManager()
    __icon = 'style="height:15px; width:auto;"'
    __sStr=f'<img src="{__am.get("str")}" {__icon}"/>'
    __sInt=f'<img src="{__am.get("int")}" {__icon}"/>'
    __sSpd=f'<img src="{__am.get("spd")}" {__icon}"/>'
    __sDex=f'<img src="{__am.get("dex")}" {__icon}"/>'
    __sEnd=f'<img src="{__am.get("end")}" {__icon}"/>'
    __sSpr=f'<img src="{__am.get("spr")}" {__icon}"/>'
    __sHp=f'<img src="{__am.get("hp")}" {__icon}"/>'
    __sTp=f'<img src="{__am.get("tp")}" {__icon}"/>'
    __sPen=f'<img src="{__am.get("pen")}" {__icon}"/>'
    __sPAtk=f'<img src="{__am.get("patk")}" {__icon}"/>'
    __sPDef=f'<img src="{__am.get("pdef")}" {__icon}"/>'
    __sMAtk=f'<img src="{__am.get("matk")}" {__icon}"/>'
    __sMDef=f'<img src="{__am.get("mdef")}" {__icon}"/>'
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

        # Build out cover page here
        self.__html += self.__cover_page()

        # Build out HTML here
        self.__html.append('<div class="section">')
        self.__html += [
            f'    <img src="{CharacterSheet.__am.get("logo")}" style="padding: 0px; float: left;"/>',
            '     <h2 class="nopad" style="font-size: 44pt; padding-top: 24pt; text-align: right;">Character Sheet</h2>'
        ]
        self.__html += self.__char_info_block()
        self.__html += self.__bg_info_block()
        self.__html += self.__flavor_section()
        self.__html += self.__notes_section()
        self.__html += self.__stats_block()
        self.__html += self.__skills_block()
        self.__html += self.__abilities_block()
        self.__html += self.__equipment_block()
        self.__html.append(f'    {"</br>"*2}')
        self.__html += self.__item_section()
        self.__html.append(f'    {"</br>"*4}')
        self.__html += self.__technique_section()
        self.__html.append('</div>')
    
    def __cover_page(self):
        return [
            f'   <strong style="font-size: 16pt;">{"&emsp;"*10}Filling Out Your Character Sheet</strong>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">1. Fill Out Background Info</h4>',
            '        </div>',
            '        <div class="cont-inner", style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}Start with the background info for your character. This is the most important 
                          section of your character sheet. Everything else should flow from this. Start by getting an 
                          idea of who your character is as a living entity. Your character should be a race and class
                          the character wants to play vs. a race and class the player "thinks will do the best." When
                          creating a character, some good questions to ask are: How does the character fit into society?
                          Are they well liked? An outcast? etc.
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">2. Fill Out Flavor Info</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}The second section you should focus on is the flavor section. Especially if
                          you're having trouble filling out your background info. The flavor section lists out
                          some specifics for your character such as bad habits, motivations, what training or
                          expertise they have, etc. This section can go a long way to helping to determine a
                          good race/class to pick or to flesh out who the character is as a living entity. Once
                          you feel good about who your character is, you're ready to move on to the other stuff.
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">3. Fill Out Top Section</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}Chances are you may have already started filling this out in the process of
                          filling out either the background info or flavor text. If there are any empty entries go
                          ahead and fill them out now. If you have a race/class in mind for your character you can
                          go ahead and jot it down. Also write down any languages your character knows. If you're 
                          making a custom race or class just list it out for now. We'll get into the specifics for
                          the class in a second
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">4. Fill Out Stats Section</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}At first glance the stat section may look extremely intimidating or complex.
                          However, the math is fairly simple; the list below will give a brief explanation of how
                          to fill this section out. For a more in-depth guide over each stat ask your DM or look at
                          the stats section of the handbook. One final thing to note, is that you don't have to have a
                          non-zero value in all stats. Having stats with a 0 value is allowed so just focus on the
                          stats that make sense for your character.
                          <ol>
                              <li>Assign 3 points to HP. All characters get at least 3 HP to start</li>
                              <li>Allocate 7 points between HP/TP however you want. (HP+TP should be 10 when finished)</li>
                              <li>Allocate the points listed for your chosen race. If making a custom race allocate 2
                                stats in a way that makes sense. Your stats should be a reflection of your race's 
                                strong points.</li>
                              <li>Allocate 2 points in any stats other than HP/TP (total points in stats other than HP/TP should be 4)</li>
                              <li>Calculate adjusted speed (&#8645;{CharacterSheet.__sSpd}) by subtracting the number of points in speed from 
                              the total speed penalty ({CharacterSheet.__sPen}) from <u>all</u> equipment, then add any points in strength and
                              finally add 2. This value is used to calculate a wide number of things. Usually when the DM asks for speed, it's
                              this value</li>
                              <li>Calculate Weapon damage (&#8645;{CharacterSheet.__sPAtk}) by adding together your weapon's base damage and
                              the points in either STR or DEX (depending on which stat your weapon uses)</li>
                              <li>Calculate physical armor points (&#8645;{CharacterSheet.__sPAtk}) by adding together your armor's base 
                              physical protection value ({CharacterSheet.__sPDef}) and the points in END</li>
                              <li>Calculate magic armor points (&#8645;{CharacterSheet.__sMDef}) by adding together your armor's base 
                              magic protection value ({CharacterSheet.__sMDef}) and the points in SPR</li>
                          </ol>
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">5. Fill Out Skill Section</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            f"""
                          {"&emsp;"*2}Skills are much more straightforward than stats. Simply copy the skills and
                          values listed under your chosen class. If you're making a custom class, You get 4 points
                          to allocate in skills needed for your class to do it's job. Remember skills are roll 
                          modifiers not values. By default skills start at -2 so putting 2 points will bring it to
                          0. Like stats, skills should fit with your character's background.
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">6. Fill Out Ability Section</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}Like skills, abilities are usually listed out on the page for the chosen
                          class. However, characters are always free to swap out an ability for one they feel fits
                          their character better. If making a custom class or even if just desired, new abilities
                          can always be created. The thing to keep in mind when creating your own abilities is that
                          'passive' abilities happen automatically and 'active' abilities must be activated. For more
                          information on these check the abilities section of the handbook or ask your DM.
            """,
            '        </div>',
            '      </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">7. List Out Equipment For Class</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}If your class uses armor or equipment list it out here.  Again make sure to
                          take the appropriate weapons/armor for your class. You may need to skip ahead to this
                          section before continuing the stat section, not only for filling out the computed stats
                          at the bottom of the section but also in order to get an idea of where to allocate your
                          stats to make sure you're using your weapon optimally.
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">8. Fill Out Technique Section</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}Techniques encompass both skills and battle techniques. Depending on your
                          class you may find you need a number of techniques to perform your job. You can have up
                          to 2 techniques to start the game with and the DM may allow more or less. If you do find
                          yourself playing with a technique heavy character; it's recommended to put at least 4
                          points in TP to ensure you have enough points to use your techniques when needed.
            """,
            '        </div>',
            '    </div>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title" style="background: #ccddff;">',
            '            <h4 class="nopad">9. Take Any Items Needed By Class</h4>',
            '        </div>',
            '        <div class="cont-inner" style="font-size: 11pt;">',
            f"""
                          {"&emsp;"*2}Finish by taking any items needed by your class. These would be items in
                          addition to equipment such as lockpicks, crafting tools, musical instruments, etc. Players
                          are also able to give their characters any items which may relate specifically to that
                          character. These are things like jewelry, access cards, pocket knives, or anything else
                          their character uses on a regular basis.
            """,
            '        </div>',
            '    </div>'
        ]
#                         ==========================================================================================

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
            '<i style="font-size:8pt;">START HERE: This should be the first section you fill out. Everything else should flow from here; this is who your character is.</i>'
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '             <h4 class="nopad">Background Info</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <span class="rel" style="width: 35%;">',
            '                <div class="container">',
            f'                   <img src="{CharacterSheet.__am.get("camera")}" style="padding: 10px; height:16px; width:auto;"/>'
            '                    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>'
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
            '    <i style="font-size:8pt;">STARTING STATS: 3 in HP + 7 in HP/TP (HP+TP should be 10), Next add points from race, then add 2 anywhere else (should have 4 points in stats).</i>'
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Stats</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            f'             <strong>HP ({CharacterSheet.__sHp}):</strong>____/____',
            f'             &emsp;&emsp;<strong>TP ({CharacterSheet.__sTp}):</strong>____/____',
            '              &emsp;&emsp;<i style="font-size: 10pt;">HP + TP Max = 25, Stat Max (Not HP/TP) = 5, Starting = 0</i><br/>'
            '              <hr style="border: 1px solid #dddddd;">'
            f'             <strong>SPD ({CharacterSheet.__sSpd}):</strong>____',
            f'             &nbsp;<strong>STR ({CharacterSheet.__sStr}):</strong>____',
            f'             &nbsp;<strong>INT ({CharacterSheet.__sInt}):</strong>____',
            f'             &nbsp;<strong>DEX ({CharacterSheet.__sDex}):</strong>____',
            f'             &nbsp;<strong>END ({CharacterSheet.__sEnd}):</strong>____',
            f'             &nbsp;<strong>SPR ({CharacterSheet.__sSpr}):</strong>____<br/>',
            '             <hr style="border: 1px solid #dddddd;">'
            '             <div style="color: #777777">',
            f'                 <strong>&#8645;{CharacterSheet.__sSpd} ({CharacterSheet.__sSpd} - {CharacterSheet.__sPen} + {CharacterSheet.__sStr}  +2):</strong>____',
            f'                 &nbsp;&emsp;<strong>&#8645;{CharacterSheet.__sPAtk} ({CharacterSheet.__sPAtk} + {CharacterSheet.__sStr}/{CharacterSheet.__sDex}):</strong>____'
            f'                 &nbsp;&emsp;<strong>&#8645;{CharacterSheet.__sPDef} ({CharacterSheet.__sPDef} + {CharacterSheet.__sEnd}):</strong>____',
            f'                 &nbsp;&emsp;<strong>&#8645;{CharacterSheet.__sMDef} ({CharacterSheet.__sMDef} + {CharacterSheet.__sSpr}):</strong>____',
            '             </div>',
            '        </div>',
            '    </div>',
        ]

    def __skills_block(self):
        html = [
            '<i style="font-size:8pt;">STARTING SKILLS: First add points from class, then add 2 (should have 6 points total). Min Value = -2, Max Value = +2, Starting = -2</i>',
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
            '    <i style="font-size: 8pt;">STARTING ABILITIES: Allocate abilities from class here</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Abilities</h4>',
            '        </div>',
        ]
        for _ in range(3):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>_____________________________________&emsp;&#9744;&nbsp;Active&emsp;&#9744;&nbsp;Passive&emsp;'
                '            <strong>Uses:</strong> _____/_____',
                '            <strong>Effect:</strong>___________________________________________________________________________<br/>',
                '        </div>',
            ]
        html.append('    </div>')
        return html

    def __equipment_block(self):
        html=[
            '    <i style="font-size: 8pt;">STARTING EQUIPMENT: List out equipment needed for class here</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Equipment</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <span style="margin: 5px 5px 0px 5px; padding: 5px 5px 0px 5px;">',
            '                <strong>Weapon</strong>',
            '            </span>',
            '            <span class="rel" style="font-size: 8pt; width: 87%; text-align: right; padding:0px; margin:0px;">',
            '                <i>Can only check 1 out of PHYS or MAG. Cannot Check DUAL if SHLD is checked or if using 2-handed weapons.</i>',
            '            </span>'
            '            <div class="container" style="margin: 0px 5px 5px 5px; padding: 0px 5px 5px 5px;">'
            '                <strong>Name:</strong>___________________________________________',
            '                <strong>Skill:</strong>___________________________<br/>',
            f'               <strong>{CharacterSheet.__sPAtk}:</strong>____',
            '                <strong>Range:</strong>____',
            '                &emsp;&#9744;&nbsp;PHYS&emsp;&#9744;&nbsp;MAG&emsp;&#9744;&nbsp;DUAL',
            '                &emsp;<strong>Stat:</strong>_____',
            f'               <strong>{CharacterSheet.__sPen}:</strong> ____',
            '                <strong>Points:</strong> ____/____',
            '                <strong>Effect(s):</strong>________________________________________________________________________',
            '            </div>',
            '            <span style="margin: 5px 5px 0px 5px; padding: 5px 5px 0px 5px;">',
            '                <strong>Armor</strong>',
            '            </span>',
            '            <span class="rel" style="font-size: 8pt; width: 89%; text-align: right; padding:0px; margin:0px;">',
            '                <i>Cannot check SHLD if DUAL is checked or if using a 2-handed weapon.</i>',
            '            </span>'
            '            <div class="container" style="margin: 0px 5px 5px 5px; padding: 0px 5px 5px 5px;">',
            '                <strong>Name:</strong>________________________&nbsp;&nbsp;',
            f'                <strong>{CharacterSheet.__sPDef}:</strong>____',
            f'                &nbsp;&nbsp;<strong>{CharacterSheet.__sMDef}:</strong>____',
            '                 &nbsp;&nbsp;&#9744;&nbsp;SHLD',
            f'                &nbsp;&nbsp;<strong>{CharacterSheet.__sPen}:</strong> ____',
            '                 &nbsp;&nbsp;<strong>Points:</strong> ____/____',
            '                <strong>Effect(s):</strong>________________________________________________________________________',
            '            </div>',
            '        </div>',
            '    </div>',
        ]
        html.append('    </div></br>')
        return html
    
    def __item_section(self):
        html=[
            '    <i style="font-size: 8pt;">STARTING ITEMS: List out items needed for class here</i>',
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
        for _ in range(17):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>_______________________________________________&emsp;',
                '            <strong>Uses:</strong>_____&emsp;',
                '            <strong>Amount:</strong>_____&emsp;',
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
            
    def __technique_section(self):
        html=[
            '<i style="font-size: 8pt;">STARTING TECHNIQUES: Take up to 2 techniques related to class here</i>',
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Techniques</h4>',
            '        </div>',
        ]
        for _ in range(12):
            html += [
                '        <div class="container" style="margin: 5px; padding: 5px;">',
                '            <strong>Name:</strong>__________________________________________',
                '            <strong>Skill:</strong>____________________________'
                f'            <strong>{CharacterSheet.__sMAtk}:</strong>_____',
                f'           &nbsp;&emsp;&emsp;<strong>{CharacterSheet.__sTp}:</strong>_____',
                '            &nbsp;&emsp;&emsp;<strong>Range:</strong>_____',
                '            &nbsp;&emsp;&emsp;<strong>Targets:</strong>_____',
                '            &nbsp;&emsp;&emsp;<strong>Points:</strong>_____/_____',
                '            <strong>Effect(s):</strong>________________________________________________________________________',
                '        </div>',
            ]
        html.append('    </div>')
        return html
    
    def __flavor_section(self):
        html = [
            '    <i style="font-size: 8pt;">Used to add more info regarding character background. This is just for fun so don\'t sweat over it too much.</i>'
            '    <div class="container pop nopad">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Flavor</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            '            <span class="rel" style="width: 30%;">',
            '                <strong>Vices</strong>',
            '                <i style="font-size:8pt;">Bad habits, personality flaws</i>',
            '            </span>',
            '            <span class="rel" style="width: 30%; ">',
            '                <strong>Virtues</strong>',
            '                <i style="font-size:8pt;">Motivations, positive traits</i>',
            '            </span>',
            '            <span class="rel" style="width: 30%;">',
            '                <strong>Training</strong>',
            '                <i style="font-size:8pt;">Knowledge, expertise, lore, etc.</i>'
            '            </span>',
            '        </div>',
        ]
        for _ in range(5):
            html += [
                '        <div class="cont-inner">',
                '            <span class="rel" style="width: 30%;">',
                '                _________________________',
                '            </span>',
                '            <span class="rel" style="width: 30%;">',
                '                _________________________',
                '            </span>',
                '            <span class="rel" style="width: 30%;">',
                '                _________________________',
                '            </span>',
                '        </div>'                
            ]
        html.append('<br/>    </div>')
        return html
    
    def __notes_section(self):
        return [
            '    <div class="container pop">',
            '        <div class="cont-title"">',
            '            <h4 class="nopad">Notes</h4>',
            '        </div>',
            '        <div class="cont-inner">',
            f'            {"<br/>"*5}'
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