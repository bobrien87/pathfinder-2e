---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Shield the Faithful"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you call upon your deity's power, you also radiate a sense of safety that fortifies your allies. An ally who begins their turn in your Shield the Faithful aura gains 10 temporary Hit Points that last for 1 round.

> [!danger] Effect: Healing Sanctuary

**Source:** `= this.source` (`= this.source-type`)
