---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Gunner|Beast Gunner]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Beast Gunner Dedication"
frequency: "once per PT1M"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You have possession of your bonded beast gun.

You draw out the bestial magic energy within your bonded beast gun to fortify yourself, purge ongoing harm, and bolster your life force with a sheath of swirling life essence. You gain temporary Hit Points equal to your level and attempt a flat check against any ongoing persistent damage, using the DC appropriate for particularly effective assistance. Using this ability depletes the magic within your bonded beast gun, preventing you from using any of its activated abilities until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
