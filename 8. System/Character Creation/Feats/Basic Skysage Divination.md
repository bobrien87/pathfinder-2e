---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Oatia Skysage|Oatia Skysage]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Oatia Skysage Dedication"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The stars move, granting you a sliver of their magic. Choose one of the following 1st-rank spells to your spell repertoire: [[Object Reading]] or [[Sure Strike]]. You can Cast this Spell as an occult Oatia skysage spell.

At 6th level, choose one of the following 2nd-rank spells to add to your spell repertoire: [[Augury]] or [[See the Unseen]]. At 8th level, you choose one of the following 3rd-rank spells to add to your spell repertoire: [[Clairaudience]] or [[Locate]].

**Source:** `= this.source` (`= this.source-type`)
