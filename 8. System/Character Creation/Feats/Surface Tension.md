---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Magus]]", "[[Water]]"]
prerequisites: "resurgent maelstrom hybrid study"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a broken weapon.

You encase the pieces of your broken weapon together with water you pull from the surrounding environment. The weapon's broken condition is temporarily suppressed, and the weapon deals an additional amount of bludgeoning damage equal to twice the number of weapon damage dice; this damage can't be changed to any other type. The weapon also gains the deadly d8 trait; if the weapon already had the deadly trait, the damage die increases by one step or to d8, whichever is higher. The first time you use this weapon to Spellstrike or get a critical success on an attack with it, the weapon is completely destroyed.

If the weapon has a Hardness greater than your level, or if it's an artifact, cursed item, or other item that's difficult to break or destroy, it is not destroyed, and this ability only lasts until the end of your turn.

**Source:** `= this.source` (`= this.source-type`)
