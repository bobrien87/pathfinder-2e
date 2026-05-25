---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Centaur]]"]
prerequisites: "budding speaker centaur heritage or Speaker in Training"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As a Speaker, you've forged a deep bond with powerful spirits who you can urge to rise up to defend you and your people. If you're a Faithspeaker, you can call on gods or powerful planar beings to cast [[Share Life]] and [[Status]], each once per day as innate divine spells; if you're a Greenspeaker, you can call on the forces of nature to cast [[Entangling Flora]] and [[Environmental Endurance]], each once per day as innate primal spells.

**Source:** `= this.source` (`= this.source-type`)
