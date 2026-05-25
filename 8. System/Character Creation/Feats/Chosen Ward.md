---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have designated an ally to be you and your companion's ward, making it your primary directive to shield them from harm. During your daily preparations, choose an ally who isn't your united companion. While either you or your united companion are adjacent to your ward, you grant them a +1 circumstance bonus to their AC and Reflex saves.

When your ward attempts a Reflex saving throw while adjacent to either you or your united companion, you can spend a Mythic Point as a reaction to allow your ward to roll that Reflex save twice and take the better result. This is a fortune effect.

> [!danger] Effect: Chosen Ward

**Special** If you have the [[Defend Our Union]] feat, it can also be triggered when a foe successfully Strikes your ward; if used in this way, the damage to your ward is reduced if your Strike is successful instead.

**Source:** `= this.source` (`= this.source-type`)
