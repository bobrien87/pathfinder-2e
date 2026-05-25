---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Campfire Chronicler|Campfire Chronicler]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Campfire Chronicler Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Stories, like fires, can create shadows as much as they illuminate. When you Offer a Story, you can become [[Concealed]] by shifting shadows for the duration instead of the normal benefits. The action then gains the shadow trait. You can't use this concealment to [[Hide]], as normal for concealing effects that leave your location obvious. The creature you share a story with can choose this benefit even if you did not.

**Source:** `= this.source` (`= this.source-type`)
