---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Gnome]]"]
frequency: "once per P1W"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** twice per week

The connection between you and the First World resonates within your body stronger than it does for most gnomes, allowing you to cross the threshold between the Universe and the First World. You gain [[Interplanar Teleport]] as a primal innate spell. You can cast it twice per week. This can be used only to travel back and forth between the First World and the Universe. Due to your body's natural resonance, you can act as a locus for the spell, and you don't require a specially attuned planar key.

**Source:** `= this.source` (`= this.source-type`)
