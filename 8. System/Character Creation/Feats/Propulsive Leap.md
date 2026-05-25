---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By expelling flames from your feet or levitating through electrical repulsion, you propel yourself through the air. For 1 minute, you gain a fly Speed equal to your Speed or 20 feet, whichever is greater. If you aren't on solid ground at the end of your turn, you must attempt another backlash check for your deviation, though you remain airborne even if you fail your check unless the damage from the check renders you [[Unconscious]].

> [!danger] Effect: Propulsive Leap

**Awakening** You blast through the air at great speed, gaining a +15-foot status bonus to your Fly speed from Propulsive Leap.

**Awakening** You can use your propulsion as a makeshift weapon. The first time each round you Fly starting from the ground, all creatures adjacent to you take 1d4 damage for every 2 levels you have, with a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
