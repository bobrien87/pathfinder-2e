---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Spellshot]]"]
cast: "`pf2:0`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You roll initiative.

You unleash a small surge of magical energy into your weapon, shrouding the bullet with potential energy and granting it the ability to deal energy damage to your foes to exploit their weaknesses. You can Interact to draw a ranged weapon. On your first three Strikes of this encounter with a firearm or crossbow, you deal an additional 1 acid, cold, fire or electricity damage per weapon damage die. You choose which damage type to deal as part of making each Strike.

> [!danger] Effect: Energy Shot

**Source:** `= this.source` (`= this.source-type`)
