---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Finesse]]", "[[Goblin]]"]
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This short, curved, and crude makeshift blade often has holes drilled into it to reduce its weight. It's a favored weapon of goblins.

**Source:** `= this.source` (`= this.source-type`)
