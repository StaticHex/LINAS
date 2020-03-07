"""
================================================================================
= Memory Class                                                                 =
= ---------------------------------------------------------------------------- =
= Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
= Completed On: 02/17/2020                                                     =
= Last Updated: 02/17/2020                                                     =
= ---------------------------------------------------------------------------- =
= description:                                                                 =
= Helper class used by the  Loader class. Defines an in-memory representation  =
= of all major components of the system such as skills, stats, items, entities,=
= etc. As well as methods for interacting with these components.               =
================================================================================
"""
# imports:
from __future__ import print_function, division
from obj_classes.category import Category
from obj_classes.section import Section
from collections import OrderedDict
class Memory:
    """
    ============================================================================
    = Constructor                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Sets up an empty memory object.                                          =
    ============================================================================
    """    
    def __init__(
        self    # (Ref) Reference to this class, required by all members
    ):
        self.__memory = OrderedDict()

    """
    ============================================================================
    = Add Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Adds a new item to memory. Can either be a category, section, or entry   =
    = and is determined based on parameters provided.                          =
    ============================================================================
    """    
    def add(
        self,                   # (Ref) Reference to this class, required by 
                                # all members
        category, 
        section     = '',       # (String) Name of the section to add to

        description = '',       # (String) Description to add if adding a
                                # new section

        entry       = None,     # (Ref) Reference to a json object to add if
                                # adding an entry.

        field       = 'name'    # (String) The field to use as a key for the
                                # entry if using a field different than name
    ):
        # Don't worry about case
        category = category.lower()
        
        # Check if category exists and create it if it doesn't
        if category not in self.__memory:
            self.__memory[category] = Category(category)
        
        # Pass off rest of details of adding to the Category class.
        self.__memory[category].add(section, description, entry, field)

    """
    ============================================================================
    = Get Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = used to access the data for a single category loaded into the internal   =
    = memory object. Accessing sections and entries is done by bubbling down   =
    = through the category class.                                              =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Ref) the data for a single category from the internal memory object.    =
    ============================================================================
    """      
    def get(
        self,       # (Ref) Reference to this class, required by all members
        category='' # (String) The category to look up in memory
    ):
        category = category.lower()
        return self.__memory[category]

    """
    ============================================================================
    = Get Category Names Method                                                =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Used to get a list of categories currently loaded into memory            =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (List<String>) A list of categories currently loaded into memory         =
    ============================================================================
    """       
    def getCategoryNames(
        self,       # (Ref) Reference to this class, required by all members
        sort=False  # (Boolean) Whether to sort the results or not
    ):
        if sort:
            return [
                x
                for x in
                sorted(self.__memory)
            ]
        return [
            x
            for x in
            self.__memory
        ]

    """
    ============================================================================
    = Exists Method                                                            =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Checks whether an entry exists in memory or not.                         =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Boolean) True if the entry does in fact exist, and false otherwise.     =
    = Also returns false if an exception was thrown while trying to access the =
    = entry.                                                                   =
    ============================================================================
    """    
    def exists(
        self,       # (Ref) Reference to this class, required by all members
        category,   # (String) The category to check for the entry in
        section='', # (String) The section to check for the entry in
        name=''     # (String) The name of the entry to check for
    ):
        # Don't care about case
        category = category.lower()
        section = section.lower()
        name = name.lower()

        # Really just passing off to the category class' version of this
        return self.__memory[category].exists(section, name)

    """
    ============================================================================
    = Str Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Override what happens when this object is cast to a string. In our case  =
    = we print a pretty tree representation of the entire memory structure.    =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (String) A string representation of this object.                         =
    ============================================================================
    """  
    def __str__(
        self    # (Ref) Reference to this class, required by all members
    ):
        ret_str=''
        for m in self.__memory.keys():
            ret_str += str(self.__memory[m])+'\n'
        return ret_str