---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Divine]]", "[[Fortune]]", "[[Linguistic]]"]
prerequisites: "Mortal Herald Dedication, master in Diplomacy"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

Your words speak divine truth, guiding blades and arrows to their mark. Choose an ally within 30 feet and attempt a [[Diplomacy]] check. The DC is equal to the hard difficulty DC of the level of your ally. On a success, the first time the targeted ally makes an attack roll before the end of their next turn, they roll the attack twice and use the better result.

> [!danger] Effect: Guiding Words

Regardless of the result, the target becomes immune to Guiding Words for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
