---
type: action
source-type: "Remaster"
traits: ["[[Light]]", "[[Spirit]]", "[[Teleportation]]", "[[Transcendence]]"]
cast: "`pf2:3`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You swing your weapon in a wide arc, releasing a blazing rainbow that deals @Damage[9d6[spirit]|options:area-damage] damage and @Damage[9d6[untyped]|options:area-damage] damage of the same type as your weapon to all enemies in a @Template[type:cone|distance:60], with a [[Fortitude]] save against your class DC. As the rainbow ripples out, you use it as a bridge to teleport to any location within the effect's area.

**Source:** `= this.source` (`= this.source-type`)
