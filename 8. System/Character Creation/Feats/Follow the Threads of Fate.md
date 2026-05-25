---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Exemplar]]", "[[Fortune]]", "[[Ikon]]"]
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a worn ikon made of cloth or a weapon ikon with a tassel, wrapping, or similar feature.

A norn's thread—spun from fate itself—runs through or wraps around your ikon.

**Transcendence—[[Unravel the Future]]** `pf2:1` (fortune, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.TIIM35m8aDUEU4gF inline]

**Source:** `= this.source` (`= this.source-type`)
