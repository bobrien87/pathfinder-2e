---
type: deity
source-type: "Remaster"
domains: "Duty, Earth, Trickery, Tyranny"
favored-weapon: "Light-hammer"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Ant Haul]], Rank 3: [[Haste]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The ancient adversary of the dwarven pantheon, Droskar once served Torag and lived among his holy family as the Father of Creation's most gifted student. But on the day Torag discovered that Droskar's seeming mastery of blacksmithing was a lie, his ingenious designs actually the creation of a demigod he'd secretly enslaved, a schism erupted. Disgusted, the Father of Creation cast Droskar out of Heaven's caverns, cursing him to never create an original work—but not before spiteful Droskar slew his captive, ensuring that the now-forgotten demigod couldn't usurp his place at Torag's forge.

Alone, rejected by the dwarves who had once worshipped him as a master artificer, Droskar raged. Hadn't he accomplished great works? True, he had enslaved another to achieve them—but didn't all gods use lesser creatures? Torag himself had legions of celestial servitors to carry out his commands. For him to punish Droskar for doing the same was clearly hypocrisy of the highest order. Brooding on such thoughts, the Dark Smith grew ever more spiteful, convinced of the injustice of his sentence.

It was in this twisted state that he heard the wailed prayers of a civilization on the edge of collapse—those dwarves who had refused to leave their ancestral Darklands cities during the Quest for Sky. Left behind by their kin and abandoned by Torag for their heresy, the dwarves found themselves beset by enemies on all sides, their numbers too few to adequately defend their homes. Despairing, they cried out for help from any god who'd listen.

And Droskar answered. Appreciating the symbolism of taking on those mortals betrayed by Torag, Droskar offered them salvation—power and protection in both the mortal world and the afterlife. Through the magic he provided, the forsaken dwarves could reclaim the shattered remnants of their empire. Yet in return, he demanded that they toil under his command for eternity.

**Title** The Dark Smith

**Areas of Concern** Cheating, exploitation, toil

**Edicts** Achieve goals at any cost, continually improve your abilities, establish dominance, work ceaselessly

**Anathema** Fail to work toward goals or grow in skill, relax excessively or give in to sloth

**Religious Symbol** fire under stone arch

**Sacred Animal** beetle

**Sacred Colors** gray, orange

**Source:** `= this.source` (`= this.source-type`)
