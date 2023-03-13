"""
Class used to create a section explaining and listing out stats for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from obj_classes.data_manager import DataManager
from typing import List

class StatSection:
    def __init__(
        self,
        system : ContentManager,
        data : DataManager

    ) -> None:
        """
       Class used to create a section explaining and listing out stats for a system

        Parameters
        ----------
        system : `ContentManager`
            The system this section is a part of
        data : `DataManager`
            The data for the class, needed load in the stats for the section
        """
        # A list of HTML tags to append to a host document
        self.__html = []

        # Get TOC data from parent
        self.__contents = system.getContents()

        # Build out HTML here
        self.__html.append('<div class="section">')
        self.__html.append(f'    {self.__contents.single("stats")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            LINAS, in general tries to keep it's scale for stat allocation fairly
            low. As stated in the introduction, the main drive for this is to
            keep damage calculations fast and straightforward. Stats can either
            be represented by numbers or by blocks (&#x25A1). For the fantasy
            system; the following stats are defined:
            """
        )]

        self.__html.append('    <ul>')
        self.__html += [ 
            f'        <p><li>{x}</li></p>' for x in  data.typeToHTMLList(
                'stats'
        )]
        self.__html.append('    </ul>')

        self.__html.append('    <p style="page-break-before: always;"><p/>')

        self.__html += [ f'    {x}' for x in system.collapse(
            """
            For the most part, a player can put points into whichever stats they
            see fit. However, that being said; there are a few restrictions:<br/>
            <ul><p><li>
            A user can only have a maximum of 25 points in HP and TP combined.
            Meaning, if the user already has 15HP, they can only have a maximum
            of 10TP.
            </li></p><p><li>
            Excluding HP and TP, the maximum number of points a user can have in
            any other stat is 5.
            </li></p><p><li>
            Excluding HP and TP, an entity can only have a total of 10 points
            among all other stats. Once again this means the total number of
            points in Strength, Intelligence, Dexterity, Spirit, Endurance, and
            Speed combined cannot be greater than 10.

            The restrictions above are put in place not only to keep damage
            calculations low; but also to try and ensure that no single player
            can run the entire campaign themselves. Additionally, this is done
            to try and keep the system from being too broken i.e. having mages
            equipped in steel plate.
            """
        )]
        self.__html.append('    <h4>Using Stats Outside Battle</h4>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            For the most part, stats are meant for doing battle calculations.
            However, LINAS likes to reward creative thinking and so there may
            be times when the DM allows stats to be calculated into the effects
            of a skill roll. For example, if playing with a character with a
            high strength rating; the DM may allow one or two points to be
            added to a dice roll to destroy something since their strength
            will undoubtedly make things easier

            Additionally, the DM may also choose to allow two players to
            compete using stats vs. skills such as just using two character's
            strength stat to determine the outcome of an arm wrestling
            competition. The specifics of using stats outside battle are fully
            up to the DM to decide how much/little they want to incorporate
            them. However, it should be noted that this is a viable option
            when creating campaigns in LINAS
            """
        )]
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