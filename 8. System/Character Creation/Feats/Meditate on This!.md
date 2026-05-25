---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Emotion]]", "[[Incapacitation]]", "[[Mental]]", "[[Rage]]"]
prerequisites: "trained in Medicine or Tian Xia Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

You meditate to alter your qi, coloring it with your resentment and anger. Until the start of your next turn, whenever you hit a creature with an unarmed Strike, or an adjacent creature deals piercing, slashing, or bleed damage to you, the creature that you hit or that damaged you must attempt a [[Will]] save against your class DC. The creature is then temporarily immune for 1 minute.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
