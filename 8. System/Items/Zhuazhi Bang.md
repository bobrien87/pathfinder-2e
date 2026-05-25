---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Disarm]]", "[[Grapple]]", "[[Razing]]", "[[Trip]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This niche close-combat weapon resembles a flail with articulated talons used to hook onto an opponent's clothing or armor.

**Source:** `= this.source` (`= this.source-type`)
