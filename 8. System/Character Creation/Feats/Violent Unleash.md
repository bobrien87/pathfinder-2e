---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Mindshift]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirement** Your previous action was to [[Unleash your Psyche]].

The force of your mind unleashing itself wracks your enemies with a violent shockwave that batters your enemies. You deal @Damage[ceil(@actor.level/2)d6[force]|options:area-damage] damage to all creatures in a @Template[emanation|distance:20], with a [[Reflex]] save.

At 5th level and every 2 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
