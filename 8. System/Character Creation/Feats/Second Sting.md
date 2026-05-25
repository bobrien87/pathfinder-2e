---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Press]]", "[[Ranger]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding two melee weapons, each in a different hand.

You read your prey's movements and transform them into openings, so failures with one weapon set up glancing blows with the other. Make a melee Strike with one of the required weapons against your hunted prey. The Strike gains the following failure effect.
- **Failure** You deal the damage the other required weapon would have dealt on a hit, excluding all damage dice. (This removes dice from weapon runes, spells, and special abilities, not just weapon damage dice.)

**Source:** `= this.source` (`= this.source-type`)
