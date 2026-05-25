---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mental]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can detect the flickers of mental activity let off by all thinking creatures. You gain [[Thoughtsense]] as a vague sense that has a range of 30 feet-like all vague senses, it's only about as precise as an average human's sense of smell, meaning you generally can predict only if a creature is present. Your thoughtsense detects only thinking creatures, so a creature that is unthinking or otherwise immune to mental effects (such as many constructs and oozes) can't be perceived using your thoughtsense, regardless of how precise it is.

While your Psyche is Unleashed, your thoughtsense upgrades to an imprecise sense, letting you use it to [[Seek]] out creatures.

**Source:** `= this.source` (`= this.source-type`)
