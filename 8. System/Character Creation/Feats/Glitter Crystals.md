---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Additive]]", "[[Alchemist]]", "[[Healing]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can mix a blend of crushed flowers and alchemical salt into an alchemical elixir with the healing trait or alchemical food. Choose one of the following effects: reduce the drained condition by 1, reduce the stupefied condition by 1, remove the [[Dazzled]] condition, or remove the [[Deafened]] condition. The creature who consumes the modified healing elixir or alchemical food gains this benefit in addition to the food or elixir's normal effects. This has no effect against permanent conditions.

**Source:** `= this.source` (`= this.source-type`)
