---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Light]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This 1-foot-long, gold-tipped rod glows after it's struck on a hard surface. For the next 6 hours, it sheds bright light in a 20-foot radius (and dim light to the next 40 feet).

> [!danger] Effect: Glow Rod

**Source:** `= this.source` (`= this.source-type`)
