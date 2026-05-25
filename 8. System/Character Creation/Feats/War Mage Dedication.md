---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "You have a spellcasting class feature."
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your studies into the battlefield applications of magic have made your spells particularly effective at disrupting enemy formations or manipulating enemy troops into positions where they are more vulnerable to wide-scale magical attacks. When you cast a non-cantrip spell that deals damage in an area, choose a number of targets equal to your Intelligence modifier who failed their saving throw against the effect. Move each one up to 10 feet from their original position after they take damage and any other effects from the spell. You can't move a creature into or through obstacles. A Medium or smaller creature counts as one target; a Large creature counts as two Medium creatures; and a Huge creature counts as four Medium creatures. You can't move Gargantuan creatures in this way.

You also gain the [[Additional Lore]] general feat for Warfare Lore. If you were already trained in Warfare Lore, you become trained in a Lore skill of your choice.

War Mage (Class Archetype)

**Source:** `= this.source` (`= this.source-type`)
