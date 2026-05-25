---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Spellshape]]"]
prerequisites: "War Mage Dedication, you can cast the shield cantrip"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a shield.

You can empower your defensive magic by channeling it through a physical shield. If your next action is to cast the [[Shield]] cantrip, you use your shield as a locus to cast the spell, raising a magical barrier in the form of a large force projection of your worn shield. You can choose for an adjacent ally to gain the benefits of the *shield* spell instead of yourself. If the ally would take damage from a physical attack while protected by your *shield* cantrip, you can use your reaction to [[Shield Block]] with the spell on their behalf.

**Source:** `= this.source` (`= this.source-type`)
