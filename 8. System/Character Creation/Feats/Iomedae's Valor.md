---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starstone Aspirant|Starstone Aspirant]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Starstone Aspirant Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You would be reduced to 0 Hit Points but not immediately killed.

Though you might not be walking the virtuous path of honor and justice most often associated with Iomedae, you have studied her mortal bravery and can emulate it when you're on the brink of defeat. You avoid being knocked out and remain at 1 Hit Point. You also gain a number of temporary Hit Points equal to your level that last for 1 minute and a +1 status bonus to AC for 1 round.

> [!danger] Effect: Iomedae's Valor (AC Bonus)

> [!danger] Effect: Iomedae's Valor (Temporary Hit Points)

**Source:** `= this.source` (`= this.source-type`)
