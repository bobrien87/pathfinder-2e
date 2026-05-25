---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Two hand d12]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** A character who is a member of the Eagle Knights has access to this weapon.

Eagle Knights charged with protecting Andoran's western border against Chelaxian incursion often carry these *+2 greater striking standard-grade silver bastard swords*, enchanted to offer greater utility when battling fiends. A greater talonstrike blade gains the Grasping Talons activation.

**Activate—Defense of Liberty** `pf2:r`

**Frequency** once per hour

**Trigger** You or your mount are targeted by a physical melee or ranged attack

**Requirements** You are aware of the attack and are not [[Off Guard]] against it

**Effect** You or your mount gain a +2 circumstance bonus to AC against the triggering attack.

> [!danger] Effect: Defense of Liberty

**Activate—Grasping Talons** `pf2:r` (arcane)

**Frequency** once per day

**Trigger** You hit with a melee Strike using the greater talonstrike blade and deal damage

**Effect** You cast a 5th-rank [[Planar Tether]] on the creature you just dealt damage to, with a DC of 34.

**Craft Requirements** For a greater talonstrike blade, supply one casting of planar tether.

**Source:** `= this.source` (`= this.source-type`)
