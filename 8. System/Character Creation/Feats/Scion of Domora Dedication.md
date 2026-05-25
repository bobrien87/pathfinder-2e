---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scions Of Domora|Scions Of Domora]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Familiar Master Dedication, you have befriended a spirit guide and it bonded with you using its Bond with Mortal ability."
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain a spirit guide ally. Your familiar takes on the form of a spirit guide specific familiar.

**Special** You can take Scion of Domora Dedication even if you have the [[Familiar Master Dedication]] and have not taken two other Familiar Master feats. You can't select another dedication feat until you have gained at least two other feats from the scion of Domora or familiar master archetypes.

**Source:** `= this.source` (`= this.source-type`)
