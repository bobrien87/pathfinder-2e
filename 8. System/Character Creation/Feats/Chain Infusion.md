---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Infusion]]", "[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The elemental matter in your blast keeps reconstituting itself to travel onward, no matter how many bodies it collides with. If your next action is an [[Elemental Blast]] and it hits, attempt a new ranged Elemental Blast from the target against a different creature that's within the blast's range, measuring from the creature you hit. You can keep chaining the blast in this way each time you hit. Your multiple attack penalty applies normally to any blasts in the chain after the first. You can make up to five blasts total, but you can't target the same creature more than once. Roll damage only once and apply it to each creature you hit. (If you start with a melee blast, you still add your Strength to only that blast, not the successive ranged blasts.)

**Source:** `= this.source` (`= this.source-type`)
