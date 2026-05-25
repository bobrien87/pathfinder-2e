---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Campfire Chronicler|Campfire Chronicler]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Campfire Chronicler Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Stories serve as beacons in the night, illuminating valuable knowledge even if the tale itself misses the mark. When you [[Offer a Story]] about any topic, you can choose that illumination in place of the normal benefits of Offer Story. You receive a +1 status bonus on checks to [[Recall Knowledge]] for the duration and can Recall Knowledge about the topic of the story as a free action. The creature you share a story with can choose this benefit even if you did not.

The bonus increases to +2 if you are a master of Religion and +3 if you are legendary.

**Source:** `= this.source` (`= this.source-type`)
