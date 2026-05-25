---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Hellbreaker Dedication"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're constantly on guard, keeping watch over your allies against fiendish forces—no one can get the jump on your group while you're around. Choose an ally you can see within 30 feet. They gain a +1 circumstance bonus to their AC and Reflex saving throws against devils and creatures allied with the Chelaxian government (as determined by the GM) until the beginning of your next turn. This action gains the visual trait, the auditory trait, or both, depending on how you alert your ally.

> [!danger] Effect: High Alert

**Source:** `= this.source` (`= this.source-type`)
