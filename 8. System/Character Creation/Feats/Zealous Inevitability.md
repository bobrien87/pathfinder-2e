---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenger|Avenger]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Avenger Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding your deity's favored weapon

You channel your zeal through a sacred weapon, bringing a foe closer to their demise. Strike a target with the required weapon. on a success, the target becomes [[Doomed]] 1 or increases the value of their doomed condition by 1 (most living creatures die when they've reached doomed 4). Creatures doomed in this way take a status penalty to their saving throws against divine spells equal to their doomed value.

> [!danger] Effect: Zealous Inevitability

A creature that would become doomed 4 by this Strike can attempt a [[Will]] save saving throw against your class DC to avoid increasing the value of their doomed condition. When this occurs, this ability gains the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
