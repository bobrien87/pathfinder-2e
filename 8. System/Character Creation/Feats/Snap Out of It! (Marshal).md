---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Marshal Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You give a quick shout, hoping to shake the fog clouding your ally's thoughts.

Choose one target ally in your marshal's aura who is affected by a mental effect that allowed a Will save and has a duration of no longer than 1 minute. That ally can immediately attempt a Will save with a +1 circumstance bonus against the effect's DC, ending the effect on a success. This can't end the effect for any creatures other than your target ally.

Regardless of the result of the save, your ally is temporarily immune to Snap Out of It! for 10 minutes.

> [!danger] Effect: Snap Out of It! (Marshal)

**Source:** `= this.source` (`= this.source-type`)
