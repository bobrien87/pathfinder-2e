---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Chronoskimmer Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By narrowing your sense of the future, you can improve that of your allies. When you roll initiative, instead of stabilizing or destabilizing your own timestream, you can grant your allies a flash of insight into their future. Choose two allies. Those allies roll their initiative roll twice and take the better result; this is a fortune effect. You roll your initiative roll twice and take the worse result; this is a misfortune effect. The two effects are tied together: if you would avoid the misfortune effect for any reason, or if any of your allies would negate their fortune effect, your Combat Premonition does nothing.

> [!danger] Effect: Combat Premonition

**Source:** `= this.source` (`= this.source-type`)
