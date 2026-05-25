---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Munitions Master|Munitions Master]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Flourish]]", "[[Unstable]]"]
prerequisites: "Munitions Master Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You Launch your light mortar.

**Requirements** You are adjacent to your light mortar.

Your innovation contains a chamber to store a small amount of compressed exhaust gas from your Launches. You can release this gas coinciding with the recoil to propel your mortar and yourself through the air to reach a better firing position. You and your light mortar move up to the light mortar's Speed in the direction of your choice. You must end this movement adjacent to your innovation.

**Source:** `= this.source` (`= this.source-type`)
