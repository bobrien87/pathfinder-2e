---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Five Breath Vanguard|Five Breath Vanguard]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Two of the five elemental stances (Ironblood Stance, Mountain Stance, Reflective Ripple Stance, Stoked Flame Stance, and Tangled Forest Stance)"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin or exposure to Tian elementalism

You flow like the elemental cycle, adapting your stance and techniques constantly in response to whatever circumstances you face. You gain the [[Cycle Elemental Stance]] action.

Five-Breath Vanguard

**Source:** `= this.source` (`= this.source-type`)
