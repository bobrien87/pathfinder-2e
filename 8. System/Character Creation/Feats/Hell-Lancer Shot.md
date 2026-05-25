---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Golden Legionnaire Dedication, trained in martial firearms"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Make a ranged Strike with a firearm against a fiend, ignoring the fiend's [[Concealed]] condition and any lesser cover. If this Strike hits, you gain a circumstance bonus to damage equal to twice the number of weapon damage dice. This counts as two attacks when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
