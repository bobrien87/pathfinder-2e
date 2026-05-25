---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Primal]]", "[[Yaksha]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As the earth drinks the light of sun and moon, so does your steady vow imbibe superlunary forces, ready to be unleashed with a moment's mantra. You can cast [[Cosmic Form]] on yourself as a 7th-rank primal innate spell once per day, your shadow lengthening and becoming a mandala of fundamental energies. In addition to the spell's normal effects, you can Sustain the spell to switch between the sun battle form and the moon battle form once per turn.

**Source:** `= this.source` (`= this.source-type`)
