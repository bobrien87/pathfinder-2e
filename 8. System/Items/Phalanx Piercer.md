---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Concussive]]", "[[Hobgoblin]]", "[[Propulsive]]", "[[Razing]]", "[[Volley 30]]"]
price: "{'gp': 10}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This massive bow is made from bone or wood reinforced with flexible metal strips and strung with reinforced cord. Designed by hobgoblin engineers to take down shielded opponents, the phalanx piercer fires heavy, iron-shod bolts.

**Source:** `= this.source` (`= this.source-type`)
