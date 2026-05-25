---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Additive]]", "[[Alchemist]]", "[[Olfactory]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can mix ingredients with a powerful sour smell into an alchemical bomb to make its explosion an overpowering stench. Any creature hit by the bomb must attempt a [[Fortitude]] save against your class DC in addition to the bomb's normal effects.
- **Success** The creature is unaffected beyond a strong craving for pickles.
- **Failure** The creature is [[Sickened]] 1.
- **Critical Failure** The creature is [[Sickened]] 2, and [[Fleeing]] for 1 round from the smell.

**Source:** `= this.source` (`= this.source-type`)
