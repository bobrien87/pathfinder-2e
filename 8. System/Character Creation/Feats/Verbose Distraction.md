---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Venture Gossip|Venture Gossip]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]"]
prerequisites: "Venture-Gossip Dedication"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are the target of a physical melee attack.

You talk so much it can be distracting to your enemies and you're often quick to remind your enemies that you're just a little guy! You don't need to be targeted! You don't need to be the focus of their frustrations! Have they tried writing to their mom or talking to a local priest of Desna? Ow!

You gain a +2 circumstance bonus to your AC against the triggering attack.

**Source:** `= this.source` (`= this.source-type`)
