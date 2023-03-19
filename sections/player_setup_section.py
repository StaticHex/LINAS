"""
Class used explain the basics of character creation for a system
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List

class NewPlayerSetupSection:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used explain the basics of character creation for a system

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
        self.__html.append(f'    {self.__contents.single("new player setup")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Another one of the major goals of this system is to keep character
            creation as  flexible and open as possible. with this in mind,
            players should always be  encouraged to create new races, or classes
            for their characters. If a player  decides to create their own class
            or race they should work with the DM to  ensure that the addition
            makes sense. With that in mind; character creation
            """
        )]
        self.__html.append("    <h3><u>1. Create Your Character's Background:</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            The first step in character creation should be to flesh out each
            player's  character as a living entity. A character's race, stats,
            class, etc. should  flow from who that character is as a living
            breathing creature; not the other  way around. Since LINAS relies
            so heavily on narration, it is very important  that characters be
            thought of in terms of their background vs. in terms of
            """
        )]
        self.__html.append("    <h3><u>2. Choose a Race and Class</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            After players decide on their character's background, the next step
            is to  choose a race and class for the character. The race and class
            should support  the character's background and most important it
            should be a race and class the character wants to play vs. a race
            and class the player "thinks will do the best." When creating a
            character, some good questions to ask are: How does the character
            fit into society? Are they well liked? An outcast? etc.

            The DM should be actively involved in all character creation
            regardless of  whether it's custom or stock. Also, it is advised that
            when creating custom  races or classes that the custom Race/Class
            sections be used as a template  (respectively) as this will help
            ensure that the created content is somewhat 
            """
        )]
        self.__html.append("    <h3><u>3. Choose Stats and Skills</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            By default, each player gets 3 points in HP + 7 points to divide out
            among HP  and TP in any way they choose. Additionally, each player
            gets gets 1 stat points and up to 2 skill points. These points are
            given in addition to any stats or  skills provided by their race and
            class by default. The DM may modify these amounts,  especially if
            wanting to run a higher level campaign. The idea being to try and
            make characters a bit more rounded out. Once again, the DM should
            work with each player to make sure their character's skill selection
            both follows the net rule of zero and also to ensure that all skills
            chosen (both positive and negative) make sense in relation to the
            character's.
            """
        )]
        self.__html.append("    <h3><u>4. Buy Items</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Each player is given 250G to start out. The DM may modify this amount
            to be  more or less depending on how much they want each player to
            start out with.  Players may also want to save their gold as shop
            amounts may offer better deals 

            It should also be noted that a player will not need to purchase items
            required  for their craft in most cases as these are considered class
            items and the  player is given an item for free. However, the player
            may also want to give  their character a bit of an edge such as
            buying a better weapon than the oneprovided by their class.
            """
        )]
        self.__html.append("    <h3><u>5. Additional Items and finishing Touches</u></h3>")
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Players can swap out their class ability for alternate abilities if
            desired and  also hammer out specific things about chosen lore,
            additional learned  languages, etc. The DM will also work with any
            characters with crafting skills 

            The goal here is to polish each character and make sure nothing feels
            off or  incomplete. To put it another way; this is where you polish
            the rough draft of  your character into the final copy. The DM should
            work with players closely  during this last step to ensure they are
            aware of all changes being made so  that there are no surprises or
            miss steps when running the campaign either on 
            """
        )]
# ==============================================================================
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