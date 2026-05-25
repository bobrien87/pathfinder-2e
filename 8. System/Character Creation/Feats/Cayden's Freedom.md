---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starstone Aspirant|Starstone Aspirant]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Starstone Aspirant Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Even if you've never downed a tankard of ale nor indulged in a night of rowdy revelry, you appreciate the dedication to freedom from Cayden Cailean and his worshippers. After much physical practice, you've become difficult to restrain, and if you're ever [[Grabbed]], you can access a little bit of the Accidental God's luck. You gain a +2 circumstance bonus to your Fortitude DC when resisting an opponent's attempts to `act grapple` you or Swallow you Whole. In addition, you gain the [[Liberate Self]] action.

**Source:** `= this.source` (`= this.source-type`)
