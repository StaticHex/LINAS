"""
Class used to create the combat section for a system, covers basic combat
If you need specialized combat; you'll need to create a new one
"""
from __future__ import print_function, division
from obj_classes.content_manager import ContentManager
from typing import List

class CombatSystem:
    def __init__(
        self,
        system : ContentManager

    ) -> None:
        """
        Class used to create the combat section for a system, covers basic combat
        If you need specialized combat; you'll need to create a new one

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
        self.__html.append(f'    {self.__contents.single("combat")}')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Combat is one area of the system in which special attention was paid.
            The reason being that many systems I've played in the past (including
            my own) had the problem that once battle started, things sort of
            slowed down. After talking with some of my friends I realized I
            wasn't the only one who noticed this. This was a big part of the
            inspiration for moving towards a light 1d6 system; the theory being
            that the DM having to stop to do a large number of calculations is what
            leads to the slowdown. That being said, battle phases are usually very
            short and the flow of battle can be described below.
            """
        )]
        self.__html.append('    <u><h3>Pre-Battle</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
             All entities roll 1d6 for initiative (both enemies and party members).
             The speed stat is added to each entity's dice roll and turn order
             proceeds based on initiative score (highest score first and lowest
             score last). If there is a tie in any score e.g. two entities both
             roll a 5, use the entities' speed stat to break the tie. If the 
             entities both have the same speed and same roll, the tying entities
             re-roll until a winner is reached; with the winner taking the higher
             spot and the loser taking the lower spot. However, when rerolling
             to break a tie an entity keeps it's original initiative score instead
             of the re-rolled score. This is done mainly to provide a simple way
             to keep turn order consistent without having to re-roll more than
             needed which tends to break the flow of the game.

             <i>Example: Let's say one entity has a speed of 3 and rolls a 3 and
             another entity has a speed of 4 and rolls a 2 such that both entities
             have an initiative roll of 6. In this c ase, the entity with the
             speed of 4 would take the higher spot and the entity with a speed
             of 3 would take the lower spot since 4 > 3.</i>

             One final note about initiative is that if an entity's speed changes
             for any reason, the changes take effect immediately without the user
             having to re-roll. If the change moves their turn position past what
             would be the next entity's turn; they take their turn immediately
             instead.

             <i>Example: An entity who has an initiative score of 5 has a magic
             technique used on them by an ally which boosts their speed by 3 points 
             giving them an initiative score of 8 and causing the entity to move 
             earlier in the turn order. The next entity after the user, only has
             an initiative score of 7. The boosted entity will take their turn
             immediately interrupting the entity with a score of 7; even though
             their turn was next.</i>
            """
        )]
        self.__html.append('    <u><h3>During Battle</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Each entity gets 1 move and 1 action during their battle round by
            default. Some  abilities or items may change this however. An entity
            can perform an action and a move in any order they wish.

            The default movement range is 2; meaning an entity can move 2 squares
            in any direction (cannot move diagonally). If an entity has points in
            speed they are added to the entity's movement. For example, if an
            entity has a value of 2 in  speed, they are able to move 4 squares. 	  	  	

            Actions consist of anything an entity does during a turn other than
            movement. This includes: using items, using skills and attacking,
            etc. Each of these  is outlined in more detail below.            
            """
        )]
        self.__html.append('    <u><h4>Using Items</h4></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            By default, an entity doesn't have to roll to use an item. The item
            is simplyused, and any effects of the item go into place. However,
            some items do require a roll to be used and any items which require
            this will have the detailspertaining ot their roll listed on them.
            """
        )]
        self.__html.append('    <u><h4>Using Skills</h4></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            There is virtually no difference between using skills inside battle
            vs. outside.The entity using the skill simply performs their 1d6
            dice roll to see if theysucceed, and then resolves the skill's
            effects according to their dice roll. Formore information on how
            skills resolve see section 3 of this guide for a fullbreakdown of
            skill usage.
            """
        )]
        self.__html.append('    <u><h4>Attacking</h4></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Attacking is very similar to skill usage and uses the same flow
            regardless of whether using a technique or physical weapon.
            Once again this is done to keep thesystem simple and battle flow itself
            unfolds in the following manner.
            <ol><li>
            Attacking entity chooses a weapon (or technique) and a skill to attack with
            as well as a target to attack (or targets if applicable)
            </li><li>
            Attacking entity rolls 1d6 against the chosen skill to see if attack
            succeeds
            </li><li>
            If the attack was successful, the attacking entity adds any stat
            points theyhave to the weapon's (or technique's) damage and then deals
            that much damage totheir target (or targets).
            <ul><li>
            If the target entity's speed is higher than the attacking entity's
            speed, thetarget entity has an option to react to the attack.
            For more information on reactions, see the section below.
            </li><li>
            Special effects of attacks such as poison or paralysis usually
            resolve duringthis step as well
            </li><li>
            Note: each stat corresponds to a certain type of weapon. Strength
            to physicalmelee weapons, dexterity to physical ranged weapons,
            intelligence to magicweapons, etc.
            </li></ul></li><li>
            Damaged entities absorb as much damage as possible into their
            armor. Armorremains damaged for the remainder of the round and an
            entity gets their full armor value back at the beginning of the 
            round.
            <ul><li>
            Note: Unless specifically stated, armor values typically are only
            for physical attacks, not magic. This means that technique damage is not
            prevented unless the armor specifically mentions preventing magic
            damage.
            </li></ul></li><li>
            Damaged entities take any damage not absorbed by armor as damage
            to HP.
            </li></ol>

            <i>Example: A rogue character with 1 point in strength targets a goblin
            with 1armor using a knife with 2 damage. The rogue rolls a 5 which
            is a success. Therogue adds their strength to their knife's damage
            for a total of 3 points of damage. The goblin's armor absorbs 1 damage
            and the goblin loses 2 HP. Thegoblin now has 0 armor until the start
            of the next round.</i>

            It should also be noted that the only difference between attacking
            with a technique and a physical weapon is that techniques have an TP cost
            which is consumed when the technique is used. This means that the TP is
            lost regardless of whether the technique is successful or not.
            Additionally, techniques are not absorbed by physical armor meaning
            unless an entity has some sort of magic protection they take the
            full brunt of the attack.

            <i>Example: A mage with 2 intelligence chooses a fireball attack to
            attack a goblin with 1 armor. The fireball attack consumes 1 TP and
            deals 2 fire damage. The mage rolls a 2 which is a fail. The mage
            would normally have done 4 damage (2intelligence + 2 damage) to the
            goblin. However, since they failed, no damage is done. The mage still
            loses 1 TP for attempting the technique however.</i>
            """
        )]
        self.__html.append('    <u><h3>Reacting To Attacks</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            If the target's speed is higher than the attacker's speed, they have
            the option to react to the attack. They can either guard, in which
            case the damage taken is cut by the difference in speed; or they may
            use a technique or ability to counter the attack. One important note on
            countering is that the target entity still takes the initial damage
            from the attack unless the technique or ability either moves the target
            out of the way of the attack or somehow redirects the damage. Also,
            redirecting damage does not negate any other effects of the attack
            (such as status conditions).

            A few other things to note are that reactions can only be done in
            cases where one of the entities involved would take damage. Reactions
            cannot be used for beneficial actions such as healing or to avoid
            status conditions.

            <i>Example: A knight wearing plate armor attacks a mage wearing
            cloth armor. Due to the knight's heavy armor, they have a SPD of 0
            while the mage has a SPD of 1. Because of this, the mage gets to
            react to the attack and they choose to guard. The knight deals 4
            damage with their sword. However, the mage only takes 2 damage
            because their robe absorbs 1 damage and the difference between
            the knight and the mage's speed is 1. The mage's armor is now
            exhausted. and combat is now resolved. </i>

            <i>Example: A swordsman wearing plate armor attacks a swordsman
            wearing chainmail armor with a sword. The swordsman wearing
            chainmail armor has a SPD of 1 with penalty and the knight has a
            SPD of 0. The second swordsman chooses to counter attack with his
            own sword. Both swordsmen deal 4 damage to each other, and both
            have the damage absorbed by their armor. The swordsman in plate
            armor has 4 points of armor left for the round and the swordsman
            in chainmail's armor is exhausted for the round. </i>
            """
        )]
        self.__html.append('    <u><h3>Adjusted Speed</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Strength and speed share a unique relationship among stats through
            the calculation of speed penalties for weapons and armor. A
            character's adjusted speed is found with the following formula<br/>
            <br/>Points in Speed + (Points in Strength - Total Speed Penalty).
            <br/>NOTE: Adjusted speed can be negative. A negative adjusted speed
            means the value is subtracted from the initiative roll instead of
            added
            
            What this means, is the more points a character has in strength,
            the less they'll be affected by speed penalties on equipment. This
            is done to create a sort of soft strength requirement for weapons
            and armor.

            For example, a mage is perfectly able to equip a full set of plate
            armor. However, doing so will put them at a disadvantage as they'll
            be unable to react to attacks and enemies will be able to react to
            their attacks more easily. This would eliminate the mage's advantage
            of being able to attack at a distance as well as being able to dodge
            heavy hitting attacks easier; effectively making life much harder
            for them.
            """
        )]
        self.__html.append('    <u><h3>Destroying The Environment</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            As a general rule; rocks, trees, and other obstacles can be destroyed
            by attacking them as well as by certain techniques and abilities. Also
            as a general rule, obstacles usually have 5 HP unless the DM declares
            otherwise. The two most common classes of obstacles are wooden and
            stone. Wooden obstacles take double damage from earth and fire magic.
            Stone obstacles take double damage from wind magic. For more
            information on why this is; check out the element system explanation
            in section 9. Once an obstacle's HP reaches 0 it is destroyed and the
            DM determines what happens at that point. 

            <i> Example: A ninja uses a substitute skill to switch places with a
            nearby log. The log takes 10 damage the ninja would have taken
            otherwise and is destroyed. The ninja switches places with where the
            log was and the log ceases to be an obstacle. During the following
            round a mage uses a fire technique. The DM declares the wood chips from
            the log are still on the targeted space resulting in the fire technique
            dealing an additional point of damage. It should be noted the above
            example is just that, an example at as with most things in the system
            what happens is largely up to the DM</i>
            """
        )]
        self.__html.append('    <u><h3>Resolving Combat</h3></u>')
        self.__html += [ f'    {x}' for x in system.collapse(
            """
            Combat ends when one side has either been completely immobilized in
            some way or willingly surrenders (in some cases this isn't an option).
            In the case of immobilization, this usually means that all entities on
            one side of battle have their HP reach 0. This could also happen as the
            result of a technique or ability such as petrification. 

            After combat is finished, the DM determines what loot (if any) the
            defeated party leaves behind. If the players' party is defeated, the
            DM decides if something happens which would result in the campaign
            coming to an end or whether the party is able to continue their journey
            i.e. being captured or thrown in prison. 
            """
        )]
        self.__html.append("</div>")

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