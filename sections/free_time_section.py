"""
Class used to create the free time section for a system, defines what players can
 do outside combat
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List

class FreeTimeSection:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used to create the free time section for a system, defines what
        players can do outside combat

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
        self.__html.append(f'    {self.__contents.single("free time")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Free time is time between battles or events in the campaign where the
            players are free to explore and engage in events or activities which
            aren't part of the main goal the party as a group is trying to
            accomplish. Examples of these could be training skills, or studying
            new skills. This also includes visiting shops, socializing in taverns,
             or other areas of interest. 

            The primary goal of free time is to provide breaks between action
            sequences both to help the DM manage the flow of the campaign and also
            to give the player's characters an opportunity to interact with each
            other as well as the surrounding environment outside of a battle
            setting.  Below is a list of some common free-time activities:
            """
        )]
        self.__html.append("    <h3><u>Training</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Characters can train in order to level up physical skills and stats.
            For example, a fighter might train endurance by sitting under a
            waterfall or a mage might train their spirit by meditating. This
            might also refer to skill training such as a swordsman taking time
            to practice their sword stances or attacks or a blacksmith taking
            some time off to work in the town's forge.
            """
        )]
        self.__html.append("    <h3><u>Studying</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """            
            Similar to training; studying can learn new skills or spells either by
            reading books or by training with an NPC who specializes in the
            skill/spell required. This is especially useful if a particular skill
            chosen by a player for their character hasn't really come up much
            during the campaign. By improving the negative skill related to the
            unwanted one, both will disappear, freeing up the skill points for
            later.
            """
        )]
        self.__html.append("    <h3><u>Shopping</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """ 
            As the name suggests, this would be visiting various shops to browse
            items. To make things interesting; the DM might consider doing things
            such as varying goods from town to town or possibly varying prices
            between regions to allow an extra incentive for checking shops as well
            as to keep things from getting stale. For players, it might be a good
            idea to save a bit of the money received during character creation in
            case the campaign's environment or circumstances make certain items
            more valuable than others.
            """
        )]
        self.__html.append("    <h3><u>Information Gathering</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """ 
            Gathering information is extremely
            important, especially in cases where none of the party members have any
            connection to the area the campaign is taking place in. Information
            gathering can help the party be better prepared for challenges and
            obstacles which may appear later and could help avoid nasty surprises.
            <p style="page-break-before: always;"></p>
            """
        )]
        self.__html.append("    <h3><u>Sightseeing</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """ 
            This primarily refers to exploring the area in which the party is
            currently resting in. This could involve visiting bars to gamble or
            drink, visiting a famous landmark such as a library or Colosseum, or
            conversing and interacting with townsfolk. Sightseeing is mainly used
            as a way for players to spend a few more minutes enjoying the game vs.
            being a purely functional activity and it is up to the DM and players
            to determine how valuable the time spent sightseeing truly is.
            """
        )]
        self.__html.append("    <h3><u>Side Quests</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """ 
            During free time activities, one of the party members may stumble
            across the opportunity for a side quest. That is, a quest not related
            to the campaign but which may offer additional chances for rewards as
            well as additional battles within the campaign. Upon receiving the
            opportunity for a side quest; the DM has the players vote on whether
            they want to pursue or abandon the side quest or not. In most cases,
            it is better to not split the group and to keep side quests as an all
            or nothing mechanism. However, the DM has the freedom to change this
            and allow one or more members of the group to attempt the side quest
            without the rest of the group. This could be especially useful in cases
            where the members not partaking need some extra free time to train or
            study or to otherwise work on fine-tuning their characters.
            <p style="page-break-before: always;"></p>

            In addition to making the game less repetitive, free time is also a
            powerful tool for the DM and the following schedule is suggested
            (but not enforced) to help play time move smoothly.
            
            <ul><li>
            Warm Up + Free Time 10 ~ 15 min
            <ul><li>
            Review what happened during the previous session
            </li><li>
            DM gives feedback to players if needed
            </li><li>
            Players give feedback to DM if needed
            </li><li>
            Players do any of the free-time activities listed above
            </li></ul></li><li>
            Campaign Time: Depends on DM
            <ul><li>
            DMs should try to stick to a set schedule and leave in a bit of buffer
            time (at least 15 min) at the end of the play session. For example
            if the party just reached a cave which the DM knows will take them a
            while to get through, but there's only 10 minutes left before the
            normal cut of time; it might be a good idea to announce free time.
            </li></ul></li><li>
            Free Time 10 ~ 15 min
            <ul><li>
            Players do any of the free-time activities listed above
            </li></ul></li></ul>

            It should also be noted that players can only perform one free time
            activity during a given free-time space. Although as always; the DM
            may choose to allow more/less free time activities as they see fit.
            """
        )]
        self.__html.append("</div>")
# ================================================================================
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