---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are a living legend, a being who cannot be claimed by death, as death has already passed you. You are beyond whatever they wish to make you. When you would be killed, you instead disappear. You reappear anywhere where your name is spoken in the next week. Your name must be said in the context of recounting one of your exploits, including your death. If the person speaking your name is a close ally (such as another PC), you return to life with only 1 Hit Point. However, if a stranger speaks your name, you return to life with full Hit Points and you gain a +1 status bonus to attack rolls, Perception, saving throws, and skill checks for 1 week.

> [!danger] Effect: Living Epic

If no one speaks your name within a week of your death, your soul enters the River of Souls, and you can be brought back to life using other means.

**Source:** `= this.source` (`= this.source-type`)
