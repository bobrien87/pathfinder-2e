---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]", "[[Spellshape]]"]
prerequisites: "War Mage Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The devastation wrought by your large-scale spells is particularly terrifying. If the next action you use is to Cast a Spell that deals damage in an area, any target who fails their saving throw is also [[Frightened]] 1 (or [[Frightened]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
