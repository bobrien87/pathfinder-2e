---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Battle Harbinger|Battle Harbinger]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Tandem Onslaught"
frequency: "once per round"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Trigger** You critically hit and Sustain a battle aura.

When your body and mind are perfectly in sync and pushed to the limit, it can produce even greater results. You channel your combat focus into the power of your battle auras. Choose one active battle aura you have; that battle aura's status bonus or penalty increases by 1, to a maximum of 4. This value remains for the rest of the aura's duration.

> [!danger] Effect: Empowered Onslaught

**Source:** `= this.source` (`= this.source-type`)
