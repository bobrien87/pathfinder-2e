---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Deadly d8]]", "[[Finesse]]"]
price: "{'sp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A war razor is an exaggerated version of the barbers' tool. It's a brittle but extremely sharp weapon that is very easy to slip into a pocket or sleeve.

**Source:** `= this.source` (`= this.source-type`)
