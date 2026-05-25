---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Elementalist|Elementalist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Elementalist Dedication"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** The spell attack roll for a foe's spell with an elemental trait targeting you fails or critically fails, and the elemental trait is in your elemental philosophy.

You seize the elemental essence of an incoming spell and redirect the spell to a creature of your choice within the spell's area. The attacker rerolls the spell's attack roll against the new target.

**Source:** `= this.source` (`= this.source-type`)
