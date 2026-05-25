---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Guerrilla Weaponry"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in your favored location; you are currently [[Hidden]], unobserved, or unnoticed by all enemies; and you are not [[Fatigued]].

You move and attack with deadly silence, unbelievable speed, and unlimited ferocity. Strike with a blowgun or sling; if the Strike is successful, the enemy cannot tell where it came from and you remain hidden. Immediately after the successful Strike, you can [[Sneak]] to a new location, Interact to reload a blowgun or sling, and Strike again, remaining hidden on a successful Strike. If the second Strike is successful, you can Sneak, Interact to reload, and then Strike with a sling or blowgun a third time, remaining hidden after a successful Strike.

After using Lonely Army, you are [[Fatigued]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
