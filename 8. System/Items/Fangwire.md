---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Deadly d8]]", "[[Finesse]]", "[[Grapple]]", "[[Kobold]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This kobold wire is thin and hard to see, making it perfect for an ambush. The wielder flicks one handle around a vulnerable spot so that it serves as a catch for the wire, then yanks the other handle back, pulling the wire tight and inflicting painful lacerations. The function and name come from a wire-based trap called a "slow fang."

**Source:** `= this.source` (`= this.source-type`)
