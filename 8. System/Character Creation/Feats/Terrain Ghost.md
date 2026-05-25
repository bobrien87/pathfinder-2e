---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Guerrilla Dedication, master in Stealth and Survival"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You move through your territory like a living shadow. Within your favored location, you're permanently under the effect of [[Vanishing Tracks]], and you're always [[Concealed]] from all foes unless you choose not to be.

**Source:** `= this.source` (`= this.source-type`)
