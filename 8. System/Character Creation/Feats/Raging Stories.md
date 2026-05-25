---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Campfire Chronicler|Campfire Chronicler]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Campfire Chronicler Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you [[Offer a Story]] about wild chances and fighting against all odds, you can wrap yourself in spectral flame in place of the normal benefits. The action then gains the fire trait. Your melee Strikes for the duration deal 2 additional fire damage. The creature you share a story with can choose this benefit even if you did not.

The fire damage increases to 4 if you are a master of Religion and 6 if you are legendary.

**Source:** `= this.source` (`= this.source-type`)
