---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eagle Knight|Eagle Knight]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Commitment to Equality"
frequency: "once per day"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Even when overpowered, Eagle Knights hold out hope. If your next action is to use [[Commitment to Equality]], you roll the Diplomacy check twice and take the higher result. If you succeed, the target also gains 25 temporary Hit Points that last for 1 minute.

> [!danger] Effect: Even the Odds (Eagle Knight)

**Source:** `= this.source` (`= this.source-type`)
