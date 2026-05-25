---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Two hand d12]]"]
price: "{'gp': 2000}"
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

This large *+2 striking standard-grade silver bastard sword* is the signature weapon of many veteran Eagle Knights. It's easily recognized by its distinctively notched blade and the stylized wings adorning its cross guard. These blades are sometimes passed down from generation to generation.

**Activate—Defense of Liberty** `pf2:r`

**Frequency** once per hour

**Trigger** You or your mount are targeted by a physical melee or ranged attack

**Requirements** You are aware of the attack and are not [[Off Guard]] against it

**Effect** You or your mount gain a +2 circumstance bonus to AC against the triggering attack.

> [!danger] Effect: Defense of Liberty

**Source:** `= this.source` (`= this.source-type`)
