---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 20}"
usage: "affixed-to-crossbow-or-firearm"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a firearm or crossbow

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt an attack roll with the affixed firearm or crossbow

**Requirements** You're trained in use of the affixed firearm or crossbow.

This simple brass shell casing contains trace amounts of alchemical ingredients and is usually attached to the underside of the affixed weapon's barrel. When activated, it causes the ammunition fired from the affixed weapon to transform into your choice of acid, cold, electricity, or fire, dealing damage of the appropriate energy type instead of its usual damage as well as 1d6 persistent damage of the same type on a critical hit.

> [!danger] Effect: Energized Cartridge

**Source:** `= this.source` (`= this.source-type`)
