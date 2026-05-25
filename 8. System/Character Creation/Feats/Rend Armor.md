---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Manipulate]]"]
prerequisites: "Hellbreaker Dedication"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a critical Strike that dealt bludgeoning or piercing damage.

Your enemies' defenses are no match for you as you wrench your weapon to compromise their armor. The creature takes a –2 circumstance penalty to their AC that lasts until they can take 10 minutes to repair their armor. The creature can also Interact to adjust their armor, which removes this penalty for 1 minute.

> [!danger] Effect: Rend Armor

**Source:** `= this.source` (`= this.source-type`)
