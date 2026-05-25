---
type: action
source-type: "Remaster"
traits: ["[[Force]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Raise the mirrored aegis, which summons ethereal shields that surround you and one ally of your choice within 15 feet in a tortoise shield formation. You and the ally gain a +1 status bonus to AC, Reflex saves, and any save against a force, spirit, vitality, or void effect for 1 minute.

> [!danger] Effect: Raise the Walls

**Source:** `= this.source` (`= this.source-type`)
