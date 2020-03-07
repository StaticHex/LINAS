"""
================================================================================
= Category Class                                                               =
= ---------------------------------------------------------------------------- =
= Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
= Completed On: 02/17/2020                                                     =
= Last Updated: 02/17/2020                                                     =
= ---------------------------------------------------------------------------- =
= description:                                                                 =
= Helper class used by the Memory, and Loader classes. Defines a category in   =
= the user guide which will either have a list of entries or a list of         =
= sections defined under it.                                                   =
================================================================================
"""
# imports:
from __future__ import print_function, division
from collections import OrderedDict
from obj_classes.section import Section

class Category:
    """
    ============================================================================
    = Constructor                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Sets up the name, as well as a list of sections and entries. Only one    =
    = of these two dicts will actually be in use at a given time.              =
    ============================================================================
    """
    def __init__(
            self,   # (Ref) Reference to this class, required by all members
            name    # (String) The name of the category to create
        ):
        self.name       = name
        self.__sections = OrderedDict()
        self.__entries  = OrderedDict()

    """
    ============================================================================
    = Add Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Either adds a new section or new entry to the category. It should be     =
    = noted that after the first section/category is added that this becomes   =
    = locked. Meaning you cannot change from sections to categories or vise    =
    = versa from that point on.                                                =
    ============================================================================
    """
    def add(
        self,                   # (Ref) Reference to this class, required by all
                                # members

        section     = '',       # (String) The name of the new section to add

        description = '',       # (String) The description for the new section
                                # to add
                             
        entry       = None,     # (Ref) Reference to a json object to either
                                # add to the specified section or to add to
                                # the category if no section was specified

        field       = 'name'    # (String) The field to use as a key when
                                # adding the entry. Most of the time this
                                # will just be name
    ):
        # We don't care about case here
        section = section.lower()
        
        # If we defined a section to add and we haven't previously added any
        # entries, attempt to add to the specified section
        if section and len(self.__entries) == 0:
            # If we passed in a description, assume we're creating a new 
            # section
            if description:
                self.__sections[section] = Section(section, description)
            # Case for if we want to both create a section AND add to it
            if entry != None:
                self.__sections[section].add(field, entry)
        else:
            # If we aren't trying to add a section, make sure we didn't add a
            # section previously and if not; add a new entry
            if entry != None and len(self.__sections) == 0:
                self.__entries[entry[field].lower()] = entry

    """
    ============================================================================
    = Get Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Either adds a new section or new entry to the category. It should be     =
    = noted that after the first section/category is added that this becomes   =
    = locked. Meaning you cannot change from sections to categories or vise    =
    = versa from that point on.                                                =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Ref) Either returns a section or a json data entry depending on what    =
    = was loaded into the category.                                            =
    ============================================================================
    """    
    def get(
        self,   # (Ref) Reference to this class, required by all members
        name='' # (String) Name of the section/entry to get from the category
    ):
        name = name.lower()
        if len(self.__sections):
            return self.__sections[name]
        return self.__entries[name]

    """
    ============================================================================
    = Get Content Names Method                                                 =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Either returns a list of sections or a list of entities depending on     =
    = what is loaded into the category                                         =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (List<String>) Either returns a list of section names or a list of entry =
    = names depending on what is loaded into the category.                     =
    ============================================================================
    """      
    def getContentNames(
        self,       # (Ref) Reference to this class, required by all members
        sort=False  # (Boolean) Whether to sort the data being returned or not
    ):
        # case for if we specified to sort
        if sort:
            # case for returning sorted list of sections
            if len(self.__sections):
                return [
                    x
                    for x in 
                    sorted(self.__sections)
                ] 
            # case for returning sorted list of entries
            return [ 
                x 
                for x in
                sorted(self.__entries)
            ]
        # case for returning unsorted list of sections
        if len(self.__sections):
            return [
                x
                for x in
                self.__sections
            ]
        # case for returning unsorted list of entries
        return [
            x
            for x in
            self.__entries
        ]

    """
    ============================================================================
    = Exists Method                                                            =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Checks whether an entry exists in the category or not                    =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Boolean) True if the entry does in fact exist, and false otherwise.     =
    = Also returns false if an exception was thrown while trying to access the =
    = entry.                                                                   =
    ============================================================================
    """        
    def exists(self, section = '', name = ''):
        section = section.lower()
        name = name.lower()
        try:
            # Case for if we're looking for an entry in a section
            if len(self.__sections):
                if section in self.__sections:
                    return self.__sections[section].exists(name)
            # Case for if we're directly looking for an entry in our category
            if name in self.__entries:
                return True
            return False
        # Case for if an error was thrown while checking
        except:
            return False

    """
    ============================================================================
    = Str Method                                                               =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Override what happens when this object is cast to a string. In our case  =
    = we print a pretty tree representation of the category.                   =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (String) A string representation of this object.                         =
    ============================================================================
    """  
    def __str__(self):
        # Start by initializing the return string with our category name
        ret_str=self.name+'\n'

        # Case for if this is a section category
        if len(self.__sections):
            # Get a list of sections for the category and loop over them
            s_keys = list(self.__sections.keys())
            for i in range(0, len(s_keys)):
                sec_sp = ' '*(len(self.name) - 1)
                # Add section name to our return string
                ret_str += '{sp}{deco}{name}\n'.format(
                    sp      = sec_sp,
                    deco    = '|_',
                    name    = s_keys[i]
                )
                # Get a list of entries for each section and loop over them
                entries = self.__sections[s_keys[i]].getEntryNames()
                for j in range(0, len(entries)):
                    # Add section entry to our return string
                    ret_str += '{pre}{bar}{sp}{deco}{name}{ret}'.format(
                        pre     = sec_sp,
                        # If this is the last section, don't print a | for the
                        # entry
                        bar     = len(s_keys) - 1 - i and '|' or ' ',
                        sp      = ' '*(len(s_keys[i])),
                        deco    = '|_',
                        name    = entries[j],
                        # If this is the last entry, don't print the \n
                        ret     = len(entries) - 1 - j 
                                  and '' or '\n'
                    )
        # Case for if this is a direct entry category
        if len(self.__entries):
            # Get a list of entries for each section and loop over them
            e_keys = list(self.__entries.keys())
            for i in range(0, len(e_keys)):
                ret_str += '{sp}{deco}{name}{ret}'.format(
                    sp      = ' '*(len(self.name) - 1),
                    deco    = '|_',
                    name    = e_keys[i],
                    # If this is the last entry, don't print the \n
                    ret     = len(e_keys) - 1 - i and '\n' or ''
                )
        # Return our string representation for this object
        return ret_str
