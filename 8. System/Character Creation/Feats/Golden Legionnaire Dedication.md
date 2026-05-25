---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in heavy armor"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're invited by a current member of the Eagle Knights or the People's Council.

You're a wall of metal standing against the tide of Andoran's enemies. When you Raise a Shield, you also gain your shield's circumstance bonus to your Fortitude DC against attempts to `act grapple`, `act reposition`, or `act shove` you. You also gain the [[Additional Lore]] general feat for Warfare Lore. If you were already trained in Warfare Lore, you also become trained in a Lore skill of your choice.

**Special** You can take this dedication even if you haven't taken more than two non-dedication feats from the Eagle Knight archetype.

Golden Legionnaire

**Source:** `= this.source` (`= this.source-type`)
