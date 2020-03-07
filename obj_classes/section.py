"""
================================================================================
= Section Class                                                                =
= ---------------------------------------------------------------------------- =
= Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
= Completed On: 02/17/2020                                                     =
= Last Updated: 02/17/2020                                                     =
= ---------------------------------------------------------------------------- =
= description:                                                                 =
= Helper class used by the  Category, Memory, and Loader classes. Defines a    =
= section in the user guide complete with a name, a description, and a set of  =
= entries listed under it.                                                     =
================================================================================
"""
# imports: 
from __future__ import print_function, division
from collections import OrderedDict

class Section:
    """
    ============================================================================
    = Constructor                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Sets up the name, description, and a new ordered dict of entries for the =
    = section.                                                                 =
    ============================================================================
    """
    def __init__(
        self,           # (Ref) Reference to this class, required by all members

        name,           # (String) The name of the section being created

        description     # (String) A description as to the kind of entries this
                        # section contains
    ):
        self.name = name
        self.description = description
        self.__entries = OrderedDict()

    """
    ============================================================================
    = Add Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Adds a new entry to the section's entry list.                            =
    ============================================================================
    """
    def add(
        self,   # (Ref) Reference to this class, required by all members 

        field,  # (String) The field to use as a key to reference the entry
                # data. Most of the time this is name.

        entry   # (Ref) A reference to a json data object. No set structure.
    ):
        self.__entries[entry[field].lower()] = entry

    """
    ============================================================================
    = Exists Method                                                            =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Checks whether an entry exists in the section or not                     =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Boolean) True if the entry does in fact exist, and false otherwise.     =
    = Also returns false if an exception was thrown while trying to access the =
    = entry.                                                                   =
    ============================================================================
    """    
    def exists(
        self,   # (Ref) Reference to this class, required by all members
        name    # (String) The name of the entry to check the section for
    ):
        name = name.lower()
        try:
            if name in self.__entries:
                return True
            return False
        except:
            return False

    """
    ============================================================================
    = Get Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Used to access the data for an individual entry                          =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Ref) The data for the specified entry                                   =
    ============================================================================
    """    
    def get(
        self,   # (Ref) Reference to this class, required by all members
        name    # (String) The name of the entry to access data for
    ):
        name = name.lower()
        return self.__entries[name]

    """
    ============================================================================
    = Get Entry Method                                                         =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Used to get a list of all entries currently loaded into the section.     =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (List<String>) By default, returns a list of entries in alphabetical     =
    = order. However, the option to sort can be turned off resulting in a list =
    = of entries as they were loaded into the section                          =
    ============================================================================
    """     
    def getEntryNames(
        self,           # (Ref) Reference to this class, required by all members
        sort=True       # (Boolean) Whether to sort what we're returning or not
    ):
        # If we specified to sort, return this as sorted
        if sort:
            return [ 
                x 
                for x in
                sorted(self.__entries)
            ]
        # If we made it here, we just want a list of entries without bothering
        # to sort
        return [
            x
            for x in
            self.__entries
        ]

