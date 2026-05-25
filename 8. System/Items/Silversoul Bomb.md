---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Mental]]", "[[Splash]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

This rare alchemical bomb gathers and concentrates the emotions that linger in a burial ground where generations of beloved ancestors have been interred, infusing that powerful emotional energy into the alchemically prepared powdered silver stored within the bomb. This energy glows with a soft, silver radiance and, if stored in a clear container, allows a silversoul bomb to be used as a torch to illuminate an area.

You gain a +1 item bonus to attack rolls, and the bomb deals 2d4 mental damage, 1d6 persistent mental damage to nindorus, and 2 mental splash damage. A creature that takes splash damage from the bomb and fails a DC 17 [[Fortitude]] save is [[Dazzled]] for 1 round as glowing silver particles cling to its face.

Nindorus are particularly harmed by silversoul bombs and take 1d6 persistent mental damage. Against nindorus, the bomb's item bonus also applies to its save DC to resist being resist being dazzled or blinded. Creatures that have weakness to silver (including most nindorus) have an equal amount of weakness to the mental damage caused by a silversoul bomb, due to the silver infused into the energy within.

**Source:** `= this.source` (`= this.source-type`)
