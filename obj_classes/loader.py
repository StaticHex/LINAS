"""
================================================================================
= Loader Class                                                                 =
= ---------------------------------------------------------------------------- =
= Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
= Completed On: 02/17/2020                                                     =
= Last Updated: 02/17/2020                                                     =
= ---------------------------------------------------------------------------- =
= description:                                                                 =
= Class responsible for loading in the dynamically defined and expandable      =
= sections of the system. These are kept in memory to make things like         = 
= character creation and section management easy.                              =
================================================================================
"""
# imports:
from __future__ import print_function, division
from obj_classes.memory import Memory
import json
import re

class Loader:
    """
    ============================================================================
    = Constructor                                                              =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Sets up the internal memory object and loads assets from file into the   =
    = internal memory object.                                                  =
    ============================================================================
    """
    def __init__(
        self,                           # (Ref) Reference to this class,
                                        # required by all members

        loadPath    = './sections/',    # (String) Folder to look for data files
                                        # in

        debug       = False):           # (String) Whether to print debug info
                                        # or not
        self.__templates    = {}
        self.__memory       = Memory()
        self.__dir          = loadPath
        self.__debug        = debug

        # load assets from file
        self.__load_templates('templates.json')
        self.__load_simple('stats.json',        'stats', 'abbr')
        self.__load_skills('skills.json')
        self.__load_simple('languages.json',    'languages')
        self.__load_simple('races.json',        'races')
        self.__load_simple('classes.json',      'classes')
        self.__load_abilities('abilities.json')
        self.__load_spells('spells.json')
        self.__load_effects('effects.json')

        if debug:
            print(self.__memory)

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
        return self.__memory.get(category)

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

        # Pass off the real work to the memory class
        return self.__memory[category].exists(section, name)

    """
    ============================================================================
    = Load Simple Method                                                       =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """ 
    def __load_simple(
        self,           # (Ref) Reference to this class, required by all
                        # members

        file,           # (String) The name of a file to load from

        cat,            # (String) The name of the category to place the loaded
                        # data under

        field='name'    # (String) The field to use as a key when loading
    ):
        jdata = self.__load_json_data(file)
        self.__memory.add(cat)
        for entry in jdata:
            self.__memory.add(
                category    = cat,
                entry       = entry,
                field       = field
            )

    """
    ============================================================================
    = Load Spells Method                                                       =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """ 
    def __load_spells(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from        
    ):
        jdata = self.__load_json_data(file)
        cat = 'spells'
        self.__memory.add(cat)
        for section in jdata:
            sec_name = section['title']
            sec_desc = section['description']
            self.__memory.add(
                category        = cat,
                section         = sec_name,
                description     = sec_desc
            )
            for spell in section['spells']:
                self.__memory.add(
                    category    = cat,
                    section     = sec_name,
                    entry       = spell
                )

    """
    ============================================================================
    = Load Skills Method                                                       =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """     
    def __load_skills(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from
    ):
        jdata = self.__load_json_data(file)
        cat = 'skills'
        self.__memory.add(cat)
        for section in jdata:
            sec_name = section['title']
            sec_desc = section['description']
            self.__memory.add(
                category    = cat, 
                section     = sec_name, 
                description = sec_desc
            )
            for skill in section['skills']:
                self.__memory.add(
                    category    = cat,
                    section     = sec_name,
                    entry       = skill
                )

        """
    ============================================================================
    = Load Effects Method                                                      =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """     
    def __load_effects(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from
    ):
        jdata = self.__load_json_data(file)
        cat = 'effects'
        self.__memory.add(cat)
        for section in jdata:
            sec_name = section['title']
            sec_desc = section['description']
            self.__memory.add(
                category    = cat, 
                section     = sec_name, 
                description = sec_desc
            )
            for skill in section['entries']:
                self.__memory.add(
                    category    = cat,
                    section     = sec_name,
                    entry       = skill
                )

    """
    ============================================================================
    = Load Abilities Method                                                    =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """     
    def __load_abilities(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from
    ):
        jdata = self.__load_json_data(file)
        cat = 'abilities'
        self.__memory.add(cat)
        for section in jdata:
            sec_name = section['title']
            sec_desc = section['description']
            self.__memory.add(
                category    = cat, 
                section     = sec_name, 
                description = sec_desc
            )
            for ability in section['abilities']:
                if '<t>' in ability:
                    t_key = ability['<t>']
                    for t in self.__templates[t_key]:
                        expanded = {}
                        expanded['name'] = ability['name'].format(**t)
                        expanded['description']=[
                            x.format(**t)
                            for x in ability['description']
                        ]
                        self.__memory.add(
                            category    = cat,
                            section     = sec_name,
                            entry       = expanded
                        )
                else:
                    self.__memory.add(
                        category    = cat,
                        section     = sec_name,
                        entry       = ability
                    )

    """
    ============================================================================
    = Load Templates Method                                                    =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = looks for the specified file in the __dir directory and attempts to load =
    = its contents into the memory object                                      =
    ============================================================================
    """     
    def __load_templates(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from
    ):
        jdata = self.__load_json_data(file)
        self.__templates = jdata

    """
    ============================================================================
    = Load Json Data Method                                                    =
    = ------------------------------------------------------------------------ =
    = description:                                                             =
    = Function responsible for actually loading in the json data from file and =
    = formatting it into a dict object.                                        =
    = ------------------------------------------------------------------------ =
    = returns:                                                                 =
    = (Ref) A json object, no set format and structure depends on object being =
    = loaded.                                                                  =
    ============================================================================
    """
    def __load_json_data(
        self,   # (Ref) Reference to this class, required by all members
        file    # (String) The name of a file to load from
    ):
        f = open(self.__dir+file,'r')
        jdata = json.loads(f.read())
        f.close()
        return jdata