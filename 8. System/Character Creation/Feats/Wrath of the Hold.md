---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Tattooed Historian|Tattooed Historian]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Tattooed Historian Dedication"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tattoos carry the strength of an innumerable horde, and you can expend one use of your storied skin's Living History ability to animate your tattoos as ghostly assailants that swarm your foes. These spirits attack all foes in a @Template[type:cone|distance:30], dealing @Damage[(floor(@actor.level/2))d6[spirit]|options:area-damage] damage. The damage increases by 1d6 at 10th level and every 2 levels thereafter. Each affected creature must attempt a Type:will check saving throw against the higher of your class DC or spell DC.

**Source:** `= this.source` (`= this.source-type`)
