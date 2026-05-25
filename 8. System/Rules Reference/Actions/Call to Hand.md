---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:1`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

With a simple flourish of your hand, you cause your autonomous spear or polearm to teleport into your grip, provided you're on the same plane as your weapon. If you're level 20, you can call to hand your weapon regardless of where it's located. If your weapon is wielded by a mythic creature that's higher level than you, you must spend a Mythic Point to Call to Hand the weapon, otherwise this action fails—you know why it failed, but you don't learn who has control of your weapon.

**Source:** `= this.source` (`= this.source-type`)
