---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Magus]]"]
prerequisites: "resurgent maelstrom hybrid study"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Requirements** You're wielding an improvised weapon.

You pour energy into an improvised weapon, speeding its destruction to grant it power. The overloaded energy grants your improvised weapon the effect of the astral, corrosive, extending, or frost rune for 1 minute, after which the item is destroyed. If the item has a Hardness greater than your level, or if it's an artifact, cursed item, or other item that's difficult to break or destroy, it is not destroyed, and this ability only lasts until the end of your turn.

This effect doesn't count against the number of property runes a weapon can have based on its potency rune, but a given weapon can only have one application of Maelstrom Flow at a time.

**Source:** `= this.source` (`= this.source-type`)
