---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Aftermath]]"]
prerequisites: "You helped to lay a haunt, ghost, or spirit to rest"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With the utmost gratitude for your help in releasing them from their unearthly coil, a tiny sliver of a ghostly entity has remained attached to you. This manifests as an echo of their former self that follows you around and that you and anyone capable of casting divine or occult spells can see and speak with. When you take this feat, work with your GM to choose one martial weapon and one skill (or an advanced weapon if you're trained in all martial weapons) that are appropriate for the spirit; once you've chosen the weapon and skill, you can't change them. You gain the [[Accept Echo]] action.

**Source:** `= this.source` (`= this.source-type`)
