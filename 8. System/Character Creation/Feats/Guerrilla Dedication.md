---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Stealth and Survival"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're skilled in subtle tactics and using the environment against your enemies. You become trained in your choice of Deception or Thievery; if you are already trained in both, you become an expert in one instead. When you take this dedication, choose a single, discrete urban or wilderness location, such as "Mzali" or "the Verduran Forest"; this becomes your favored location. When you are in this location and undetected by all enemies, you can [[Sneak]] without attempting a Stealth check as long as you move no more than half your Speed. During exploration, this also allows you to automatically approach within 15 feet of other creatures while Avoiding their Notice, as long as they aren't actively Searching or on guard.

You can change your favored location by spending 1 week of downtime in the new location you would like to set as your favored location.

Guerrilla

**Source:** `= this.source` (`= this.source-type`)
