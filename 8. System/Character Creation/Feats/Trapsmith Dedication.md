---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trapsmith|Trapsmith]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Snarecrafter Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use glimmering gears and gnashing mechanisms to manufacture snares using specialized parts. Your snares include clockwork and steam-powered cogwheels and gears, and their gush of steam can hinder those you ensnare. If you choose to construct a snare using gears and a creature fails their saving throw against the snare, all creatures are [[Concealed]] to that creature for 1 round, as a burst of steam obscures its vision.

**Special** You can select the dedication feat for the Trapsmith archetype even if you haven't yet gained three feats from the Snarecrafter archetype.

**Source:** `= this.source` (`= this.source-type`)
