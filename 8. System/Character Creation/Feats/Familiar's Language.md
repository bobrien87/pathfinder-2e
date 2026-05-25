---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Witch]]"]
prerequisites: "a familiar"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned to speak with your familiar and other creatures like it. You can ask questions of, receive answers from, and use the Diplomacy skill with creatures of the same family of animals as your familiar. For example, if your familiar were a cat, you could gain the effects of [[Speak with Animals]] for any felines (including leopards, lions, and tigers, among others). This ability doesn't make them more friendly than normal. If your familiar ever changes to a different creature, you can't use this ability for 1 week while you absorb your new familiar's language.

**Special** This feat has the trait corresponding to the tradition of spells you cast (arcane, divine, occult, or primal).

**Source:** `= this.source` (`= this.source-type`)
