"""
Class used to create a section explaining and listing out skills for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List
import os

class SkillSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
       Class used to create a section explaining and listing out skills for a system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        data : `DataManager`
            The data for the class, needed load in the skills for the section
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        # Build out HTML here
        # ======================================================================
        # = Skills Section
        # ======================================================================
        self.__html.append('<div class="section">') 
        self.__html.append(f'    {self.__contents.single("skills")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            One of the major goals for this system is to present skill usage
            in a way which is flexible and open. This means that the skills
            listed in this section can be thought of as guidelines or
            "recommended skills" only. An entity always has the ability to use
            any skill they desire even if they don't have it chosen as a skill.
            One caveat with this: The DM always has the right to veto the playr's
            usage of a particular skill if using the skill wouldn't make sense
            from the standpoint of their character; e.g. a character using a
            flight skill when they have no means to do so.

            Skills themselves are kept fairly abstract and are more of roll
            modifiers vs. an actual measure of an entity's ability. Any skill
            an entity is considered "skilled" at gets a +1 or +2 added to their
            roll for that skill depending on the number of points in that skill.
            On the opposing end of this scale; any skill an entity is considered
            "unskilled" at gets a -1 or -2 added to their roll for that skill.
            If an entity tries to use a skill which they do not have any points
            in, it is considered to be an "unskilled" roll and the entity rolls
            at -2. Once again this allows some flexibility within the system and
            allows players to at least try to compensate for weak or missing
            skills without being completely locked out of using them.

            Rather than a simple pass/fail roll, LINAS uses a more dynamic 
            system for skill usage in an attempt to make games more narrative
            focus vs. crunch and run so to speak. Most rolls use a single d6
            roll laid out in the following manner:
            <br/><br/><strong>1 = You fail, and...</strong> (always fails
            regardless of roll modifiers)
            <br/><strong>2 = You fail</strong>
            <br/><strong>3 = You fail, but...</strong>
            <br/><strong>4 = You succeed, but...</strong>
            <br/><strong>5 = You succeed</strong>
            <br/><strong>6 = You succeed, and...</strong> (always succeeds
            regardless of roll modifiers)
            
            LINAS uses the above mapping in order to keep things from becoming
            sterile or rote and also to give the DM a bit more control over the
            flow of gameplay. For example, let's say a group really needs an
            artifact to continue with the campaign but the only character which
            could have identified the artifact's use rolled a 3
            (you fail, but...). In this case, it could be that although the
            character failed to identify the artifact, they're able to sense
            it's related to the area; allowing the party to still use the
            artifact (albeit in a more restricted manner).

            The DM may also choose to give additional bonuses or penalties to
            skill usage based on environmental conditions or party status. For
            example, if it's raining the DM may announce that all usage of the
            perception skill gets -1 since the rain would make it harder to
            discern what's going on at greater distances.
            <p style="page-break-before: always;">
            """+f"""
            <img src="file:///{os.getcwd()}/assets/skill_roll.png"
            style="padding: 10px; float: right;"/>
            With all this taken into consideration,
            modifiers turn skill rolls into a sort of sliding scale. At the
            center, the scale is completely balanced; however the odds may be
            for or against an entity depending on a variety of factors. However,
            despite this; a natural 1 is <u><strong>ALWAYS</strong></u> you fail
            and... and a natural 6 is <u><strong>ALWAYS</u></strong> you succeed
            and... This is done ton ensure that there is never a case where the
            need to roll is completely eliminated due to a 100% pass or fail rate.

            Like stats, there are no rules about which skills an entity
            can/cannot use and using a specific skill is mainly up to the players
            and the DM to work out amongst themselves. That being said, there are
            a few set restrictions regarding skills which must be observed:
            <ul><li>
            An entity cannot allocate more points than a +2 in a particular skill.
            <ul><li>
            It should be noted that past this point it wouldn't matter anyway,
            given a 1 is <strong><u>ALWAYS</u></strong> you fail and... however,
            the take away here is there's no way to increase a skill such that
            an entity has a 100% success chance.
            </li></ul></li><li>
            The sum of an entity's skill points in all skills cannot exceed 12. 
            If an entity  already has 12 points allocated and wants to learn a
            new skill. Points will need to be taken from some other skill and
            put into the new one
            <ul><li>
            The idea behind this is that each entity fully maxed out can have
            1 combat skill and 2 other skills they're fully mastered in.
            </li><li>
            Example: An archer has the following skill setup<br/><br/>
            Archery: +2 (4 points)<br/>
            Fletching: +1 (3 points)<br/>
            Magic +1 (3 points)<br/>
            Perception +0 (2 points)<br/><br/>
            The campaign has been more combat heavy and the archer hasn't
            really used fletching but has more heavily needed to rely
            on perception and sensing. The DM allots 2 skill points at the
            end of the session but the archer cannot improve the skills they
            want. They elect to remove 2 points from Fletching and apply 1
            to perception and 1 to sensing. Their new skill set is:<br/><br/>
            Archery: +2 (4 points)<br/>
            Fletching: -1 (1 points)<br/>
            Magic +1 (3 points)<br/>
            Perception +1 (3 points)<br/>
            Sensing -1 (1 point)<br/><br/>
            </li><li>
            Reallocation is treated as a form of allocation. Therefore, 
            entities do not have to wait until they have all 12 points allocated
            in order to re-allocate some of those points. However, allocation
            can only be done if the entity in question has points to allocate
            and if the DM decides it's a suitable time for the entity to
            allocate their points.
            <ul><li>
            Example: A warrior had put 2 points in magic at the start of the
            campaign such that they have the following skills<br/><br/>
            Swordsmanship +0 (2 points)<br/>
            Magic +0 (2 points)<br/></br>
            but has decided to go more of a physical strength based
            route. The DM assigns 1 skill point at the end of the session.
            The warrior elects to reassign 1 point from magic into
            swordsmanship rather than simply increasing either skill. Their
            skills now look like the following<br/><br/>
            Swordsmanship +1 (3 points)<br/>
            Magic -1 (1 point)</br>
            </li></ul></li></ul>

            It is important that both the DM and the players understand the
            restrictions put on both skills and stats moving forward as they 
            play a crucial role in keeping the game balanced
            """
        )]
        
        # Page break
        self.__html.append(f'    {system.pageBreak()}')
        
        # Load in skills
        self.__html += [ f'    {x}' for x in 
            data.typeToHTMLList('skills')
        ]
        self.__html.append('</div>')

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