---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fighter]]", "[[Ranger]]", "[[Rogue]]", "[[Stance]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a two-handed hammer, spear, or polearm.

You enter a stance that allows you to leverage the haft of your weapon to brutal effect as an effective and frighteningly efficient weapon in its own right. You treat the haft of your wielded weapon as a simple weapon dealing 1d4 bludgeoning damage. The haft is in the club group and has the agile and finesse traits. The haft shares any fundamental runes attached to the main weapon, so long as it would normally qualify for them.

While in Haft Striker Stance, you can use feats and abilities that normally require you to be wielding two melee weapons each in a different hand, treating the haft as the second weapon, but you can't use abilities that require you to be wielding a two-handed weapon.

**Source:** `= this.source` (`= this.source-type`)
