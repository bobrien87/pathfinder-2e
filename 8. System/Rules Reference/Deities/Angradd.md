---
type: deity
source-type: "Remaster"
domains: "Fate, Fire, Protection, Zeal"
favored-weapon: "Greataxe"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Blistering Invective]], Rank 3: [[Fireball]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Forge-Fire, Army-Cleaver, High Marshall, The Tempered. Worshipers of Angradd call on him by many names as they join battle against enemies that threaten the stability of their communities. The most aggressive and proactive of the gods in the dwarven pantheon, Angradd calls on his followers to seek out and destroy foes of the dwarven people, not simply fortify themselves from danger or put their trust in defensive measures. Often depicted in art as a powerful, axe-wielding warrior with hair and beard of flame, Angradd is venerated by those burning with zeal to seek out and destroy evil. During the Quest for Sky, Angradd's followers often formed the vanguard for the migrating dwarven nation, striking out against the many monsters, hazards, and foes that stood between the dwarves and the surface. Philosophically, followers of Angradd consider each opponent they strike down to be fuel for their fire, contending that each challenge allows them to grow their strength and spread their god's influence like the light from a beacon in the darkness.

For Angradd's followers, the mere act of contending with evil on the battlefield is an act of worship, but the god's adherents also incorporate worship of the Forge-Fire into their daily activities, either as a sole focus or as a part of venerating the larger dwarven pantheon. Smiths consecrate weapons to Angradd as they are forged, and adherents often recite passages from Angradd's Tempering, the god's holy text, when maintaining their armaments. When age or injury prevent a follower from actively partaking in battle, they turn to training the next generation. Teachers called by Angradd excel in conveying battlefield strategy, and many are revered for their encyclopedic knowledge of foes' tactics, abilities, and weaknesses—knowledge typically hard won from a lifetime of practical experience. Even in retirement, the god's followers attempt to contribute to martial efforts by weaving his scarlet and gold war banners or gathering medical supplies to send to the front lines.

**Title** The Forge-Fire

**Areas of Concern** Fire, offensive war, tradition

**Edicts** Seek and destroy evil, study evil to learn the best way to destroy it, train others in righteous ways

**Anathema** Allow weaker evils to survive due to the presence of larger evils, deceive others outside of tactical gain

**Religious Symbol** fiery axe

**Sacred Animal** boar

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
