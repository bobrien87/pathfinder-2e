---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Flourish]]", "[[Monk]]", "[[Occult]]", "[[Water]]"]
prerequisites: "Reflective Ripple Stance"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're hit by a physical melee attack by an attacker you can see that's in reach.

**Requirements** You're in Reflective Ripple Stance.

After the triggering attack is done, Step. You must end this Step within the attacker's reach. Then, you can attempt an Athletics check to [[Disarm]] or [[Trip]] the attacker.

**Source:** `= this.source` (`= this.source-type`)
