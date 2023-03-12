"""
Class used to create the introduction section for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List

class IntroductionSection:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used to create the introduction section for a system

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
        self.__html.append(f'    {self.__contents.single("introduction")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Welcome to LINAS Tabletop; first I'd like to thank you for picking
            up our system and giving it a try. This system was developed by 
            myself (Joseph Bourque) along with some of my close friends who 
            not only helped me test the system but which also contributed to 
            it immensely.

            The initial inspiration for LINAS came from my own experiences 
            with different tabletop systems; as well as hearing about some
            of my friends' experiences. My goal with this system is to
            create a fluid and fast system which is easy to set up and start
            playing. I also wanted a system where battle calculations move
            quickly so that the flow of the game is interrupted as little
            as possible.

            The system is purposely kept light with the intent that character
            development and progression be done primarily through questing and 
            training vs. leveling up. The idea being to shift the focus more on 
            the story being told and to try and make characters more dynamic and
            rounded out vs. just a collection of stats.

            Most importantly, my goal is to develop something fun to play and
            with that in mind I hope you enjoy using this system and that you
            continue to use it in the future. Thank you so much again for
            giving our system a shot and I hope all your campaigns with this
            system go well.

            <br/>Sincerely,<br/>Joseph Bourque
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