---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Fire]]", "[[Kitsune]]"]
prerequisites: "Foxfire"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you critically hit with a [[Foxfire]] Strike, the target takes an additional 1d4 persistent damage of the same type as the foxfire. You gain an item bonus to this persistent damage equal to the foxfire's item bonus to attack rolls. When the target taking persistent damage comes into physical contact with another creature (for instance, if one of its allies touches it while [[Administering First Aid]]), you can use a reaction to command the flame to leap to the second target, ending the persistent damage on the first creature and moving it to the second.

**Source:** `= this.source` (`= this.source-type`)
