---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained to resist the manipulations of fiends, and your Hellknight discipline makes you difficult to influence. You gain a +1 circumstance bonus to saves against effects that could inflict the controlled or frightened conditions.

If a mental effect would compel you to act in a way that violates your Hellknight order's tenets (as determined by the GM), you can attempt to break free from the effect as a free action triggered by receiving the violating order, and you gain a new Will save against the effect. You can attempt this save even if the effect would normally prevent you from acting of your own volition. You can attempt this new save only once for a given effect, even if you're compelled to violate your order's tenets multiple times. You can't receive a worse result on this Will save than you originally got against the compelling mental effect.

**Source:** `= this.source` (`= this.source-type`)
