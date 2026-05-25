---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Nephilim]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your blood bears the mark of a demon, a living embodiment of sin from the fetid depths of the Outer Rifts. Demonic power pulses through your veins and manifests in a different way for each pitborn, whether you have webbed fingers and thrive in the water, large hands capable of wrestling larger foes, or some other manifestation. You are trained in Athletics. If you were already trained in Athletics (from your background or class, for example), you instead become trained in a skill of your choice.

You also gain any one common 1st-level skill feat with a prerequisite of trained in Athletics, as reflects the manifestation of your fiendish blood.

**Source:** `= this.source` (`= this.source-type`)
