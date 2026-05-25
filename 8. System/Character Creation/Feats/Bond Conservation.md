---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Manipulate]]", "[[Spellshape]]", "[[Wizard]]"]
prerequisites: "arcane bond"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** The last action you used was to Cast a Spell enabled by [[Drain Bonded Item]].

By efficiently and carefully manipulating the arcane energies unleashed by your bonded item, you can conserve just enough power to cast another spell, though this second spell is slightly weaker. You gain an extra use of Drain Bonded Item. You can use it to cast a spell 2 or more ranks lower than the previous spell, and must use it before the end of your next turn or you lose it.

**Source:** `= this.source` (`= this.source-type`)
