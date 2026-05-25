---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Flexible]]"]
price: "{'gp': 3}"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This armor consists of a chest plate, typically made out of bronze or other water-resistant alloys, strapped to the body with a leather harness and featuring a skirt of leather pleats reinforced with metal studs to protect the upper legs.

**Source:** `= this.source` (`= this.source-type`)
