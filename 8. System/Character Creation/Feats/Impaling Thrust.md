---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a melee weapon that deals piercing damage.

You impale your enemy and hold it in place with your weapon, and leave it bleeding when it gets free. Make a melee Strike with a melee weapon that deals piercing damage. If the Strike hits and deals damage, your target is [[Grabbed]] until it successfully Escapes, you attack with the weapon again, or you Release the required weapon, whichever comes first. When the target is no longer grabbed, it takes persistent bleed damage equal to the weapon's number of weapon damage dice.

**Source:** `= this.source` (`= this.source-type`)
