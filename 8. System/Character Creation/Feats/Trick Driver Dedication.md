---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trick Driver|Trick Driver]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Driving Lore"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are equally at home piloting any vehicle, adapting yourself instantly to varied controls, movements, and handling. Whenever piloting a vehicle requires a Piloting Lore or Sailing Lore check, you can use your Driving Lore proficiency instead. You can use Dexterity in place of Intelligence when attempting piloting checks with Driving Lore. You become an expert in Driving Lore. At 7th level, you become a master in Driving Lore, and at 15th level, you become legendary in Driving Lore.

Trick Driver

**Source:** `= this.source` (`= this.source-type`)
