---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'value': {}}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Society Scenario #6-05: Silver Bark, Golden Blades"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You strike an unholy target with the affixed weapon

**Requirements** You're trained in the affixed weapon.

This small glowing sprig of cherry tree flowers is only granted by Sakura, the kami of Silvertree. When activated, the affixed weapon gains the holy trait for the triggering attack and all other attacks for 1 minute.

> [!danger] Effect: Sakura's Sprig

**Source:** `= this.source` (`= this.source-type`)
