---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Animist]]", "[[Apparition]]", "[[Aura]]", "[[Exploration]]"]
prerequisites: "Apparition Sense"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your allied apparitions ward you against the predations of their restless peers. You and allies in a @Template[type:emanation|distance:30] gain a +2 status bonus to [[Recall Knowledge]] checks about spirits, haunts, and undead. While you're [[Searching]] or [[Detecting Magic]] in exploration mode, this bonus also applies to AC and saves against reactions any of you trigger from haunts and spirits. During your first turn in an encounter, you and allies in the aura have resistance equal to half your level against damage dealt by haunts or spirits.

**Source:** `= this.source` (`= this.source-type`)
