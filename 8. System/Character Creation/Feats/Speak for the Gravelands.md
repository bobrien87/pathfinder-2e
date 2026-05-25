---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Halcyon Speaker|Halcyon Speaker]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Halcyon Speaker Dedication, trained in Nature, can cast at least one spell with the vitality trait"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're a member of the Vellumis Scholars.

You have learned much of what the Gravelands need and are confident in your ability to speak for them. You gain the [[Geomancer Dedication]] archetype feat, even if you normally couldn't take another dedication feat until you take more feats from your current archetype. You can benefit from the following Gravelands terrain attunement when in the Gravelands.

**Gravelands** (vitality) You gain a +1 status bonus to saving throws against the spells and abilities of haunts and undead creatures for 1 round.

> [!danger] Effect: Terrain Attunement (Gravelands)

**Source:** `= this.source` (`= this.source-type`)
