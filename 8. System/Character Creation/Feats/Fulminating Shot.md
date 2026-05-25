---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spellshot|Spellshot]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Spellshot Dedication"
frequency: "once per round"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round.

You channel magic into your next shot. Choose acid, cold, electricity, or fire. If you hit with your next attack roll using a firearm or crossbow before the end of your turn, you deal 1d6 additional damage of this type. At 12th level, this increases to 2d6 additional damage, and at 18th level, it increases to 3d6 additional damage.

**Source:** `= this.source` (`= this.source-type`)
