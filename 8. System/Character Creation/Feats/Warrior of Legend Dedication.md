---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warrior Of Legend|Warrior Of Legend]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "warrior of legend"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have been given a powerful blessing of battle that is also your cursed doom. As long as you aren't wearing heavy armor or wielding a shield, spears and polearms you wield gain the parry trait. If the weapon already has the parry trait, increase the bonus when parrying to +2. In addition, you deal an additional amount of damage equal to your [[Doomed]] value with weapons in the spear and polearm groups. This damage is the same type as the required weapon.

Warrior of Legend

**Source:** `= this.source` (`= this.source-type`)
