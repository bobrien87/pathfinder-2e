---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Light]]", "[[Magical]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *everlight* crystal is one of the most common applications of permanent magic. This stone or gem sheds magical bright light constantly in a 20-foot radius (and dim light for the next 20 feet). The light requires no oxygen, generates no heat, and can't be extinguished, though the crystal can be covered.

**Source:** `= this.source` (`= this.source-type`)
