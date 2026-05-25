---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Bulwark]]", "[[Entrench ranged]]", "[[Ponderous]]"]
price: "{'gp': 8500}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The joints of this black *+2 greater resilient fortification fortress plate* look like swirling vortices of silver. Non-magical ammunition and thrown weapons aimed at you are destroyed after they hit you and deal damage or miss you. You also have resistance 10 to physical damage from ranged attacks.

When an enemy's ranged attack misses you or hits you and deals no damage, the armor absorbs the projectile. When it has absorbed six projectiles, the armor glows at the joints.

**Activate** `pf2:r` (manipulate)

**Frequency** once per minute

**Trigger** A ranged weapon Strike targets a creature within 20 feet of you and the attacker hasn't yet rolled its attack

**Effect** The triggering Strike targets you instead of its intended target.

**Activate** `pf2:1` Interact

**Requirements** The *black hole armor* has absorbed six or more projectiles

**Effect** All the projectiles absorbed by the armor appear out of thin air, as though transported there, falling in a @Template[burst|distance:10] within 120 feet of you. Each creature in the burst takes @Damage[10d8[piercing]|options:area-damage] with a DC 35 [[Reflex]] save. The absorbed projectiles are all expended, and the armor's joints stop glowing.

**Source:** `= this.source` (`= this.source-type`)
