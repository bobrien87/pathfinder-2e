---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Awakened animal]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have retained your sharp animal senses even after awakening. Choose one of the following senses appropriate to your kind of animal: darkvision, echolocation 10 feet, low-light vision, scent (imprecise) 30 feet, or tremorsense (imprecise) 30 feet. (Echolocation allows you to use hearing as a precise sense at the listed range.) If your animal kind doesn't typically have a specific type of sense, you can't gain that sense with this feat.

**Special** You can take this feat multiple times, choosing a different sense each time.

**Source:** `= this.source` (`= this.source-type`)
