---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sleepwalker|Sleepwalker]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Incapacitation]]", "[[Mental]]", "[[Occult]]"]
prerequisites: "Infiltrate Dream"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While Infiltrating a Dream, you can also implant a suggestion in the target's mind. The target must attempt a [[Will]] save against your class DC or spell DC, whichever is higher, to resist your modification, which has the effects of a [[Subconscious Suggestion]] spell, but even on a critical success, the target doesn't realize you were trying to control them and might not recognize your presence in the dream.

The suggestion remains in the target's subconscious for 1 week or until triggered. Their memories of carrying out the suggestion are hazy and dreamlike, and they might not remember doing it unless later reminded.

**Source:** `= this.source` (`= this.source-type`)
